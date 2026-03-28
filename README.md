# 🤖 MCP-Based Maid Matching Agent

## 📌 Overview
This project demonstrates an AI agent that uses the Model Context Protocol (MCP) to connect to an external data source and provide intelligent responses.

The agent retrieves maid profiles from an MCP server and presents the best matches based on user requirements.

---

## 🏗️ Architecture

User → Agent (Cloud Run) → MCP Server → Dataset

---

## ⚙️ Features

- AI agent processes natural language queries  
- MCP server exposes structured tool (`find_maids`)  
- Clean separation of reasoning and data access  
- Fully deployed on Google Cloud Run  
- Web-based UI for interaction  

---

## 🔌 MCP Tool

**find_maids(skill)**  
Returns maid profiles matching the required skill.

---

## 🧪 Example

### Input
```json
{"query": "Need a maid for cooking"}

Output

Top matching maids:

1. Anita (5 yrs)
   Skills: cooking, elder care
   Language: Tamil

🌐 Deployment

Agent URL: https://maid-agent-968767205311.us-central1.run.app
MCP Server: Deployed separately on Cloud Run

📁 Project Structure

maid-mcp-agent/
│
├── agent/
├── mcp_client/
├── mcp_server/
├── data/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

🚀 Technologies Used
FastAPI
Python
Model Context Protocol (MCP)
Google Cloud Run
Docker

🎯 Key Learning
Separation of AI reasoning and tool execution
Building scalable AI agents
Deploying microservices on Cloud Run
MCP-based integrations

🏆 Conclusion

This project successfully demonstrates how AI agents can securely interact with external systems using MCP, fulfilling all project requirements.