print("Starting MCP server...")
from fastapi import FastAPI
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "maids.json")

with open(DATA_PATH) as f:
    maids = json.load(f)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP Server Running"}

@app.post("/call_tool")
def call_tool(payload: dict):
    tool = payload.get("tool")
    params = payload.get("params", {})

    if tool == "find_maids":
        skill = params.get("skill", "").lower()

        results = [
            m for m in maids
            if skill in [s.lower() for s in m["skills"]]
        ]

        return {"results": results}

    return {"error": "Tool not found"}