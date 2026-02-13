from agents import Agent
from pathlib import Path
from src.config import VECTOR_STORE_ID

PROMPT_PATH = Path("src/prompts/system_prompt.txt")

def build_agent():
    instructions = PROMPT_PATH.read_text(encoding="utf-8")

    tools_list = []

    if VECTOR_STORE_ID:
        from agents import tool as agent_tool
        tools_list.append(
            agent_tool.FileSearchTool(
                vector_store_ids=[VECTOR_STORE_ID]
            )
        )

    agent = Agent(
        name="Mozondó",
        instructions=instructions,
        tools=tools_list,
    )

    return agent
