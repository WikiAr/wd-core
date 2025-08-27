import aiohttp
import asyncio
import json
from pathlib import Path

env_path = Path(__file__).parent / ".env2"

with open(env_path, "r") as f:
    api_token = f.read().strip()


async def invoke_chute():

    headers = {
        "Authorization": "Bearer " + api_token,
        "Content-Type": "application/json"
    }

    body = {
        "model": "zai-org/GLM-4.5-Air",
        "messages": [
            {
                "role": "user",
                "content": "Tell me a 250 word story."
            }
        ],
        "stream": True,
        "max_tokens": 1024,
        "temperature": 0.7
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
                "https://llm.chutes.ai/v1/chat/completions",
                headers=headers,
                json=body
        ) as response:
            async for line in response.content:
                line = line.decode("utf-8").strip()
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = data.strip()
                        if chunk:
                            print(chunk)
                    except Exception as e:
                        print(f"Error parsing chunk: {e}")


async def invoke_chute2():

    headers = {
        "Authorization": "Bearer " + api_token,
        "Content-Type": "application/json"
    }

    body = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {
                "role": "user",
                "content": "Tell me a 250 word story."
            }
        ],
        "stream": True,
        "max_tokens": 1024,
        "temperature": 0.7
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
                "https://llm.chutes.ai/v1/chat/completions",
                headers=headers,
                json=body
        ) as response:
            async for line in response.content:
                line = line.decode("utf-8").strip()
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = data.strip()
                        if chunk:
                            print(chunk)
                    except Exception as e:
                        print(f"Error parsing chunk: {e}")

asyncio.run(invoke_chute2())
