from __future__ import print_function
import json
import os
from watson_developer_cloud import ConversationV1

#########################
# message
#########################

conversation = ConversationV1(
    username = 'ed62bc7e-3c21-4a8a-8cd9-aefa4f9bc049',
    password = 'HsXuM4Ifqchf',
    version='2017-04-21')

# replace with your own workspace_id
workspace_id = '88d55040-992c-49e6-b90d-5d271202c9e6'
if os.getenv("conversation_workspace_id") is not None:
    workspace_id = os.getenv("conversation_workspace_id")

response1 = conversation.message(workspace_id=workspace_id, input={})
print(json.dumps(response1, indent=2))

response2 = conversation.message(workspace_id=workspace_id, input={'text': 'What is the IP address?'})
print(json.dumps(response2, indent=2))






