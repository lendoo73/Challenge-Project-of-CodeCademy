#### QUEUES: PYTHON

# [Queues Python Introduction](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-queues-python/exercises/queues-python-intro)

As previously mentioned, a queue is a data structure that contains an ordered set of data that follows a FIFO (first in, first out) protocol. 
You can visualize it as a line at a deli:
* The customer at the front of the line (equivalent to the head in a queue) is the first customer to get served
* Any new customer must go to the back of the line (the tail of the queue) and wait until everyone in front of them has been served (no line cutters allowed in this deli!)
* The deli server only needs to know about the current order

Now, we can use Python to build out a Queue class with those three essential queue methods:
* **enqueue()** which will allow us to add a new node to the tail of the queue
* **dequeue()** which will allow us to remove a node from the head of the queue and return its value
* **peek()** which will allow us to view the value of head of the queue without returning it

We’ll also set up a few helper methods that will help us keep track of the queue size in order to prevent queue *“overflow”* and *“underflow.”*

# [Queues Python Size](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-queues-python/exercises/queues-python-size)
Bounded queues require limits on the number of nodes that can be contained, while other queues don’t. 
To account for this, we will need to make some modifications to our `Queue` class so that we can keep track of and limit size where needed.

We’ll be adding two new properties to help us out here:
* A `size` property to keep track of the queue’s current size
* A `max_size` property that bounded queues can utilize to limit the total node count

In addition, we will add three new methods:
* `get_size()` will return the value of the `size` property
* `has_space()` will return `True` if the queue has space for another node
* `is_empty()` will return `True` if the size is `0`

# [Enqueue](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-queues-python/exercises/queues-python-enqueue)
“Enqueue” is a fancy way of saying “add to a queue,” and that is exactly what we’re doing with the `enqueue()` method.

There are three scenarios that we are concerned with when adding a node to the queue:
1. The queue is empty, so the node we’re adding is both the head and tail of the queue
2. The queue has at least one other node, so the added node becomes the new tail
3. The queue is full, so the node will not get added because we don’t want queue “overflow”

# [Dequeue](https://www.codecademy.com/courses/linear-data-structures/lessons/learn-queues-python/exercises/queues-python-dequeue)
We can add items to the tail of our queue, but we remove them from the head using a method known as `dequeue()`, which is another way to say “remove from a queue”. 
Like `enqueue()`, we care about the size of the queue — but in the other direction, so that we prevent queue “underflow”. 
After all, you don’t want to remove something that isn’t there!

As with `peek()`, our `dequeue()` method should return the value of the head. 
Unlike, `peek()`, `dequeue()` will also remove the current head and replace it with the following node.

For dequeue, there are three scenarios that we will take into account:
1. The queue is empty, so we cannot remove or return any nodes lest we run into queue “underflow”
2. The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue’s `head` and `tail` to `None`
3. The queue has more than one node, and we just remove the `head` node and reset the `head` to the following node

