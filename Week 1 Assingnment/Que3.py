#Consider the following function f:
def mys(m):
  if m == 1:
    return(1)
  else:
    return(m+mys(m-1))
#Which of the following is correct?
 # a)The function always terminates with mys(n) = factorial of n
 # b)The function always terminates with mys(n) = 1+2+...+n
 # c)The function terminates for positive n with mys(n) = factorial of n
 # d)The function terminates for positive n with mys(n) = 1+2+...+n
'''Answer'''
#example to verify 
print(mys(5))
# 15=5+4+3+2+1
print('1+2+3+....+n')
#print(mys(-5)) 

