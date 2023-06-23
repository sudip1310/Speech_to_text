import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech to Text Conversion")
    st.write("Please grant microphone permission to proceed.")
    
    # Initialize speech recognizer
    r = sr.Recognizer()
    
    # Request microphone permission
    with sr.Microphone() as source:
        st.write("Please select an audio input device:")
        devices = sr.Microphone.list_microphone_names()
        device = st.selectbox("Audio Input Device", devices)
        st.write(f"You selected: {device}")
        
        # Set the selected device as the input source
        r = sr.Recognizer()
        r.pause_threshold = 0.7
        r.energy_threshold = 4000
        r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_adjustment_ratio = 1.5
        r.dynamic_energy_adjustment_samples = 800
        
        with sr.Microphone(device_index=devices.index(device)) as source:
            st.write("Listening...")
            audio = r.listen(source)
        
        try:
            st.write("Processing...")
            text = r.recognize_google(audio)
            st.write(f"Text: {text}")
        except sr.UnknownValueError:
            st.write("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Speech Recognition service; {e}")
        
if __name__ == '__main__':
    main()
