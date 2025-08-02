import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_current_weather(location: str) -> str:
    # Placeholder implementation
    return "its sunny in the california"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
