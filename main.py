import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import re
import random
import wikipedia

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hi! How may I help you?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data.lower()
        except sr.UnknownValueError:
            print("Sorry! I am unable to understand.")
            return None

def speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()
    
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        return f"Multiple results found. Please be more specific. Options: {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        return "Sorry, no matching page found on Wikipedia."
    
def handle_conversation(topic):
    responses = {
        "how are you": ["I'm doing well, thank you!", "Feeling great, how about you?"],
        "what's your name": ["My name is Alina, how can I assist you today?"],
        "thank you": ["You're welcome!", "Glad I could help!"],
        "how is the weather": ["The weather is nice today!", "It's sunny outside."],
        "can you help me": ["Of course! What do you need assistance with?"],
        "tell me about yourself": ["I'm Alina, a virtual assistant designed to assist you with various tasks."],
        "do you have friends": ["I'm here to be your friend and assist you whenever you need help!"],
        "do you get tired": ["I don't experience fatigue like humans, so I'm always available to help you."],
        "goodbye": ["Goodbye!", "See you later!"]
    }
    if topic in responses:
        return random.choice(responses[topic])
    else:
        return "Sorry, I'm not sure how to respond to that."

def main():       
    if "hey alina" in listen_command().lower():     
        while True:     
            command = listen_command().lower()
            print(command)
                
            if "how are you" in command or "what's your name" in command or "thank you" in command or "goodbye" in command or "the weather" in command or "help me" in command or "about yourself" in command or "you have friends" in command or " you get tired" in command:
                response = handle_conversation(command)
                speech(response)
                
            elif "old are you" in command or "your age" in command:
                age = "I am two years old"
                speech(age)
                    
            elif any(word in command for word in ["time right now", "time", "time now", "tell me the time"]):
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speech("The time is " + current_time)
                
            elif "youtube" in command:
                speech("Opening youtube")
                webbrowser.open("https://www.youtube.com/")
                
            elif any(word in command for word in ["joke", "jokes"]):
                joke = pyjokes.get_joke(language="en", category="neutral")
                speech(joke)
                
            elif any(word in command for word in ["open google", "open chrome", "open google chrome"]):
                speech("Opening Google")
                webbrowser.open("https://www.google.com/")

            elif any(word in command for word in ["exit", "bye"]):
                speech("Goodbye")
                break
            
            elif "wikipedia" in command:
                speech("What do you want to search on Wikipedia?")
                query = listen_command()
                if query:
                    wikipedia_info = search_wikipedia(query)
                    speech(wikipedia_info)

    else:
        print("No input!")

main()
