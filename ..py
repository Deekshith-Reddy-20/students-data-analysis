import speech_recognition as sr
from deep_translator import GoogleTranslator
from monsterapi import client

# ==========================
# Monster API Key
# ==========================
API_KEY = "YOUR_MONSTER_API_KEY"

monster_client = client(API_KEY)

# ==========================
# Speech To Text
# ==========================
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10)

            text = recognizer.recognize_google(
                audio,
                language="en-US"  # Change if needed
            )

            return text

        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None

        except sr.RequestError as e:
            print("Speech Recognition Error:", e)
            return None

# ==========================
# Translate To English
# ==========================
def translate_to_english(text):
    try:
        translated = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)

        return translated

    except Exception as e:
        print("Translation Error:", e)
        return text

# ==========================
# Generate Image
# ==========================
def generate_image(prompt):

    print("\n🖼 Generating Image...")
    print("Prompt:", prompt)

    result = monster_client.generate(
        model="txt2img",
        data={
            "prompt": prompt,
            "samples": 1
        }
    )

    return result

# ==========================
# Main Function
# ==========================
def speech_to_image():

    text = speech_to_text()

    if not text:
        return

    print("\nDetected Text:")
    print(text)

    english_prompt = translate_to_english(text)

    print("\nEnglish Prompt:")
    print(english_prompt)

    result = generate_image(english_prompt)

    print("\n✅ Image Generated:")
    print(result)

# ==========================
# Run Once
# ==========================
speech_to_image()