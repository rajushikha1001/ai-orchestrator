import os
from dotenv import load_dotenv

# --- Load .env from THIS folder ---
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

print("DEBUG OPENAI KEY:", OPENAI_KEY)   # REMOVE LATER

if not OPENAI_KEY:
    raise RuntimeError("❌ OPENAI_API_KEY NOT LOADED — check backend/.env")

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from agent_tools import classify_sentiment


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
   
)

tools = [
    Tool(
        name="Sentiment Classifier",
        func=classify_sentiment,
        description="Use this to classify text sentiment."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

def run_agent(query: str):
    return agent.run(query)
