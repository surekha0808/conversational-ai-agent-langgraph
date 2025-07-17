# LangGraph Chatbot Agent with Cohere

## Description

This project demonstrates the integration of **LangGraph** with **Cohere's LLMs** to create a smart conversational agent. It showcases how structured conversation flows can be managed through LangGraph while utilizing Cohere's `command-r-plus` model for natural language understanding and response generation.

## Features

* Interactive command-line chat with Cohere integration
* Structured conversation flow via LangGraph's state graph
* Chat history memory using LangGraph's message utilities
* Extensible and modular architecture
* Graceful error handling and CLI exit support

## Technologies Used

* **LangGraph** for conversation flow control
* **Cohere** (via Python SDK) for AI responses
* **Python** as the main programming language
* **dotenv** for managing environment variables securely
* **Type hinting** and **LangGraph message utilities** for state management

## Skills Learned

* Integrating LangGraph with Cohere’s new ClientV2
* Managing structured conversation states and flows
* Building memory-aware chat agents
* Secure API management using environment variables
* Developing production-ready conversational agents

## Tools Used

* Visual Studio Code / Cursor IDE
* Git for version control
* Cohere Python SDK
* LangGraph for conversational logic
* Python 3.10+

## Project Implementation

### 1. Project Setup

* **Dependencies**: Installed Cohere SDK and LangGraph
* **Environment**: Used `.env` to securely manage the Cohere API key
* **Structure**: Modular code in `chatbot_agent.py`

### 2. Core Implementation

* **LangGraph Setup**: Defined `ChatState` and used `StateGraph` to manage flow
* **Cohere Integration**: Used `co.chat()` method for generating responses
* **Message History**: Maintained full history using `add_messages` from LangGraph

### 3. Application Logic

* **Agent Function**: `chatbot_agent()` creates conversation history and calls Cohere
* **Error Handling**: Clean handling of runtime and API issues
* **Conversation Termination**: Detects user exit via `'quit'`, `'exit'`, or `Ctrl+C`

### 4. User Interface

* **CLI Interface**: Simple terminal interface
* **User Experience**: Prints responses clearly, handles edge cases cleanly

### 5. Deployment and Testing

* **Local Testing**: Easily run with Python CLI
* **Environment Verification**: Checks if API key is loaded
* **Streaming Ready**: Structured to support `chat_stream` later

## Installation

1. **Clone the Repository**:
   `git clone https://github.com/surekha0808/conversational-ai-agent-langgraph.git
2. **Install Dependencies**:
   `pip install -r requirements.txt`
3. **Set Up Environment**:
   Create `.env` file with:

   ```
   COHERE_API_KEY=your-api-key-here
   ```
4. **Run the App**:
   `python chatbot_agent.py`

## Project Documentation

### Architecture

```
├── chatbot_agent.py       # Main chat implementation using LangGraph + Cohere
├── requirements.txt       # Python dependencies
├── .env                   # API key storage (not committed)
├── .gitignore             # Git configuration
└── README.md              # Project documentation
```

### Implementation

* Integrates LangGraph with Cohere’s `command-r-plus` model
* Uses `TypedDict` and `Annotated` for type-safe conversation state
* Supports building structured flows through `StateGraph`
* Prints assistant responses in real time

### Interactive Demo

```
Chat with AI Assistant (type 'quit' to exit)
User: How do I bake a cake?
Assistant: To bake a cake, start by preheating your oven...
```

### Setup Process

* Use `python-dotenv` to load API key
* Install all dependencies with pip
* Ensure `.env` is properly configured
* Run the bot and begin chatting

## License

MIT License (adjust as needed)
