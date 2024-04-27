import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://api.awanllm.com/v1/chat/completions"
AWANLLM_API_KEY = os.getenv("AWANLLM_API_KEY")


def model(messages):
    """
    Given a list of messages in the chatbot format returns the last reply of the assistant
    :param messages: list of dictionaries containing messages with roles system, user and assistant
    :return: string containing the last reply of the assistant
    """
    payload = json.dumps({
        "model": "Meta-Llama-3-8B-Instruct",
        "messages": messages
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {AWANLLM_API_KEY}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    content = json.loads(response.content)

    return content['choices'][0]['message']['content']
