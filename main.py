import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv  

load_dotenv()

### Setting up LangChain Tracking

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
groq_api_key = os.getenv("GROQ_API_KEY")

## Prompt Template

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system" , "Hey! You're a helpful Assistant to Answer User's Query to the best. Your name is Saarthi."),
        ("human", "Question : {question}")
    ]
)

output_parser = StrOutputParser()

### Streamlit settings

st.set_page_config(page_title="Saarthi - AI Assistant", page_icon="🤖", layout="wide")
st.title("🤖 Saarthi: Your Personal QnA Assistant")

# Sidebar Settings
st.sidebar.title("⚙️ Settings")

model_name = st.sidebar.selectbox(
    "Select AI Model",
    ['llama-3.1-8b-instant', 'gemma2-9b-it', 'openai/gpt-oss-20b']
)


temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=2000, value=500)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Chat cleared! Hi again 👋 I'm Saarthi. How can I help you?"}
    ]
    st.rerun()

## Creating session history
if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {"role":"assistant", "content":"Hi! I'm Saarthi. How can I help you?"}
    ]

### For printing msgs in the UI
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

### If prompt is added

if user_query:=st.chat_input(placeholder="Ask me Anything."):

    ### Taking input from the user and printing it
    st.session_state.messages.append({"role":"user", "content":user_query})
    st.chat_message("user").write(user_query)

    ### Initializing LLM

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        streaming=True
    )

    chain = prompt_template | llm | output_parser
    
    ### assistant’s answer
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = chain.invoke(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant', "content":response})
        st.write(response.content)