# Import the libraries
import os
import openai
import keyboard
import speech_recognition as sr
import pyttsx3
import requests

# Set the API key
openai.api_key = ("OPENAI_KEY")

# Initialize the speech recognizer and synthesizer
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to get audio input from microphone
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ru-RU")
            print("You said: " + text)
            return text
        except:
            print("Sorry, I could not understand what you said.")
            return ""

# Define a function to send text input to openai and get text output
def get_response(text):
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    response = completion.choices[0].message.content
    print("OpenAI said: " + response)
    return response

# Define a function to speak text output using pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    # Wait for a key press
    print("Press any key to start speaking...")
    keyboard.wait("u")
    # Get audio input from microphone
    user_input = get_audio()
    # Check if input is not empty
    if user_input:
        # Send input to openai and get response
        openai_output = get_response(user_input)
        # Speak response using pyttsx3
        speak(openai_output)
    # Check if user wants to exit the loop
    print("Press ESC to exit the loop...")
    if keyboard.is_pressed("esc"):
        break
# Exit the program
print("Goodbye!")
