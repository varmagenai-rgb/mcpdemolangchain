# MCP Demo with LangChain

Demo of the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) with LangChain and LangGraph. An agent uses tools from two MCP servers—math (stdio) and weather (HTTP)—via Groq.

## Architecture

```
client.py  →  MultiServerMCPClient  →  ChatGroq + ReAct agent
                 │
                 ├── mathserver.py   (stdio transport)
                 │     tools: add, subtract, multiply
                 │
                 └── weather.py      (streamable HTTP on :8000)
                       tool: get_weather
```

## Requirements

- Python 3.13
- A [Groq](https://console.groq.com/) API key

## Setup

```bash
# Create and activate a virtual environment (optional if using uv)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt
# or: uv sync
```

Copy the example env file and add your key:

```bash
copy .env.example .env          # Windows
# cp .env.example .env          # macOS / Linux
```

Edit `.env`:

```
GROQ_API_KEY=your_api_key_here
```

## Run

1. Start the weather MCP server (HTTP):

```bash
python weather.py
```

This serves MCP at `http://localhost:8000/mcp`.

2. In another terminal, run the LangChain client (it starts the math server over stdio automatically):

```bash
python client.py
```

The agent will answer a math query using the math tools, then a weather query using `get_weather`.

## Project layout

| File | Role |
|------|------|
| `mathserver.py` | FastMCP math tools over **stdio** |
| `weather.py` | FastMCP weather tool over **streamable HTTP** |
| `client.py` | LangChain/LangGraph agent that loads both MCP servers |
| `.env.example` | Template for API keys |
| `requirements.txt` / `pyproject.toml` | Dependencies |

## Tools

**Math** (`mathserver.py`)

- `add(a, b)` — add two integers
- `subtract(a, b)` — subtract two integers
- `multiply(a, b)` — multiply two integers

**Weather** (`weather.py`)

- `get_weather(city)` — returns a demo weather string for a city

## Notes

- The weather tool is a stub for demonstration; it does not call a real weather API.
- Ensure `mathserver.py` is reachable from the working directory when running `client.py` (or update the path in `client.py`).
- Keep the weather server running before invoking the client’s weather query.
