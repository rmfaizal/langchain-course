from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOpenAI(model='gpt-4')
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


def react_prompt():
    print("Hello from langchain course - react prompt")
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the Dubai area and list their details"
        }
    )
    print(result)




if __name__ == '__main__':
    react_prompt()

