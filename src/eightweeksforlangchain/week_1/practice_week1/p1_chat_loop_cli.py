from langchain.messages import SystemMessage, HumanMessage, AIMessage
from config import init_model

messages: list[SystemMessage|HumanMessage|AIMessage] = [
    SystemMessage("你是一位专热情的解答助手，回答要简洁。"),

]
model = init_model('qwen-plus')

print("你好！我是你的AI助手，有什么可以帮到你的吗？尽管提问")
while True:
    in_str = input()
    if in_str == "exit":
        print("AI对话程序已退出")
        break
    messages.append(HumanMessage(in_str))
    response = model.invoke(messages)
    messages.append(AIMessage(response.content))
    print(response.content)

print(messages)
