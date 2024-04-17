import json
import requests
import openai
import os

api_key = os.environ['API_KEY']
openai.api_key = api_key

# Obtain message from openai api with query
def openai_test(question):
        prompt = question
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question},
            ],
        )
        return response['choices'][0]['message']['content'].strip()


def handler(event, context):
    # Parse the incoming event from LINE
    line_event = json.loads(event['body'])
    
    # Extract the message text from the LINE event
    message_text = line_event['events'][0]['message']['text']
    
    # Fetch reply from openai api by using message as query
    answer = openai_test(message_text)

    # Prepare the reply message
    reply_message = {
        'replyToken': line_event['events'][0]['replyToken'],
        'messages': [
            {
                'type': 'text',
                'text': answer
            }
        ]
    }
    
    # Send the reply message back to LINE
    line_reply_url = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer k2ozAZcy5l8FsA+tGyV/pRCqdIKwej9CAQ3psVRT+N5FRDnSWS4vvXn2pK3A8/pAqoIM2YvU2IZOvsiJKWPJIMaCapA32X4UEQN7ub0LhydShPjqmjS0BxFqTjuaKecDFfATtDeQjGETc+PSANkO0gdB04t89/1O/w1cDnyilFU='
    }
    response = requests.post(line_reply_url, headers=headers, data=json.dumps(reply_message))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message echoed successfully!')
    }