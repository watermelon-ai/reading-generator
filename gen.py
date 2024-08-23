import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.environ["api_token"]

from openai import OpenAI
client = OpenAI(
  api_key=api_token,
  base_url="https://api.deepseek.com/beta",
)

template_file = "reading_generator/prompts/gen_single_paper.txt"
with open(template_file, "r", encoding="utf-8") as f:
    template = f.read()

input_file = "input.txt"
with open(input_file, "r", encoding="utf-8") as f:
    input_content = f.read()

input_content = template.format(query=input_content)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": input_content},
  ],
    max_tokens=1024,
    temperature=0.7,
    stream=False
)

output_content = response.choices[0].message.content

output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(output_content)
