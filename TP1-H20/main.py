import Algo3
import Algo2
import Algo1
import sys


def main(argv):
	if argv[0] == "conv":
		Algo1.main(argv)
	elif argv[0] == "strassen":
		Algo2.main(argv)
	elif argv[0] == "strassenSeuil":
		Algo3.main(argv)
	return
  
if __name__ == "__main__":
    main(sys.argv[1:])
