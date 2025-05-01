# Variables
VENV = venv
PYTHON = $(VENV)\Scripts\python
PIP = $(VENV)\Scripts\pip

# Default paths
DATA_PATH = data/survey_lung_cancer.csv
MODEL_PATH = models/best_gboost_model.pkl
FEATURES_PATH = models/feature_names.pkl

.PHONY: init
init:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: run
run:
	$(PYTHON) run.py

.PHONY: train
train:
	$(PYTHON) -m flask train --data_path=$(DATA_PATH) --model_save_path=$(MODEL_PATH) --feature_names_path=$(FEATURES_PATH)

.PHONY: predict
predict:
	$(PYTHON) -m flask predict --model_path=$(MODEL_PATH) --feature_names_path=$(FEATURES_PATH) --features=$(FEATURES)

.PHONY: clean
clean:
	rmdir /s /q __pycache__
	rmdir /s /q $(VENV)