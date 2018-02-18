import json
import os
from watson_developer_cloud import ConversationV1

#########################
# message
#########################

userin = '';
ip_addr = '';
watson_input = ''
nmap_out = open("nmap_out.txt","r")
conversation = ConversationV1(
    username = 'ed62bc7e-3c21-4a8a-8cd9-aefa4f9bc049',
    password = 'HsXuM4Ifqchf',
    version = '2017-04-21')

workspace_id = '88d55040-992c-49e6-b90d-5d271202c9e6'
if os.getenv("conversation_workspace_id") is not None:
    workspace_id = os.getenv("conversation_workspace_id")

response1 = conversation.message(workspace_id=workspace_id, input={})
print(json.dumps(response1['output']['text'][0], indent=2))

ip_addr = input("Enter an IP address: ")
watson_input = watson_input + ip_addr #watson_input.write(ip_addr)

while userin is not 'q':
    userin = input("type response or q to quit: ")
    if userin == "I entered the IP":
        print (watson_input)
    if userin == "Give me the raw nmap output":
        for line in nmap_out:
            print (line)
    response2 = conversation.message(workspace_id=workspace_id, input={'text': str(userin)})
    print(json.dumps(response2['output']['text'][0], indent=2))
    
nmap_out.close()
