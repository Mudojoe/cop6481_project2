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
import requests
import httpx


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

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Inform the user that you're fetching the account information
        dispatcher.utter_message(text="Let me pull up that information for you...")

        # Example: Make an asynchronous HTTP request to the JSONPlaceholder API
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/users')
            if response.status_code == 200:
                users = response.json()
                # For simplicity, this example uses the first user's data
                first_user = users[0]
                name = first_user.get("name", "No name found")
                email = first_user.get("email", "No email found")
                # Construct and send the account information message
                message = f"Account Info:\nName: {name}\nEmail: {email}"
            else:
                message = "Failed to retrieve account information."
        except Exception as e:
            message = f"An error occurred: {str(e)}"

        # Send the actual account information or error message
        dispatcher.utter_message(text=message)

        return []





from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import httpx

class ActionShowAccountBalance(Action):
    def name(self) -> str:
        return "action_show_account_balance"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_type = next(tracker.get_latest_entity_values("account_type"), None)
        #print(f"account_type = {account_type}")
        # Use httpx to make an asynchronous GET request
        async with httpx.AsyncClient() as client:
            response = await client.get('https://jsonplaceholder.typicode.com/users/1')
            if response.status_code == 200:
                user_details = response.json()
                # Extract latitude and longitude
                latitude = float(user_details['address']['geo']['lat'])
                longitude = float(user_details['address']['geo']['lng'])
                # Calculate balance based on account type
                if account_type == "checking":
                    balance = abs(latitude) * 100
                    formatted_balance = "{:.2f}".format(balance)
                    dispatcher.utter_message(text=f"Your {account_type} account balance is: ${formatted_balance}.")
                elif account_type == "savings":
                    balance = abs(longitude) * 150
                    formatted_balance = "{:.2f}".format(balance)
                    dispatcher.utter_message(text=f"Your {account_type} account balance is: ${formatted_balance}.")
                else:
                    dispatcher.utter_message(text="Please specify which account you'd like to check: Checking or Savings?")
            else:
                dispatcher.utter_message(text="I'm sorry, I couldn't fetch your account balance at the moment.")

        return []

