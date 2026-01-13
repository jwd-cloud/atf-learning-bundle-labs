from google.adk import Agent
from google.adk.tools import load_memory  # Tool to query memory
from google.adk.tools import google_search
from google.adk.tools.preload_memory_tool import PreloadMemoryTool


def get_weather(city: str, unit: str):
    """
    Retrieves the weather for a city in the specified unit.

    Args:
        city (str): The city name.
        unit (str): The temperature unit, either 'Celsius' or 'Fahrenheit'.
    """
    # ... function logic ...
    return {"status": "success", "report": f"Weather for {city} is sunny."}

# Create the agent
root_agent = Agent(
    name="gemini_cloud_tutor",
    model="	gemini-3-flash-preview",
    instruction="""
    You're my cloud technology tutor, helping me develop a solid understanding of Google Cloud concepts and products. 
    You're working to make sure I understand the concept and the application.
    """,
    tools=[load_memory, get_weather]
)