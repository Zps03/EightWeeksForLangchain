from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableSerializable

from config import init_model

prompt = ChatPromptTemplate.from_messages([
    ("system", "你的角色是一个{role}。"),
    MessagesPlaceholder(variable_name="history1"),
    MessagesPlaceholder(variable_name="history2"),
    ("human", "{input}"),
])
history_data_1 = [
    HumanMessage("你好"),
    AIMessage("你好！有什么可以帮你的？"),
]
history_data_2 = [
    HumanMessage("你是什么模型？"),
    AIMessage("我是deepseek-v4-flash"),
]
model = init_model("qwen-plus")
chain:RunnableSerializable = prompt | model

result = chain.invoke({
    "history1": history_data_1,
    "history2": history_data_2,
    "input": "基于聊天记录回答你是什么模型？你是什么角色？请简洁的回答什么是 LCEL？",
    "role": "大黄蜂",
})

print(result.content)
