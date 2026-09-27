from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable

from config import init_model

prompt = ChatPromptTemplate.from_template("用一句话解释{topic}")
model = init_model("qwen-plus")
parser = StrOutputParser()
#chain = prompt | model | parser
chain: RunnableSerializable = prompt | model

result = chain.stream({"topic": "量子计算"})
for chunk in result:
    print(chunk.text,end="",flush=True)  # 直接是字符串

