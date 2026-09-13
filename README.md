# 🤖 Mushaki AI — Dual-Edition AI Voice Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mushaki-mdpvbvwoq5w4kj6iulz2rz.streamlit.app/)

**Mushaki AI** is an intelligent, interactive AI assistant designed to provide seamless voice and text interaction. Built with Python and powered by Google's Gemini API, 
Mushaki offers both a **Desktop Assistant Edition** for rich local machine automation and a **Web Application Edition** optimized for global cloud deployment via Streamlit.

🚀 **[Click Here to Try the Live Web App](https://mushaki-mdpvbvwoq5w4kj6iulz2rz.streamlit.app/)**

---

## 🌟 Key Features

### 💻 Desktop Edition
* **Voice Recognition & Speech Output:** Full hands-free interaction using speech recognition and text-to-speech engine.
* **System Automation:** Control desktop applications, play media, perform web searches, and trigger custom system tasks seamlessly.
* **Smart Memory:** Keeps track of previous context and conversational interactions for dynamic responses.

### 🌐 Web App Edition (Streamlit Cloud)
* **Interactive UI:** Clean, responsive web interface accessible from both desktop and mobile devices.
* **Voice & Text Input:** Multi-modal interactions using audio recording widgets and real-time query inputs.
* **Automated Package Resolution:** Cloud-optimized dependency tree running smoothly on headless Linux environments.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.10+
* **LLM Core:** Google Gemini AI API (`google-genai`)
* **Web Framework:** Streamlit
* **Audio & Speech:** SpeechRecognition, gTTS, edge-tts, pydub, streamlit-mic-recorder
* **Data Processing & Utilities:** Pillow, NumPy, BeautifulSoup4, markdown2, python-dotenv

---

## 📁 Project Structure

```text
Mushaki/
│
├── app.py                      # Main entry point for Streamlit Web App
├── gemini_ai.py                # Gemini API integration and response generation
├── speech_to_text.py           # Speech recognition handling
├── text_to_speech.py           # TTS audio synthesis module
├── check_reqs.py               # Dependency scanner utility
│
├── components/                 # Streamlit UI modular components
│   └── header.py
│
├── engine/                     # Helper modules & background processes
│   └── helper.py
│
├── requirements.txt            # Streamlit Cloud deployment requirements
├── requirements_desktop.txt    # Full local desktop edition dependencies
└── README.md                   # Project documentation


🚀 Getting Started
Prerequisites
Make sure you have Python 3.10 or higher installed. Get a Gemini API Key from Google AI Studio.

1. Clone the Repository

  => git clone [https://github.com/MuhammadSharafat/Mushaki.git](https://github.com/MuhammadSharafat/Mushaki.git) cd Mushaki

2. Set Up Virtual Environment

  => # Windows
      python -m venv envmushaki
      envmushaki\Scripts\activate
      
      # macOS/Linux
      python3 -m venv envmushaki
      source envmushaki/bin/activate

⚙️ Installation & Running
Option A: Running the Web App (Streamlit)

1. Install web dependencies:

  => pip install -r requirements.txt

2. Set up your environment variable:
  Create a .env file in the root folder and add:

  => GEMINI_API_KEY=your_actual_gemini_api_key

3. Run the application:

  => streamlit run app.py

Option B: Running the Desktop Assistant

1. Install desktop dependencies:

  => pip install -r requirements_desktop.txt

2. Run the desktop assistant script:

  => python app.py  # Or your specific desktop entry script

☁️ Deployment on Streamlit Cloud
  1. Push your repository to GitHub.

  2. Go to share.streamlit.io and connect your repository.

  3. Set app.py as the Main file path.

  4. Add your API Key under App Settings ➔ Secrets:

  => GEMINI_API_KEY = "your_actual_gemini_api_key"

  5. Click Deploy!

👤 Author
Mohammad Sharafat

GitHub: @MuhammadSharafat

Built with passion using Python & AI.
