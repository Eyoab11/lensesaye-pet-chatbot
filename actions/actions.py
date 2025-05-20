import pandas as pd
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionHandleSymptoms(Action):
    def name(self):
        return "action_handle_symptoms"

    async def run(self, dispatcher, tracker, domain):
        animal = tracker.get_slot("animal_type")
        symptom = tracker.get_slot("symptom")

        if not animal or not symptom:
            response = "I need more details about the animal and symptom. Could you clarify?"
            dispatcher.utter_message(text=response)
            return []

        # Load the disease dataset
        try:
            df = pd.read_csv("knowledge_base/animal_diseases.csv")
            # Find matching row (case-insensitive)
            match = df[(df['animal_type'].str.lower() == animal.lower()) & 
                      (df['symptom'].str.lower() == symptom.lower())]
            if not match.empty:
                causes = match.iloc[0]['possible_causes']
                advice = match.iloc[0]['general_advice']
                response = f"{symptom} in your {animal} could be caused by {causes}. {advice}"
            else:
                response = f"I'm not a vet, but {symptom} in your {animal} could have various causes. Please consult a vet for accurate advice."
        except Exception as e:
            response = f"Sorry, I couldn't fetch information about {symptom} for your {animal}. Please consult a vet."

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