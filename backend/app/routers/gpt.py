from fastapi import APIRouter, Body, Depends
import openai
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..security import get_current_active_user, has_role
from .. import schemas, models

router = APIRouter(prefix="/gpt", tags=["gpt"])

@router.post("/chat")
async def chat(prompt: str = Body(..., embed=True), current_user: models.User = Depends(has_role(["admin", "expert", "advanced"])), db: Session = Depends(get_db)):
    # In a real application, you would use current_user.id to log interactions or manage usage.
    # For now, we'll just use a dummy response.
    
    # Example of how to use OpenAI API (ensure OPENAI_API_KEY is set in environment)
    # try:
    #     response = openai.ChatCompletion.create(
    #         model="gpt-4.1", # Or whatever model you intend to use
    #         messages=[
    #             {"role": "system", "content": "You are a helpful trading assistant."},
    #             {"role": "user", "content": prompt}
    #         ]
    #     )
    #     ai_response = response.choices[0].message.content
    # except Exception as e:
    #     ai_response = f"Error communicating with AI: {e}"

    ai_response = f"KI-Antwort auf: {prompt} (User: {current_user.email})"
    
    # Log the interaction (optional)
    audit_log = models.AuditLog(user_id=current_user.id, action="GPT Chat", details=f"Prompt: {prompt}, Response: {ai_response}")
    db.add(audit_log)
    db.commit()
    db.refresh(audit_log)

    return {"response": ai_response}