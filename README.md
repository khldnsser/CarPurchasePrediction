
# Car Purchase Prediction

This project is a machine learning model built to predict whether a person will purchase a car based on their demographic and financial data. The model is implemented using Python with Keras for the neural network and is designed to be run in a Google Colab or local environment.

## Project Structure

```
CarPurchasePrediction/
├── README.md                   # Project documentation
├── data/
│   └── car_data.csv            # Dataset for training and testing the model
├── notebook/
│   └── CarPurchasePrediction.ipynb  # Jupyter notebook with the complete workflow
├── requirements.txt            # List of dependencies for the project
└── src/
    └── carpurchaseprediction.py # Python script for the model
```

## Installation

### Cloning the Repository

To set up the project locally, clone the repository:

```bash
git clone https://github.com/<YOUR_USERNAME>/CarPurchasePrediction.git
cd CarPurchasePrediction
```

### Setting Up the Virtual Environment

1. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Dataset

The dataset, `car_data.csv`, is located in the `data/` folder and includes the following columns:

- **User ID**: A unique identifier for each user (not used in the model).
- **Gender**: Gender of the user (categorical feature).
- **Age**: Age of the user.
- **AnnualSalary**: The user's annual salary.
- **Purchased**: Target variable indicating whether the user purchased a car (1 for Yes, 0 for No).

## Model

The model is a feed-forward neural network built with Keras and has the following architecture:

- **Input layer**: Accepts three features (Gender, Age, AnnualSalary).
- **Hidden layers**: Two fully connected layers with ReLU activation.
- **Output layer**: A single neuron with sigmoid activation for binary classification.

### Model Training

The model is trained using binary cross-entropy loss and the Adam optimizer. The dataset is split into training and testing sets (80% training, 20% testing).

### Explanation of `random_state`

In `train_test_split`, the `random_state` parameter is used to ensure consistent data splitting for reproducibility, so each run of the code produces the same training and test sets.

## Running the Model

### Using the Jupyter Notebook

To run the model in a Jupyter notebook environment, open `notebook/CarPurchasePrediction.ipynb` in Google Colab or a local Jupyter environment and execute the cells sequentially.

### Running the Script

To run the model from the command line, execute:

```bash
python src/carpurchaseprediction.py
```

## Interactive Prediction Demo

The project includes an interactive function, `predict_purchase`, which allows you to enter a person's demographic data (gender, age, and annual salary) to get a prediction on whether they are likely to purchase a car.

### Running the Interactive Demo

You can run the demo by executing the following code within the script:

```python
def predict_purchase(model, scaler):
    # Prompt the user for input and preprocess the data
    ...
    # Make a prediction based on the input data
    ...
```

## Requirements

All required libraries are listed in `requirements.txt`. Key libraries include:
- `numpy`
- `pandas`
- `scikit-learn`
- `tensorflow`

To install dependencies, run:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.
