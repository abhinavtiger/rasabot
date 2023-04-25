# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet, ConversationPaused, ConversationResumed, EventType
# from rasa_sdk.forms import FormAction
# import logging
# from rasa_sdk.events import ReminderScheduled


# class ActionUserMessage(Action):

#     def name(self) -> Text:
#         return "form_get_details"

#     def run(
#         self,slot_value: Any,dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
#     ) -> Dict[Text, Any]:

#      return []
        # required_slots = ["name", "number", "reason"]


        # # All slots are filled.
        # for i in required_slots:
        #      return [SlotSet("requested_slot")]

    # def name(self) -> Text:
    #     return "form_get_details"

    # @staticmethod
    # def required_slots(tracker: Tracker) -> List[Text]:
    #     """A list of required slots that the form has to fill."""
         
    #     return ["name", "number", "reason"]

    # def submit(self,dispatcher, tracker: Tracker, domain: Dict[Text, Any],):
    #     # dispatcher.utter_message(template="utter_details_thanks",
    #     #                          Name=tracker.get_slot("name"),
    #     #                          Mobile_number=tracker.get_slot("number"),
    #     #                          Reason=tracker.get_slot("reason"))

        

    #     return []
    
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
