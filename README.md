# [Your Project Name Here]
> Finance Knowledge quiz

## Overview
>> This program is a quiz designed to ask users finance question from
> different topics like investments, financial markets and managerial finance.
> The quiz will be broken down into 3 segments for the 3 topics and the total points will be given
> to users at the end of each segment, then the overall points will be displayed after the three
> segments are done.
> How this works is, users will be given a closed ended question (options available).
> They will be asked to pick from 4 options, a, b, c, and d.
> Conditional statements: If they get it right (if the answer is a), "correct!" will be displayed, and
> the option to moveto the next question will appear (yes/no).
> If they choose to continue the next question appears.
> Else, their overall point with be displayed as calculated.
> Elif, they got the question wrong (b, c, or d), it will display "incorrect, the answer is {}"
> Then it gives them the option to move to the next question with a yes/no question.
> Else, if the input they give is not (a, b, c or d), it will display "you imputed a wrong value,
> try again, and it gives them the question again until they put in a correct value.
> The total score is then calculated and tiers to knowledge will be given at the end of the quiz.
> 

## Sample Questions and Responses
> Managerial Finance
>
> Question 1:
> Which of the following is an element in calculating the present value of future cash flows?
> a. Standard Deviation
> b. Weighted Average Cost of Capital
> c. Marginal Tax
> d. Inflation
>
> Question 2: 
> The formula for determining a firm's free cash flows is:
> a. sales less operating costs and taxes less required investments in operating capital.
> d. the required investments in operating capital divided by net income.
> c. sales less operating costs and taxes.
> d. sales less operating costs.
>
> Financial Markets
>
> Question 3:
> Which of the following is a money market security?
> a. six-month treasury bill
> b. municipal bond
> c. mortgage
> d. corporate bond	
>
> Questiion 4:
> As a result of less favorable economic conditions, there is a(n) ____ demand for loanable funds,
> causing an ____ shift in the demand curve.
> a. decreased; inward
> b. decreased; outward
> c. increased; outward
> d. increased; inward
>
> Investments
>
> Question 5:
> A corporate bond is an example of a?
> a. diversified asset.
> b. real asset.
> c. capital gain.
> d. financial asset. 
>
> Questtion 6:
> 
> Example:
> Which of the following painters is an Impressionist?
> 1. Monet
> 2. Warhol
> 3. Rembrandt

## Variables
> **DELETE AND REPLACE ME:** List the variables your program uses. For
> each one, note what it stores and why you structured it that way,
> especially for variables tracking results, explain whether a single
> variable or multiple variables makes sense for your program's logic.
>
> Example:
> - `score` (int): tracks total quiz points. A single variable works here
>   since results are cumulative and only one final score matters.
> - `decade_1920s_points`, `decade_1960s_points`, `decade_1980s_points`
>   (int): separate variables needed since multiple decades can tie for
>   highest score, one combined variable couldn't represent that.
> - `user_choice` (str or int): stores the user's response to a question,
>   compared against expected options to decide which branch of the
>   conditional runs.

## Conditional Logic Outline
> **DELETE AND REPLACE ME:** Outline every conditional statement in your
> program, in the order they appear. For each one, describe it in plain
> language (no code needed): which question/condition it relates to,
> each branch (`if`/`elif`/`else`), the exact condition that triggers
> each branch, the action(s) that happen in each branch, and note any
> nested conditionals and why they're nested.
>
> Example:
> - **Conditional statement 1** — related to "Which of the following
>   painters is an Impressionist? 1-Monet 2-Warhol 3-Rembrandt"
>   - `if` response is 1 (Monet): display congratulatory message,
>     increment `score` by 1
>   - `else`: display incorrect message and explain the correct answer
>
> - **Conditional statement 2** — reveals final results based on `score`
>   - `if` score is 3: display high-knowledge message
>   - `elif` score is 1 or 2: display some-knowledge message
>   - `else`: display message encouraging the user to learn more

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
