# 🤖 Saarthi - Your Personal AI Assistant

Saarthi is a **Streamlit-powered chatbot** built using **LangChain** and **Groq LLMs**.  
It provides an interactive way to ask questions and get instant answers, while keeping track of chat history.  

---

## ✨ Features
- 🗨️ Interactive chat interface with memory  
- ⚙️ Sidebar to select model, temperature, and max tokens  
- 🧹 Clear chat history button  
- 🚀 Powered by **LangChain** + **Groq API**  
- 📊 Expandable sidebar for advanced settings  

---

## 🛠️ Installation & Setup

### 1. Clone the repository
bash

git clone <your-repo-url>

cd <your-repo-folder>

### 2. Create a Virtual Environment
python -m venv venv

On Windows

    venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Environment Variables for securing API keys

LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
GROQ_API_KEY=your_groq_api_key

### 5. Run the application

streamlit run main.py

---

### Project Structure

├── main.py          # Streamlit chatbot app
├── requirements.txt # Python dependencies
├── .env             # Environment variables (not committed to Git)
└── README.md        # Project documentation

---

### Issues Faced During the Development

While building the chatbot, I ran into this error:

TypeError: Expected a Runnable, callable or dict.
Instead got an unsupported type: <class 'str'>

### Cause

The error occurred because I reused the variable name prompt:

    - First, as a ChatPromptTemplate (Runnable object).

    - Then, as the user input string from st.chat_input.

When passed into the chain, prompt was treated as a string instead of a Runnable, which caused the error.

### Solution

I fixed this by renaming variables:

    - prompt_template → for the LangChain prompt

    - user_query → for user input

This resolved the error and the chatbot worked correctly.




