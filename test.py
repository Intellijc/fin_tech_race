import os
from openai import OpenAI

# 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
# 初始化Openai客户端，从环境变量中读取您的API Key
client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://xh.v1api.cc/v1",
    # 从环境变量中获取您的 API Key
    api_key="sk-EgYyrdANt4O1Lis4L8G7KBR1a31qQAswl4E07REPDuaOd23S",
)

model ="chatgpt-4o-latest"

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model=model,
    messages=[
        {"role": "system", "content": "你是人工智能助手"},
        {"role": "user", "content": "你好"},
    ],
)
print(completion.choices[0].message.content)

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model=model,
    messages=[
        {"role": "system", "content": "你是人工智能助手"},
        {"role": "user", "content": "你好"},
    ],
    # 响应内容是否流式返回
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="")
print()