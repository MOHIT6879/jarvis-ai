from asr import record_audio, transcribe_audio
from agent import get_llm_response
from t import speak_text
from actions import execute_task
from fuzzywuzzy import fuzz

WAKE_WORD = "hey jarvis"
EXIT_WORDS = [
    "shutdown jarvis", "shut down jarvis", "terminate jarvis",
    "goodbye", "exit jarvis", "stop listening"
]

def is_wake_word(phrase):
    return WAKE_WORD in phrase.lower()

def is_exit_command(phrase):
    phrase = phrase.lower()
    return any(exit_cmd in phrase for exit_cmd in EXIT_WORDS)

def fuzzy_task_match(user_input):
    known_commands = [
        "open youtube", "search", "shutdown", "weather", "open gmail",
        "play music", "news", "time", "date", "remember", "recall"
    ]
    for command in known_commands:
        if fuzz.partial_ratio(user_input.lower(), command) > 70:
            return command
    return None

def main_loop():
    print("🎙️ Jarvis is listening... Say 'Hey Jarvis' to activate.")
    while True:
        record_audio(duration=4)
        user_input = transcribe_audio()
        print(f"👂 Heard: {user_input}")

        if is_exit_command(user_input):
            speak_text("Shutting down. Goodbye.")
            break

        elif is_wake_word(user_input):
            speak_text("Yes, how can I help you?")
            record_audio(duration=6)
            command = transcribe_audio()
            print(f"🗣️ You said: {command}")

            if is_exit_command(command):
                speak_text("Shutting down. Goodbye.")
                break

            task_response = execute_task(command)
            if task_response:
                speak_text(task_response)
            else:
                reply = get_llm_response(command)
                speak_text(reply)
        else:
            print("🔇 No wake word or exit command detected.")

if __name__ == "__main__":
    main_loop()
