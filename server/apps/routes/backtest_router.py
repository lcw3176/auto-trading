from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import logging
from datetime import datetime
from apps.services import coin_service

router = APIRouter()


@router.websocket("/backtest")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_json()

            result = coin_service.get_candle_data(ticker_kor=data['ticker'],
                                         interval_kor=data['candleMinute'],
                                         start_date=data['startDate'],
                                         end_date=data['endDate'])

            for i in result:
                await websocket.send_json(i)

    except WebSocketDisconnect:
        await websocket.close()



@router.get("/backtest")
def get_backtest_info():
    # fixme 코인에 한정되지 않게 수정

    return coin_service.get_backtest_info()