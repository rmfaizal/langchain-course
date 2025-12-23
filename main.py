from courses.intro import intro
from courses.react_agent import *
from courses.react_native_tool_calling import native_tool_calling
from courses.reactprompt import *
from courses.searchagents import *


def main():
    """
    Topics are separated as packages inside courses.
    :return:
    """
    print("Hello from Langchain Tutorial")
    # intro : Sample chat using models from OpenAI and Ollama
    intro()
    # tavily_search() : Sample web search using standard TavilySearch tool
    tavily_search()
    # search() : Sample web search using custom Search tool and tavily.search method (create_agent)
    custom_search()
    # react_prompt() : Sample web search using react prompt tavily.search method
    react_prompt()
    # create_react_agents are recommended for older langchain versions, langchain v1.0+ recommends create_agent
    # react_agent_with_output_parser() : Sample web search using react agent with output parser
    react_agent_with_output_parser()
    # react_agent_with_structured_output() : Sample web search using react agent with structured output (recommended
    # method over output parser)
    react_agent_with_structured_output()
    # native_tool_calling() : Manual Tool and LLM calling , instead of using Langchain Agent
    native_tool_calling()


if __name__ == "__main__":
    main()
