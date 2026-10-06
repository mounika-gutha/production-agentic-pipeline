from dataclasses import dataclass
@dataclass
class ChatRequest:
    session_id:str
    message:str
    provider:str='auto'
