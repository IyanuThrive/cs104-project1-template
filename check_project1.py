"""
Project 1 Code Checker
Analyzes a student's main.py against the Project 1 rubric criteria.

This is a self-check / grading-support tool, NOT an automatic grader.
Qualitative criteria (naming quality, grammar, overall clarity, "works as
a whole") still need a human read-through and a test run, this tool
surfaces counts and flags so that read-through goes faster and more
consistently.

Students can run this on their own code before submitting to check they've
hit the required counts. Instructors/TFs can run the same tool while
grading to speed up the objective parts of the rubric.

Usage:
    python3 check_project1.py main.py
"""

import ast
import sys
from collections import Counter

# Constructs considered beyond Project 1's scope (variables, input, print,
# if/elif/else, relational/logical operators). Adjust this list if your
# students have already covered any of these by the Project 1 deadline.
# A construct showing up here isn't proof of cheating or AI use, it's a
# prompt to ask the student to explain that part of their code.
OUT_OF_SCOPE_NODES = {
    ast.FunctionDef: "function definition (def)",
    ast.AsyncFunctionDef: "function definition (async def)",
    ast.For: "for loop",
    ast.While: "while loop",
    ast.Try: "try/except",
    ast.ClassDef: "class definition",
    ast.ListComp: "list comprehension",
    ast.DictComp: "dict comprehension",
    ast.SetComp: "set comprehension",
    ast.Lambda: "lambda function",
    ast.With: "with statement",
    ast.Import: "import statement",
    ast.ImportFrom: "import statement",
}

GENERIC_NAMES = {"x", "y", "z", "a", "b", "c", "temp", "tmp", "val", "data", "foo", "bar"}


def load_tree(filepath):
    with open(filepath, "r") as f:
        source = f.read()
    return ast.parse(source, filename=filepath), source


def find_variables(tree):
    """Collect simple Name assignment targets and a rough inferred type."""
    variables = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables[target.id] = infer_type(node.value)
        elif isinstance(node, ast.AugAssign):
            if isinstance(node.target, ast.Name):
                variables.setdefault(node.target.id, "numeric (incremented)")
    return variables


def infer_type(value_node):
    if isinstance(value_node, ast.Constant):
        return type(value_node.value).__name__
    if isinstance(value_node, ast.Call):
        func = value_node.func
        if isinstance(func, ast.Name):
            if func.id == "input":
                return "str (from input)"
            if func.id in ("int", "float", "str", "bool"):
                return func.id
    return "unknown/expression"


def find_input_calls(tree):
    """Return the variable names assigned directly from input(), including
    a variable assigned from a cast of input(), like int(input(...))."""
    input_vars = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            func = node.value.func
            is_input = isinstance(func, ast.Name) and func.id == "input"
            is_cast_of_input = (
                isinstance(func, ast.Name)
                and func.id in ("int", "float")
                and node.value.args
                and isinstance(node.value.args[0], ast.Call)
                and isinstance(node.value.args[0].func, ast.Name)
                and node.value.args[0].func.id == "input"
            )
            if is_input or is_cast_of_input:
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        input_vars.append(target.id)
    return input_vars


def find_conditionals(tree):
    """Count If nodes, and how many have an elif or else branch."""
    if_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.If)]
    with_branch = sum(1 for node in if_nodes if node.orelse)
    return if_nodes, with_branch


def find_operators(tree):
    comparisons = Counter()
    boolops = Counter()
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            for op in node.ops:
                comparisons[type(op).__name__] += 1
        if isinstance(node, ast.BoolOp):
            boolops[type(node.op).__name__] += 1
    return comparisons, boolops


def find_out_of_scope(tree):
    found = []
    for node in ast.walk(tree):
        for node_type, label in OUT_OF_SCOPE_NODES.items():
            if isinstance(node, node_type):
                found.append(label)
    return Counter(found)


def find_cast_chains(tree):
    """Map a variable to the variable it was cast from, e.g.
    response5_num = int(response5)  ->  {'response5_num': 'response5'}
    This lets us trace a two-step cast (get input, then cast on the next
    line) back to the original input variable.
    """
    derived_from = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            func = node.value.func
            if (
                isinstance(func, ast.Name)
                and func.id in ("int", "float", "str", "bool")
                and node.value.args
                and isinstance(node.value.args[0], ast.Name)
            ):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        derived_from[target.id] = node.value.args[0].id
    return derived_from


def variables_linked_to_conditionals(tree, input_vars):
    """Does an input variable, or a variable cast from it (directly or
    via a two-step cast on a later line), ever appear inside an If test?
    Catches the common 'got input, but never branched on it' gap without
    flagging the normal cast-then-use pattern as a false positive.
    """
    derived_from = find_cast_chains(tree)
    linked_any_name = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            names_in_test = {n.id for n in ast.walk(node.test) if isinstance(n, ast.Name)}
            linked_any_name.update(names_in_test)

    linked_input_vars = set()
    for var in input_vars:
        # walk the chain: var -> cast var -> cast of cast var ...
        chain = {var}
        current = var
        for _ in range(5):  # small safety bound, cast chains are never deep
            derived_names = [k for k, v in derived_from.items() if v == current]
            if not derived_names:
                break
            current = derived_names[0]
            chain.add(current)
        if chain & linked_any_name:
            linked_input_vars.add(var)
    return linked_input_vars


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check_project1.py path/to/student_main.py")
        sys.exit(1)

    filepath = sys.argv[1]
    tree, source = load_tree(filepath)

    print(f"\n{'='*60}")
    print(f"Project 1 Code Check: {filepath}")
    print(f"{'='*60}\n")

    # Syntax check
    try:
        compile(source, filepath, "exec")
        print("Code compiles with no syntax errors.\n")
    except SyntaxError as e:
        print(f"Syntax error, code does not run as-is: {e}\n")

    # Variables (rubric: up to 10 points)
    variables = find_variables(tree)
    print(f"--- Variables ({len(variables)} found) | rubric: up to 10 pts ---")
    for name, vtype in variables.items():
        flag = "  <- generic name, check it's meaningful" if name.lower() in GENERIC_NAMES else ""
        print(f"  {name}: {vtype}{flag}")
    type_diversity = len(set(variables.values()))
    print(f"  Distinct inferred types: {type_diversity} (more diversity = stronger)")
    print()

    # Input usage (rubric: up to 10 points, 2 per prompt)
    input_vars = find_input_calls(tree)
    linked = variables_linked_to_conditionals(tree, input_vars)
    print(f"--- User Input ({len(input_vars)} input() calls found) | rubric: up to 10 pts ---")
    print(f"  Variables: {input_vars}")
    print(f"  Linked to a conditional (used in an if/elif test): {sorted(linked)}")
    unlinked = set(input_vars) - linked
    if unlinked:
        print(f"  FLAG: collected but never used in a condition: {sorted(unlinked)}")
    print(f"  Rubric needs 5+ instances feeding conditional logic.")
    print()

    # Conditionals (rubric: up to 15 points)
    if_nodes, with_branch = find_conditionals(tree)
    print(f"--- Conditional Statements | rubric: up to 15 pts ---")
    print(f"  Total if blocks (including nested): {len(if_nodes)}")
    print(f"  Blocks with an elif/else branch: {with_branch}")
    print(f"  Rubric needs 5+ total, at least 3 with elif/else.")
    print()

    # Operators (rubric: up to 8 points)
    comparisons, boolops = find_operators(tree)
    print(f"--- Operators | rubric: up to 8 pts ---")
    print(f"  Relational operators used: {dict(comparisons) if comparisons else 'none found'}")
    print(f"  Logical operators used (and/or): {dict(boolops) if boolops else 'none found'}")
    print()

    # Out of scope constructs (integrity/understanding flag, not a rubric line)
    out_of_scope = find_out_of_scope(tree)
    print(f"--- Constructs Beyond Project 1 Scope ---")
    if out_of_scope:
        print("  FLAG: found constructs not required for this project. This is")
        print("  not proof of cheating or AI use on its own, ask the student to")
        print("  walk through this part of their code during grading or the")
        print("  checkpoint follow-up:")
        for label, count in out_of_scope.items():
            print(f"     - {label} (x{count})")
    else:
        print("  None found, code stays within if/elif/else, input, and print.")
    print()

    # Messaging (rubric: up to 7 points, human judgment)
    print_count = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Call)
                       and isinstance(n.func, ast.Name) and n.func.id == "print")
    print(f"--- Messaging | rubric: up to 7 pts ---")
    print(f"  print() calls: {print_count}")
    print(f"  Manually review: are messages clear, grammatically correct,")
    print(f"  and not too terse or too verbose? (this needs a human read)")
    print()

    print(f"{'='*60}")
    print("Reminder: this tool checks structure and counts. It cannot judge")
    print("naming quality, message clarity, or whether the program truly")
    print("'works as a whole' (rubric: up to 10 pts), that still needs a")
    print("human read-through and a test run with a few different inputs.")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
