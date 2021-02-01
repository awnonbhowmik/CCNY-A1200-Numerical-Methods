"""
This code does not involve 
"""
def bisection(f,a,b,N):
  if f(a)*f(b)>0:
    print("Bisection method fails!")
    return None
  
  for i in range(1,N+1):
    c=(a+b)/2

    if f(a)*f(c)>0:
      a=c
    elif f(a)*f(c)<0:
      b=c
    elif f(c)==0:
      return c
    
    else:
      print("Bisection method fails!")
      return None
    
  return (a+b)/2

f=lambda x: x**2-x-1
approx_phi = bisection(f,1,2,25)
print("Solution: {:5f}".format(approx_phi))

f=lambda x: x**3-x-1
sol = bisection(f,1,2,25)
print("Solution: {:5f}".format(sol))
