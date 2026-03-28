import requests

MCP_SERVER_URL = "https://mcp-server-968767205311.us-central1.run.app"

def call_mcp_tool(tool, params):
    try:
        response = requests.post(
            f"{MCP_SERVER_URL}/call_tool",
            json={"tool": tool, "params": params},
            timeout=5
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}