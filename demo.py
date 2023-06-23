from speechtotext import *


question=" "
st.title("Speech to Text Converter")
st.write("Click the 'Start' button and speak into your microphone.")

if st.button("Start"):
    question= speech_to_text()

print(question)

