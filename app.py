import chainlit as cl
from agents.chatbot_agent import run_chatbot

@cl.on_message
async def on_message(msg: cl.Message):
    from agents.chatbot_agent import run_chatbot
    try:
        response = await run_chatbot(msg.content)
        await cl.Message(content=response).send()
    except Exception as e:
        await cl.Message(content=f"⚠️ Error: {e}").send()

