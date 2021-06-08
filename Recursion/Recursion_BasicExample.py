"""
Introduction
Recursion is a technique for solving problems where the solution to a particular problem depends on the solution to a smaller instance of the same problem.
Consider the problem of calculating  𝟸𝟻 . 
Let's assume to calculate this, you need to do one multiplication after another. 
That's  2∗2∗2∗2∗2 . We know that  25=2∗24 . 
If we know the value of  24 , we can easily calculate  25 .
We can use recursion to solve this problem, since the solution to the original problem ( 2𝑛 ) depends on the solution to a smaller instance ( 2𝑛−1 ) of the same problem. 
The recursive solution is to calculate  2∗2𝑛−1  for all n that is greater than 0. 
If n is 0, return 1. We'll ignore all negative numbers.
Let's look at what the recursive steps would be for calculating  25 .
25=2∗24 
25=2∗2∗23 
25=2∗2∗2∗22 
25=2∗2∗2∗2∗21 
25=2∗2∗2∗2∗2∗20 
25=2∗2∗2∗2∗2∗1
"""
def power_of_2(n):
    if n == 0:
        return 1
    return 2 * power_of_2(n - 1)

print(power_of_2(5))