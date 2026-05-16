"""
============================================================================================
Script  : app.py
Purpose : Launches the Gradio web interface for the GraphRAG AI Analytics Chatbot,
          routing user queries through the PuppyGraph agent and rendering responses.
Run     : python app.py
============================================================================================
"""

import gradio as gr
from puppygraph_agent import pg_agent

CUSTOM_CSS = """
.chatbot-responsive {
  height: clamp(400px, 65vh, 800px) !important;
  overflow: hidden !important;
  display: flex !important;
  flex-direction: column !important;
}
.chatbot-responsive > div {
  flex: 1 !important;
  min-height: 0 !important;
  overflow: hidden !important;
  display: flex !important;
  flex-direction: column !important;
}
.chatbot-responsive > div > div {
  flex: 1 !important;
  min-height: 0 !important;
}
"""

def chat_fn(message, history):
    try:
        final = None
        for msg in pg_agent.query(message):
            if not getattr(msg, "tool_calls", None):
                final = msg
        return final.content if final else "No response returned."
    except Exception as e:
        return f"Sorry, I hit an error while querying the graph: {e}"


with gr.Blocks(css=CUSTOM_CSS) as demo:
    gr.ChatInterface(
        fn=chat_fn,
        title="GraphRAG AI Analytics Chatbot",
        description="Query customer profiles, product details, and sales transactions from the DataAnalytics database using natural language.",
        chatbot=gr.Chatbot(elem_classes="chatbot-responsive"),
    )
    gr.HTML(
        """
        <div style="text-align:center; font-size:0.75em; color:#666; padding:10px 0;">
            © 2026 github.com/haziqrozman
        </div>
        """
    )

if __name__ == "__main__":
    demo.launch()