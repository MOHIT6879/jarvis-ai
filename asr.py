import sounddevice as sd
from scipy.io.wavfile import write
import os
from faster_whisper import WhisperModel

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎤 Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("✅ Recorded.")

def transcribe_audio(filename="input.wav", model_size="base"):
    model = WhisperModel(model_size, compute_type="int8", device="cpu")  # ✅ Force CPU
    segments, _ = model.transcribe(filename)
    text = " ".join(segment.text for segment in segments)
    return text.strip()