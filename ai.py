import speech_recognition as sr
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
from playsound import playsound
import ollama
import os
import time

# ==========================================
# SETTINGS
# ==========================================

WAKE_WORD = "jarvis"

recognizer = sr.Recognizer()

# ==========================================
# SPEAK FUNCTION
# ==========================================

def speak(text, lang='en'):

    try:

        filename = "reply.mp3"

        tts = gTTS(
            text=text,
            lang=lang
        )

        tts.save(filename)

        playsound(filename)

        os.remove(filename)

    except Exception as e:

        print("TTS Error:", e)

# ==========================================
# AI FUNCTION (OLLAMA)
# ==========================================

def ask_ai(question):

    try:

        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    'role': 'user',
                    'content': question
                }
            ]
        )

        return response['message']['content']



    except Exception as e:

        return f"AI Error: {e}"

# ==========================================
# LISTEN FUNCTION
# ==========================================

def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        # Reduce noise
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        recognizer.pause_threshold = 1.5

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            print("Recognizing...")

            text = recognizer.recognize_google(
                audio,
                language='en-IN'
            )

            print("You Said:", text)

            return text.lower()

        except sr.WaitTimeoutError:

            print("No speech detected.")

            return ""

        except sr.UnknownValueError:

            print("Could not understand.")

            return ""

        except Exception as e:

            print("Speech Error:", e)

            return ""

# ==========================================
# MAIN PROGRAM
# ==========================================

print("====================================")
print("  AI Voice Assistant Started")
print("====================================")

print(f"Say '{WAKE_WORD}' to activate.\n")

while True:

    text = listen()

    # WAKE WORD DETECTION
    if WAKE_WORD in text.lower():

        print("\nWake word detected!")

        speak("Yes, how can I help you?")

        # LISTEN FOR COMMAND
        command = listen()

        if command == "":
            continue

        try:

            # DETECT LANGUAGE
            user_lang = detect(command)

            print("Detected Language:", user_lang)

            # TRANSLATE TO ENGLISH
            english_text = GoogleTranslator(
                source='auto',
                target='en'
            ).translate(command)

            print("Translated To English:", english_text)

            # ASK AI
            answer = ask_ai(english_text)

            print("AI Response:", answer)

            # TRANSLATE BACK
            final_answer = GoogleTranslator(
                source='en',
                target=user_lang
            ).translate(answer)

            print("Final Response:", final_answer)

            # SPEAK RESPONSE
            speak(final_answer, lang=user_lang)

        except Exception as e:

            print("Error:", e)

    time.sleep(1)