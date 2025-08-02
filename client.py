from asyncio import transports
from email import message
from http import client
from click import command
from  langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http",
            }
        }
    )

    import os
    os.environ["Groq_API_Key"] = os.getenv("Groq_API_Key")
    tools = await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(tools, model)
    math_response=await agent.ainvoke(
        {"messages":[{"role":"user","content":"What is ((3+5)-2)*2?"}]}
    )
    print("math_response: ",math_response['messages'][-1].content)
    tools = await client.get_tools()

if __name__ == "__main__":
    asyncio.run(main())