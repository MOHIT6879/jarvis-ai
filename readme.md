# 🎙️ Jarvis - Voice Assistant (Offline+LLM Enabled)

Jarvis is a voice-activated AI assistant that can perform tasks like opening websites, searching online, providing weather updates, reading the news, answering questions using an LLM (via OpenRouter), and even remembering what you tell it—all through natural speech.

---

## 🚀 Features

- ✅ Wake-word activation: **"Hey Jarvis"**
- ✅ Natural voice command handling via [Whisper](https://github.com/openai/whisper) ASR
- ✅ Task execution (open YouTube, Gmail, play music, etc.)
- ✅ Weather updates via `wttr.in`
- ✅ Real-time news via [NewsAPI](https://newsapi.org/)
- ✅ Memory (basic in-session recall)
- ✅ LLM integration via [OpenRouter](https://openrouter.ai/)
- ✅ Graceful shutdown via commands like "Shutdown Jarvis", "Goodbye", etc.
- ❌ No `pyautogui` required (fully compatible on most systems)

---

## 🧠 Requirements

### 🐍 Python Version
```bash
Python 3.11
📦 Install Dependencies
We recommend using a virtual environment:

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
Install the dependencies:


pip install -r requirements.txt
📦 requirements.txt


pyttsx3
fuzzywuzzy
faster-whisper
openai
requests
sounddevice
scipy
pydub
numpy
keyboard
psutil
langchain
python-dotenv
rich

🔑 Environment Setup
Create a .env file in the root directory and add your OpenRouter API key:


OPENROUTER_API_KEY=your_openrouter_api_key
To get a key, visit https://openrouter.ai.

You can change the default LLM in config.py.

🗂️ File Structure

.
├── actions.py          # Task execution logic
├── agent.py            # LLM API (OpenRouter)
├── asr.py              # Whisper speech-to-text
├── config.py           # Environment & model config
├── main.py             # Main loop (wake word + logic)
├── t.py                # Text-to-speech engine (pyttsx3)
├── .env                # Secret key for OpenRouter
├── requirements.txt    # Python dependencies
└── README.md
🎤 How It Works
Jarvis passively listens for the wake word: "Hey Jarvis"

Once triggered, it records your next command (e.g. "Search for Python tutorials")

Jarvis attempts to:

Match your request to a known task (open YouTube, fetch weather, etc.)

Or pass it to a large language model (via OpenRouter)

The response is spoken aloud using text-to-speech.

🧪 Supported Commands
🗂️ Core Task Examples
Command Example	Action
"Open YouTube"	Launch YouTube in browser
"Search for Python tutorials"	Google search
"What's the weather in Delhi?"	Weather from wttr.in
"Play music"	Opens Spotify
"Tell me the time/date"	Current time/date
"Remember I have a meeting"	Saves to session memory
"What did I say?"	Recalls remembered items
"Shutdown system"	Shuts down laptop

❌ Exit Commands
"Shutdown Jarvis"

"Terminate Jarvis"

"Stop listening"

"Goodbye"

🗝️ API Keys
🔐 OpenRouter (LLM)
Signup at https://openrouter.ai

Add your key to .env as:

OPENROUTER_API_KEY=your_key_here

⚙️ Run the Assistant

python main.py
Jarvis will listen for:

"Hey Jarvis"
Then respond to your command.