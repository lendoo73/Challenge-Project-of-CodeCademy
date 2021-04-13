#### TECHNICAL INTERVIEW PRACTICE WITH PYTHON

# [Longest Common Subsequence](https://www.codecademy.com/courses/technical-interview-practice-python/projects/longest-common-subsequence)

Given two strings: `"ABAZDC"` and `"BACBAD"`, how can we determine the longest common subsequence?

In other words, what series of letters from left to right do they share? 
The letters don’t need to be directly next to each other. 
In this example, the longest sequence is `"ABAD"` for a length of `4`.

Longest Common Subsequence may seem like an obscure problem, but it has applications in genomics. 
“A”, “C”, “G”, and “T” represent the four nucleotide bases of a DNA strand. 
The longest common subsequence of among these letters would provide valuable information about two people’s genetics.

A naive approach would be to generate every subsequence of each string. 
We then check the longest generated subsequence of each string to see if they match, checking smaller and smaller subsequences if they don’t. 
This approach has a big O runtime of `O(2^N)`.

Let’s apply what we’ve learned about Dynamic Programming to produce a more efficient solution!
