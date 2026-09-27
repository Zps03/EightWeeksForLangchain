from config import init_model
import asyncio
model = init_model("qwen-plus")

# 1. 单次
print("单次")
response = model.invoke("你好")
print(response.content)
# 2. 批量（并行）
print("\n批量（并行）")
responses = model.batch(["你好", "再见", "谢谢"])
for r in responses:
    print(r.content)

# 3. 流式
print("\n流式")
for chunk in model.stream("讲一个短故事"):
    print(chunk.content, end="", flush=True)

# 4. 异步
print("\n异步")
async def main():
    res = await model.ainvoke("你好")
    print(res.content)
asyncio.run(main())

