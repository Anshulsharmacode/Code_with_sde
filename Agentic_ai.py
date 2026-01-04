#Agentic Ai in min using langchain
import os 
import webbrowser
from langchain.agents import initialize_agent 
from langchain.agents import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool

@tool
def open_website(url: str) -> str:
    """Opens a website in the default web browser."""
    webbrowser.open(url)
    return f"Website {url} opened successfully."

tools = [open_website]

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature=0.5,

)

agent = initialize_agent(
    llm=llm,
    tools=tools, 
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose= True
)

agent.run("Open the webpage 'https://www.wikipedia.org/'")
