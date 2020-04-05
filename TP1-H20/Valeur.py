import Algo1
import Algo2
import Algo3 
import sys


def main(argv):
	size = 9
	print("SIZE = " + str(size))
	print("Algorithme 3 :")
	for i in range(1,6):
		for j in range(i,6):
			file = open("gen_matrix/ex_" + str(size) + "." + str(i), "r")
			n = file.readline()
			file.close()
			A = Algo3.readFile("gen_matrix/ex_" + str(size) + "." + str(i))
			B =  Algo3.readFile("gen_matrix/ex_" + str(size) + "." + str(j))
			Algo3.printTime(A,B)
	return
  
if __name__ == "__main__":
    main(sys.argv[1:])
