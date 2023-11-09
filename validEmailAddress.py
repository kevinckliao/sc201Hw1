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
		score = 0
		for i in range(len(WEIGHT)):
			score += WEIGHT[i][0] * feature_vector[i] 
			valid_val = "Valid" if score > 0.1 else "Invalid"
		print("{:20.16f}  {:8} {:40}    {}-{}".format(
			score, valid_val, maybe_email, feature_vector[0:5], feature_vector[5:] ))

def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	
	for i in range(len(feature_vector)):
		if i == 0: # in str
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1: # no . befire @
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
		elif i == 2: # str before @
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[0] != "" else 0
		elif i == 3: # str after @
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[-1] != "" else 0
		elif i == 4: # . after @
			if feature_vector[0]:
				feature_vector[i] = 1 if "." in maybe_email.split('@')[-1]  else 0
		elif i == 5: # with space
			feature_vector[i] = 1 if " " in maybe_email else 0
		elif i == 6: # end with .com
			feature_vector[i] = 1 if maybe_email[-4:] == ".com" else 0
		elif i == 7: # end with .edu
			feature_vector[i] = 1 if maybe_email[-4:] == ".edu" else 0
		elif i == 8: # end with .com
			feature_vector[i] = 1 if maybe_email[-3:] == ".tw" else 0
		elif i == 9: # length > 10
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0
	#print ( feature_vector )
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	with open(DATA_FILE, "r") as f:
		lines = f.readlines()
		# *remove invisible such as \n or space at begin/end of line
		return [line.strip() for line in lines]


if __name__ == '__main__':
	main()
