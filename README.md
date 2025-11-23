# 🌟 Gemini AI Chatbot (Streamlit)

A powerful, interactive AI chatbot powered by Google's **Gemini 2.5 Flash** model,
built using Streamlit. This version features a native chat interface and is capable of processing text and images in the same conversation.

---------------------------
🔧 Requirements
---------------------------
- **Python 3.8+**
- **[Streamlit](https://streamlit.io/) (For the web application framework)**
- **[google-generativeai](https://pypi.org/project/google-generativeai/) (For connecting to the Gemini API)**
- **[python-dotenv](https://pypi.org/project/python-dotenv/) (For managing the API key)**
- **[Pillow (PIL)](https://pypi.org/project/pillow/) (For image processing)**

  ### Installation :
    ```bash
    pip install -r requirements.txt
    ```
---------------------------
🚀 How to Run the App
---------------------------

1. Clone or Download this project.

2. Edit `.env` file and add your Gemini API key :
   **GEMINI_API_KEY = "your_api_key_here"**

3. Download Requirements Using pip :
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app using Streamlit :
   ```bash
   python -m streamlit run chatbot.py
   ```
6. Open the app in your browser and start chatting!

---------------------------
💡 Enhanced Features
---------------------------
- **Native Chat UI** : Uses Streamlit's st.chat_message for a modern, fluid conversational experience.
- **Response Streaming** : Provides real-time output from the Gemini model.
- **Persistent Chat History** : Maintains conversation context, including previously uploaded images.
- **Clear Controls** : Includes a sidebar button to easily clear the chat history.
- **Robust Error Handling** : Includes handling for All errors.
- **Multimodal Input** : The chatbot now accepts both text and image files (PNG, JPG, JPEG) in a single prompt.
- **Image Display** : Uploaded images are rendered directly in the user's chat message.

---------------------------
📁 File Structure
---------------------------
- chatbot.py           : Main Streamlit app
- `.env`                 : Stores your Gemini API key
- requirements.txt     : Project dependencies
- README.md            : You're reading it!

---------------------------
🛡️ Notes
---------------------------
- Make sure you have a valid Gemini API key from Google AI Studio.
- This app runs locally — no data is stored or shared.

---------------------------
