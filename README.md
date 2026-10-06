# 🤖 Gemini SQL Assistant

Gemini SQL Assistant is an AI-powered web application that allows users to interact with a SQLite database using **natural language**.

Instead of writing SQL queries manually, users can simply ask questions such as:

- "Show all students"
- "What is the minimum age of students?"
- "Show the details of student Sahithi"
- "How many students are there?"
- "Show students from AI & DS"

The application uses **Google Gemini API** to convert natural-language questions into SQL queries and executes those queries on a SQLite database.

---

## 🚀 Features

- 🗣️ Ask database questions in plain English
- 🤖 Automatically generate SQL queries using Gemini AI
- 🗄️ Execute generated SQL queries on SQLite
- 📊 Display query results in a user-friendly format
- ⚡ Simple and interactive Streamlit interface
- 🔐 API key stored securely using environment variables
- ❌ Prevents unnecessary manual SQL writing

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Google Gemini API**
- **SQLite**
- **SQL**
- **python-dotenv**

---

## 📂 Project Structure

```text
Gemini-SQL-Assistant/
│
├── app.py
├── database.py
├── .gitignore
├── requirements.txt
└── README.md
