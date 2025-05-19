# 🛠 Predictive Maintenance System (Flask Web App)

This is a machine learning-based web application that predicts machine failure using real-time sensor inputs. Built with **Flask**, the app uses a **Random Forest Classifier** trained on predictive maintenance data.

---

## 🚀 Features

- Predicts equipment failure based on 8 real-time sensor inputs.
- Web interface built with Flask and styled with CSS.
- Integrates a trained ML model (`rf_model.pkl`) using joblib.
- Fully deployable on Render or Heroku.

---

## 📂 Project Structure

```
predictive-maintenance-system/app
│
├── app.py                  # Flask backend
├── rf_model.pkl            # Trained machine learning model
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment (Render/Heroku)
├── templates/
│   └── index.html          # Web form
├── static/
│   └── style.css           # CSS styling
└── README.md               # Project documentation
```

---

## 💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/predictive-maintenance-app.git
cd predictive-maintenance-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000/`

---

## 🌐 Deployment on Render

1. Push your project to a GitHub repository.
2. Create a free Render account at [render.com](https://render.com).
3. Create a **new web service** and connect your repo.
4. Fill in:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3.x
5. Click **Deploy**.

---

## 📊 Model Details

- **Algorithm**: Random Forest Classifier
- **Accuracy**: 99.7%
- **Metrics**: Precision = 94%, Recall = 97%, F1-score = 95%
- **Trained On**: Preprocessed machine sensor data (`processed_data.csv`)
- **Features**: Temperature, Torque, Tool Wear, Rotational Speed, etc.

---

## 📧 Contact

Built by Abhimantr Singh  
📫 Email: abhimantrsingh@gmail.com  
🏫 VIT Chennai | Dept. of CSE

---

## 📄 License

This project is for educational and demonstration purposes only.
