import speech_recognition as sr
import sounddevice as sd
import numpy as np


def record_audio(duration=5, sample_rate=16000):
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    return np.array(audio).flatten()


def listen_for_command():
    r = sr.Recognizer()
    audio_data = record_audio()
    audio_sample = sr.AudioData(audio_data.tobytes(), sample_rate=16000, sample_width=2)

    try:
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio_sample)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


def main():
    listen_for_command()