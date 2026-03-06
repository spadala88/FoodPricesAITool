from fastapi import FastAPI, HTTPException, Form
from agent import ChatAgent

app = FastAPI()

chat_agent = ChatAgent()

@app.post("/chat")
async def chat(
    query: str = Form(...)
):
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    print("asking agent")

    result = await chat_agent.run(query)

    return {
        "answer": result
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)