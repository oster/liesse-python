from Complexe import *

class Serie(object):

    def __init__(self, dipole1, dipole2):
        # constructeur
        self.d1 = dipole1
        self.d2 = dipole2

    def __str__(self):
        # sous forme de chaine de caractere
        return "Serie(" + self.d1 + ", " + self.d2 + ")"

    def impedance(self, omega):
        return self.d1.impedance(omega).add(self.d2.impedance(omega))

if __name__ == "__main__" :
	from Self import *
	from Resistance import *
	
	r = Serie(Self(5e-2), Resistance(1e2))
	expected_result = Complexe(100, 15.708)
	result = r.impedance(314.16)
	print "got " + str(result) + ", expected " + str(expected_result)
	
	
