# app/routes/chat.py
# 실시간 그룹 채팅을 위한 WebSocket API 엔드포인트
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

router = APIRouter()

# 그룹별로 채팅 연결을 관리할 수 있도록 간단한 연결 리스트 사용
active_connections: List[WebSocket] = []

@router.websocket("/ws/{group_id}")
async def websocket_endpoint(websocket: WebSocket, group_id: str):
    """
    그룹 채팅을 위한 WebSocket 연결을 처리합니다.
    각 메시지를 연결된 모든 클라이언트에게 브로드캐스트합니다.
    """
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # 모든 연결에 메시지 전송
            for connection in active_connections:
                await connection.send_text(f"[Group {group_id}] {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
