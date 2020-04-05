import algo_glouton
import algo_voisinage
import algo_dynamique
import sys


def main(argv):
	if argv[0] == "glouton":
		algo_glouton.main(argv)
	elif argv[0] == "heuristique":
		algo_voisinage.main(argv)
	elif argv[0] == "dp":
		algo_dynamique.main(argv)
	return
  
if __name__ == "__main__":
    main(sys.argv[1:])
