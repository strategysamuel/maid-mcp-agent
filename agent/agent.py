from mcp_client.client import call_mcp_tool

def process_query(user_query: str):
    try:
        query = user_query.lower()

        if "cook" in query:
            skill = "cooking"
        elif "elder" in query:
            skill = "elder care"
        elif "child" in query:
            skill = "child care"
        else:
            return "Sorry, I couldn't understand your requirement."

        response = call_mcp_tool("find_maids", {"skill": skill})

        if "error" in response:
            return f"Error connecting to MCP server: {response['error']}"

        maids = response.get("results", [])

        if not maids:
            return "No matching maids found."

        result = "Top matching maids:\n\n"

        for i, m in enumerate(maids, 1):
            result += (
                f"{i}. {m['name']} ({m['experience']} yrs)\n"
                f"   Skills: {', '.join(m['skills'])}\n"
                f"   Language: {m['language']}\n\n"
            )

        return result

    except Exception as e:
        return f"Internal error: {str(e)}"