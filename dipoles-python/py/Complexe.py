from math import sqrt, atan2

class Complexe(object):

    def __init__(self, re, im):
        # constructeur
        self.re = float(re) # partie reelle
        self.im = float(im) # partie imaginaire
            
    def __str__(self):
        # sous forme de chaine de caractere
        return "%g + %gi" % (self.re,self.im)
        
    def add(self, other):
        return Complexe(self.re + other.re, self.im + other.im)
        
    def sub(self, other):
        return Complexe( self.re - other.re, self.im - other.im)
        
    def mul(self, other):
        return Complexe(self.re*other.re - self.im*other.im,  self.re*other.im + self.im*other.re)
        
    def div(self, other):
        denominator = other.re ** 2 + other.im ** 2
        return Complexe( \
            (self.re * other.re + self.im * other.im) / denominator,
            (self.im * other.re - self.re * other.im) / denominator )
            
    def conj(self):
        return Complexe(self.re, -self.im)
        
    def abs(self):
        return sqrt(self.re ** 2 + self.im ** 2)
        
    def arg(self):
        return atan2(self.im, self.re)
        
    def inv(self):
	    m = self.re ** 2 + self.im ** 2
	    return Complexe(self.re / m, - self.im / m)
	
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        #return self.im == other.im and self.re == other.re

    def __ne__(self, other): 
	    return not self == other

if __name__ == "__main__" :
    from math import pi
    
    x = Complexe(0, 1)
    y = Complexe(1, 0)
    z = Complexe(1, 1)
    
    print "x =", x
    print "y =", y
    print "z =", z
    print
    
    print "x + y =", z
    print "x - y =", x.sub(y)
    print "x * y =", x.mul(y)
    print "x * z =", x.mul(z)
    print "x / x =", x.div(x)
    print "x / z =", x.div(z)
    print "conj(z) =", z.conj()
    print "abs(z)**2 =", z.abs()**2
    print "check:", z.mul(z.conj())
    print "arg(z) =", z.arg() * 180/pi
    print "inv(x) = ", x.inv()
    print "inv(y) = ", y.inv()
    print "inv(z) = ", z.inv()
