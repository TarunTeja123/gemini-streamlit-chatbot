import streamlit as st 
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

def load_model() :
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key :
        st.error("Enter Api Key :")
        st.stop() 
    model_name = "models/gemini-2.5-flash"
    genai.configure(api_key = api_key)
    return genai.GenerativeModel(model_name)

def display_chat_history(chat) :
    for msg in chat.history :
        with st.chat_message(msg.role) :
            for part in msg.parts :
                if part.text :
                    st.markdown(part.text)
                elif part.inline_data :
                    st.image(part.inline_data.data)

def main() :
    st.markdown("""
    <h1 style="text-align:center;"> Gemini AI Chatbot </h1>
    """,unsafe_allow_html=True)
    model = load_model()
    if "chat" not in st.session_state :
        st.session_state.chat = model.start_chat(history=[])
    st.sidebar.title("Controls")
    if st.sidebar.button("Clear Chat History") :
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()
    display_chat_history(st.session_state.chat)
    prompt_dict = st.chat_input("Ask Me Anything",accept_file="multiple",file_type=["png","jpg","jpeg"])
    if prompt_dict :
        prompt_all = []
        images_display = []
        prompt = prompt_dict.get("text")
        if prompt :
            prompt_all.append(prompt)
        uploaded_files = prompt_dict.get("files")
        if uploaded_files :
            for file in uploaded_files :
                img = Image.open(file)
                prompt_all.append(img)
                images_display.append(img)
        if prompt_all :
            with st.chat_message("user") :
                st.markdown(prompt)
            if images_display :
                cols = st.columns(len(images_display))
                for id,img in enumerate(images_display) :
                    cols[id].image(img,width="stretch")
            try :
                with st.spinner("Loading...") :
                    response = st.session_state.chat.send_message(prompt_all,stream=True)
                    with st.chat_message("model") :
                        st.write_stream(chunk.text for chunk in response)
            except Exception as e :
                st.error(e)

if __name__ == "__main__" :
    main()
