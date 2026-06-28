# import pyttsx3
# import pymysql as ms
# import os
# from dotenv import load_dotenv

# # Load .env
# load_dotenv()

# # Text-to-Speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def sleepy(voice):
#     engine.say(voice)
#     print(f"Response: {voice}")
#     engine.runAndWait()

# def main():
#     conn = ms.connect(
#         # host=os.getenv("DB_HOST"),
#         # user=os.getenv("DB_USER"),
#         # password=os.getenv("DB_PASSWORD"),
#         # database=os.getenv("DB_NAME")
#         host="localhost",
#         user="root",
#         password="Yashraj@6350",
#         database="chatbot"
#     )
#     mycursor = conn.cursor()
    
#     while True:
#         ask = input("Ask : ").strip()
#         if ask.lower() == "bye":
#             sleepy("Goodbye! Take care.")
#             break

#         text_clean = ask.replace(" ", "").lower()
#         mycursor.execute("SELECT * FROM chatbotdata")
#         data = mycursor.fetchall()
        
#         found = False
#         for q, a in data:
#             if text_clean == q:
#                 sleepy(a)
#                 found = True
#                 break

#         if not found:
#             message = "I don't know what you asked. Please enter your question with an answer to teach me. I'll remember it."
#             sleepy(message)
#             datakey = input("Enter what you asked me: ").strip().replace(" ", "").lower()
#             datavalue = input("Enter the response to this question: ").strip()
#             if datakey and datavalue:
#                 mycursor.execute("INSERT INTO chatbotdata VALUES (%s, %s)", (datakey, datavalue))
#                 conn.commit()
#                 sleepy("Thank you! I have learned this now.")

#     conn.close()

# if __name__ == "__main__":
#     main()

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
