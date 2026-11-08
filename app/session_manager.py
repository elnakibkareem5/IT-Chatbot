# In-memory or Redis ticket/turn tracker

from typing import Dict, List, Optional
import Time

class TicketSessionManager:
	def __init__(self, max_turns: int = 3):
		self.max_turns = max_turns
		self.sessions: Dict[str, dict] = {}
	def get_or_create_session(self, ticket_id: str) -> dict:
	if ticket_id not in self.sessions:
            self.sessions[ticket_id] = {
                "turns": 0,
                "status": "ACTIVE",
                "history": [
                    {
                        "role": "system",
                        "content": (
                            "You are an IT Support Assistant. Help users resolve standard software, "
                            "hardware, and networking issues step-by-step. Keep answers concise."
                        )
                    }
                ],
                "created_at": time.time()
            }
            return self.sessions[ticket_id]
