import asyncio
from agents import Agent, Runner, ComputerTool, Computer
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    tools=[
        ComputerTool(Computer()),
    ],
)

async def main():
    result = await Runner.run(agent, "你可以用 ComputerTool 做什麼事情")
    print(result.final_output)
    
asyncio.run(main())