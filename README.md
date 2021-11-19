# OOP_EX1
This is the second assignment in the Object Oriented Programing course:
In this assignment we program an off-line algorithm for a smaart elevator system. In this README file I will provide a short explanation of the code and the documentation of it.
I couldn't find sufficiant scholar material for this assignment, so I will cite here the articles i cited in the last assignment:
A Stackoverflow thread with excellent discussion on how to design an elevator system: https://stackoverflow.com/questions/493276/modelling-an-elevator-usingobject-oriented-analysis-and-design
A GeeksforGeeks articles that briefly goes on the concept of a smart elevator system https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup
A Reddit thread with supportive questions on the way to build an elevator system: https://www.reddit.com/r/CS_Questions/comments/7zde0h/design_an_elevator_system

The algorithm itself works in a way of dynamic programming. after receiving the list of calls, we call the function 'Allocate' for each of them using a for loop. The allocation function is a basic minimum function that compares different times given to it by a function that each elevator runs: 'gettimeforcall'. this is where the dynamic programming comes into effect, as the class 'Elevator' has a list that keeps within it all the calls that are handled by the elevator, and a dictionary that keeps for every call the amount of time it would take for the elevator to finish that call. because of this dictionary, the function 'gettimeforcall' just calculates the time it would take for the elevator to finish this new call, and adds to it the times for all the other calls handled by the elevator. That way, we get a fairly accurate answer and save a lot of time avoiding nested loops or recursion.
