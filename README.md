# Data-structures
## Authors: Karen Wong & Scott Schmidt

It holds sample code for a number of classic data structures implemented in Python.

Current Data Structures in this repo:

## Single-Linked List
  * In a singly linked list each node in the list stores the contents of the node and a pointer or reference to the next node in the list. It does not store any pointer or reference to the previous node.
  * We approached this data structure by learning the importance of writing tests, with the intent to improve our test driven development skills. Although we were't able to write every test first, we were able to sharpen those skills, and have a better understanding of both testing and the Single-Linked List data structure.

## Stack
  * A stack is a basic data structure that can be logically thought as linear structure represented by a real physical stack or pile, a structure where insertion and deletion of items takes place at one end called top of the stack.
  * We modeled the Stack data structure by first writing tests. This project was quite a bit easier given the limited functionality of a stack, and the fact that we were able to use the concept of Composition to accomplish our task. We drew on the pre-existing methods of the Linked List to manage each of the tasks of our Stack.

## Queue
  * A queue is structured, as described above, as an ordered collection of items which are added at one end, called the “rear,” and removed from the other end, called the “front.” Queues maintain a FIFO ordering property.
  * We approached writing our queue functionality by writing tests which would evaluate the outcome of adding and removing to and from the queue, as well as verifying the size of the queue. This data structure presented a challenge by having to rethink through the previous data structures, and modifying the functionality that we've implemented in the past to accomodate the FIFO properties of the Queue.

## Doubly Linked List
  * A doubly-linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains two fields, called links, that are references to the previous and to the next node in the sequence of nodes.
  * We completed this data structure with more ease than in past exercises. The different approach we took, by hand-drawing actionable steps within our data structure, helped visualize each step of the process, and made writing code much simpler!

## Binary Heap
  * A binary Heap is a complete binary tree which satisfies the heap ordering property. The ordering can be one of two types: the min-heap property: the value of each node is greater than or equal to the value of its parent, with the minimum-value element at the root.
  * The Binary heap was the most complicated data structure that we've completed thus far. It presented a logical challenge that pressed us to really consider how we wrote our code.
  (At this point we plan to rewrite this project to be more Pythonic when we have time available)

## Priority Queue
  * A priority queue is an abstract data type which is like a regular queue or stack data structure, but where additionally each element has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority.
  * With the Binary Heap in place this data structure didn't present any major challenge other than planning and execution based on the available methods of the Binary Heap.



## Interview Challenge: Proper Parenthetics
  * Build a quick Python function that takes a unicode string (text) as input and returns one of three possible values:

    * Return 1 if the string is "open" (there are open parens that are not closed)
    * Return 0 if the string is "balanced" (there are an equal number of open and closed parentheses in the string)
    * Return -1 if the string is "broken" (a closing parens has not been proceeded by one that opens)


Sources: http://interactivepython.org/courselib/static/pythonds/BasicDS/SimpleBalancedParentheses.html
