import pyttsx3
import pymysql as ms

def speak(text):
    try:
        engine = pyttsx3.init()   # हर बार नया engine
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # female voice
        print("Response:", text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("Voice Error:", e)

def main():
    conn = ms.connect(
        host="localhost",
        user="root",
        password="Yashraj@6350",
        database="chatbot"
    )
    cursor = conn.cursor()

    while True:
        ask = input("Ask : ").strip()

        if ask.lower() == "bye":
            speak("Goodbye! Take care.")
            break

        text_clean = ask.replace(" ", "").lower()

        cursor.execute("SELECT * FROM chatbotdata")
        data = cursor.fetchall()

        found = False
        for q, a in data:
            if text_clean == q:
                speak(a)
                found = True
                break

        if not found:
            speak("I don't know. Please teach me.")
            key = input("Enter question: ").strip().replace(" ", "").lower()
            value = input("Enter answer: ").strip()

            if key and value:
                cursor.execute(
                    "INSERT INTO chatbotdata VALUES (%s, %s)",
                    (key, value)
                )
                conn.commit()
                speak("Learned successfully")

    conn.close()

if __name__ == "__main__":
    main()
