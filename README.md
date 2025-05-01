
---

# Lung Cancer Prediction API with Makefile Automation

This project automates the training and deployment of a lung cancer prediction model using **Gradient Boosting** and a **Flask API**. It uses a **Makefile** to streamline setup, training, prediction, and cleanup tasks.

---

## Features

- **Makefile Automation**  
  Automates setup, training, predictions, and cleanup via simple terminal commands.

- **Gradient Boosting Classifier**  
  A high-performance model used for accurate lung cancer prediction.

- **RESTful Flask API**  
  Provides endpoints for training and making predictions.

- **Data Preprocessing**  
  Handles cleaning, feature engineering, and class imbalance correction.

---

## Makefile Commands (Windows Instructions)

Use the following commands in a terminal with `make` support (e.g., Git Bash):

### 1. Setup

Installs dependencies and creates a virtual environment:

```bash
make init
```

This command:
- Creates a virtual environment in the `venv` directory
- Upgrades `pip`
- Installs all dependencies listed in `requirements.txt`

### 2. Run Flask App

```bash
make run
```

Starts the Flask development server using the virtual environment.

### 3. Train Model

```bash
make train 
```

Arguments:
- `DATA_PATH`: Path to the dataset CSV file
- `MODEL_PATH`: Output path for the trained model
- `FEATURES_PATH`: Output path for the saved feature names

### 4. Make Prediction 
Default features: [60, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2]

```bash
make predict   
```
### Or custom FEATURES :
Example of custom features "55, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1"
```bash
Make Prediction FEATURES="[55, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1]" 
```

Arguments:
- `MODEL_PATH`: Path to the saved model
- `FEATURES_PATH`: Path to saved feature names
- `FEATURES`: Space-separated list of input values for prediction

### 5. Clean Environment

```bash
make clean
```

Removes generated files and folders:
- `venv/`
- `__pycache__/`

---

## API Endpoints

### 1. Train Model

- **Endpoint**: `/train`  
- **Method**: `POST`  
- **Request Body**:

```json
{
  "data_path": "data/survey_lung_cancer.csv",
  "model_save_path": "models/best_gboost_model.pkl",
  "feature_names_path": "models/feature_names.pkl"
}
```

- **Success Response**:

```json
{
  "message": "Model trained successfully",
  "result": {
    "accuracy": 0.9375,
    "best_params": {
      "learning_rate": 0.01,
      "max_depth": 3,
      "n_estimators": 200
    }
  }
}
```

### 2. Make Prediction

- **Endpoint**: `/predict`  
- **Method**: `POST`  
- **Request Body**:

```json
{
  "model_path": "models/best_gboost_model.pkl",
  "feature_names_path": "models/feature_names.pkl",
  "features": [60, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2]
}
```

- **Success Response**:

```json
{
  "prediction": [1],
  "result_label": "Present"
}
```

---

## Manual Setup (Without Makefile)

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

- Windows:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python run.py
```

---

## Dataset Format

The input dataset should be in CSV format and must contain the following columns:

- `AGE`
- `GENDER`
- `SMOKING`
- `ANXIETY`
- `YELLOW_FINGERS`
- `PEER_PRESSURE`
- `CHRONIC DISEASES`
- `FATIGUE`
- `ALLERGY`
- `WHEEZING`
- `ALCOHOL CONSUMPTION`
- `COUGHING`
- `LUNG_CANCER` (Target: 0 = Absent, 1 = Present)

---

## Example Usage

### Train the Model

```json
{
  "data_path": "data/survey_lung_cancer.csv",
  "model_save_path": "models/best_gboost_model.pkl",
  "feature_names_path": "models/feature_names.pkl"
}
```

### Make a Prediction

```json
{
  "model_path": "models/best_gboost_model.pkl",
  "feature_names_path": "models/feature_names.pkl",
  "features": [60, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2]
}
```

---

## Project Structure

```
project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
├── data/
│   └── survey_lung_cancer.csv
├── models/
│   ├── best_gboost_model.pkl
│   ├── feature_names.pkl
├── requirements.txt
├── run.py
├── Makefile
├── README.md
```

---

## Author

- Tasnim Mtir

---

## Acknowledgments

Here's a polished **Acknowledgments** section following your preferred format:

---

## Acknowledgments

This project utilizes these open-source technologies:

- [Scikit-learn](https://scikit-learn.org/) - Machine learning modeling and evaluation  
- [Imbalanced-learn](https://imbalanced-learn.org/) - Handling class imbalance in the dataset  
- [Flask](https://flask.palletsprojects.com/) - REST API development and deployment  
- [Pandas](https://pandas.pydata.org/) - Data preprocessing and feature engineering  
- [Joblib](https://joblib.readthedocs.io/) - Model serialization and loading  
- [Make](https://www.gnu.org/software/make/) - Build automation and task management  
