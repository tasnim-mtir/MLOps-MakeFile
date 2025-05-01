# Lung Cancer Prediction API with Makefile Automation

This project focuses on automating the training and prediction workflow for a lung cancer prediction model using a **Makefile**. The model is built using the **Gradient Boosting (GBoost)** algorithm, and the API is implemented with Flask for seamless interaction.

---

## Features

- **Makefile Automation**:
  - Automates the setup, training, and prediction processes.
  - Simplifies running common tasks with a single command.
- **Gradient Boosting Classifier**:
  - A robust and efficient machine learning model for prediction.
- **RESTful API**:
  - Endpoints to train the model and make predictions.
- **Preprocessing**:
  - Handles data cleaning, feature engineering, and handling class imbalance.

---

## Makefile Commands (Windows Instructions)

The project includes a Makefile to automate the workflow. Below are the available commands and their usage instructions specifically for Windows users.

### 1. **Setup**
Installs all required dependencies.

```bash
make init
```

This will:
- Create a virtual environment in the `venv` folder.
- Upgrade `pip`.
- Install all the required dependencies from `requirements.txt`.

### 2. **Run**
Runs the Flask application.

```bash
make run
```

This will:
- Use the virtual environment to execute the `run.py` script, starting the Flask server.

### 3. **Train**
Trains the Gradient Boosting model using the specified dataset and saves the trained model.

```bash
make train DATA_PATH=data/survey_lung_cancer.csv MODEL_PATH=models/best_gboost_model.pkl FEATURES_PATH=models/feature_names.pkl
```
- **DATA_PATH**: Path to the dataset CSV file.
- **MODEL_PATH**: Path to save the trained model.
- **FEATURES_PATH**: Path to save the feature names used during training.

### 4. **Predict**
Makes a prediction using the trained model and given feature input.

```bash
make predict MODEL_PATH=models/best_gboost_model.pkl FEATURES_PATH=models/feature_names.pkl FEATURES="45 1 1 1 0 1 0 1 1 1 0 1"
```
- **MODEL_PATH**: Path to the trained model.
- **FEATURES_PATH**: Path to load the feature names.
- **FEATURES**: Space-separated list of input feature values for prediction.

### 5. **Clean**
Cleans up generated files (e.g., logs, temporary files, etc.).

```bash
make clean
```

This will:
- Remove the `venv` folder.
- Remove the `__pycache__` folder.

---

## Endpoints

### 1. **Train Model**

**Endpoint**: `/train`

**Method**: `POST`

**Request Body**:
```json
{
  "data_path": "Path to the dataset CSV file",
  "model_save_path": "Path to save the trained model",
  "feature_names_path": "Path to save the feature names"
}
```

**Response**:
- On success:
  ```json
  {
    "message": "Model trained successfully",
    "result": {
      "accuracy": 0.9375598086124401,
      "best_params": {
        "learning_rate": 0.01,
        "max_depth": 3,
        "n_estimators": 200
      }
    }
  }
  ```
- On failure:
  ```json
  {
    "error": "Error message"
  }
  ```

---

### 2. **Predict**

**Endpoint**: `/predict`

**Method**: `POST`

**Request Body**:
```json
{
  "model_path": "Path to the trained model",
  "feature_names_path": "Path to the saved feature names",
  "features": [Feature values as an array]
}
```

**Response**:
- On success:
  ```json
  {
    "prediction": [1],
    "result_label": "Present"
  }
  ```
- On failure:
  ```json
  {
    "error": "Error message"
  }
  ```

---

## Setup

### 1. Install Dependencies
If you are not using the `Makefile`, manually install the dependencies with:
```bash
pip install -r requirements.txt
```

### 2. Run the Application
Start the Flask app:
```bash
python run.py
```

---

## Dataset Format

The dataset must be in CSV format and include the following columns:
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
- `LUNG_CANCER` (Target variable: 0 = Absent, 1 = Present)

---

## Example Usage

### Train the Model
Send a POST request to `/train` with the following JSON body:
```json
{
  "data_path": "data/survey_lung_cancer.csv",
  "model_save_path": "models/best_gboost_model.pkl",
  "feature_names_path": "models/feature_names.pkl"
}
```

### Make a Prediction
Send a POST request to `/predict` with the following JSON body:
```json
{
  "model_path": "models/best_gboost_model.pkl",
  "feature_names_path": "models/feature_names.pkl",
  "features": [60, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2]
}
```

**Response**:
```json
{
  "prediction": [1],
  "result_label": "Present"
}
```

---

## File Structure
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
├── README.md
```

---

## Authors

- **Tasnim Mtir** - Initial work
---

## Acknowledgments

- [Scikit-learn](https://scikit-learn.org/)
- [Imbalanced-learn](https://imbalanced-learn.org/)
- [Flask](https://flask.palletsprojects.com/)