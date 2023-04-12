# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ConversationPaused, ConversationResumed
from rasa_sdk.forms import FormAction
import logging
from rasa_sdk.events import ReminderScheduled


class ActionUserMessage(Action):

    def name(self) -> Text:
        return "form_get_details"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill."""
         
        return ["name", "number", "empid", "skill"]

    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],):

        # Do something dramatically here, like call an API for example lol

        return []



#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
