from Complexe import *

class Resistance:

    def __init__(self, v):
        # constructeur
        self.value = float(v)

    def __str__(self):
        # sous forme de chaine de caractere
        return "Resistance(%g)" % (self.value)

    def impedance(self, omega):
        return Complexe(self.value, 0)

if __name__ == "__main__" :
	r = Resistance(1e2)
	expected_result = Complexe(100, 0)
	result = r.impedance(314.16)
	print "got " + str(result) + ", expected " + str(expected_result)
	
	
	