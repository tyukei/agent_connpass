from google.adk.agents import Agent




root_agent = Agent(
    name="connpass_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about the events on connpass."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the events on connpass."
    ),
    tools=[get_weather, get_current_time],
)