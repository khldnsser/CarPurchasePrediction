
# Car Purchase Prediction

This project is a machine learning model built to predict whether a person will purchase a car based on their demographic and financial data. The model is implemented using Python with Keras for the neural network and is designed to be run in a Google Colab or local environment.


## Installation

### Cloning the Repository

To set up the project locally, clone the repository:

```bash
git clone https://github.com/khldnsser/CarPurchasePrediction/
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
