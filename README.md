# 💡 Project Title: UDP Broadcasting – Treasure Hunt Clues

## 📌 Project Overview
This project implements a **broadcast-based treasure hunt game** using Python and the UDP protocol. A central **server** broadcasts **encrypted clues** over the network using **UDP broadcasting**. Multiple **clients** connected to the same network listen for these messages, **decode the encrypted clues in real time**, and display them.

The project uses a **Caesar cipher encryption technique** to add a simple layer of cryptography. This makes it engaging and educational by combining basic cryptography with network communication.

---

## 🎯 Objective
- To learn how **UDP broadcast communication** works in real-time.
- To simulate a **multi-client system** where all clients receive the same broadcasted data.
- To apply **basic encryption/decryption** for encoding treasure hunt clues.
- To develop a simple, fun game logic that introduces core network programming concepts.

---

## ⚙️ Technologies and Concepts Used

| Component        | Description                                                  |
|------------------|--------------------------------------------------------------|
| **Python 3.x**   | Programming language used for both server and client         |
| **UDP Protocol** | For broadcasting data packets across the local network       |
| **Socket Library** | Used to create and bind server-client connections         |
| **Caesar Cipher** | For encrypting and decrypting clues (simple substitution cipher) |
| **Localhost Testing (127.0.0.1)** | Used for simulating all clients on the same machine |

---

## 🚀 How It Works

### 🧠 Logic Flow

**Server Side**
- Reads a list of predefined clues.
- Encrypts each clue using Caesar Cipher (shift = 3).
- Broadcasts the encrypted clues every few seconds via UDP to a specific port.

**Client Side**
- Listens on the same port for incoming UDP broadcast messages.
- Receives the encrypted clue.
- Decrypts the clue using the reverse Caesar Cipher.
- Displays the readable clue to the user.

---

## 🧪 How to Run the Project (Step-by-Step)

> 💡 Make sure Python 3 is installed on your machine and added to the system path.

### 📁 1. Open the Project Folder in Terminal
Navigate to the folder where your files are stored:
```bash
cd path_to/UDP_Treasure_Clues
### 1️⃣ Run the Server
```bash
python server.py
python client.py
