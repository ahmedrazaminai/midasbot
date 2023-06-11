from fastapi import FastAPI, websockets

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: websockets.WebSocket):
    await websocket.accept()
    text = await websocket.receive_text()
    print(f"Message received: {text}")
    await websocket.send_text(f"Message text was: {text}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)