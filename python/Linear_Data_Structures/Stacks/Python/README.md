#### STACKS: PYTHON
# [Stacks Python Introduction](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-stacks-python/exercises/stacks-python-intro)
There are three main methods that we want our stacks to have:
* Push - adds data to the “top” of the stack: `push()`
* Pop - provides and removes data from the “top” of the stack: `pop()`
* Peek - provides data from the “top” of the stack without removing it: `peek()`
* 
We also need to consider the stack’s size and tweak our methods a bit so that our stack does not “overflow”.

# [Push and Pop](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-stacks-python/exercises/stacks-python-push-and-pop)
The stack’s `push()` and `pop()` methods are our tools to add and remove items from it. 
`pop()` additionally returns the value of the item it is removing. 
Keep in mind that ***we can only make modifications to the top of the stack***.

# [Size](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-stacks-python/exercises/stacks-python-size-i)
With stacks, size matters. 
If we’re not careful, we can accidentally over-fill them with data. 
Since we don’t want any ***stack overflow***, we need to go back and make a few modifications to our methods that help us track and limit the stack size so we can keep our stacks healthy.

What do we do if someone tries to `peek()` or `pop()` when our stack is empty?

How do we keep someone from `push()`ing to a stack that has already reached its limit?

How do we even know how large our stack has gotten?

# [Helper methods: `has_space()` and `is_empty()`](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-stacks-python/exercises/stacks-python-size-ii)
Helper methods simplify the code we’ve written by abstracting and labeling chunks of code into a new function.
1. The name tells us what this function does. Without a helper, we’d need to read the code to understand its meaning.
2. The function lets us repeat this behavior. Without a helper, we’d need to keep rewriting the same code!

First, we want one that checks if our stack has room for more items. 
We can use this in `.push()` to guard against pushing items to our stack when it’s full.

Second, it’s helpful to have a method that checks if the stack is empty…
