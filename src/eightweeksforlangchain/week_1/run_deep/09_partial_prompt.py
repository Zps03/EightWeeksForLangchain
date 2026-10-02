from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("你是一名{role}，请解释{concept}。")   #提示词模版
print(prompt.messages)
partial_prompt = prompt.partial(role="Python 导师")       #先预填充部分变量
print(partial_prompt.messages)
concept = input("请输入要解释的内容：")
result = partial_prompt.invoke({"concept": concept})    #invoke生成最终的提示词
print(result.to_string())

