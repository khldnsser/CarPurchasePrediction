# -*- coding: utf-8 -*-
"""CarPurchasePrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12l0OlvSwjjF4s58m4MhEalFOcSn9Jj1I
"""

from google.colab import files
Car_data_file = files.upload()

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# We read the dataset into a datframe
dataset = pd.read_csv("car_data.csv")
print(dataset)

#We now want to change the categorical data into numerical values to feed them into neural network
#We also want to drop the User ID column becasue it is an unnecessary feature
le = LabelEncoder()
dataset["Gender"] = le.fit_transform(dataset["Gender"])
dataset = dataset.drop("User ID", axis=1)
print(dataset)

#We now want to prepare the data for training
'''what is random state'''


X = dataset[['Gender', 'Age', 'AnnualSalary']]
Y = dataset['Purchased']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# Standardize the features for better performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# We now build the model
# We use Sequential because it allows us to build a "sequential" stack of layers with one input tensor and one output tensor, which is ideal for feed-forward neural networks

model = Sequential()

model.add(Input(shape = (X_train.shape[1],)))

model.add(Dense(units=16, activation='relu'))

model.add(Dense(units=8, activation='relu'))

model.add(Dense(units=1, activation='sigmoid'))

# We now compile the model

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#We now train the model

model.fit(X_train,Y_train, epochs = 50, batch_size = 10, validation_data=(X_test,Y_test))

# Evaluate the model on the test data
test_loss, test_accuracy = model.evaluate(X_test, Y_test)
print("Test Accuracy:", test_accuracy)

#This is an Interactive demo generated by ChatGPT that'll query the model to get inference based on the input from the user.


def predict_purchase(model, scaler):
    # Step 1: Prompt the user for input
    gender = input("Enter Gender (Male/Female): ")
    age = int(input("Enter Age: "))
    annual_salary = float(input("Enter Annual Salary: "))

    # Step 2: Process the input data
    # Convert gender to numerical value
    if gender.lower() == "male":
        gender = 1
    elif gender.lower() == "female":
        gender = 0
    else:
        print("Invalid input for gender.")
        return

    # Create a DataFrame for the new data
    new_data = pd.DataFrame([[gender, age, annual_salary]], columns=['Gender', 'Age', 'AnnualSalary'])

    # Scale the data (using the same scaler fitted on the training data)
    new_data_scaled = scaler.transform(new_data)

    # Step 3: Make a prediction
    prediction = model.predict(new_data_scaled)

    # Convert the output to a binary class (0 or 1) based on a threshold
    predicted_class = int(prediction > 0.5)

    # Step 4: Display the result
    if predicted_class == 1:
        print("The model predicts that the person will purchase a car.")
    else:
        print("The model predicts that the person will NOT purchase a car.")


predict_purchase(model, scaler)