from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the weather of a city"""
    return f"The weather of {city} is is always raining"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")