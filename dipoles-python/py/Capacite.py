from Complexe import *

class Capacite(object):

    def __init__(self, v):
        # constructeur
        self.value = float(v)

    def __str__(self):
        # sous forme de chaine de caractere
        return "Capacite(%g)" % (self.value)

    def impedance(self, omega):
        return Complexe(0, -1 / (self.value*omega))

if __name__ == "__main__" :
	r = Capacite(42)
	expected_result = Complexe(0, 7.578789e-5)
	result = r.impedance(314.16)
	print "got " + str(result) + ", expected " + str(expected_result)
	
	
