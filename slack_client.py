from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_BOT_TOKEN, SLACK_CHANNEL_ID

#Initializing the Stack Client with Bot Tokens
client = WebClient(token=SLACK_BOT_TOKEN)

#Function to post a message to Slack Client
def post_message_to_slack(message):
    try:
        response = client.chat_postMessage(channel=SLACK_CHANNEL_ID, text=message)
    except SlackApiError as e:
        print(f"Error posting to Slack: {e.response['error']}")

#Function to post question-answer pairs to slack
def post_results_to_slack(results):
    message = "Here are the answers to your questions:\n"
    for question, answer in results.items():
        message += f"*{question}*\n{answer}\n\n"
    post_message_to_slack(message)
