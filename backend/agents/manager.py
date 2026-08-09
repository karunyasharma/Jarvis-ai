from graph.state import GraphState
from services.llm_service import chat_with_jarvis
from memory.chat_memory import memory
from tools.calculator import calculate


def manager_node(state: GraphState):

    session_id = state.get("session_id", "default")
    message = state.get("message", "")

    # Calculator tool
    if message.lower().startswith("calculate "):
        expression = message[10:].strip()
        result = calculate(expression)

        memory.add_message(session_id, "user", message)
        memory.add_message(session_id, "assistant", result)

        return {
            "session_id": session_id,
            "message": message,
            "history": memory.get_history(session_id),
            "response": result,
        }

    # Get conversation history
    history = memory.get_history(session_id)

    prompt = """You are Jarvis, a helpful AI assistant.

Use the conversation history below to answer the user's current message.
Remember information the user has previously shared.
If the answer is not present in the conversation history, answer normally.

Conversation history:
"""

    for msg in history:
        prompt += f'{msg["role"]}: {msg["content"]}\n'

    prompt += f"\nuser: {message}\nassistant:"

    # Get AI response
    response = chat_with_jarvis(prompt)

    # Save conversation
    memory.add_message(session_id, "user", message)
    memory.add_message(session_id, "assistant", response)

    return {
        "session_id": session_id,
        "message": message,
        "history": memory.get_history(session_id),
        "response": response,
    }
