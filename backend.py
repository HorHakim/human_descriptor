import base64
import requests
import os
import io
from mistralai import Mistral

from dotenv import load_dotenv
load_dotenv()



def format_image_into_base64(image):
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")  # ou "PNG"
    img_bytes = buffer.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")
    return img_base64




def describe_human(image):
    base64_image = format_image_into_base64(image)

    model = "pixtral-12b-2409"
    api_key = os.environ["MISTRAL_KEY"]
    client = Mistral(api_key=api_key)


    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Est ce que tu peux décrire cette image d'humain en lui faisant des compliments ?"
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}" 
                }
            ]
        }
    ]

    # Get the chat response
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )


    return chat_response.choices[0].message.content









