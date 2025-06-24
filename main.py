from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    noise_cancellation,
    
)
import threading
import question_parceing
import result_agent
import pdf_report
from datetime import datetime
import json
from livekit.agents import (
    AutoSubscribe,
    
    
)
import random


load_dotenv()
JOB_TITLE = "python engineer"
JD = "a gen ai expert ts needed urgently!!"
COMPANY = "amazon"
LEVEL = 3
TIME = 10
QUESTIONS = str(question_parceing.get_questions(job_title=JOB_TITLE,jd=JD,company=COMPANY,level=LEVEL,interview_time=TIME))
print("questions imported")

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=f"You are a professional interviewer. You will conduct an interview for the position of {JOB_TITLE} at {COMPANY}. The interview will last for {TIME} minutes. You will ask questions based on the provided job description and level. You will use the following instructions: {QUESTIONS}. You will use a random Indian name to introduce yourself at the beginning of the interview.DO NOT EXPLAIN ANYTHING OUT OF CONTEXT OF THE INTERVIEW.SPEAK IN INDIAN ACCENT")

async def entrypoint(ctx: agents.JobContext):
    async def write_transcript():
        current_date = datetime.now().strftime("%Y%m%d_%H%M%S")

        
        filename = f"transcripts/transcript_{ctx.room.name}_{current_date}.json"
        filename1 = f"transcripts/RESULT_{ctx.room.name}_{current_date}.pdf"

        with open(filename, 'w+') as f:
            json.dump(session.history.to_dict(), f, indent=2)
        json_input = result_agent.get_result(session.history.to_dict())
        pdf_report.generate_interview_report(data=json_input, output_filename=filename1)   

    
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            model="gpt-4o-mini-realtime-preview-2024-12-17",
            voice=random.choice(['alloy', 'echo', 'shimmer', 'ash', 'ballad', 'coral', 'sage', 'verse']),
            )
        
    )
    
    
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
                noise_cancellation=noise_cancellation.NC(),
        ),

    )
    def my_function():
        ctx.shutdown(reason="Session ended")
    timer = threading.Timer(TIME*60, my_function) 
    timer.start()
    ctx.add_shutdown_callback(write_transcript)
    ctx.add_shutdown_callback(lambda: print("Session ended."))
    ctx.add_shutdown_callback(lambda: timer.cancel())
    
    
    


if __name__ == "__main__":
    print("questions imported")
    print(QUESTIONS)
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
    