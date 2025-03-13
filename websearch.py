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

"""
Considering your appreciation for ambiance and the current weather conditions in San Francisco, here are some coffee shops that offer a cozy and inviting atmosphere:

**[Caffe Trieste](https://www.google.com/maps/search/Caffe+Trieste%2C+San+Francisco%2C+CA)**
_San Francisco, CA_
Established in 1956, this historic North Beach café exudes old-world charm with its vintage decor and live music sessions. It's an iconic spot to enjoy a classic espresso while soaking in the artistic ambiance.

**[The Mill](https://www.google.com/maps/search/The+Mill%2C+San+Francisco%2C+CA)**
_San Francisco, CA_
Located on Divisadero Street, The Mill combines artisanal coffee with freshly baked bread in a rustic setting. The warm wooden interiors and natural light create a welcoming environment, perfect for a leisurely coffee break.

**[Four Barrel Coffee](https://www.google.com/maps/search/Four+Barrel+Coffee%2C+San+Francisco%2C+CA)**
_San Francisco, CA_
Situated in the Mission District, Four Barrel offers a minimalist yet cozy space with high ceilings and a focus on quality coffee. The absence of Wi-Fi encourages patrons to unwind and enjoy the ambiance.

**[Sightglass Coffee](https://www.google.com/maps/search/Sightglass+Coffee%2C+San+Francisco%2C+CA)**
_San Francisco, CA_
With its industrial-chic design and on-site roastery, Sightglass provides a unique coffee experience. The spacious interior and attention to detail make it a great place to relax and savor your drink.

**[Ritual Coffee Roasters](https://www.google.com/maps/search/Ritual+Coffee+Roasters%2C+San+Francisco%2C+CA)**
_San Francisco, CA_
A pioneer in the specialty coffee scene, Ritual's Hayes Valley location, housed in a repurposed shipping container, offers a charming and intimate setting to enjoy meticulously crafted brews.

**[Andytown Coffee Roasters](https://www.google.com/maps/search/Andytown+Coffee+Roasters%2C+San+Francisco%2C+CA)**
_San Francisco, CA_
Known for its signature Snowy Plover drink, Andytown's cozy atmosphere and commitment to quality make it a must-visit. The Outer Sunset location provides a warm refuge from the rain.

Given the forecasted heavy rain and strong winds today, it's advisable to choose a coffee shop close to your location to minimize exposure to the elements. All the mentioned establishments are known for their inviting atmospheres, making them excellent choices to enjoy a warm beverage while staying dry and comfortable. 
OPENAI_API_KEY is not set, skipping trace export
"""