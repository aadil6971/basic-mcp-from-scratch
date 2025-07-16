# mcp-from-scratch

This project is a demonstration of the `mcp` (Multi-Tool-Co-Protocol) library, showcasing how to create and orchestrate multiple tool servers with a client that uses a LangChain agent to consume the exposed tools.

## Overview

The project consists of three main components:

1.  A **Math Server** (`mathserver.py`) that exposes basic arithmetic functions (`add`, `multiple`).
2.  A **Weather Server** (`weather.py`) that exposes a function to get the weather for a given location.
3.  A **Client** (`client.py`) that connects to both servers, gathers the available tools, and uses a LangChain ReAct agent powered by the Groq API to answer questions by calling these tools.

## Features

*   **Multiple Tool Servers**: Demonstrates running two separate tool servers.
*   **stdio Transport**: The Math Server uses standard I/O for communication.
*   **HTTP Transport**: The Weather Server uses HTTP for communication.
*   **LangChain Integration**: The client uses `langchain-mcp-adapters` to seamlessly integrate the tools from the MCP servers into a `langgraph` agent.
*   **LLM Integration**: Uses `langchain-groq` to connect to a fast LLM for agentic reasoning.

## Components

### `mathserver.py`

A simple tool server built with `mcp.server.fastmcp`.

*   **Tools**:
    *   `add(a: int, b: int) -> int`: Adds two numbers.
    *   `multiple(a: int, b: int) -> int`: Multiplies two numbers.
*   **Transport**: `stdio`

### `weather.py`

Another tool server built with `mcp.server.fastmcp`.

*   **Tools**:
    *   `get_weather(location: str) -> str`: Returns a mock weather forecast.
*   **Transport**: `streamable-http` (runs on `http://127.0.0.1:8000`)

### `client.py`

The main application that orchestrates the servers and the agent.

*   It initializes a `MultiServerMCPClient` to connect to the `math` and `weather` servers.
*   It fetches the tools from all connected servers.
*   It creates a `create_react_agent` from `langgraph` using the Groq model.
*   It invokes the agent to solve a math problem, which demonstrates the agent's ability to use the tools from the `mathserver`.

## Installation

1.  Clone the repository.
2.  It is recommended to create a virtual environment.
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Create a `.env` file and add your Groq API key:
    ```
    GROQ_API_KEY="your-groq-api-key"
    ```

## Usage

To run the project, you need to start the servers and then the client.

1.  **Start the Weather Server** (in a separate terminal):
    ```bash
    python weather.py
    ```
    This will start the server on `http://127.0.0.1:8000`.

2.  **Run the Client** (in another terminal):
    ```bash
    python client.py
    ```
    The client will automatically start the `mathserver.py` as a subprocess using `stdio` transport. It will then connect to the weather server, initialize the agent, and ask it to solve a math problem.

You should see output similar to this:

```
Math response: The result of (3 + 5) * 12 is 96.
```

## Dependencies

This project uses the following major Python libraries:

*   `langchain-groq`
*   `langchain-mcp-adapters`
*   `mcp`
*   `langgraph`
*   `python-dotenv`