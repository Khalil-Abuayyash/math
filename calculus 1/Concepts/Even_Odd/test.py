import operator
import functools
import time

nums = list(range(1, 100000))

# Using reduce with operator.mul
start = time.time()
functools.reduce(operator.mul, nums)
print("Reduce:", time.time() - start)

# Using a for loop
start = time.time()
result = 1
for num in nums:
    result *= num
print("For-loop:", time.time() - start)
