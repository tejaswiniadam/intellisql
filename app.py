import streamlit as st
import sqlite3
from google import genai

# Configure Gemini client
client = genai.Client(api_key="AIzaSyALlaPC-P1cMZ484mUvdMYfsEVqOlHNcYk")


# Gemini function
def get_response(question):

    prompt = """
    Convert English question into SQL query.
    Table: STUDENTS (NAME, CLASS, MARKS)
    Use DISTINCT to avoid duplicates.
    Return ONLY SQL query.
    """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt + question
    )

    sql = response.text.strip()

    # Clean unwanted characters
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.replace("\n", " ")
    sql = sql.strip()

    return sql


# Database function
def run_query(sql):
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()
        return rows, None
    except Exception as e:
        return None, str(e)


# Streamlit UI
st.title("IntelliSQL - AI SQL Generator")

question = st.text_input("Ask your question")

if st.button("Generate"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        sql = get_response(question)

        st.subheader("Generated SQL:")
        st.code(sql, language="sql")

        result, error = run_query(sql)

        if error:
            st.error("SQL Error: " + error)
        else:
            st.subheader("Result:")
            st.table(result)
