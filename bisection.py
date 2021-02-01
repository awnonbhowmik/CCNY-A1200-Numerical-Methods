def bisection(f,a,b,tol):
  if f(a)*f(b)>0:
    print("Bisection method fails!")
    return None
  
  i = 0
  while True:
    c=(a+b)/2
    i+=1

    if f(a)*f(c)>0:
      a=c
    elif f(a)*f(c)<0:
      b=c
    elif f(c)==0:
      return c
    
    else:
      print("Bisection method fails!")
      return None

    if abs(b-a)<tol:
      return c,i
    
  return (a+b)/2

if __name__=="__main__":
  f=lambda x: x**2-x-1
  approx_phi = bisection(f,1,2,0.001)
  print("Solution for x^2-x-1 = 0:\nx = {:5f}\tIterations: {}".format(approx_phi[0],approx_phi[1]))

  f=lambda x: x**3-x-1
  sol = bisection(f,1,2,0.001)
  print("Solution for x^3-x-1 = 0:\nx = {:5f}\tIterations: {}".format(sol[0],sol[1]))
