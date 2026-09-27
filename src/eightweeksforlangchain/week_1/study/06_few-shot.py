from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
)
from langchain_core.runnables import RunnableSerializable
from config import init_model

example_prompt = ChatPromptTemplate.from_messages([
    #("human", "{input}"),
    #("ai", "{output}"),

    HumanMessagePromptTemplate.from_template("{input}"),
    AIMessagePromptTemplate.from_template("{output}"),
])
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "3*5", "output": "15"},
]
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是数学计算器，输出结果并分析计算过程。"),
    few_shot_prompt,
    ("human", "{input}"),
])
print(final_prompt)
model = init_model()
chain: RunnableSerializable = final_prompt | model | StrOutputParser()
res = chain.stream({"input":"5+6*7"})
for chunk in res:
    print(chunk,end="",flush=True)



