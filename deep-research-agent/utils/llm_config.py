from dotenv import load_dotenv  # Import load_dotenv to load environment variables
import os
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

def load_llm():
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),  # Use the GROQ_API_KEY from the .env file
        model="llama3-70b-8192",  # Or "llama3-70b-8192", depending on your setup
        temperature=0.7
    )


