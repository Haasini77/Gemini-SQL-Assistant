import streamlit as st
import os
import sqlite3
import time
from dotenv import load_dotenv  #python to read values from a env. file
from google import genai
from google.genai.errors import ServerError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)  #creates gemini client


#create the basic streamlit page
st.set_page_config(
    page_title="Gemini SQL Assistant",
    page_icon="🤖"
)

# Simple UI styling
st.markdown("""
<style>
    .main {
        max-width: 900px;
        margin: auto;
    }

    h1 {
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 35px;
    }

    .stButton > button {
        width: 200px;
        border-radius: 8px;
        height: 45px;
        font-size: 16px;
    }

    .result-box {
        padding: 15px;
        border-radius: 8px;
        background-color: #f5f5f5;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)


st.title("🤖 Gemini SQL Assistant")

st.markdown(
    '<p class="subtitle">Ask questions about your database in plain English</p>',
    unsafe_allow_html=True
)


#create the question input
question = st.text_input(
    "Enter your question:",
    placeholder="Example: How many AI & DS students are there?"
)

submit = st.button("🔍 Generate SQL Query")


if submit:

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    prompt = f"""
   You are an SQL query generator
   
   The database contaains a table called students with these columns
   -id
   -name
   -age
   -branch
   
   Genearte a SQLite SQL query for the users question
   IMPORTANT:
   -Use ONLY the columns listed above.
   -Do not invent column names.
   -The branch column contains values such aas 'AI & DS'.
   -Return ONLY the SQL query ,nothing else.

    Question: {question}

    """

    #generate the sql query
    response = None

    for attempt in range(3):
        try:
            response = client.models.generate_content(
              model="gemini-3.5-flash-lite",
                contents=prompt
            )
            break

        except ServerError:
            if attempt < 2:
                time.sleep(5)
            else:
                st.error("Gemini is temporarily unavailable. Please try again after a few seconds.")
                st.stop()

    sql_query = response.text.strip()

    # Remove markdown code fences
    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip()

    st.subheader("Generated SQL Query")
    st.code(sql_query, language="sql")

    st.success("SQL query generated successfully")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        result = cursor.execute(sql_query)

        #fetchall()->gets all rows returned by the SQL query
        rows = result.fetchall()

        st.subheader("Query Result")

        if rows:
            st.dataframe(rows, use_container_width=True)
        else:
            st.info("No results found.")

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        conn.close()