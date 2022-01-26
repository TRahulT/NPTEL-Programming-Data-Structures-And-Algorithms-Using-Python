#What is h(60)-h(45), given the definition of h below?
def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)
print(h(60))#divisible sum[sum+i]
print(h(45))

print(107-32)