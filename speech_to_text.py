# This was written by Ibrahim Al-Shinnawi, shinnawi.com, on 2024 01 06. 

import os
from openai import OpenAI

# Set your OpenAI API key
# Set your openai api key as an env var called OPENAI_API_KEY
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
import speech_recognition as sr

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

# Set up the microphone for audio input
microphone = sr.Microphone()

# Function to ask a question to ChatGPT
def ask_chatgpt(question):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",  # Update this to your desired model
        messages=[
            {"role": "system", "content": "You are a helpful assistant who answers questions."},
            {"role": "user", "content": question}
        ],
        temperature=0)
        response_message = response.choices[0].message.content
        return response_message.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main loop
while True:
    with microphone as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google's speech recognition
            question = recognizer.recognize_google(audio)
            print(f"You asked: {question}")

            # Get response from ChatGPT
            response = ask_chatgpt(question)
            if response:
                print(f"ChatGPT: {response}")
            else:
                print("No response received.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
