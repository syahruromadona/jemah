import os
import openai
import config
openai.api_key = os.getenv("OPENAI_API_KEY")

def openAiQuery(query):
    response = openai.Completion.create(
        model="text-babbage-001",
        prompt=query,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    answer = response['choices'][0]['text']
    return answer