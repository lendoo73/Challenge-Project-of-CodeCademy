#### TECHNICAL INTERVIEW PROBLEMS: DYNAMIC PROGRAMMING

# [Introduction to Dynamic Programming](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-dynamic-programming/exercises/dynamic-programming-intro)

Dynamic programming is an optimization strategy for designing algorithms. 
The technique is beneficial for technical interviews because solving problems with an optimal big O runtime will improve your chances of being hired.

We’ll describe dynamic programming with a question: 
What is `1 + 1 + 1 + 1`?

Now, what is one more, or `1 + 1 + 1 + 1 + 1`?

For the first question, you counted each `1` to arrive at `4`, but for the second question, you only needed to add `1` to the previous total. 
You “stored” the previous sum to avoid a calculation already performed.

That’s dynamic programming! 
Break a problem into smaller sub-problems, store the answers to the sub-problems, and use those stored answers to solve the original problem.

We need overlapping sub-problems for the stored answers to be useful; 
answers for overlapping sub-problems are consistent and relevant to the original problem.

With a linear search, we examine each element in a collection to find a target element. 
We can’t apply dynamic programming because there is no overlapping sub-problem. 
An element’s location can vary between searches and the location in one search has no relevance to another search in a larger collection.

# [Dynamic Programming Review](https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-dynamic-programming/exercises/dynamic-programming-review)

Dynamic programming is a technique to optimize solutions for problems which have a structure that involves repeated, identical computations.

For dynamic programming to work, it’s essential that the problem can be broken into overlapping sub-problems which combine into a solution for the original problem.

Dynamic programming requires us to store the answers to sub-problems so they can be retrieved as components to larger solutions. 
We memoize the solutions by storing them inside a data structure with efficient look-up.

While dynamic programming can be tricky to master, it’s an essential tool for optimizing many useful algorithms. 
The key idea is to break the problem down, solve each sub-problem, and combine the sub-answers.

The difficulty lies in how the problem is broken apart, how the sub-answers are stored, and how they’re used to solve the original problem.

For Fibonacci, we stored the previous numbers so we did not need to recompute them.

For Knapsack, we stored which items gave us the best value for every size knapsack. 
Then we could efficiently retrieve the best option whenever adding a new item.
