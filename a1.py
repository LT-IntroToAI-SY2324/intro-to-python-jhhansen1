# """Assignment 1

# Fill in the following function skeletons - descriptions are provided in 
# the docstring (the triple quote thing at the top of each function)

# Some assert statements have been provided - write more of them to test your code!

# The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
# a function. They should be removed and replaced with your solution.

# This portion of the assignment will not be graded, but this gives you some problems to 
# check, if you do not complete the generative AI portion of the assignment.
# """

from typing import List, TypeVar


def absolute(n: int) -> int:
    if  n<0:
        return n*-1
    else:
        return(n)
    
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
#     raise NotImplementedError("absolute")


def factorial(n: int) -> int:
#     """Takes a number n, and computes the factorial n! You can assume the passed in
#     number will be positive
 x=n
 y=n
 while x>1:
    x=x-1
    y=y*(x)
 return y
    


#     Args:
#         n - the number to compute factorial of

#     Returns:
#         factorial of the passed in number
#     """
#     raise NotImplementedError("factorial")


T = TypeVar("T")


def every_other(lst: list[T]) -> list[T]:
#     """Takes a list and returns a list of every other element in the list, starting with
#     the first.
 x=0
 newLst=[]
 for r in range(len(lst)):
    if (r%2==0):
      newLst.append(lst[r])
 return newLst
   
#     Args:
#         lst - a list of any (constrained by type T to be the same type as the returned
#             list)

#     Returns:
#         a list of every of other item in the original list starting with the first
#     """
#     raise NotImplementedError("every_other")


def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    s=0
    for x in lst:
        s+=x
    return s 


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    x=0
    for el in lst:
        x+=el
    x=x/len(lst)
    return x


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    medianValue=0
    if len(lst)%2!=0:
     medianValue=lst[len(lst)//2]
    if len(lst)%2==0:
     medianValue=(lst[len(lst)//2]+lst[len(lst)//2-1])//2
    return medianValue


def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
    knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
    'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    counter=0
    while (len(lst)>2): 
       for i in range(3):
         counter+=1
         if counter>=len(lst):
           counter=0
       del(lst[counter])
    return lst
    
           
          
          

      

# # this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")