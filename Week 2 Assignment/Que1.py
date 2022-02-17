'''Write a function repfree(s) that takes as input a string s and checks whether 
any character appears more than once. The function should return True if there 
are no repetitions and False otherwise.'''
def repfree(s):
    for point in range(len(s)):
        for j in range(point+1,len(s)):
            if s[point]==s[j]:
                return False
    return True
s1=[2,4,54,2,1,5]
print(repfree(s1))