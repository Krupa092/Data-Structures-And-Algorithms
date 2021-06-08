"""
A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps at a time. 
Given that the staircase has a total n steps, 
write a function to count the number of possible ways in which child can run up the stairs.
For e.g.
n == 1 then answer = 1
n == 3 then answer = 4
The output is 4 because there are four ways we can climb the staircase:
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
3 steps
n == 5 then answer = 13
"""
def staircase(n):
    # Base Case - What holds true for minimum steps possible 
    # i.e., n == 1? Return the number of ways the child can climb one step.
    # Inductive Hypothesis - What holds true for n == 2 or n == 3?
    #  Return the number of ways to climb them.
    # Inductive Step (n > 3) - use Inductive Hypothesis to formulate a solution
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n-1) + staircase(n - 2) + staircase(n - 3)

def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case = [4, 7]
test_function(test_case)
test_case = [5, 13]
test_function(test_case)