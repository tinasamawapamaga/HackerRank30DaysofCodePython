#Read a string S, and print its integer value; 
#if S cannot be converted to an integer, print 'Bad String'
#I thought it was going to be harder
import sys

S = input().strip()
try: 
    print (int(S))
except ValueError: 
    print ("Bad String")
