def countdown(n):
    '''A countdown using recursion'''
    print('Entering countdown(', n, ')')
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)
    print('Exiting from countdown(', n, ')')

def countup(n):
    '''prints 'Blastoff!' followed by the numbers 1 to n on separate lines'''
    if n == 0:
        print('Blastoff!')
    else:
        countup(n - 1)
        print(n)

def countdownBy2(n):
    '''counts down in increments of 2'''
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdownBy2(n - 2)

def digitalSum(n):
    '''The digital sum of a number n is the sum of its digits.
    this takes a positive integer n and returns its digital sum.'''
    if n < 10:
        return n
    else:
        return digitalSum(n%10) + digitalSum(n//10)

def digitalRoot(n):
    '''The digital root of a non-negative integer n is computed as follows.
    Begin by summing the digits of n. The digits of the resulting number are then summed,
    and this process is continued until a single-digit number is obtained.'''
    if n < 10:
        return n
    else:
        return digitalRoot(digitalSum(n))

def gcd(a, b):
    '''computes the greatest common divisor of two numbers'''
    if b == 0: return a
    return gcd(b, a % b)

def hailstone(n):
    '''The hailstone sequence starting at a positive integer n is generated by following two simple rules.
    If n is even, the next number in the sequence is n/2. If n is odd, the next number in the sequence is 3*n+1.
    Repeating this process, we generate the hailstone sequence. It stops when the sequence reaches the number 1.'''
    print(int(n))
    if n==1:
        return
    elif n%2==0:
        hailstone(n/2)
    elif n%2==1:
        hailstone(3*n+1)

def nestedListSum(NL):
    '''Computing the sum of the elements in a nested list.'''
    if isinstance(NL, int):     # case (a): NL is an integer
        return NL               # base case

    sum = 0                     # case (b): NL is a list of nested lists
    for i in range(0, len(NL)): # add subsums from each part of the main list
        sum = sum + nestedListSum(NL[i])
    return sum                  # all done

def nestedListContains(NL, target):
    '''takes a nested list NL of integers and an integer target,
    and indicates whether target is contained anywhere in the nested list.'''
    if isinstance(NL, int):
        if NL == target:
            return True
        else:
            return
    if isinstance(NL, list):
        for i in range(len(NL)):
            contains = nestedListContains(NL[i], target)
            if (contains==True):
                return True
    return(False)

def ruler(n):
    '''produces a recursive ruler-like design'''
    if n==1:
        print('-')
    else:
        ruler(n-1)
        print(n*'-')
        ruler(n-1)