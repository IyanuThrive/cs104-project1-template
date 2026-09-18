# [Finance Knowledge Quiz]
> Test your finance knowledge to know your level

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
> b. the required investments in operating capital divided by net income.
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
> a. diversified asset
> b. real asset
> c. capital gain
> d. financial asset 
>
> Question 6:
> Return volatility that is associated with the overall market is called
> a. diversifiable risk.	
> b. systemic risk.	
> c. correlated risk.	
> d. liquidity risk.
>
> 

## Variables
> answer(str): asks user's current input each time you ask a question 
> q1_answer: holds question 1 answer
> q2_answer: holds question 2 answer
> q3_answer: holds question 3 answer
> q4_answer: holds question 4 answer
> q5_answer: holds question 5 answer
> q6_answer: holds question 6 answer
> continue_quiz(bool): sets the stage for a while loop
> cont: asks the user if they want to continue the quiz after every question (1-5), but not question 6
> multiple variables to track scores are needed here because scores are given for each segment
> managerial_finance_points(int): tracks and accumulate point for the managerial finance segment
> financial_markets_points(int): tracks and accumulate point for the financial markets segment
> investments_points(int): tracks and accumulate point for the investments segment
> total_points(int): this will accumulate the score of the managerial_finance_points,
> financial_markets_points and investments_points.
> 
> 

## Conditional Logic Outline
> Conditional Statement 1:
> -if triggers when the user's input equals "b" (WACC, the correct answer). Displays
> "Correct!" and add a point to managerial_finance_points.
> -elif triggers when the input is "a", "c", or "d" (a valid letter, but not the correct one).
> then displays "Incorrect, the answer is b."
> -else branch — triggers when the input is anything other than a, b, c, or d. Action: display "You
> inputted a wrong value, try again," then the question is presented again.
> Condition Statement 1a: 
> --if when the user responds "yes" to continuing, displays total managerial finance point
> Action: move on to Question 2.
> --else branch — triggers when the user responds "no" (or anything not "yes"). Action: display the
> user's current total points and end the quiz early. (cont. is asked after each valid response)
>
> Conditional Statement 2:
> -if answer is "a" (sales less operating costs and taxes less required investment in operating
> capital): display "Correct!", increment managerial_finance_points
> -elif answer is "b", "c", or "d": display "Incorrect, the answer is a"
> -else: display "You inputted a wrong value, try again," re-ask the question
> Conditional Statement 2a:
> --if "yes", displays total managerial finance points: move to Question 3
> (end of Managerial Finance segment);
> --else: display current total points and end. Nested for the same reason as above.
>
> Conditional Statement 3:
> -if answer is "a" (six-month T-bill): display "Correct!", increment financial_markets_points
> -elif answer is "b", "c", or "d": display "Incorrect, the answer is a"
> -else: display "You inputted a wrong value, try again," re-ask the question
> Conditional Statement 3a:
> --if "yes", displays total financial markets points: move to Question 4;
> --else: display current total points and end.
>
> Conditional Statement 4:
> -if answer is "a" (decreased demand; inward shift): display "Correct!", increment
> financial_markets_points
> -elif answer is "b", "c", or "d": display "Incorrect, the answer is a"
> -else: display "You inputted a wrong value, try again," re-ask the question
> Conditional Statements 4a:
> --if "yes", displays total financial markets points: move to Question 5
> (end of Financial Markets segment);
> --else: display current total points and end.
>
> Conditional Statement 5:
> -if answer is "d" (financial asset): display "Correct!", increment investments_points
> -elif answer is "a", "b", or "c": display "Incorrect, the answer is d"
> -else: display "You inputted a wrong value, try again," re-ask the question
> Conditional Statement 5a:
> --if "yes", displays total investments points: move to Question 6;
> --else: display current total points and end.
>
> Conditional Statement 6:
> -if answer is "b" (systematic risk): display "Correct!", increment investments_points
> and display current investment points and total_points
> -elif answer is "a", "c", or "d": display "Incorrect, the answer is b",
> and display current investment points and total_points
> -else: display "You inputted a wrong value, try again," re-ask the question
> Conditional Statement 6a: 
> Unlike Questions 1–5, Question 6 has no nested continue prompt, since there is no further question
> to move to — the program proceeds directly to final scoring.
> 
> Conditional Statement 7:
> if total_points is high (e.g., 5–6): display a top-tier message (e.g., "Expert level knowledge!")
> elif total_points is moderate (e.g., 3–4): display a mid-tier message (e.g., "Solid foundational
> knowledge")
> else (total_points is low, e.g., 0–2): display a message encouraging the user to learn more

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
