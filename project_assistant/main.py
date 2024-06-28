import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import music_lib# Ensure this module is correctly imported and available
import requests



news_api="4bb5c892c4cd44da9724b333f623b76d"



# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech(text):
    voices = engine.getProperty('voices')   
    engine.setProperty('voice', voices[1].id)  
    engine.say(text)
    engine.runAndWait()
    

def process(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif"open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com/?hl=en")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com/profile.php?id=100045636951652")
    elif "open twitter" in command.lower():
        webbrowser.open("https://x.com")
    elif "open photos" in command.lower():
        os.startfile(r"D:\images of mobile\nothing images")
    elif "news" in command.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
        if r.status_code == 200: # this stands for ok response
        # Parse the JSON response
            data = r.json()
            # Extract the titles of the articles
            titles = [article['title'] for article in data['articles']]

            # Print the titles
            for title in titles:
                speech(title)
    elif command.lower().startswith("play"):
        try:
            song=command.lower().split(" ")[1]
            link=music_lib.music(song)
            webbrowser.open(link)
        except:
            speech("an error occured") 
             
    else:
        print(command)        
             
def activated(keyword):
    with sr.Microphone() as source:
        print("Listening for the keyword:", keyword)
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()
                print("You said:", text)

                if keyword in text:
                    print(f"Keyword '{keyword}' detected!")
                    speech(" yes sir")
                    
                    # Use the same source for the subsequent command
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    process(command)
                    speech("Command processed.")
                    
                    
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError:
                print("Sorry, my speech service is down.")
            except KeyboardInterrupt:
                print("Exiting...")
                

if __name__ == "__main__":
    activated("friday")
