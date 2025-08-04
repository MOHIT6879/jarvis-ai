import os
import webbrowser
import requests
import platform
from datetime import datetime

memory = []

def remember(command):
    memory.append(command)
    return "Okay, I've remembered that."

def recall_memory():
    if memory:
        return "Here's what you've asked me to remember:\n" + "\n".join(memory)
    return "You haven't asked me to remember anything yet."

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_gmail():
    webbrowser.open("https://mail.google.com")

def play_music():
    webbrowser.open("https://open.spotify.com")

def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def shutdown_system():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 5")
    elif platform.system() == "Linux":
        os.system("shutdown now")
    elif platform.system() == "Darwin":
        os.system("sudo shutdown -h now")

def get_weather(city="Delhi"):
    try:
        url = f"https://wttr.in/{city}?format=3"
        res = requests.get(url)
        return res.text
    except:
        return "Weather service is currently unavailable."

def get_time():
    now = datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

def get_date():
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."



def execute_task(command):
    command = command.lower()

    if "open youtube" in command:
        open_youtube()
        return "Opening YouTube."

    elif "open gmail" in command:
        open_gmail()
        return "Opening Gmail."

    elif "play music" in command:
        play_music()
        return "Playing music."

    elif "search" in command:
        search_query = command.split("search", 1)[1].strip()
        if search_query:
            search_google(search_query)
            return f"Searching for {search_query} on Google."
        else:
            return "Please specify what you'd like me to search."

    elif "shutdown system" in command or "shut down laptop" in command:
        shutdown_system()
        return "Shutting down the system."

    elif "weather" in command:
        if "weather in" in command:
            city = command.split("weather in", 1)[1].strip()
        else:
            city = "Delhi"
        return get_weather(city)

    elif "time" in command:
        return get_time()

    elif "date" in command:
        return get_date()

    elif "remember" in command:
        return remember(command)

    elif "recall" in command or "what did i say" in command:
        return recall_memory()

    return None
