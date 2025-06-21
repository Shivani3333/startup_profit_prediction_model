
## 🧠 Project Overview

This project uses the **Startup Profit Prediction dataset** to explore how different types of spending affect a startup’s profit. The goal is to build a simple machine learning model that can predict profit based on:

* R\&D Spend
* Administration Cost
* Marketing Spend

The app is built using **Streamlit**, allowing users to enter input values and get instant predictions from the trained model.

The results are **independent of the startup's city**, as shown in the exploratory analysis and plots.

---

## 📊 About the Dataset

Each row in the dataset represents one startup and includes the following columns:

* **R\&D Spend**: Money spent on research and development
* **Administration**: Money spent on admin work (salaries, rent, etc.)
* **Marketing Spend**: Money spent on advertising and promotions
* **State**: The location of the startup (e.g., California, Florida)
* **Profit**: The actual profit earned by the startup

This dataset is commonly used in beginner-level machine learning tutorials for practicing **Linear Regression**. It’s simple and helps demonstrate how input features relate to a target variable (profit).

---

## 🛠️ Tech Stack Used

* **Python**
* **Pandas, NumPy** – data handling
* **Matplotlib, Seaborn** – data visualization
* **Scikit-learn** – machine learning (Linear Regression)
* **Pickle** – saving the trained model
* **Streamlit** – creating the web application

---


### 🖥️ Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/Shivani3333/startup_profit_prediction_model.git
   cd startup_profit_prediction_model
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate       # For Windows  
   # OR  
   source venv/bin/activate    # For macOS/Linux
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`.

---

### 🌐 Run Online (Streamlit Cloud)

You can also access the app online here:
🔗 [Open the Startup Profit Prediction App](https://startupprofitpredictionmodel-abcxyz.streamlit.app/)

##APPS visuals
![image](https://github.com/user-attachments/assets/e84f5c68-6f29-4f03-a947-615d4ef0be5f)


