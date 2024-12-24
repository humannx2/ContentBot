from crewai import Task
from tools import search_tool
from agents import content_writer,trend_finder,copy_writer

# Trend finder task
trend_task=Task(
    agent=trend_finder,
    description=("Identify the trending topics in {niche} niche."),
    expected_output="A List of top 3 most trending topics based on the {niche} niche",
    tools=[search_tool],
)

# Content writer task
content_task=Task(
    agent=content_writer,
    description=("Write an educating and exciting summary on the topic of {topic}"),
    expected_output="A comprehensive paragraph detailing the information about the topic of {topic}",
    tools=[search_tool],
    output_file='content.md'
)
# Copy task
Copy_task=Task(
    agent=copy_writer,
    description=("Write a Social Media copy based on the content {contents}"),
    expected_output="A 200 character post that has a hook, informative content, and CTA towards the end",
    output_file='copy.md'
)