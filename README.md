# AI Assistant Chat Application

This is a simple chat application that uses the Ollama API to provide responses. The web interface is built with Gradio and FastAPI.

## Features

* Chat with an Ollama language model.

* Simple, clean web interface using Gradio.

* Supports conversation history.

* Uses FastAPI for the backend.

## Prerequisites

* Python 3.10 or higher

* UV package manager

* Ollama API access and an API key

## Installation

1. **Clone the repository**

git clone https://github.com/maryamabdallahmohamed/Ai_Assistant.git cd Ai_Assistant


2. **Install UV package manager** (if you don't have it)

curl -LsSf https://astral.sh/uv/install.sh | sh


3. **Install dependencies**

uv sync


## Configuration

1. Create a file named `.env` in the project's root directory.

touch .env


2. Add your Ollama API key to this file:

OLLAMA_API_KEY=your_api_key_here


## How to Run

1. Use UV to run the application:

uv run python chat_app.py


2. Open your browser and go to `http://127.0.0.1:7860`.

## Troubleshooting

* **API Key Not Found:** Make sure the `.env` file exists in the correct directory and contains your API key.

* **Port Already in Use:** If port 7860 is busy, you can change it in `chat_app.py`. Find the line `demo.launch(...)` and add `server_port=YOUR_PORT`.

## Contributing

Pull requests are welcome.

1. Fork the repository.

2. Create a new feature branch.

3. Commit your changes.

4. Open a Pull Request.

To add a new package during development, run:

uv add package-name


## License

This project is available under the MIT License.