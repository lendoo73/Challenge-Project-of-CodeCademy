#### TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS

# [Introduction](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-intro)

Lists are a fundamental data type in Python. 
Projects make extensive use of lists to store data in sequential order. 
You should expect at least one technical interview question that requires working with lists.

This lesson introduces common interview problems that involve lists. 
We solve each question in two ways: 
* an inefficient naive solution 
* * and an optimized solution which improves the *big O time* and/or *space efficiency*.

The problems are meant to be open-ended: tests will pass with the correct output from a given input. 
Optimal implementations require that code executes within a time or space requirement.

We detail our approach in the hint for each question.

Make a note of clarifications and ambiguities for each question. 
This is a crucial step. 
Interviewers often leave this to you so they can see how you problem-solve.

<hr />
How would you write a function that checks if a string is a palindrome?

What are some assumptions you had? 
Did you have any questions?

Here are some questions which clarify exactly what the function should return.
* Should you consider spaces? For example, is “taco cat” a palindrome?
* Is punctuation ignored or considered part of the string?
* What are the edge cases? Those unconsidered scenarios which break your program. Would an empty string be considered a palindrome?

The **palindrome.py** has four definitions of the `palindrome()` function, each return different results based on the input!

By asking questions, you can prevent writing code that solves the wrong problem. Test out these inputs:
```Python
"aba" or "abba" # "simple" palindromes
"taco cat" # palindrome with spaces
"racecar!" # palindrome with punctuation
"able was I, ere I saw elba" # both!
```

