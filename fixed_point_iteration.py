from numpy import sqrt

"""
Given an equation f(x)=c, we are required to transform it
into a form x=g(x), such that |g'(x)|<1. This guarantees
convergence to a root.

In this code, the number of iterations is not user defined,
rather it is solely dependent on tolerance.
"""

def fpi(f,x0,tol):
  i = 0

  while True:
    i+=1
    x=f(x0)

    if abs(x-x0)<tol:
      return x,i
    
    x0 = x

if __name__=="__main__":
  #Solving x^3+x^2-1=0
  f = lambda x: x**3 + x**2 - 1
  g = lambda x: 1/sqrt(x+1)

  sol=fpi(g,0,0.001)
  print("Solution to x^3 + x^2 - 1 = 0\nx = {:5f}\tIterations: {}".format(sol[0],sol[1]))
