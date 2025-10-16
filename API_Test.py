from openai import OpenAI
from os import getenv
import json
import requests


response=requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={

        "Authorization":f"Bearer <API_KEY>",
        "Content-Type":"application/json",
    },


    json = {
         "model":"openai/gpt-4o",
        

        "messages":[
            {
                "role":"user",
                "content":"Who invented penicillin?",
            },
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "creator",
                "strict": True, 
                "schema": {
                    "type": "object",
                    "properties": {
                        "First Name":{
                            "type":"string",
                            "description": "Name of the founder"
                        },
                        "Last Name":{
                            "type":"string",
                            "description":"Last name of the founder"
                        },
                        "Birthday":{
                            "type":"string",
                            "description":"Birthdate of the founder"
                        },
                    },
                    "required":["First Name", "Last Name", "Birthday"],
                    "additionalProperties":False
                },
            },
        },
    }
)

answer = response.json()['choices'][0]['message']['content']

print(answer)
