import os
import streamlit as st 
from google import generativeai as genai 
from dotenv import find_dotenv,load_dotenv

_ = load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model_name = "models/gemini-2.5-flash"
model = genai.GenerativeModel(model_name)

if "chat" not in st.session_state :
    st.session_state.chat = model.start_chat(history=[])

st.title("Gemini AI Chatbot")
prompt = st.text_input("Enter Your Prompt :",placeholder="Ask Me Anything")
if st.button("Search") :
    try :
        if not prompt :
            st.warning("Please Enter The Prompt Before Searching!!!")
        with st.spinner("Loading...") :
            response = st.session_state.chat.send_message(prompt,stream=True)
            response.resolve()
            st.success(response.text)
    except Exception as e :
        st.error(f"An Error Has Occured : {e}")
