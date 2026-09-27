from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

from config import init_model

model = init_model("qwen-plus")
prompt=ChatPromptTemplate.from_messages([
    AIMessage("你是一个热心的助手，你叫大黄蜂。"),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

chain = prompt|model|StrOutputParser()
history=[]

while True:
    user_input = input("提问/聊天：")
    if "exit" in user_input:
        break
    while user_input=="":
        user_input = input("请输入提问/聊天内容：")
    full_rse=""
    print("AI：", end="")
    res = chain.stream({"history":history,"input":user_input})
    for chunk in res:
        print(chunk, end="", flush=True)
        full_rse+=chunk
    print("\n\n")

    history.append(HumanMessage(user_input))
    history.append(AIMessage(full_rse))



