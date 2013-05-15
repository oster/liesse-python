from Complexe import *

class Self(object):

    def __init__(self, v):
        # constructeur
        self.value = float(v)

    def __str__(self):
        # sous forme de chaine de caractere
        return "Self(%g)" % (self.value)

    def impedance(self, omega):
        return Complexe(0, self.value*omega)

if __name__ == "__main__" :
	r = Self(7e-2)
	expected_result = Complexe(0, 21.9912)
	result = r.impedance(314.16)
	print "got " + str(result) + ", expected " + str(expected_result)
	
	
