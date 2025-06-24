import streamlit as st
import speech_recognition as sr

st.title("Speech to Text Web App")

uploaded_file = st.file_uploader("Upload a WAV audio file", type=["wav"])

if uploaded_file is not None:
    recognizer = sr.Recognizer()
    with sr.AudioFile(uploaded_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")