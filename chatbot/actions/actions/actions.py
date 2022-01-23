# This files contains custom actions which can be used to run
# custom Python code.

import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


    



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        fact_list = ["Did you know that the average North American uses 700 lbs. of paper a year. This equals approximately 465 trees per person, just for paper!", "Did you know that a glass bottle will take 40,000 years to decompose if it’s not recycled.",
             "Did you know that recycling a single aluminium can will save enough electricity to power a TV for three hours.", "Did you know that recycling a single glass bottle will save enough energy to power a light bulb for four hours.",
             "Did you know that that Earth’s surface is 70% water, but many people go without access to fresh water every day.", " Did you know that turning the faucet off when you’re brushing your teeth and taking quicker showers will use less water and leave more for others to use.",
             "Did you know that turning your home’s thermostat down by a single degree can save your family 8% in heating costs.", "Did you know that paper bags are not really better than plastic bags. Approximately 14 million tress are cut down each year for paper bags. Remember to use your cloth bags!",
             "Did you know that around 15% of the carbon released in the environment is due to deforestation and change in the use of land.", "Did you know that the Golden Toad is the first species to go extinct due to climate change.",
             "Did you know that vehicles like cars and trucks contribute to 20% of carbon emissions in the United States.", "Did you know that climate change enhances the spread of pests that causes life-threatening diseases like dengue, malaria, Lyme disease etc.",
             "Did you know that the number of climate change-related incidents has increased fourfold between 1980 and 2010.", "Did you know that 600000 deaths occur worldwide every year due to climate change. 95% of these deaths take place in developing countries.",
             "Did you know that in 2003, around 70,000 deaths occurred in Europe alone due to diseases caused by rising temperatures.", "Did you know that around 27,000 trees are cut down each day just to produce toilet paper", "Did you know that about five million tons of oil produced in the world end up in oceans every year.",
             "Did you know that 78% of marine mammals are at risk of accidental deaths, such as getting caught in fishing nets.", "Did you know that a single cow can release between 200 and 400 pounds of methane gas through burps and farts each year. These levels are 20 times more powerful than carbon dioxide gas.",
             "Did you know that air pollution causes 36,000 deaths in the UK a year.", "Did you know that having plants inside your home helps to reduce air pollutants.", "Did you know that if deforestation continues at current rates, they will be gone in 100 years.", "Did you know that species are dying off 1,000 faster than they did before humans arrived.",
             "Did you know that there are six times as much plastics in the oceans than there is plankton.", "Did you know that noise pollution from ships causes cellular damage to invertebrates.", "Did you know that from 2030-2050, climate change will cause 250,000 deaths a year.",
             "Did you know that every tonne of paper recycled saves 17 trees"]

        decider = random.randint(0,3)
        if decider==1:
            if(len(fact_list)==0):
                fact_list = ["The average North American uses 700 lbs. of paper a year. This equals approximately 465 trees per person, just for paper!", "A glass bottle will take 40,000 years to decompose if it’s not recycled.",
             "Recycling a single aluminium can will save enough electricity to power a TV for three hours.", "Recycling a single glass bottle will save enough energy to power a light bulb for four hours.",
             "The Earth’s surface is 70% water, but many people go without access to fresh water every day.", "Turning the faucet off when you’re brushing your teeth and taking quicker showers will use less water and leave more for others to use.",
             "Turning your home’s thermostat down by a single degree can save your family 8% in heating costs.", "Paper bags are not really better than plastic bags. Approximately 14 million tress are cut down each year for paper bags. Remember to use your cloth bags!",
             "Around 15% of the carbon released in the environment is due to deforestation and change in the use of land.", "The golden Toad is the first species to go extinct due to climate change.",
             "Vehicles like cars and trucks contribute to 20% of carbon emissions in the United States.", " Climate change enhances the spread of pests that causes life-threatening diseases like dengue, malaria, Lyme disease etc.",
             "The number of climate change-related incidents has increased fourfold between 1980 and 2010.", "Above 600000 deaths occur worldwide every year due to climate change. 95% of these deaths take place in developing countries.",
             "In 2003, around 70,000 deaths occurred in Europe alone due to diseases caused by rising temperatures.", "Around 27,000 trees are cut down each day just to produce toilet paper", "About five million tons of oil produced in the world end up in oceans every year.",
             "Seventy-eight percent of marine mammals are at risk of accidental deaths, such as getting caught in fishing nets.", "Interesting facts about the environment show that a single cow can release between 200 and 400 pounds of methane gas through burps and farts each year. These levels are 20 times more powerful than carbon dioxide gas.",
             "Air pollution causes 36,000 deaths in the UK a year.", "Having plants inside your home helps to reduce air pollutants.", "If deforestation continues at current rates, they will be gone in 100 years.", "Species are dying off 1,000 faster than they did before humans arrived.",
             "There is six times as much plastic in the oceans than there is plankton.", "Noise pollution from ships causes cellular damage to invertebrates.", "From 2030-2050, climate change will cause 250,000 deaths a year.",
             "Every tonne of paper recycled saves 17 trees"]

            fact_index = random.randint(0, len(fact_list)-1)
            chosen_phrase = fact_list[fact_index]
            dispatcher.utter_message(text=chosen_phrase)
            fact_list.remove(chosen_phrase)

        


        return []
