import common

def dot(vec1, vec2):
	return vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]

def subtract(vec1, vec2):
	vec1[0] -= vec2[0]
	vec1[1] -= vec2[1]
	vec1[2] -= vec2[2]

def add(vec1, vec2):
	vec1[0] += vec2[0]
	vec1[1] += vec2[1]
	vec1[2] += vec2[2]

def scale(vec1, num):
	vec1[0] *= num
	vec1[1] *= num
	vec1[2] *= num

def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	
	#Train
	weight = [0, 0, 0]
	change = True
	while(change):
		change = False
		for data in data_train:
			classification = None
			feature = [data[0], data[1], 1]
			if dot(weight, feature) >= 0:
				classification = 1
			else:
				classification = -1
			
			#Modify classes
			real_class = None
			if data[2] == 0:
				real_class = -1
			else:
				real_class = 1


			if classification != real_class:
				if real_class == -1:
					subtract(weight, feature)
				else:
					add(weight, feature)
				change = True
	
	#Test
	for data in data_test:
		classification = None
		feature = [data[0], data[1], 1]
		if dot(weight, feature) >= 0:
			data[2] = 1
		else:
			data[2] = 0
	return


def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	
	weights = common.init_data(10, 3)
	learning_rate = 0.01
	errors = 1000
	
	#Train
	while (errors/float(common.constants.TRAINING_SIZE) >= 0.05):
		errors = 0

		for data in data_train:
			
			feature = [data[0], data[1], 1]
			
			classification = None
			activation_score = float('-inf')
			
			for y in range(10):
				weight = weights[y]
				score = dot(weight, feature)
				if score > activation_score:
					activation_score = score
					classification = y

			if classification != data[2]:
				errors += 1
				scale(feature, learning_rate)
				subtract(weights[classification], feature)
				add(weights[int(data[2])], feature)

	#Test
	for data in data_test:
		feature = [data[0], data[1], 1]
		
		classification = None
		activation_score = float('-inf')
		
		for i in range(10):
			weight = weights[i]
			dot_prod = dot(weight, feature)
			if dot_prod > activation_score:
				activation_score = dot_prod
				classification = i
		
		data[2] = classification

	return
