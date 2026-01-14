from pydantic import BaseModel

class WazuhEvent(BaseModel):
    rule_id: str
    agent: str
