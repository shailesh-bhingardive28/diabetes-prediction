# 🩺 Diabetes Prediction System

A Machine Learning based web application that predicts whether a person is likely to have diabetes based on medical input parameters.

The project uses a Support Vector Machine (SVM) model and provides an interactive prediction interface built with Streamlit.

## 📌 Project Overview

Diabetes is a common health condition that can be predicted using various medical parameters.

In this project, a machine learning classification model is trained on the **PIMA Indians Diabetes Dataset** to predict the diabetes outcome.

The complete workflow includes:

* Data loading and exploration
* Data preprocessing
* Feature standardization
* Model training
* Model evaluation
* Saving the trained model
* Building an interactive Streamlit application
* Deployment using Streamlit Community Cloud

## 🤖 Machine Learning Model

The project uses:

**Support Vector Machine (SVM)**

```text
Kernel: Linear
```

Before prediction, the input features are standardized using:

```text
StandardScaler
```

## 📊 Model Performance

| Metric            | Result |
| ----------------- | -----: |
| Training Accuracy | 78.66% |
| Testing Accuracy  | 77.27% |

## 📥 Input Features

The application accepts the following 8 features:

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

The model predicts:

```text
0 → Not Diabetic
1 → Diabetic
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Support Vector Machine
* StandardScaler
* Streamlit
* Jupyter Notebook
* Git
* GitHub

## 📁 Project Structure

```text
Diabetes-Prediction/
│
├── app.py
├── diabetes.csv
├── diabetes_model.sav
├── scaler.sav
├── requirements.txt
├── Diabetes.ipynb
├── .gitignore
└── README.md
```

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd diabetes-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🌐 Live Demo

🔗 **Live Application:**
shailesh-diabetes-prediction
.streamlit.app

## 💻 GitHub Repository

🔗 **GitHub:**
https://github.com/shailesh-bhingardive28/diabetes-prediction.git

## 📚 Learning Outcomes

Through this project, I learned and practiced:

* Machine Learning classification
* Data preprocessing
* Feature scaling
* SVM model implementation
* Model evaluation
* Model serialization
* Streamlit application development
* Git and GitHub
* ML model deployment

## ⚠️ Disclaimer

This application is developed for **educational and demonstration purposes only**. It should not be considered a substitute for professional medical diagnosis or advice.

## 👨‍💻 Author

**Shailesh Bhingardive**

Aspiring Data Scientist | Machine Learning Enthusiast

---

⭐ If you find this project useful, consider giving the repository a star!
