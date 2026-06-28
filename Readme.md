# 💤 Sleepy Chatbot

**SleepyBot** is a simple command-line chatbot built using **Python**, **MySQL**, and **Text-to-Speech**.  
It learns responses dynamically from user input and stores them in a MySQL database.

---

## 🧠 Features

- 🗣️ Speaks answers using `pyttsx3`
- 📚 Learns new question-answer pairs when it doesn't know the answer
- 💾 Saves everything in a MySQL database (`chatbotdata` table)
- 🔁 Keeps learning and growing over time

---

## 🛠️ Technologies Used

- Python 3.8+
- MySQL Server
- `pyttsx3` for text-to-speech
- `mysql-connector-python` for MySQL connection
- `python-dotenv` for environment variables

---

## 🧩 Setup Instructions

### 1. Install Dependencies

Use the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### 2. Create MySQL Database and Table

Login to MySQL and run this SQL:

```sql
CREATE DATABASE chatbot;

USE chatbot;

CREATE TABLE chatbotdata (
    question VARCHAR(255) PRIMARY KEY,
    answer TEXT
);
```

---

### 3. Setup Environment Variables

Create a `.env` file in the root of your project:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=chatbot
```

> ⚠️ Note: This file contains sensitive info. It is already listed in `.gitignore` and should NOT be pushed to GitHub.

---

### 4. Run the Chatbot

```bash
python sleepy_chatbot.py
```

- Type anything to chat with SleepyBot.
- If the bot doesn't know an answer, it will ask you to teach it.
- Type `bye` to exit the bot.

---

## 📁 Project Structure

```
sleepy-chatbot/
├── sleepy_chatbot.py        # Main chatbot logic
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignored files
└── .env                     # Environment variables (not pushed)
```

---

## 💡 Future Improvements

- GUI version using Tkinter
- Voice input using speech recognition
- Offline version using SQLite
- Flask-based web interface
- Save chat history in file or DB

---

## 📃 License

This project is free and open-source.  
You are free to use, modify, and share it for educational or non-commercial purposes.

---

## 👨‍💻 Author

Made with ❤️ by **[Your Name]**  
> Want to collaborate or suggest features? Feel free to contribute!