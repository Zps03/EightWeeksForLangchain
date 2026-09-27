from langchain.messages import SystemMessage, HumanMessage
from config import init_model

model = init_model("qwen-plus")

messages = [
    SystemMessage("你是一位专业的 Python 导师，回答要简洁。"),
    HumanMessage("什么是列表推导式？"),
]

response = model.stream(messages)
for chunk in response:
    print(chunk.text,end="",flush=True)

