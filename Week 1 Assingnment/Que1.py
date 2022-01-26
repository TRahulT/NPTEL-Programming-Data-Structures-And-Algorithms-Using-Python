#All questions carry equal weightage. All Python code is assumed to be executed using Python3.
 #You may submit as many times as you like within the deadline. Your final submission will be graded.
''' Question 1=What is the value of f(3456) for the function below?'''
def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/7,d+1)
    return(d)
print(f(3456))#answer
'''explanation:
while x>=1
1. x=3456/7 results=493.71 ,d=d+1=0+1=1
2. x=493.71/7 results=70.53,1+1=2
3. x=70.53/7  results=10.07,2+1=3
4. x=10.07/7 results=1.439,3+1=4
5. x=1.439/7 results=0.205,4+1=5
now condition terminates

x<1
ANSWER=5'''