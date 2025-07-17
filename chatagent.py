import os
from typing import Annotated
from dotenv import load_dotenv
import cohere
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

# Load environment variables
load_dotenv()

# Initialize Cohere client
co = cohere.Client(api_key=os.getenv("COHERE_API_KEY"))

class ChatState(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot_agent(state: ChatState):
    # Get the last message
    last_message = state["messages"][-1]
    
    # Create the full conversation context
    conversation_history = []
    for msg in state["messages"]:
        if hasattr(msg, 'content'):
            content = msg.content
            role = "USER" if msg.type == "human" else "CHATBOT"
        else:
            content = msg[1] if isinstance(msg, tuple) else str(msg)
            role = "USER" if msg[0] == "user" else "CHATBOT"
        
        conversation_history.append({"role": role, "message": content})
    
    # Use Cohere's chat endpoint
    response = co.chat(
        model="command-r-plus",  # or "command-r", "command-light"
        message=last_message.content if hasattr(last_message, 'content') else last_message[1],
        temperature=0.7,
        chat_history=conversation_history[:-1] if len(conversation_history) > 1 else [],
        preamble="You are a helpful AI assistant."
    )
    
    return {"messages": [response.text]}

# Create the graph
chat_graph = StateGraph(ChatState)

# Add nodes and edges
chat_graph.add_node("chatbot_agent", chatbot_agent)
chat_graph.add_edge(START, "chatbot_agent")
chat_graph.add_edge("chatbot_agent", END)

# Compile the graph
graph_app = chat_graph.compile()

def stream_graph_updates(user_input: str):
    for event in graph_app.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1])

if __name__ == "__main__":
    print("Chat with AI Assistant (type 'quit' to exit)")
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Thank you and Goodbye!")
                break
            stream_graph_updates(user_input)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Test API key (optional)
print(f"Cohere API Key loaded: {bool(os.getenv('COHERE_API_KEY'))}")
