import os
import streamlit as st 
from google import generativeai as genai 
from dotenv import find_dotenv,load_dotenv
from google.api_core import exceptions as google_exceptions

model_name  = "models/gemini-2.5-flash"

def load_model() :
    try :
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key :
            st.error("'GEMINI_API_KEY' Not Found.")
            st.stop()
        genai.configure(api_key = api_key)
        return genai.GenerativeModel(model_name)
    except Exception as e :
        st.error(f"Error Loading Model : {e}")
        st.stop()

def display_chat_history(chat) :
    for message in chat.history :
        with st.chat_message(message.role) :
            st.markdown(message.parts[0].text)

def main() :
    st.markdown("""
                <h1 style = "text-align:center;">
                      Gemini AI Chatbot
                </h1>
                """,unsafe_allow_html=True)
    model = load_model()
    st.sidebar.title("Controls")
    if st.sidebar.button("Clear Chat Histoy") :
        st.session_state.chat = model.start_chat(history = [])
        st.rerun()
    if "chat" not in st.session_state :
        st.session_state.chat = model.start_chat(history = [])
    display_chat_history(st.session_state.chat)
    prompt = st.chat_input("Ask Me Anything")
    if prompt :
        with st.chat_message("user") :
            st.markdown(prompt)
        try :
            with st.spinner("Loading...") :
                response = st.session_state.chat.send_message(prompt,stream=True)
                with st.chat_message("model") :
                    st.write_stream(chunk.text for chunk in response)
        except google_exceptions.ResourceExhausted as e:
            st.error(f"API Quota Exceeded: You've used your API limit. {e}")
        except google_exceptions.PermissionDenied as e:
            st.error(f"API Key Error: Check your API key. {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__" :
    main()
