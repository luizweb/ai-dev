from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8050,  # only used for SSE transport (set this to any port)
)


# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


# Run the server
if __name__ == "__main__":
    transport = "stdio"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")
    

# ---------------------
# --- MCP Inspector ---
# ---------------------

# Para executar o servidor com o MCP Inspector:
# $ mcp dev server.py

# Pode aparecer a seguinte mensagem:
# $ mcp dev server.py
# Need to install the following packages:
# @modelcontextprotocol/inspector@0.14.3
# Ok to proceed? (y) 

# abrir o endereço do MCP Inspector no navegador (Safari):
# http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=<a_sixty_four_character_token>
# clicar em 'Connect'

# Clicar em 'Tools' >> 'List Tools'
