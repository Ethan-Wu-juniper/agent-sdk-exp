import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner


load_dotenv()

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent]
)

async def main():
    result = await Runner.run(triage_agent, "What is the capital of France?")
    print(result.final_output)

asyncio.run(main())

"""
The capital of France is Paris. It's not only the political center of the country but also a major cultural, economic, and historical hub. Paris has played a significant role throughout French history, from the French Revolution to being a central figure in the arts and fashion.
"""