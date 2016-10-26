# Simple example to demonstrate the use of a Decision Tree from
# the scikit-learn library package.

# Uses a small dataset of 11 samples to predict the binary gender
# given inputs of height, weight, and shoe size.

from sklearn import tree

#Initialize the Decision Tree Classifier
clf = tree.DecisionTreeClassifier()

#list of [height, weight, shoe size] (dataset)
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
     [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#list of 'male' or 'female' corresponding to above dataset
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female',
     'female', 'female', 'male', 'male']

#Generates a model for the datasets
clf = clf.fit(X, Y);

height = input('Enter the height (in cm): ')
weight = input('Enter the weight (in kg): ')
shoe_size = input('Enter the Euro shoe size: ')
prediction = clf.predict([[height, weight, shoe_size]])

print(prediction[0])