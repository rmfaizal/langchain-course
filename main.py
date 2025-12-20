from courses.intro import intro
from courses.searchagents import *


def main():
    print("Hello from Langchain Tutorial")
    # intro : Sample chat using models from OpenAI and Ollama
    intro()
    # tavily_search() : Sample web search using standard TavilySearch tool
    tavily_search()
    # search() : Sample web search using custom Search tool and tavily.search method
    custom_search()


if __name__ == '__main__':
    main()
