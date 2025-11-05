import ollama
import os
from ollama import Client
import dotenv
import gradio as gr

dotenv.load_dotenv()

client = Client(
    host="https://ollama.com",
    headers={'Authorization': f"Bearer {os.environ.get('OLLAMA_API_KEY')}"}
)


def chat(messages: list) -> str:
    try:
        response = client.chat(
            model='gpt-oss:120b',
            messages=messages,
            stream=False
        )

        # Preferred: response.message.content (if the client returns that structure)
        if hasattr(response, "message") and hasattr(response.message, "content"):
            return response.message.content
        
        # Fallback: try accessing as dict
        if isinstance(response, dict) and 'message' in response:
            return response['message'].get('content', str(response))

        # Last fallback: try string conversion
        return str(response)
    except Exception as e:
        # Return an error string so the UI doesn't crash
        return f"[ollama error] {e}"


def gradio_chat(message: str, history: list) -> str:
    # Convert Gradio history format to Ollama message format
    messages = []
    for user_msg, bot_msg in history:
        messages.append({'role': 'user', 'content': user_msg})
        messages.append({'role': 'assistant', 'content': bot_msg})
    
    # Add current message
    messages.append({'role': 'user', 'content': message})
    
    # Get response
    response = chat(messages)
    return response


# Create the Gradio interface
demo = gr.ChatInterface(
    fn=gradio_chat,
    title="Ollama Chat Assistant",
    description="Chat with gpt-oss:120b model via Ollama",
    examples=[
        "explain gradio?",
        "What is AI?"
    ],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()