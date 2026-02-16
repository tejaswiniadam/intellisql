import streamlit as st
import sqlite3
import pandas as pd
from google import genai

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="IntelliSQL - AI SQL Generator",
    page_icon="💻",
    layout="centered"
)

# -------------------------
# CUSTOM DARK UI CSS
# -------------------------
st.markdown("""
<style>

body {
    background-color: #0E1117;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white;
}

.stTextInput input {
    background-color: #262730;
    color: white;
}

.stButton button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    padding: 10px;
    font-weight: bold;
}

[data-testid="stTable"] {
    color: white;
}

[data-testid="stDataFrame"] {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# GEMINI CLIENT
# -------------------------
client = genai.Client(api_key="AIzaSyALlaPC-P1cMZ484mUvdMYfsEVqOlHNcYk")

# -------------------------
# GEMINI FUNCTION
# -------------------------
def get_response(question):

    prompt = """
    Convert English question into SQL query.
    Table name: STUDENTS
    Columns: NAME, CLASS, MARKS

    Only return SQL query.
    Do not return explanation.
    Do not return ```sql or ```
    """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt + question
    )

    sql = response.text.strip()

    # remove unwanted formatting if exists
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql


# -------------------------
# DATABASE FUNCTION
# -------------------------
def run_query(sql):

    conn = sqlite3.connect("data.db")

    cursor = conn.cursor()

    cursor.execute(sql)

    rows = cursor.fetchall()

    conn.close()

    return rows


# -------------------------
# STREAMLIT UI
# -------------------------
st.title("💻 IntelliSQL - AI SQL Generator")

st.write("Ask your database question in plain English:")

question = st.text_input("Example: show all students")

if st.button("Generate SQL"):

    if question:

        sql = get_response(question)

        st.subheader("Generated SQL")

        st.code(sql, language="sql")

        result = run_query(sql)

        if result:

            df = pd.DataFrame(result, columns=["Name", "Class", "Marks"])

            st.subheader("Result")

            st.dataframe(df, use_container_width=True)

        else:

            st.warning("No results found.")

    else:

        st.warning("Please enter a question.")
