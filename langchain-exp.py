from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm


load_dotenv()
model = ChatOpenAI(model="gpt-4o")
checkpointer = InMemorySaver()


history_tutor_agent = create_react_agent(
    model,
    [],
    prompt="You provide assistance with historical queries. Explain important events and context clearly.",
    name="History_Tutor",
)

math_tutor_agent = create_react_agent(
    model,
    [],
    prompt="You provide help with math problems. Explain your reasoning at each step and include examples",
    name="Math_Tutor",
)

triage_agent = create_react_agent(
    model,
    [
        create_handoff_tool(agent_name="Math_Tutor", description="Specialist agent for math questions"),
        create_handoff_tool(agent_name="History_Tutor", description="Specialist agent for historical questions")
    ],
    prompt="You determine which agent to use based on the user's homework question",
    name="Triage_Agent",
)

workflow = create_swarm(
    [triage_agent, history_tutor_agent, math_tutor_agent],
    default_active_agent="Triage_Agent"
)
app = workflow.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "1"}}
    turn_1 = app.invoke(
        {"messages": [{"role": "user", "content": "What is the capital of France?"}]},
        config,
    )
    print(turn_1["messages"][-1].content)
    
"""
The capital of France is Paris. Known as the "City of Light" (La Ville Lumière), Paris is not only the political center of the country but also a major hub for art, fashion, gastronomy, and culture. Its rich history and numerous landmarks, including the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum, make it one of the most visited cities in the world. Paris has played a significant role in European history and has been at the heart of events like the French Revolution and various cultural and intellectual movements.
"""