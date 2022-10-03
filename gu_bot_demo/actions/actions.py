# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

import rasa.core.tracker_store
from rasa.shared.core.trackers import DialogueStateTracker
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation=tracker.events
        print(conversation)
        import os
        if not os.path.isfile('chats.txt'):
            with open('chats.txt','w') as file:
                file.write("This is a file that keeps track and records a whole conversation.\n")
        chat_data=''
        for i in conversation:
            if i['event'] == 'user':
                chat_data+='\nIntent: '+i['parse_data']['intent']['name']+' '+'\nUserText: '+i['text']+'\n'
                print('user: {}'.format(i['text']))
                if len(i['parse_data']['entities']) > 0:
                    chat_data+=i['parse_data']['entities'][0]['entity']+','+i['parse_data']['entities'][0]['value']+','+'\n'
                    print('extra data:', i['parse_data']['entities'][0]['entity'], '=',
                          i['parse_data']['entities'][0]['value'])
            elif i['event'] == 'bot':
                print('Bot: {}'.format(i['text']))
        else:
            with open('chats.txt','a') as file:
                file.write(chat_data)
    
        dispatcher.utter_message(text="The Chat message was saved for the developers to review and improve upon the chatbot.")

        return []