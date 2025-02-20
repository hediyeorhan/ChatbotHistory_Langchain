from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from langserve import add_routes
from fastapi import FastAPI
from typing import List


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key = os.getenv("GEMINI_API_KEY"))


store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | model
config = {"configurable": {"session_id": "firstChat"}}
with_message_history = RunnableWithMessageHistory(chain, get_session_history)


if __name__ == "__main__":

    while True:
        user_input = input("> ")
        for r in with_message_history.stream(
                {
                    "messages": [HumanMessage(content=user_input)]
                },
                config=config,
        ):
            print(r.content, end="")