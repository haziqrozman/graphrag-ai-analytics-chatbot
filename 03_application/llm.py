"""
============================================================================================
Script  : llm.py
Purpose : Configures the LangChain LLM instance pointing to a locally hosted
          model served via LM Studio.
============================================================================================
"""

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    temperature=0,
    base_url="http://127.0.0.1:1234/v1",
    api_key="EMPTY"
)