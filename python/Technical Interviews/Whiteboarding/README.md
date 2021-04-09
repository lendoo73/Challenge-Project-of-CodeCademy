#### TECHNICAL INTERVIEWS: WHITEBOARDING

# [Introduction](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/technical-interview-wb/exercises/technical-interview-wb-intro)

Aspiring developers must pass a technical interview to be hired as a professional. 
These interviews evaluate the candidate’s ability to write code, articulate their thought process, and problem solve in a timed environment.

Technical interviews take many forms: 
writing code alongside an employee of the company, 
testing online with a third-party service, 
take-home challenges spanning several days, 
and more!

A whiteboarding technical interview requires the interviewee to plan and code the solution by hand. 
The candidate relies on their ability to communicate without the assistance of a text editor or web browser.

This lesson covers strategies to improve performance in a whiteboarding interview. 
Each exercise features a step in the interview with a video demonstration of the technique.

The steps are:
1. **Clarify** the Problem
2. Create **Inputs**
3. **Outline** the Solution
4. **Code** the Solution
5. **Test** the Solution
6. **Analyze** the Solution

[![Video](https://img.youtube.com/vi/SgAVxPV9JVk/0.jpg)](https://www.youtube.com/watch?v=SgAVxPV9JVk)


#### [Cheatsheet](https://www.codecademy.com/learn/technical-interview-practice-python/modules/technical-interviews-whiteboarding/cheatsheet)

# [Clarifying the Problem](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/technical-interview-wb/exercises/technical-interview-wb-clarify)

Whiteboarding interviews begin with a problem from the interviewer. 
The interviewee must be confident they understand the dimensions of the problem!

Software development is full of ambiguity. 
Programming requires concrete deliverables, but company needs can be murky. 
Even when the need is clear, a feature could have dozens of possible implementations. 
The ability to clearly define a problem is an important skill to demonstrate.

When the interviewer presents their technical question, repeat the question back to the interviewer **in your own words**. 
This gives you a moment to think and will resolve any glaring misunderstandings.

Once you’ve repeated the question, **ask every clarifying question that comes to mind**.

Assumptions must be communicated to the interviewer so there is agreement on the scope of the problem.

For example, if asked:
> Write a function that returns duplicate characters in string.

Here are some questions which may come to mind:
* What is the desired return value? True|False, a list of characters, or …?
* Do punctuation and spaces count as “characters”?
* Should case be considered? Are "a" and "A" duplicates?
* Should we be checking for [Unicode](https://en.wikipedia.org/wiki/Unicode) characters?
* Can we assume it’s a 26 character alphabet?

We’ll apply these steps to a single problem through the rest of the lesson.
```
Given a list of numbers, return whether the list contains Pythagorean Triplets.
```
Rephrase this problem in your own words and write that down.

Then, write down every question or assumption you have.

Watch the video to see how we clarified this question.

[![Video](https://img.youtube.com/vi/xzYgM0eIauA/0.jpg)](https://www.youtube.com/watch?v=xzYgM0eIauA)

# [Producing Inputs and Finding Edge Cases](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/technical-interview-wb/exercises/technical-interview-wb-input)

When the question is clear, we then produce concrete inputs and outputs. 
These inputs guide a solution for the remainder of the interview so write them on the board!

You may still be unclear how to solve the problem in code, but it’s certain that given an input, `X`, your function will produce an output, `Y`.

Make one input the happy path: input that reflects a common scenario.

For example, you’re asked to write a function which capitalizes the first letter of an input string.

A good input could be `"apple"`, which returns `"Apple"` because this demonstrates the function’s purpose.

If the input were `"Apple"`, it would return `"Apple"`. 
That’s correct but less informative.

Also think about edge cases, or inputs which **do not** reflect a common scenario and may cause problems.

For the capitalization function, what should you return if given `None` as input? 
Or a number?

Write inputs and outputs for the Pythagorean Triplet problem.

Try to give yourself a few different cases.

Watch the video to see how we made inputs/outputs.

[![Video](https://img.youtube.com/vi/tccfJmGM0XI/0.jpg)](https://www.youtube.com/watch?v=tccfJmGM0XI)

# [Writing the Outline](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/technical-interview-wb/exercises/technical-interview-wb-outline)

It’s time to start breaking down the problem by category.

Given a question which requires the use of a stack, what do you know about stacks? 
Have you encountered other problems that use stacks and how were they solved?

Is this a searching question? 
Can you sort the input and will that help? 
Does this problem sound like it can be modeled as a graph, with vertices and connected edges?

Understanding the applications of different data structures is very useful! 
The more questions you practice, the more you will be able to see patterns between problems.

This step varies the most because it requires details of the specific problem, but regardless of the question make certain you are communicating with the interviewer as a potential co-worker. 
Show them your thought process!

During this step, the interviewer may make suggestions on how to proceed. 
Acknowledge the interviewer and incorporate their suggestions into your approach.

Don’t disregard their input! 
It gives the impression you would be difficult to work with on the job.

When you and the interviewer are satisfied with a workable solution, write the steps next to your input. 
Follow these steps as you write code on the board.

Come up with an outline of how to solve the Pythagorean Triplet problem.

Don’t worry about efficiency, just aim for high-level steps which will produce the correct output.

Watch the video when you’re ready to move on.

[![Video](https://img.youtube.com/vi/yt-YB_9ZHUE/0.jpg)](https://www.youtube.com/watch?v=yt-YB_9ZHUE)









