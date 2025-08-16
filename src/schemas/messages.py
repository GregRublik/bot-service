from pydantic import BaseModel

class OutgoingMessage(BaseModel):
    text: str
    chat_id: int
    date: str
