import pickle

# AnnUnpickler class

class AnnUnpickler(object):

	# Function that unpickles the given ANN pickled file

	@staticmethod
	def unpickle(source):
		with open(source, "rb") as f: ann = pickle.load(f)
		return ann