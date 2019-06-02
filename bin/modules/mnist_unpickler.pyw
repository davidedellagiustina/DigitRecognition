import pickle

# MnistUnpickler class

class MnistUnpickler(object):

	# Function that pickles the arrays into a binary file

	@staticmethod
	def unpickle(source):
		with open(source, "rb") as f:
			mnist_training_data, mnist_test_data = pickle.load(f)
		return (mnist_training_data, mnist_test_data)