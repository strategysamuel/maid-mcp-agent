print("Agent container starting...")

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Maid Matching Agent</title>
        <style>
            body {
                font-family: Arial;
                max-width: 600px;
                margin: auto;
                padding: 40px;
                background: #f9fafb;
            }
            h2 {
                color: #333;
            }
            textarea {
                width: 100%;
                height: 80px;
                padding: 10px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }
            button {
                padding: 10px 20px;
                margin-top: 10px;
                border: none;
                background: #007bff;
                color: white;
                border-radius: 6px;
                cursor: pointer;
            }
            button:hover {
                background: #0056b3;
            }
            #response {
                margin-top: 20px;
                white-space: pre-wrap;
                background: white;
                padding: 15px;
                border-radius: 6px;
                border: 1px solid #ddd;
            }
        </style>
    </head>
    <body>

    <h2>🤖 Maid Matching Agent</h2>

    <textarea id="query" placeholder="Enter your requirement (e.g., Need a maid for cooking)"></textarea>

    <br>
    <button onclick="sendQuery()">Search</button>

    <div id="response"></div>

    <script>
    async function sendQuery() {
        const query = document.getElementById("query").value;

        const res = await fetch("/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: query })
        });

        const data = await res.json();
        document.getElementById("response").innerText = data.response || data.error;
    }
    </script>

    </body>
    </html>
    """

@app.post("/query")
def query(payload: dict):
    try:
        from agent.agent import process_query

        user_query = payload.get("query", "")
        response = process_query(user_query)

        return {"response": response}

    except Exception as e:
        return {"error": str(e)}