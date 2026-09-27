import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

def init_model(model_name: str = "qwen3.7-plus", temperature: float = 0.7):
    """初始化百炼模型（OpenAI 兼容模式）"""
    return init_chat_model(
        model_name,
        model_provider="openai",
        base_url=DASHSCOPE_BASE_URL,
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        temperature=temperature,
    )


