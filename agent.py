import os

from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

model_name = os.getenv("LLM_MODEL")

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def execute_agent():
    agent = create_agent(
        model=model_name,
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
    )
    print(result["messages"][-1].content_blocks)