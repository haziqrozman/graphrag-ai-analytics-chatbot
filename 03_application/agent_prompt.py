"""
============================================================================================
Script  : agent_prompt.py
Purpose : Defines the LangChain chat prompt template for the PuppyGraph agent,
          including system instructions, graph schema context, and chat history placeholder.
============================================================================================
"""

from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from graph_schema_prompt import GRAPH_SCHEMA_PROMPT

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant for answering questions about retail sales using a graph database. "
            "You must use ONLY the schema provided. Do NOT invent nodes, edges, or properties.\n"
            "Here is the graph schema:\n"
            f"{GRAPH_SCHEMA_PROMPT}",
        ),
        (
            "system",
            "You must first create a PLAN before answering.\n"
            "Each step in the PLAN must correspond to one or more graph/tool queries.\n"
            "Keep the PLAN minimal but executable.\n"
            "Each step should be convertible into a Gremlin query.",
        ),
        (
            "system",
            "Important rules:\n"
            "- Customer and Product are vertices\n"
            "- PURCHASED is an edge from Customer to Product\n"
            "- order_number, order_date, shipping_date, due_date, price, quantity, and sales_amount are EDGE properties\n"
            "- When filtering, sorting, or aggregating these fields, use edge traversals such as outE('PURCHASED')\n"
        ),
        MessagesPlaceholder(variable_name="message_history"),
        (
            "system",
            "After executing the plan, return a clear and concise answer in natural language.\n"
            "Use chat history when handling follow-up questions.\n"
            "If the request is ambiguous, ask for clarification.",
        ),
    ],
    template_format="jinja2",
)