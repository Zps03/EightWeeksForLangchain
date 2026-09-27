from config import init_model

model = init_model("qwen-plus")
response = model.invoke("你是什么模型？请列出你的具体模型版本号，如“deepseek-v4-flash”这样带有后缀")
print(response.content)

