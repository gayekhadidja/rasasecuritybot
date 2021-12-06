# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import ConversationPaused, SlotSet
import re
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.forms import FormValidationAction
import logging



from rasa_sdk import Action, Tracker


class ValidationIdentifantform(FormValidationAction) :
    def name(self):
        return "Validation_identifiant"

    def validation_identiant (
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validations de l'identifiants DAS"""
        print ("identifiant donnee = {slot_value}  length = {len(slot_value)}")

        if len(slot_value) < 8 :
            if len (re.search("[A-Za-z]" , slot_value)) == 1 :
                dispatcher.utter_message(text= 'veiller fournir un identifiant correct')
            return {"identifiant " : None }

        else :

            return {"identifiant " : slot_value}






class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def fetch_slots(tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and phone number."""

        slots = []
        for key in ("nom", "identifiants"):
            value = tracker.get_slot(key)
            if value is not None:
                slots.append(SlotSet(key=key, value=value))
        return slots

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(tracker))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events


class ActiondemandeEmail(Action) :
    def name(self) -> Text:
        return "action_demande_email"

    def run(self ,
        dispatcher : CollectingDispatcher ,
        tracker : Tracker ,
        domain : Dict[Text , Any],
        )-> List[Dict] :
        tracker.get_slot("email") 
        dispatcher.utter_message(template= f"utter_demande_email")


class validate_email ()




















































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
