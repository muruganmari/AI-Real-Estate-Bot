from crewai import Crew
from agent import property_researcher, property_analyst
from task import property_research_task, analysis_task
import streamlit as st



crew = Crew(
    agents = [property_researcher ],
    tasks=[property_research_task],
    verbose = True
)

task_output = crew.kickoff()
print(task_output)