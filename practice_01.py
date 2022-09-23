'''
Q.1. Compute and return the square root of x, where x is guaranteed to be a non-negative
integer. And since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned. Also, talk about the time complexity of your
code.
Test Cases:
Input: 4
Output: 2
Input: 8
Output: 2
Explanation: The square root of 8 is 2.8284...., the decimal part is truncated and 2 is
returned.'''


def Square_root(n):
    s = 0
    e = n
    ans = -1
    while(s <= e):
        mid = s+(e-s) // 2
        if(mid * mid == n):
            return mid
        elif(mid*mid > n):
            e = mid-1
        else:
            s = mid+1
            ans = mid
    return ans


'''
Q.2. You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.
Test Cases:
Input: [0,0,0,1,1,1,1,1,1]
Output: 3
Explanation: 0 indicates a good version and 1 indicates a bad version. So, the index of
the first 1 is at 3. Thus, the output is 3
'''


def firstocc(num, low, high, target):
    ans = -1
    while(low <= high):
        mid = low+(high-low) // 2
        if num[mid] == target:
            ans = mid
            high = mid-1
        elif target < mid:
            high = mid - 1
        else:
            low = mid + 1
    return ans




#arr = [4,1,9,2,3,6]
# l=selection_sort(arr)
# for i in range(0,len(arr)):
#print(arr[i], end = " ")
'''
Q.3. Given a positive integer num, write a program that returns True if num is a perfect
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code.
Test Cases:
Input: 16
Output: True
Input: 14
Output: False
'''

def Perfect_Square_root(n):
    s = 0
    e = n
    ans = -1
    while(s <= e):
        mid = s+(e-s) // 2
        if(mid * mid == n):
            return mid
        elif(mid*mid > n):
            e = mid-1
        else:
            s = mid+1





num = [5, 7, 7, 8, 8, 10]
target = 8
low = 0
high = len(num)-1
a = firstocc(num, low, high, target)
print(a)
b = Square_root(26)
print(b)
n=25
if Perfect_Square_root(n)==None:
  print(False)
else:
   print(True)
