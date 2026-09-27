from langchain.messages import HumanMessage
from config import init_model
import base64


image_path = "./assets/荷兰wh860.jpg"
with open(image_path, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

mime_type = "image/jpeg"

message = HumanMessage(
    content=[
        {"type": "text", "text": "请描述这张图片。"},
        {
            "type": "image_url",
            "image_url": {"url": f"data:{mime_type};base64,{image_data}"}
        }
    ]
)
model = init_model("qwen3.8-max")
response = model.invoke([message])
print(response.content)

