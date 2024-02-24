# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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


from typing import Any, Text, Dict, List
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.events import SlotSet
class ActionSaveName(Action):
    def name(self) -> Text:
        return "action_save_name"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = \
	next(tracker.get_latest_entity_values("name"), None)
        dispatcher.utter_message(text=f"Hello, {name}!")
        return []





class ActionCustomGreet(Action):
    def name(self) -> str:
        return "action_custom_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> List[Dict[Text, Any]]:
        greeted = tracker.get_slot("greeted")
        if not greeted:
            message = (
                "Welcome to the COP6481 Branch of the FinTech World Bank\n\n"
                "Your userid has been verified\n\n"
                "What would you like help with today?\n\n"
            )
            dispatcher.utter_message(text=message)
            return [SlotSet("greeted", True)]
        else:
            dispatcher.utter_message(text="Hi there, what can I do for you?")
            return []


class ActionShowAccountInfo(Action):
    def name(self) -> str:
        return "action_show_account_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_account_info")
        return []

