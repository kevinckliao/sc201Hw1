"""
File: validEmailAddress.py
Name: 廖悠行
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: TODO:
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	count = 0
	maybe_email_list = read_in_data()
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		# TODO:
		score = 0
		for i in range(len(WEIGHT)):
			score += WEIGHT[i][0] * feature_vector[i] 
			valid_val = "Valid" if score > 0 else "Invalid"
			print("#{} {} , Score: {}".format(i+1,valid_val,score) )

def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [1] * len(WEIGHT)
	"""
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
		###################################
		#                                 #
		#              TODO:              #
		#                                 #
		###################################
	"""
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	f = open(DATA_FILE, "r")
	return f.readlines()


if __name__ == '__main__':
	main()
