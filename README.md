# Classifier

Classification using perceptron

## Description

The classifier's objective is to desipher a smartphone password input. It is trained using accelerometer data gathered from the phone, where each data point includes x and y values from the accelerometer alongside the corresponding numeric button press. This perceptron-based classifier can accurately determine the pressed button solely from the accelerometer data.

### _part_one_classifier(data_train,data_test)_

A simple binary classifier that can classify 2D data that is linearly separable.

The function receives:
- A bidimensional structure ```data_train``` of size ```TRAINING_SIZE x 3```. Every row contains a value for ```x``` in position 0, a value for for ```y``` in position 1 and a value for the class in position 2.
- A bidimensional structure ```data_test``` of size ```TEST_SIZE x 3```. Every row contains a value for ```x``` in position 0, a value for for ```y``` in position 1 and an empty space for the class in position 2.

The function modifies the third column of the ```data_test``` structure, by entering the right class of each element. Valid values for classes are 0 or 1.

### _part_two_classifier(data_train,data_test)_

A classifier that takes in the accelerometer training data and test data, and correctly classifies the test data.

The function receives:
- A bidimensional structure data_train of size ```TRAINING_SIZE x 3```. Every row contains a value for ```x``` in position 0, a value for for ```y``` in position 1 and a value for the class in position 2.
- A bidimensional structure ```data_test``` of size ```TEST_SIZE x 3```. Every row contains a value for ```x``` in position 0, a value for for ```y``` in position 1 and an empty space for the class in position 2.

The function modifies the third column of the ```data_test``` structure, by entering the right class of each element. Valid values for classes are 0 to 9.
