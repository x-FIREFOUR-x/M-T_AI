import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skfuzzy.fuzzymath as fuzzmath


#-------------------------------1---------------------------------
def triangle(x, a, b, c):
    f = fuzz.trimf(x, [a, b, c])
    plt.plot(x, f)
    plt.title(f"trimf(x,P) P=[{a}, {b}, {c}]")
    plt.show()

def trapezoid(x, a, b, c, d):
    f = fuzz.trapmf(x, [a, b, c, d])
    plt.plot(x, f)
    plt.title(f"trapmf(x,P) P=[{a}, {b}, {c}, {d}]")
    plt.show()


#-------------------------------2---------------------------------
def gauss(x, z, G):
    f = fuzz.gaussmf(x, z, G)
    plt.plot(x, f)
    plt.title(f"gauss(x,P) P=[{z}, {G}]")
    plt.show()

def gauss2side(x, z1, G1, z2, G2):
    f = fuzz.gauss2mf(x, z1, G1, z2, G2)
    plt.plot(x, f)
    plt.title(f"gauss2(x,P) P=[{z1}, {G1}, {z2}, {G2}]")
    plt.show()


#-------------------------------3---------------------------------
def bell(x, a, b, c):
    f = fuzz.gbellmf(x, a, b, c)
    plt.plot(x, f)
    plt.title(f"Bell(x,P) P=[{a}, {b}, {c}]")
    plt.show()


#-------------------------------4---------------------------------
def sigma(x, a, c):
    f = fuzz.sigmf(x, a, c)
    plt.plot(x, f)
    plt.title(f"Sigma(x,P) P=[{a}, {c}]")
    plt.show()

def Dsigma(x, a1, c1, a2, c2):
    f = fuzz.dsigmf(x, a1, c1, a2, c2)
    plt.plot(x, f)
    plt.title(f"DSigma(x,P) P=[{a1}, {c1}, {a2}, {c2}]")
    plt.show()

def Psigma(x, a1, c1, a2, c2):
    f = fuzz.psigmf(x, a1, c1, a2, c2)
    plt.plot(x, f)
    plt.title(f"PSigma(x,P) P=[{a1}, {c1}, {a2}, {c2}]")
    plt.show()


#-------------------------------5---------------------------------
def zmf(x, a, b):
    f = fuzz.zmf(x, a, b)
    plt.plot(x, f)
    plt.title(f"Z-function(x,P) P=[{a}, {b}]")
    plt.show()

def pimf(x, a, b, c, d):
    f = fuzz.pimf(x, a, b, c, d)
    plt.plot(x, f)
    plt.title(f"PI-function(x,P) P=[{a}, {b}, {c}, {d}]")
    plt.show()

def smf(x, a, b):
    f = fuzz.smf(x, a, b)
    plt.plot(x, f)
    plt.title(f"S-function(x,P) P=[{a}, {b}]")
    plt.show()


#-------------------------------6---------------------------------
def maxf(x, y1, y2):
    z1, z2 = fuzzmath.fuzzy_or(x, y1, x, y2)
    z3, z4 = fuzzmath.fuzzy_and(x, y1, x, y2)
    plt.plot(z1, z2, color='blue')
    plt.plot(z3, z4, linestyle='--', color='blue')
    plt.title(f"Max(or)")
    plt.show()

def minf(x, y1, y2):
    z1, z2 = fuzzmath.fuzzy_and(x, y1, x, y2)
    z3, z4 = fuzzmath.fuzzy_or(x, y1, x, y2)
    plt.plot(z1, z2, color='blue')
    plt.plot(z3, z4, linestyle='--', color='blue')
    plt.title(f"Min(and)")
    plt.show()


#-------------------------------7---------------------------------
def interMaxf(x, y1, y2):
    y = y1 + y2 - (y1 * y2)
    plt.plot(x, y)
    plt.plot(x, y1, linestyle='--')
    plt.plot(x, y2, linestyle='--')
    plt.title(f"interpretation Max(or)")
    plt.show()

def interMinf(x, y1, y2):
    y = y1 * y2
    plt.plot(x, y)
    plt.plot(x, y1, linestyle='--')
    plt.plot(x, y2, linestyle='--')
    plt.title(f"interpretation Min(and)")
    plt.show()


#-------------------------------8---------------------------------
def notf(x, y1):
    y = fuzz.fuzzy_not(y1)
    plt.plot(x, y)
    plt.plot(x, y1, linestyle='--')
    plt.title(f" not")
    plt.show()



if __name__ == '__main__':
   x = np.arange(-10, 11, 0.25)
   triangle(x, -5, 0, 6)
   trapezoid(x, -4, 1, 6, 9)
   gauss(x, 0, 5)
   gauss2side(x, 0, 5, 2, 8)
   bell(x, 7, 3, 0)
   sigma(x, -5, 3)
   Dsigma(x, -5, 3, 5, 2)
   Psigma(x, -5, 3, 5, 2)
   zmf(x, 0, 3)
   pimf(x, 1, 3, 5, 8)
   smf(x, 0, 3)
   maxf(x, fuzz.gaussmf(x, 0, 5),  fuzz.gaussmf(x, 5, 5))
   minf(x, fuzz.gaussmf(x, 0, 5), fuzz.gaussmf(x, 5, 5))
   interMaxf(x, fuzz.gaussmf(x, 0, 5), fuzz.gaussmf(x, 5, 5))
   interMinf(x, fuzz.gaussmf(x, 0, 5), fuzz.gaussmf(x, 5, 5))
   notf(x, fuzz.gaussmf(x, 0, 5))


