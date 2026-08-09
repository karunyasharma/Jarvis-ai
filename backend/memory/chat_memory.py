from database.db import SessionLocal
from database.models import Conversation


class ChatMemory:

    def get_history(self, session_id: str):

        db = SessionLocal()

        try:
            messages = (
                db.query(Conversation)
                .filter(Conversation.session_id == session_id)
                .order_by(Conversation.id.asc())
                .all()
            )

            return [
                {
                    "role": message.role,
                    "content": message.content,
                }
                for message in messages
            ]

        finally:
            db.close()

    def add_message(self, session_id: str, role: str, content: str):

        db = SessionLocal()

        try:
            message = Conversation(
                session_id=session_id,
                role=role,
                content=content,
            )

            db.add(message)
            db.commit()

        finally:
            db.close()


memory = ChatMemory()
