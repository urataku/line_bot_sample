import os
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

def lambda_handler(event, context):
    body = json.loads(event["body"])
    action_events = body['events']
    line_bot_api = LineBotApi(os.environ['ACCESS_TOKEN'])
    for data in action_events:
        if data['type'] != 'message':
            continue
        if data['message']['type'] != 'text':
            continue

        text_message = TextSendMessage(data['message']['text'])
        line_bot_api.reply_message(data['replyToken'], text_message)

    return {"statusCode" : 200}