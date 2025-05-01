from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_ollama.llms import OllamaLLM

# ✅ Use LangChain Ollama LLM instead of LiteLLM string
custom_llm = OllamaLLM(model="ollama/qwen3:1.7b")

# Create tool
search_tool = SerperDevTool()

# Define agent
researcher = Agent(
    llm=custom_llm,
    role="Retail Property Research Analyst",
    goal="Find top retail property investment locations in Tamil Nadu.",
    backstory="Experienced real estate analyst specializing in Indian markets.",
    tools=[search_tool],
    verbose=True
)

# Define task
task = Task(
    description="Identify emerging high-potential retail zones in Tamil Nadu.",
    expected_output="Top 5 cities with market insights and ROI estimates.",
    agent=researcher
)

# Run crew
crew = Crew(
    agents=[researcher],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()