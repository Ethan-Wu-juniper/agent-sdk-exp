import asyncio
from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    tools=[
        WebSearchTool(),
    ],
)

async def main():
    result = await Runner.run(agent, "Which coffee shop should I go to, taking into account my preferences and the weather today in SF? I love ambiance.")
    print(result.final_output)
    
asyncio.run(main())