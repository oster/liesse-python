from Complexe import *

class Parallele:

    def __init__(self, dipole1, dipole2):
        # constructeur
        self.d1 = dipole1
        self.d2 = dipole2

    def __str__(self):
        # sous forme de chaine de caractere
        return "Parallel(" + self.d1 + ", " + self.d2 + ")"

    def impedance(self, omega):
        c1 =  self.d1.impedance(omega)
        c2 =  self.d2.impedance(omega)
        return c1.inv().add(c2.inv()).inv()

if __name__ == "__main__" :
	from Self import *
	from Capacite import *
	from Resistance import *
	
	r = Parallele(Self(5e-2), Capacite(9e-4))
	expected_result = Complexe(0, -4.564497387210561)
	result = r.impedance(314.16)
	print "got " + str(result) + ", expected " + str(expected_result)

	r = Parallele(Resistance(1e2), Parallele(Self(5e-2), Capacite(9e-4)))
	expected_result = Complexe(0.2079131844185524, -4.55500719534011)
	result = r.impedance(314.16)
	print "got " + str(result) + ", expected " + str(expected_result)
	
	
