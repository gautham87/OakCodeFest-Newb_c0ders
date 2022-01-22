# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# This variable contains the all the facts the chatbot will use
Fact_list = ["The average North American uses 700 lbs. of paper a year. This equals approximately 465 trees per person, just for paper!", "A glass bottle will take 40,000 years to decompose if it’s not recycled.",
             "Recycling a single aluminium can will save enough electricity to power a TV for three hours.", "Recycling a single glass bottle will save enough energy to power a light bulb for four hours.",
             "The Earth’s surface is 70% water, but many people go without access to fresh water every day.",
             "Turning your home’s thermostat down by a single degree can save your family 8% in heating costs.", "Paper bags are not really better than plastic bags. Approximately 14 million tress are cut down each year for paper bags. Remember to use your cloth bags!",
             "Around 15% of the carbon released in the environment is due to deforestation and change in the use of land.", "The golden Toad is the first species to go extinct due to climate change.",
             "Vehicles like cars and trucks contribute to 20% of carbon emissions in the United States.", " Climate change enhances the spread of pests that causes life-threatening diseases like dengue, malaria, Lyme disease etc.",
             "The number of climate change-related incidents has increased fourfold between 1980 and 2010.", "Above 600000 deaths occur worldwide every year due to climate change. 95% of these deaths take place in developing countries.",
             "In 2003, around 70,000 deaths occurred in Europe alone due to diseases caused by rising temperatures.", "Around 27,000 trees are cut down each day just to produce toilet paper", "About five million tons of oil produced in the world end up in oceans every year.",
             "Seventy-eight percent of marine mammals are at risk of accidental deaths, such as getting caught in fishing nets.", "Interesting facts about the environment show that a single cow can release between 200 and 400 pounds of methane gas through burps and farts each year. These levels are 20 times more powerful than carbon dioxide gas.",
             "Air pollution causes 36,000 deaths in the UK a year.", "Having plants inside your home helps to reduce air pollutants.", "If deforestation continues at current rates, they will be gone in 100 years.", "Species are dying off 1,000 faster than they did before humans arrived.",
             "There is six times as much plastic in the oceans than there is plankton.", "Noise pollution from ships causes cellular damage to invertebrates.", "From 2030-2050, climate change will cause 250,000 deaths a year.",
             "Every tonne of paper recycled saves 17 trees"]
#
class ActionHelloWorld(Action):
#
     def name(self) -> Text:
        return "action_hello_world"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         dispatcher.utter_message(text="Hello World!")
#
         return []
