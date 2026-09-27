from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

prompt = PromptTemplate.from_template(
    "你是一名{role}，请设计{feature}的测试用例。"
)
result_1 = prompt.invoke({"role": "Python 导师", "feature": "用户登录"})
print(result_1)


prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一名{role}，擅长{skill}。"),
    ("human", "请解释{concept}。"),
])

result_2 = prompt.invoke({
    "role": "Python 导师",
    "skill": "数据结构",
    "concept": "哈希表",
})
print(result_2)

