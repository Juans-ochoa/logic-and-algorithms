"""
  if (test for the base case)
    return some the base case
  else if (test for another base case)
    return some for another base case
  ## The recursive case
  else
    return (some work and then recursive call)
"""


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(6))


def towersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
    if numberOfDisks:
        towersOfHanoi(numberOfDisks-1, startPeg, 6 - startPeg - endPeg)
        print('Move disk %d from peg %d to peg %d' %
              (numberOfDisks, startPeg, endPeg))
        towersOfHanoi(numberOfDisks - 1, 6-startPeg-endPeg, endPeg)


towersOfHanoi(4)


def isArrayInSortedOrder(array):
    if len(array) == 1:
        return True
    return array[0] <= array[1] and isArrayInSortedOrder(array[1:])


print(isArrayInSortedOrder([127, 220, 246, 277]))
print(isArrayInSortedOrder([127, 220, 246, 277, 32]))
