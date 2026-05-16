"""
============================================================================================
Script  : puppygraph_agent.py
Purpose : Initialises the PuppyGraphAgent by wiring the PuppyGraph client,
          LLM, and chat prompt template into a single agent instance.
============================================================================================
"""

from puppygraph.rag import PuppyGraphAgent
from puppygraph_client import client
from llm import llm
from agent_prompt import chat_prompt_template

pg_agent = PuppyGraphAgent(
    puppy_graph_client=client,
    llm=llm,
    chat_prompt_template=chat_prompt_template
)