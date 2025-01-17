# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:19:53 2022

@author: brist
"""

'''
Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.

Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.

Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.

Complex Number Algebra - Show addition, multiplication, negation, and inversion of complex numbers in separate functions. (Subtraction and division operations can be made with pairs of these operations.) Print the results for each operation tested.

Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.

Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).

Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.

Limit Calculator - Ask the user to enter f(x) and the limit value, then return the value of the limit statement Optional: Make the calculator capable of supporting infinite limits.

Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.
'''

def find_pi(n, rounding=False):
    '''
    Return pi to n digits, truncating by default, with option 
    for rounding. Limit 6 digits (it's badly optimized!)

    Parameters
    ----------
    n : int
        Number of digits.
    rounding : bool, optional
        Whether the value should be rounded instead of
        truncated. The default is False.

    Returns
    -------
    An estimation of pi.

    '''
    digit_limit = 6
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n > digit_limit:
        raise ValueError('limit n to {}'.format(digit_limit))
    if n < 0:
        raise ValueError('n must be non-negative')
    if not isinstance(rounding, bool):
        raise TypeError('rounding must be assigned' +
                        'a bool value')
        
    # quick Gregory-Leibniz series
    pi = 0
    k = -1
    iterator = 10000000
    for i in range(iterator):
        k *= -1 # flip sign
        o = 1 + 2*i # next odd term
        pi += 4/(k*o) # sum
    
    if rounding == False:
        str1 = str(pi)
        str1 = str1[:n+2] # feels like cheating
        pi = float(str1)
    else:
        pi = round(pi, n)
    
    return pi
    

def find_e(n, rounding=False):
    '''
    Return e to n digits, truncating by default, with option 
    for rounding. Limit 14 digits (it's badly optimized!)

    Parameters
    ----------
    n : int
        Number of digits.
    rounding : bool, optional
        Whether the value should be rounded instead of
        truncated. The default is False.

    Returns
    -------
    An estimation of e

    '''
    digit_limit = 14
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n > digit_limit:
        raise ValueError('limit n to {}'.format(digit_limit))
    if n < 0:
        raise ValueError('n must be non-negative')
    if not isinstance(rounding, bool):
        raise TypeError('rounding must be assigned' +
                        'a bool value')
            
    # quick manual factorial define
    def factorial(x):
        output = 1
        for n in range(2, x+1):
            output *= n
        return output
    
    # now calculate e
    e = 0
    iterator = 100
    for i in range(iterator):
        e += 1/(factorial(i))
    
    if rounding == False:
        str1 = str(e)
        str1 = str1[:n+2] # feels like cheating
        e = float(str1)
    else:
        e = round(e, n)
    
    return e


def fibonacci(n, terms=None):
    '''
    Returns nth sequence in Fibonacci sequence
    Option to set first two terms as a list object

    Parameters
    ----------
    n : int
        Term to return in Fibonacci sequence.
    terms : list, optional
        First two terms of sequence. Will default to [0, 1]
        with no input from user.

    Returns
    -------
    Integer from Fibonacci sequence.

    '''
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n <= 0:
        raise ValueError('n must be positive')
    if terms is None:
        fib = [0, 1]
    elif not isinstance(terms, list):
        raise TypeError('terms must be list type')
    elif len(terms) != 2:
        raise ValueError('terms must be list of len 2')
    elif not all(isinstance(n, int) for n in terms):
        raise ValueError('both items in terms must be int type')
    else:
        fib = terms
    
    if n < 3:
        return fib[n-1]
    else:
        for i in range(n-2): 
            # weird behavior if user inputs 1 or 0... quick fix
            
            fib.append(fib[-2]+fib[-1])
        return fib[-1]
    
    
def prime_factors(x):
    '''
    Returns list of all prime factors of positive integer x

    Parameters
    ----------
    x : int
        Positive integer to factorize

    Returns
    -------
    List

    '''
    if not isinstance(x, int):
        raise TypeError('x must be integer')
    if x < 1:
        raise ValueError('x must be greater than 1')
    
    # special case for 1
    if x == 1:
        return [1]
    
    # otherwise assume 1 is there and start with 2+
    factors = [1] # add first factor
    dividend = x  # we will iterate through this, 
                  # dividing it by most recently found factor
    
    while(dividend != 1): # could be better without breaks maybe? but it works
        if len(factors) == 1:
            divisor = 2 # we don't want to start on one
        else:
            divisor = factors[-1] # make test divisor 
        for k in range(divisor, x+1): # need to iterate all the way to x
            if dividend % k == 0: # first divisor that yeilds 0 remainder
                factors.append(k) # add it to the list
                dividend = dividend / k # and set a new dividend
                break
        # if dividend == 1: # once we only have 1 remaining, stop
        #     break

    return factors



