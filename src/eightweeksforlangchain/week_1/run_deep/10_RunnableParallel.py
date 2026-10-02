from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from config import init_model

prompt_joke = ChatPromptTemplate.from_template("讲一个关于{topic}的笑话")
prompt_fact = ChatPromptTemplate.from_template("说一个关于{topic}的冷知识")
model = init_model()
parser = StrOutputParser()
chain = RunnableParallel({
    "joke": prompt_joke | model | parser,
    "fact": prompt_fact | model | parser,
})

result = chain.invoke({"topic": "AI"})
# result = {"joke": "...", "fact": "..."}