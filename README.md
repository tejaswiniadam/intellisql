# IntelliSQL – AI Powered SQL Query Generator

IntelliSQL is an AI-powered web application that converts natural language questions into SQL queries and executes them on a SQLite database.

This project uses Google's Gemini AI model to understand user questions and automatically generate SQL queries.

---

## Features

• Convert English questions into SQL queries  
• Execute queries on SQLite database  
• Display results instantly  
• AI-powered using Gemini API  
• Simple and clean Streamlit interface  

---

## Technologies Used

• Python  
• Streamlit  
• SQLite  
• Google Gemini AI API  
• GitHub  
• Streamlit Cloud (Deployment)

---

## How it Works

1. User enters question in English  
   Example:  
   "Show all students"

2. Gemini AI converts it into SQL query  
   Example:  
   SELECT * FROM STUDENTS;

3. Query executes on SQLite database

4. Results displayed in web interface

---

## Sample Questions

• Show all students  
• Show students with marks above 80  
• Count total students  
• Show student names only  
• Show average marks  

---

## Project Structure

IntelliSQL/
│
├── app.py              # Main Streamlit application
│
├── data.db             # SQLite database containing STUDENTS table
│
├── requirements.txt    # Required Python libraries for deployment
│
├── README.md           # Project documentation


## Deployment

This project is deployed using Streamlit Cloud.

---

## Author

Tejaswini Adam

---

## Future Improvements

• Support multiple tables  
• Support INSERT, UPDATE, DELETE queries  
• Add authentication  
• Improve UI design  
