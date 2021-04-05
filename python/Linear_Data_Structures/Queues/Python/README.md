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

