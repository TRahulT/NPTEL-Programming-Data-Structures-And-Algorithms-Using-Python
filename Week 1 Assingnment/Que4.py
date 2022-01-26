#For what value of n would g(375,n) return 4?
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)
# (res,m)=(res+1,m/n)
# (0,375)=(0+1,375/n)
#mention in the question res=4 we have to find n?
#res = 4 means we have to divde m/n**4 the conditon true
#so the answer is 375/256=1.46 but if we divide with 625 it becomes 0.6 m<n false 
print(g(375,4))