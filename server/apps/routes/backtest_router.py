from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import logging
from datetime import datetime

router = APIRouter()


@router.websocket("/backtest")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_json()


            await websocket.send_json({
                "open": 100,
                "high": 120,
                "low": 80,
                "close": 90,
                "time": datetime.now().timestamp() / 1000 + 32400,
            })

    except WebSocketDisconnect:
        logging.info("WebSocket connection closed")
        await websocket.close()