from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionHandleSymptoms(Action):
    def name(self):
        return "action_handle_symptoms"

    async def run(self, dispatcher, tracker, domain):
        animal = tracker.get_slot("animal_type")
        symptom = tracker.get_slot("symptom")
        response = f"I see your {animal} is experiencing {symptom}. Please consult a vet for accurate advice."
        dispatcher.utter_message(text=response)
        return []

class ActionProvideRecipeIngredients(Action):
    def name(self):
        return "action_provide_recipe_ingredients"

    async def run(self, dispatcher, tracker, domain):
        animal = tracker.get_slot("animal_type")
        ingredient = tracker.get_slot("ingredient")
        response = f"For a {animal} recipe, you could use safe ingredients like {ingredient or 'chicken, carrots'}. Want a specific recipe?"
        dispatcher.utter_message(text=response)
        return []