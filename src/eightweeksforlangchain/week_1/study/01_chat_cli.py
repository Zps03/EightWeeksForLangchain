from config import init_model
from dotenv import load_dotenv

load_dotenv()

model = init_model("qwen3.5-flash")
response=model.stream("帮我生成一篇300字作文，题目为《碧蓝的湖》，要求用俄语写作")
for chunk in response:
    print(chunk.content,end="",flush=True)

'''
# ChatOpenAI初始化模型，调用api
chat_model = ChatOpenAI(

    #model="deepseek-v4-flash",
    #model="qwen3.8-flash",
    #model="glm-5.2",
    #model="kimi-k2.5",

    model="qwen3.8-flash",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
response = chat_model.invoke("你是什么模型？你能做什么？")
print(response.text)
'''


