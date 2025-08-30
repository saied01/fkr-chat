# Real-Time Chat Application (fkr-chat)

A simple real-time chat application built with **Python**, **Flask**, and **Socket.IO**.  
This project demonstrates how to create a web-based chat room where users can join, send messages instantly, and see messages from others in real time.

---

## 🚀 Features

- Users can create or join a chat room.  
- Real-time messaging with **WebSockets** via Flask-SocketIO.  
- Simple UI with HTML, CSS, and JavaScript.  
- Session management to prevent unauthorized access to chat rooms.  
- Multiple users supported simultaneously.  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SocketIO  
- **Frontend:** HTML, CSS, JavaScript  
- **WebSockets:** Socket.IO  
- **Environment:** Virtualenv / venv (recommended)  

---

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fkr-chat.git
   cd fkr-chat


 2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux / Mac
   venv\Scripts\activate      # On Windows

 3.Install dependencies:
   ```bash
   pip install -r requirements.txt

 4. Run the Flask server:
   ```bash
   python main.py

 5. Open your browser at:
   ```bash
   http://localhost:5000
