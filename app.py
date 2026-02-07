import streamlit as st
import google.generativeai as genai

# Set page configuration
st.set_page_config(page_title="English Grammar Assistant", page_icon="📝")

# Sidebar for API Key
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter your Gemini API Key", type="password")
    st.markdown("[Get your API key manually](https://aistudio.google.com/) if you don't have one.")

# Main app
st.title("📝 English Grammar Assistant")
st.write("Enter an English sentence below, and I'll check its grammar for you using Gemini AI.")

user_input = st.text_area("Your Sentence:", height=150, placeholder="e.g., He go to school yesterday.")

if st.button("Analyze Grammar"):
    if not api_key:
        st.warning("Please enter your Gemini API Key in the sidebar to proceed.")
    elif not user_input:
        st.warning("Please enter a sentence to analyze.")
    else:
        try:
            # Configure Gemini API
            genai.configure(api_key=api_key)
            
            # Use the requested model
            model = genai.GenerativeModel('gemini-3-flash-preview') 


            prompt = f"""
            Please act as an expert English grammar teacher.
            Analyze the following sentence:
            "{user_input}"

            Tasks:
            1. Identify any grammatical errors.
            2. Provide the corrected version of the sentence.
            3. Explain each error and correction clearly in bullet points.
            4. If the sentence is already correct, compliment the user and explain why it is correct.
            5. Provide a more natural or native-speaker sounding alternative if applicable.

            Output format should be Markdown.
            """

            with st.spinner("Analyzing..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.info("Ensure your API key is correct and valid for the 'gemini-2.0-flash-exp' model.")
