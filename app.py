import base64
import time
from pathlib import Path

import streamlit as st
from streamlit_mic_recorder import mic_recorder

from chat_memory import (
    add_conversation,
    get_conversation,
    load_conversations,
    update_conversation,
)
from components.header import show_header
from gemini_ai import ask_gemini
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech

st.set_page_config(
    page_title="Mushaki AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)


def load_css():
    css_file = Path("styles/style.css")
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as file:
            st.html(f"<style>{file.read()}</style>")


def play_hidden_audio(audio_bytes):
    """Plays audio invisibly without showing any player box below text"""
    if not audio_bytes:
        return
    audio_base64 = base64.b64encode(audio_bytes).decode()
    st.html(
        f"""
        <audio id="mushaki-audio-element" autoplay style="display:none;">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        <script>
            const audioElem = document.getElementById('mushaki-audio-element');
            if(audioElem) {{
                audioElem.play();
            }}
        </script>
        """
    )


def generate_voice(text):
    try:
        return text_to_speech(text)
    except Exception as error:
        print("Text-to-speech error:", error)
        return None


def typewriter(text):
    placeholder = st.empty()
    current = ""
    for word in text.split():
        current += word + " "
        placeholder.markdown(current)
        time.sleep(0.015)
    return current.strip()


def submit_text():
    text = st.session_state.get("message_input", "").strip()
    if text:
        st.session_state.pending_text = text
        st.session_state.message_input = ""


load_css()

# =========================
# SESSION STATE
# =========================

if "conversations" not in st.session_state:
    st.session_state.conversations = load_conversations()

if "current_conversation_id" not in st.session_state:
    if st.session_state.conversations:
        st.session_state.current_conversation_id = (
            st.session_state.conversations[0]["id"]
        )
    else:
        conversation = add_conversation(st.session_state.conversations)
        st.session_state.conversations = load_conversations()
        st.session_state.current_conversation_id = conversation["id"]

current_conversation = get_conversation(
    st.session_state.conversations,
    st.session_state.current_conversation_id,
)

if current_conversation is None:
    conversation = add_conversation(st.session_state.conversations)
    st.session_state.conversations = load_conversations()
    st.session_state.current_conversation_id = conversation["id"]
    current_conversation = conversation

messages = current_conversation.get("messages", [])

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    logo = Path("www/assets/logo.png")
    if logo.exists():
        encoded_logo = base64.b64encode(logo.read_bytes()).decode()
        st.html(
            f"""
            <div class="sidebar-logo">
                <img src="data:image/png;base64,{encoded_logo}">
            </div>
            """
        )

    st.html(
        """
        <div class="sidebar-brand">Mushaki AI</div>
        <div class="sidebar-description">Personal AI Assistant</div>
        <div class="sidebar-status">
            <span class="sidebar-status-dot"></span> System Online
        </div>
        """
    )

    st.divider()

    if st.button("＋  New Chat", use_container_width=True):
        conversation = add_conversation(st.session_state.conversations)
        st.session_state.conversations = load_conversations()
        st.session_state.current_conversation_id = conversation["id"]
        st.rerun()

    st.html('<div class="chat-history-title">Chat History</div>')

    for conversation in st.session_state.conversations[:8]:
        title = conversation.get("title", "New Chat")
        if len(title) > 28:
            title = title[:28] + "..."
        is_current = (
            conversation["id"] == st.session_state.current_conversation_id
        )
        button_label = f"● {title}" if is_current else f"○ {title}"
        if st.button(
            button_label,
            key=f"chat_{conversation['id']}",
            use_container_width=True,
        ):
            st.session_state.current_conversation_id = conversation["id"]
            st.rerun()

    st.divider()
    st.html('<div class="chat-history-title">Statistics</div>')

    total_chats = len(st.session_state.conversations)
    total_messages = sum(
        len(item.get("messages", []))
        for item in st.session_state.conversations
    )

    st.html(
        f"""
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{total_chats}</div>
                <div class="stat-label">Conversations</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{total_messages}</div>
                <div class="stat-label">Messages</div>
            </div>
        </div>
        """
    )

    st.divider()

    if st.button("Clear Current Chat", use_container_width=True):
        update_conversation(
            st.session_state.conversations,
            st.session_state.current_conversation_id,
            [],
        )
        st.session_state.conversations = load_conversations()
        st.rerun()

    st.html('<div class="sidebar-version">Mushaki AI · v2.0</div>')

# =========================
# HEADER & WELCOME
# =========================

show_header()

if not messages:
    st.html(
        """
        <div class="welcome-card">
            <div class="welcome-icon">🤖</div>
            <div class="welcome-title">How can I help you?</div>
            <div class="welcome-text">
                I'm Mushaki, your intelligent personal AI assistant. Ask questions, explore ideas, write content, learn new topics, or simply have a conversation.
            </div>
        </div>
        """
    )
    st.html('<div class="section-title">Try asking</div>')

    prompt_cols = st.columns(3)
    prompts = [
        "Explain machine learning simply",
        "Help me improve my English",
        "Give me a Python project idea",
    ]
    for index, prompt in enumerate(prompts):
        with prompt_cols[index]:
            if st.button(
                prompt, key=f"prompt_{index}", use_container_width=True
            ):
                st.session_state.pending_prompt = prompt
                st.rerun()

# =========================
# CHAT HISTORY
# =========================

for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================
# INPUT BAR & MIC
# =========================

voice_recording = None

with st.container(key="chat_input_bar"):
    input_col, send_col, mic_col = st.columns(
        [8, 1, 1], vertical_alignment="center"
    )

    with input_col:
        st.text_input(
            "Message Mushaki",
            placeholder="Message Mushaki...",
            label_visibility="collapsed",
            key="message_input",
            on_change=submit_text,
        )

    with send_col:
        st.button(
            "➤",
            key="send_button",
            use_container_width=True,
            on_click=submit_text,
        )

    with mic_col:
        # Stable Python-native Microphone Component
        voice_recording = mic_recorder(
            start_prompt="🎙️",
            stop_prompt="⏹️",
            key="native_mic_recorder",
            use_container_width=True,
        )

# =========================
# INPUT PROCESSING
# =========================

pending_prompt = st.session_state.pop("pending_prompt", None)
pending_text = st.session_state.pop("pending_text", None)
user_prompt = pending_text or pending_prompt

# Process Voice Recording Data
if voice_recording and "bytes" in voice_recording:
    audio_bytes = voice_recording["bytes"]
    if audio_bytes:
        with st.spinner("Processing Voice..."):
            try:
                voice_text = speech_to_text(audio_bytes)
                if voice_text:
                    user_prompt = voice_text
                else:
                    st.warning("Could not recognize voice. Please try again.")
            except Exception as e:
                st.error(f"Voice Recognition Error: {e}")

# =========================
# PROCESS USER PROMPT
# =========================

if user_prompt:
    messages.append({"role": "user", "content": user_prompt})
    update_conversation(
        st.session_state.conversations,
        st.session_state.current_conversation_id,
        messages,
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Mushaki is thinking..."):
            try:
                answer = ask_gemini(user_prompt)
            except Exception as error:
                answer = f"I am temporarily unable to generate a response. Error: {error}"

        displayed_answer = typewriter(answer)
        voice_audio = generate_voice(displayed_answer)

        if voice_audio:
            play_hidden_audio(voice_audio)

    messages.append({"role": "assistant", "content": displayed_answer})
    update_conversation(
        st.session_state.conversations,
        st.session_state.current_conversation_id,
        messages,
    )
    st.session_state.conversations = load_conversations()

# =========================
# FOOTER
# =========================

st.html(
    """
    <div class="footer">
        Mushaki AI · Intelligent conversations, powered by Gemini
    </div>
    """
)