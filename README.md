<div align="center">

# 🤖 Mushaki AI

### A dual-edition AI assistant — talk to it, type to it, and let it get things done.

Powered by **Google Gemini** · Built with **Python**, **Streamlit** and **Eel**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)](https://mushaki-mdpvbvwoq5w4kj6iulz2rz.streamlit.app/)
[![Gemini](https://img.shields.io/badge/Google-Gemini%20API-4285F4?logo=google&logoColor=white)](https://aistudio.google.com/)
[![Platform](https://img.shields.io/badge/Desktop%20Edition-Windows-0078D6?logo=windows&logoColor=white)](#-desktop-edition)
[![Portfolio](https://img.shields.io/badge/Portfolio-sharafatalam.netlify.app-0A66C2)](https://sharafatalam.netlify.app/)

[🚀 **Try the Live Web App**](https://mushaki-mdpvbvwoq5w4kj6iulz2rz.streamlit.app/) ·
[🌐 **Portfolio**](https://sharafatalam.netlify.app/) ·
[💻 **GitHub**](https://github.com/MuhammadSharafat)

</div>

---

## 📖 Overview

**Mushaki AI** is an intelligent personal assistant built for natural **voice and text interaction**. It ships in two editions that share the same Gemini-powered core:

- 💻 **Desktop Assistant Edition** — a Windows voice assistant with face authentication, hotword listening, app launching, YouTube playback and Android phone control (messages and calls) over ADB.
- 🌐 **Web Application Edition** — a polished Streamlit chat app with voice input, spoken replies, and saved multi-conversation history, deployable to the cloud.

Mushaki understands **English, Bangla and Banglish**, and replies in the same language and style you use.

---

## 📸 Screenshots

<div align="center">

| 💻 Desktop Edition | 🌐 Web Edition |
|:---:|:---:|
| <img src="assets/desk.png" alt="Mushaki AI desktop assistant" width="440"> | <img src="assets/web.png" alt="Mushaki AI web app" width="440"> |

</div>

---

## ✨ Key Features

### 🌐 Web Edition (Streamlit)

| Feature | Description |
|---|---|
| 💬 **Multi-conversation chat** | Start new chats, switch between recent conversations from the sidebar, and clear the current chat at any time. Titles are generated automatically from your first message. |
| 🎙️ **Voice input** | Record a question with the built-in microphone popover; speech is transcribed and sent to Mushaki automatically. |
| ⌨️ **Text input** | Type and press Enter or the send button. |
| 🔊 **Spoken replies** | Every answer is read aloud with text-to-speech, with the audio player hidden for a clean interface. |
| ✍️ **Typewriter responses** | Answers stream onto the screen word by word. |
| 🌍 **Multilingual** | Understands English, Bangla and Banglish and answers in the user's own style. |
| 💡 **Suggested prompts** | A welcome screen with one-click starter prompts for new chats. |
| 📊 **Usage statistics** | Sidebar counters for total conversations and messages. |
| 💾 **Persistent history** | Conversations are saved with timestamps and restored on the next visit. |
| 🎨 **Custom UI** | Custom CSS styling, branded sidebar with logo, and a live "System Online" status indicator. |
| 📱 **Responsive** | Works on desktop and mobile browsers. |

### 💻 Desktop Edition

| Feature | Description |
|---|---|
| 🔐 **Face authentication** | The assistant verifies your face on startup and greets you by voice once authenticated. |
| 🗣️ **Hotword listening** | A dedicated background process listens for the wake word, so you can speak hands-free. |
| 🎙️ **Voice recognition & speech output** | Full voice interaction with spoken responses. |
| 🖥️ **App control** | Open desktop applications such as Notepad and Word by voice. |
| ▶️ **YouTube playback** | Say "play *song name* on YouTube" and Mushaki finds and plays it. |
| 📱 **Android phone control (ADB)** | Send messages and make audio or video calls on a connected Android phone; the ADB helpers can also tap the screen, type text, answer or end calls, and navigate back. |
| 🧠 **Smart memory** | Keeps track of previous context and conversational interactions. |
| 🪟 **Animated startup** | Staged startup screens (loader → face authentication → success → main screen) with start-up sound. |

---

## 🗣️ Voice Command Examples (Desktop Edition)

| Say | What happens |
|---|---|
| `open youtube` | Opens YouTube |
| `open notepad` | Opens Notepad |
| `open word` | Opens Microsoft Word |
| `play <song name> on youtube` | Finds and plays that video on YouTube |
| `send message to <contact name>` | Sends a message to the contact |
| `make a video call to <contact name>` | Starts a video call with the contact |
| `make a audio call to <contact name>` | Starts an audio call with the contact |

---

## 🔀 Choosing an Edition

| | 💻 Desktop Edition | 🌐 Web Edition |
|---|:---:|:---:|
| Voice input | ✅ | ✅ |
| Spoken responses | ✅ | ✅ |
| Face authentication | ✅ | — |
| Hotword (wake word) listening | ✅ | — |
| Open apps / play YouTube by voice | ✅ | — |
| Android phone control (ADB) | ✅ | — |
| Multi-conversation chat history | — | ✅ |
| Works from any browser / mobile | — | ✅ |
| Cloud deployment | — | ✅ |
| Operating system | Windows | Any |
| Requirements file | `requirements_desktop.txt` | `requirements.txt` |

---

## 🧩 How It Works

### Web Edition

```
 Voice (microphone)                Typed message
        │                                │
        ▼                                │
 Speech-to-text                          │
        └──────────────► Prompt ◄────────┘
                            │
                            ▼
              Google Gemini + Mushaki persona
                            │
                            ▼
            Markdown → clean plain-text answer
                     ┌──────┴───────┐
                     ▼              ▼
           Typewriter display   Text-to-speech
                                 (auto-played)
                            │
                            ▼
             Saved to conversation history
```

### Desktop Edition

```
 run.py ──┬── Process 1: Eel UI (main.py) ──► Face authentication ──► Voice commands
          │                                                              │
          └── Process 2: Hotword listener ────────────────────────────►  ▼
                                                     App launching · YouTube · Gemini answers
                                                     Android control via ADB · Spoken replies
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Language** | Python 3.10+ |
| **LLM Core** | Google Gemini API (`google-genai`) |
| **Web Framework** | Streamlit |
| **Desktop UI** | Eel (HTML/CSS/JS front end served locally) |
| **Audio & Speech** | SpeechRecognition, gTTS, edge-tts, pydub, streamlit-mic-recorder |
| **Text Processing** | markdown2, BeautifulSoup4 |
| **Phone Automation** | Android Debug Bridge (ADB) |
| **Utilities** | Pillow, NumPy, python-dotenv |

---

## 📁 Project Structure

```
Mushaki/
│
├── app.py                      # Streamlit web app (chat UI, voice input, sidebar, history)
├── main.py                     # Desktop edition: Eel UI + face-authentication startup flow
├── run.py                      # Desktop launcher: starts the UI and hotword listener processes
├── gemini_ai.py                # Gemini client and the Mushaki persona (system prompt)
├── chat_memory.py              # Conversation storage: create / load / update / delete chats
├── speech_to_text.py           # Speech recognition handling
├── text_to_speech.py           # TTS audio synthesis
├── device.bat                  # Windows batch helper used at desktop startup
│
├── engine/                     # Core assistant modules
│   ├── features.py             #   Assistant features (hotword, sounds, speech, actions)
│   ├── command.py              #   Voice command handling
│   ├── auth/recoganize.py      #   Face authentication
│   ├── config.py               #   Configuration (API key)
│   └── helper.py               #   Helpers: YouTube term extraction, ADB actions, markdown → text
│
├── components/                 # Streamlit UI components
│   └── header.py
├── styles/style.css            # Web app styling
├── www/                        # Desktop UI front end (index.html, assets/logo.png, ...)
├── assets/                     # README screenshots
│
├── conversations.json          # Saved chat history (created at runtime)
├── memory.json                 # Legacy memory file (auto-migrated into conversations.json)
├── packages.txt                # System packages for cloud deployment
├── requirements.txt            # Web edition requirements
├── requirements_desktop.txt    # Desktop edition requirements
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

| | Web Edition | Desktop Edition |
|---|:---:|:---:|
| Python 3.10+ | ✅ | ✅ |
| [Gemini API key](https://aistudio.google.com/) (free) | ✅ | ✅ |
| Microphone | ✅ (for voice) | ✅ |
| Windows + Microsoft Edge | — | ✅ |
| Webcam (face authentication) | — | ✅ |
| Android phone with USB debugging + ADB | — | ✅ (for phone features) |

### 1. Clone the repository

```bash
git clone https://github.com/MuhammadSharafat/Mushaki.git
cd Mushaki
```

### 2. Create a virtual environment

**Windows**
```bash
python -m venv envmushaki
envmushaki\Scripts\activate
```

**macOS / Linux** *(web edition only)*
```bash
python3 -m venv envmushaki
source envmushaki/bin/activate
```

### 3. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

> 🔒 Never commit your `.env` file or API key.

---

## ⚙️ Installation & Running

### Option A — Web App (Streamlit)

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app opens in your browser at the local Streamlit address.

### Option B — Desktop Assistant (Windows)

```bash
pip install -r requirements_desktop.txt
python run.py
```

`run.py` starts two processes: the Eel interface (which opens in Microsoft Edge app mode at `http://localhost:8000`) and the hotword listener. Complete the face authentication when prompted, then start giving voice commands.

---

## ☁️ Deployment on Streamlit Cloud

Only the **Web Edition** can be deployed to the cloud; the desktop edition needs your local machine (camera, apps and phone).

1. Push your repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repository.
3. Set **`app.py`** as the **Main file path**.
4. Add your API key under **App Settings ➜ Secrets**:

   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key"
   ```

5. Click **Deploy** 🎉

---

## 🔐 Privacy & Data

- Chats are stored as plain JSON in `conversations.json` on the machine or server running the app.
- On the hosted demo, that file lives on the server, so please **don't enter personal or sensitive information** there.

---

## 👤 Author

**Mohammad Sharafat Alam Saki**

- 🌐 Portfolio: [sharafatalam.netlify.app](https://sharafatalam.netlify.app/)
- 💻 GitHub: [@MuhammadSharafat](https://github.com/MuhammadSharafat)

---

<div align="center">

Built with passion using **Python** & **AI** 💙

⭐ If you find this project useful, consider giving it a star!

</div>
