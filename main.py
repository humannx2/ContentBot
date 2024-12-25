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
    cache=False,
    max_rpm=100,
    share_crew=True
)

crew2 = Crew(
    agents=[content_writer],
    tasks=[content_task],
    process=Process.sequential,
    memory=True,
    cache=False,
    max_rpm=100,
    share_crew=True
)

crew3 = Crew(
    agents=[copy_writer],
    tasks=[Copy_task],
    process=Process.sequential,
    memory=True,
    cache=False,
    max_rpm=100,
    share_crew=True
)

result=crew1.kickoff({"niche":"Search Engine Optimization"})
# print(result.raw)
result_raw=result.raw
topics = result_raw.strip().split("\n")
cleaned_topics = [topic.split(", ", 1)[1] if ", " in topic else topic for topic in topics]

print(cleaned_topics)

for topic in cleaned_topics:
    print(topic)
    # result2 = crew2.kickoff(inputs={"topic": topic})
    crew2.kickoff(inputs={"topic":topic})
#     # print(result2)

# # content=result2.raw

# contents = result2_raw.strip().split("\n")
# cleaned_content = [topic.split(". ", 1)[1] if ". " in content else content for content in contents]

# for content in cleaned_content:
#     result3=crew3.kickoff({"contents":content})

