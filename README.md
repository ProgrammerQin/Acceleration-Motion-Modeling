# Acceleration_Motion_Linear_Model

Suppose object A is traveling towards object B with a speed v. A and B are separated by a distance d. 
If A is decelerating by a value of a , we want to determine if it will hit the object B. 
The user must provide the following values d, v and a. 
d is in the range [5,10]
a is in the range [-100,0]
v is in the range [1,10]

The distance travelled by the object A in time t (a positive number less than 10 that is also
to be received from the user) can be calculated as
𝑠 = max(0, 𝑣𝑡 + 0.5𝑎𝑡!)
If s is greater than or equal to d then the object will collide. 

Write a python program that does the following: 
(i) determines if the objects collide for a given set of d, v, a and t. 
(ii) for a given value of d and v, and starting with a = -50, 
determines the critical value of a at which A will just touch B.

Hint: To find the critical value of a, keep increasing a by a small amount (example, 0.2 ), and for each
value of a scan through a long range of t to conclusively establish if the object A hits B or not. Note: All
values are floating point data.

