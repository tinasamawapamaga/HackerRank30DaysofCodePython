#Write a Calculator class with a single method: int power(int,int). The power method takes two integers,  
#n and p, as parameters and returns the integer result of n^p.
#If either  or  is negative, then the method must throw an exception with the message:
# "n and p should be non-negative."

class Calculator: 
    def __init__(self):
        self=self
    def power(self,n,p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
