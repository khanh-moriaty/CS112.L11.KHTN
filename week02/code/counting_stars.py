mum = 1
def ss(x, y , i, j):
    global a,b,c,d
    q = x[j] - x[i]
    p = y[j] - y[i]
    if q <= 0 or p <= 0 :
        return 0
    q = abs(q)
    p = abs(p)
    if p * b > q * a and p * d < q * c:
        return 1
    return 0
def _lis( x , y , n ): 
  
    # to allow the access of global variable 
    global maximum,res
  
    # Base Case 
    if n == 1 : 
        return 0
  
    # maxEndingHere is the length of LIS ending with arr[n-1] 
    maxEndingHere = 0
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    res.append(0)
    for i in range(n): 
        for j in range(i):
            if ss(x,y,i,j) :
                res[i] = max(res[i],res[j] + 1)
                #print(x[i],y[i],x[j],y[j])
    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
  
    return res[n-1]
def lis(x,y): 
  
    # to allow the access of global variable 
    global maximum 
  
    # lenght of arr 
    n = len(x) 
  
    # maximum variable holds the result 
    maximum = 0
    for i in range(n):
        res.append(0)
    # The function _lis() stores its result in maximum  
    return _lis(x, y , n)  
n = int(input())
s = input().split()
a,b = [int(x) for x in s[0].split('/')]
c,d = [int(x) for x in s[1].split('/')]
x = [0]
y = [0]
res = []
for i in range(n):
    x1,x2 = [int(x) for x in input().split()]
    x.append(x1)
    y.append(x2)
z = list(zip(x,y))
z = sorted(z, key=lambda w: w[0]*(10**5) + w[1],reverse = True )
x,y = zip(*z)
print(lis(x,y))
