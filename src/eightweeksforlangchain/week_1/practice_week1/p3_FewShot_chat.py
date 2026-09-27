from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate,\
    FewShotChatMessagePromptTemplate

from config import init_model

example_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template("{input}"),
    AIMessagePromptTemplate.from_template("{output}"),
])

example = [
    {"input":"今天收到心仪公司的录用通知，太开心了", "output":"积极"},
    {"input": "这家店的服务特别贴心，体验超出预期", "output": "积极"},
    {"input": "虽然有点累，但看到孩子笑得那么开心，觉得一切都值得", "output": "积极"},
    {"input": "排队等了两小时，结果还告诉我预约取消了", "output": "消极"},
    {"input": "他说话阴阳怪气，让人很不舒服", "output": "消极"},
    {"input": "这电影太无聊了，我中途差点睡着", "output": "消极"},
    {"input": "还行吧", "output": "中性"},
    {"input": "也就那样", "output": "中性"},
    {"input": "今天阴天，气温和昨天差不多", "output": "中性"},
]

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=example,
)
final_prompt = ChatPromptTemplate.from_messages([
    SystemMessage("你是一名情感分析师，分析结果输出必须严格使用{ 积极 / 消极 / 中性 }这三个词中的一个，不带标点、不带解释"),
    few_shot_prompt,
    HumanMessagePromptTemplate.from_template("{input}"),
])
model = init_model(model_name="qwen-plus", temperature= 0)
chain = final_prompt | model |StrOutputParser()

input_list = [
    {"input": "虽然今天加班到很晚，但项目顺利通过了，心里挺高兴"},
    {"input":"满心期待地打开包裹，结果东西是坏的，客服还一直推脱"},
    {"input":"还可以吧，没什么特别感觉，说不上好也说不上差"},
    {"input":"凑合吧"},
    {"input":"你可是真牛逼呢，给我乐的"},

]

for input_dict in input_list:
    print(input_dict.get("input"))
    res = chain.stream(input_dict)
    for chunk in res:
        print(chunk, end="", flush=True)
    print()


"""
    {"input":"这家店的服务特别贴心，体验超出预期", "output":"积极"},
    {"input":"虽然有点累，但看到孩子笑得那么开心，觉得一切都值得", "output":"积极"},
    {"input":"排队等了两小时，结果还告诉我预约取消了", "output":"消极"},
    {"input":"他说话阴阳怪气，让人很不舒服", "output":"消极"},
    {"input":"这电影太无聊了，我中途差点睡着", "output":"消极"},
    {"input":"还行吧", "output":"中性"},
    {"input":"也就那样", "output":"中性"},
    {"input":"今天阴天，气温和昨天差不多", "output":"中性"},"""