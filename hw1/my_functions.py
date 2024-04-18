# Gary Szczotka

def flmult(nums):
    """
    Multiplies the first and last values of an int list and returns the result
    Assumes there are at least 2 values in the list
    """
    f_val = nums[0]
    l_val = nums[-1]
    return f_val * l_val

def larger(val1, val2):
    """
    Returns the larger of val1 and val2
    """
    if val1 > val2:
        return val1
    else: return val2

nums1 = [5,4,3,8,6]
nums2 = [10,15]
nums3 = [50,3,4,44,19,24,76,2]

print(flmult(nums1)) # expected 30
print(flmult(nums2)) # expected 150
print(flmult(nums3)) # expected 100

print(larger(5,10)) # expected 10
print(larger(20,14)) # expected 20
print(larger(13,13)) # expected 13