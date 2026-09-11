import json
import os
import uuid
from datetime import datetime


CONVERSATIONS_FILE = "conversations.json"
OLD_MEMORY_FILE = "memory.json"


def _now():
    return datetime.now().isoformat()


def _create_id():
    return str(uuid.uuid4())


def _generate_title(messages):
    for message in messages:
        if message.get("role") == "user":
            text = message.get("content", "").strip()

            if not text:
                continue

            if len(text) > 35:
                return text[:35] + "..."

            return text

    return "New Chat"


def create_conversation():
    return {
        "id": _create_id(),
        "title": "New Chat",
        "created_at": _now(),
        "updated_at": _now(),
        "messages": []
    }


def load_conversations():

    if os.path.exists(CONVERSATIONS_FILE):
        try:
            with open(
                CONVERSATIONS_FILE,
                "r",
                encoding="utf-8"
            ) as f:
                conversations = json.load(f)

            if isinstance(conversations, list):
                return conversations

        except (json.JSONDecodeError, OSError):
            return []

    if os.path.exists(OLD_MEMORY_FILE):
        try:
            with open(
                OLD_MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as f:
                old_messages = json.load(f)

            if isinstance(old_messages, list) and old_messages:

                conversation = {
                    "id": _create_id(),
                    "title": _generate_title(old_messages),
                    "created_at": _now(),
                    "updated_at": _now(),
                    "messages": old_messages
                }

                conversations = [conversation]

                save_conversations(conversations)

                return conversations

        except (json.JSONDecodeError, OSError):
            pass

    return []


def save_conversations(conversations):

    with open(
        CONVERSATIONS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            conversations,
            f,
            ensure_ascii=False,
            indent=4
        )


def get_conversation(
    conversations,
    conversation_id
):

    for conversation in conversations:

        if conversation.get("id") == conversation_id:
            return conversation

    return None


def update_conversation(
    conversations,
    conversation_id,
    messages
):

    conversation = get_conversation(
        conversations,
        conversation_id
    )

    if conversation is None:
        return conversations

    conversation["messages"] = messages
    conversation["title"] = _generate_title(messages)
    conversation["updated_at"] = _now()

    save_conversations(conversations)

    return conversations


def add_conversation(conversations):

    conversation = create_conversation()

    conversations.insert(
        0,
        conversation
    )

    save_conversations(conversations)

    return conversation


def delete_conversation(
    conversations,
    conversation_id
):

    conversations = [
        conversation
        for conversation in conversations
        if conversation.get("id") != conversation_id
    ]

    save_conversations(conversations)

    return conversations