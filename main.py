from courses.intro import intro
from courses.searchagents import *
from courses.reactprompt import *


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
    # search() : Sample web search using custom Search tool and tavily.search method
    custom_search()
    # react_prompt() : Sample web search using react prompt tavily.search method
    react_prompt()


if __name__ == '__main__':
    main()
