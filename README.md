# Flights SQL Analytics App

This is a **Streamlit web application** that connects to a **MySQL database** to fetch and analyze flights data. It allows users to search for available flights, check sources/destinations, and visualize data analytics using Plotly charts.

## 🚀 Features
* **Check Flights:** Select source and destination cities to filter available flights.
* **Analytics Dashboard:** View data visualizations (line charts, scatter plots) powered by Plotly Express.
* **Database Driven:** Built-in dynamic data fetching using MySQL connector.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** MySQL
* **Visualizations:** Plotly Express

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd flights-sql-app
   ```

2. **Install the required packages:**
   ```bash
   pip install streamlit mysql-connector-python plotly pandas
   ```

3. **Database Configuration:**
   * Make sure your local MySQL server is running on `127.0.0.1`.
   * Create a database named `flights`.
   * Keep user as `root` and password empty `''` (or update them in `dbhelper.py`).

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```
