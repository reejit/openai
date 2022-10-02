import requests
import os
import json
import openai
def write(query):
 openai.api_key = os.environ.get("KEY")

 response = openai.Completion.create(
  model="text-davinci-002",
  prompt=query,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
 )
 #print(response.replace("\n", "<br>"))
 
 r = json.loads(str(response))
 
 x = r['choices'][0]['text']
 x.replace
 print(x)
 return x


