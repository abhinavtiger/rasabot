
import json
import time
import datetime
from typing import Text, Dict, List, Any, Optional
from matplotlib.pyplot import text
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk import events
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import (  # noqa: 401
    EventType,
    SlotSet,
    AllSlotsReset,
    FollowupAction
)

class ActionUserMessage(Action):
    def name(self) -> Text:
        return "action_ask_greet"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Hey! How are you?",
                                 buttons=[
                                     {"title": "Great", "payload": "/mood_great"},
                                     {"title": "Sad", "payload": "/mood_unhappy"}
                                 ])                     
        return []

class ActionUserWelcome(Action):
    def name(self) -> Text:
        return "action_welcome"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Welcome To Registeration Portal",
                                 buttons=[
                                     {"title": "Register", "payload": "/affirm"},
                                     {"title": "Not Interested", "payload": "/not_interest"}
                                 ])
        return []



class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_get_details"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if len(slot_value) <= 1:
            dispatcher.utter_message(text="That's very short name.")
            return {"name": None}
        else:
            return {"name": slot_value}
class AskName(Action):
    def name(self) -> Text:
        return "action_ask_name"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[EventType]:
        
        msg = "Hello! Could you please provide your name?"
        dispatcher.utter_message(text=msg)
        return []

class AskNumber(Action):
    def name(self) -> Text:
        return "action_ask_number"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[EventType]:
        
        msg = "Could you please provide your contact number?"
        dispatcher.utter_message(text=msg)
        return []

class AskReason(Action):
    def name(self) -> Text:
        return "action_ask_reason"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[EventType]:
        
        msg = "Could you please provide the reason for joining this institution?"
        dispatcher.utter_message(text=msg)
        return []

class SubmitRegistrationName(Action):
    def name(self) -> Text:
        return "action_submit_registration_form"

    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        Name = tracker.get_slot("name")
        Mobile_number= tracker.get_slot("number")
        Reason= tracker.get_slot("reason")
        text=['Thanks for providing the given details your \nName: {} \nMobile_number: {} \nReason for placement: {}'.format(Name, Mobile_number,Reason)]
        dispatcher.utter_message(text)

        return []


    
# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"

#     def run(
#         self,
#         slot_value: Any,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_details_thanks",
#                                  Name=tracker.get_slot("name"),
#                                  Mobile_number=tracker.get_slot("number"),
#                                  Reason=tracker.get_slot("reason"))

