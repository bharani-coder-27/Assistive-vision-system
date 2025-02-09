import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_transcribe():
    with mic as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=0.1)
        try:
            audio = r.listen(source, timeout=3)
            user_input = r.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
        except sr.WaitTimeoutError:
            print("Listening timed out, no input received.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
            return None