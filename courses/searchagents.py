from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch


class Source(BaseModel):
    """Schema for a source used by the Agent"""

    url:str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")


tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
         The search results
    """
    print(f"Searching for {query}")
    # return "Tokyo weather is sunny"
    return tavily.search(query=query)


def custom_search():
    llm = ChatOpenAI(model='gpt-5-nano')
    # llm = ChatOllama(model='gemma3:270m')
    tools = [search]
    agent = create_agent(model=llm, tools=tools)
    print("Hello from Tutorial: Tavily Custom Search")
    # result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    result = agent.invoke({"messages": HumanMessage(content="search for job postings for an ai engineer using langchain in the Dubai area on linkedin and list their details")})
    print(result)


def tavily_search():
    llm = ChatOpenAI(model='gpt-5-nano')
    # llm = ChatOllama(model='gemma3:270m')
    tools = [TavilySearch()]
    agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
    print("Hello from Tutorial: tavily search")
    # result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    result = agent.invoke({"messages": HumanMessage(content="search for job postings for an ai engineer using langchain in the Dubai area on linkedin and list their details")})
    print(result)


if __name__ == '__main__':
    # custom_search()
    tavily_search()
