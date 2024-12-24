from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool,SeleniumScrapingTool
from dotenv import load_dotenv
import os
import re

load_dotenv()

search_tool = SerperDevTool(
    search_url="https://google.serper.dev/search",
    n_results=4,
)

# def get_trending_topics(query):
#     raw_topics = search_tool.run(search_query=query)

#     # Parse the raw string output into a list of dictionaries
#     pattern = r"Title:\s*(.*?)\s*Link:\s*(https?://[^\s]+)\s*Snippet:\s*(.*?)\n"
#     parsed_topics = [
#         {"title": match[0], "link": match[1], "snippet": match[2]}
#         for match in re.findall(pattern, raw_topics, re.DOTALL)
#     ]
#     return parsed_topics


# # def extract(query):
# #     parsed_topics=get_trending_topics(query)
# #     # scraper_tools=ScrapeWebsiteTool()
# #     for topic in parsed_topics:
# #         scraper_tool = ScrapeWebsiteTool(website_url=topic["link"])
# #         text=scraper_tool.run
# #         print(f"Content from {topic['title']}:\n{text}\n")
# # extract("Machine Learning")

# def extract(query):
#     parsed_topics=get_trending_topics(query)
#     for topic in parsed_topics:
#         # print(topic["link"])
#         tool = SeleniumScrapingTool(
#     website_url=topic["link"],
#     css_element='.main-content'
# )
#         text=tool.run
#         print(f"Content from {topic['title']}:\n{text}\n")
# extract("Machine Learning")

# # # print(search_tool.run(search_query="ChatGPT"))
# # def get_trending_topics(query):
# #     return search_tool.run(search_query=query)

# # # Regex pattern to extract Title, Link, and Snippet
# # pattern = r"Title:\s*(.*?)\s*Link:\s*(https?://[^\s]+)\s*Snippet:\s*(.*?)\n"

# # # Get trending topics for 'AI'
# # raw_topics = get_trending_topics("AI")
# # print("Parsed Search Results:\n")

# # # Use regex to find all matches
# # matches = re.findall(pattern, raw_topics, re.DOTALL)
# # parsed_topics=[]

# # for match in matches:
# #     title, link, snippet = match
# #     parsed_topics.append({
# #         "title": title,
# #         "link": link,
# #         "snippet": snippet
# #     })

# # # # Print the parsed results
# # # for match in matches:
# # #     title, link, snippet = match
# # #     print(f"Title: {title}")
# # #     print(f"Link: {link}")
# # #     print(f"Snippet: {snippet}")
# # #     print("-" * 50)  # Add separator for better readability

# # # Print the parsed dictionary
# # for topic in parsed_topics:
# #     print(f"Title: {topic['title']}")
# #     print(f"Link: {topic['link']}")
# #     print(f"Snippet: {topic['snippet']}")
# #     print("-" * 50)

# # # Access the results programmatically as a list of dictionaries
# # print("\nList of Dictionaries:", parsed_topics)

