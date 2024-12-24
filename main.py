from crewai import Crew, Process
from tools import search_tool
from agents import trend_finder,content_writer,copy_writer
from tasks import trend_task,content_task,Copy_task
from dotenv import load_dotenv
import re

load_dotenv()

crew1 = Crew(
    agents=[trend_finder],
    tasks=[trend_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

crew2 = Crew(
    agents=[content_writer],
    tasks=[content_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

crew3 = Crew(
    agents=[copy_writer],
    tasks=[Copy_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result=crew1.kickoff({"niche":"Artificial Intelligence"})
print(result.raw)
result_raw=result.raw
topics = result_raw.strip().split("\n")

# Step 2: Remove any numbers or periods and clean the topics list
cleaned_topics = [topic.split(". ", 1)[1] if ". " in topic else topic for topic in topics]

# Print the final list of topics
# print(cleaned_topics)


# if result.json_dict:
#     print(f"JSON Output: {json.dumps(result.json_dict, indent=2)}")
# print(result['result']['topics'])

for topic in cleaned_topics:
    result2 = crew2.kickoff(inputs={
        "topic": topic  # Use the result from the trend_finder agent
    })
    print(result2)

content=result2.raw

result3=crew3.kickoff({"contents":content})
print(result3)

