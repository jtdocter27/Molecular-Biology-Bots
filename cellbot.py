import google.generativeai as genai
import os
import random

#export GOOGLE_API_KEY='AIzaSyA6R_vXh8_a8f62CWyKW6OWDbF2uekfCg8'


class Cellbot: 
    def __init__(self): #consructor, sets the initial state of the object (In this case, cellbot) by defining certain attributes. Method == class function
        self.chat_history = []
        self.api_key = 'AIzaSyA6R_vXh8_a8f62CWyKW6OWDbF2uekfCg8'
        # os.getenv('GOOGLE_API_KEY')
        
        if self.api_key:
            genai.configure(api_key=self.api_key)  # Configure API key
            self.model = genai.GenerativeModel('gemini-2.0-flash')

        else:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        
    def history(self):
        return self.chat_history
    
    def add(self, role, message):
        self.chat_history.append({'role': role, 'message': message})

    def rules(self, user_input): #These are hardcoded rules within the chatbot. 
        if 'cresten' in user_input.lower():
            return 'Supreme Overlord Cresten decrees a doubling of cells! Hazaah!'
        if 'john' in user_input.lower():
            return 'Do not ask questions about my creator. Half your cells are destroyed'
        if 'tardigrade' in user_input.lower():
            return 'Eureka! You found a tardigrade! x10 cells'
        if 'crying' in user_input.lower():
            return 'There\'s no crying in baseball'
        if 'tricerotops' in user_input.lower():
            return 'It\'s not a buffalo! +1 carbon courtesy of the SEEC cafe' 
        if '  ' in user_input.lower():
            return 'Youve unlocked the mirror forms of all your macromolecules - and half of your cells must fight half of your cells. Ask Cresten. Good luck'
        if 'troy and abed in the morning' in user_input.lower():
            return 'one of your cells has become aware it is a simulated entity in a game...'

        if any(word in user_input.lower() for word in ['master', 'evolve all']):
            self.traits = ['Histone Coiling creates resistance to DNA damage +3, requires 1 C and 1E to activate', 'Crispr-Cas: Can generate any trait you want but must delete after one use', 'Cell Wall, all defense rolls +2, requires 1 C and 1 E'
                           , 'Modified lipid layer, temp resistance (user selects), all temp resistance rolls +1', 'Centromeres - resistance to DNA damage +3, requires 1C and 1E to activate', 'Improved cofactors, e+1, no cost to protein specialists, all else 2C', 
                            'Surface Modification Site Modification - resistance to viral attack +3, requires 1e to use', 'Supercoiling - no cost to nucleic acid specialist, all else +2e to activate, defense to damage +4', 'Slime layer - no cost for carbohydrate specialist, defense +3, 1e and 2C to use for all else', 
                              'Larger storage granules - no cost for carbohydrate specialists - double any stored C or N', 'Outcompete for C - >d15 roll by every other organism to see if they have access to the identical carbon source that turn, 2e to activate', 
                               'Genome expansion +1 trait', 'Gas Vacuoles - photosynthesis receives a +3 on the roll for energy generation, 2C to use', 'DNA methylation - resistance to viral attack +7, requires 1C to use', 'Deplete N - >d15 roll from all other organisms to see if they have access to N for growth, 2e to activate', 
                                'Transposon site mutation - Gain a bonus trait with each viral attack', 'Nutrient exchange - Shuttle Cs for es or es for Cs (no mixing per turn) with another organism, requires 1e to activate', 'Evolved transporters - +3C, requires 1e to use', 
                                'Cellulose Synthesis - if carbohydrate specialist, this occurs at no cost, all other +2C and +2e, resistance to all damage +5, excess 1e and 1C storage automatic', 'Lipid sacs - if lipid specialist, this occurs at no cost, all other +2C and +2e, resistance to toxic damage +7, resistance to membrane damages +10, excess 3e and 1C storage automatic', 
                                 'Novel energy source, only applicable to organos, e+3','Double rRNA encoded on genome, express +1 trait', 'Create toxin - if carbohydrate specialist, this occurs at no cost, all other +3C and +1e, all competing organisms roll under "poisoned" condition, all non-metabolic rolls -5', 
                                   'New pigments - only applicable to phototrophs, e+7, required 2C to use', 'Improved ftsZ, if growth requirement >1, then growth e and C -1 (minimum of 1 still required)', 'DnaJ - All resistance to nucleic acid damage rolls +7, requires 1C and 1e to use', 
                                      'GroEL - All resistance to damage rolls +7, requires 1 C and 1 e to use', 'Super Oxide Dismutase - All O2 resistance rolls +7, requires 1 C and 1 e to use', 'Wood-Linjedhal Pathway - Novel Carbon Source Pathway - Resistant to Carbon Limitation - requires 3e to use', 'Evolved NADH-Ubiquone Oxidoreductase - Respiration chain e+1', 'Evolved ATPase - Respiration chain e+1', 
                                         'Plasmid - hold and express one trait at no cost', 'Conjugation - copy a trait from any other cell, requires 3e and 3C to activate', 'Flagella - protein action, flea the environment, roll to see if the stress even effects (>d15, avoids), requires 3e to activate', 'Predation - bonus carbon source and energy source, all other players must roll a >d15 to avoid predation, roll 2 d6s to determine number of cells consumed, if also expressing flagella, roll 10 d6s, requires 5e', 
                                            'Transformation - at the end of the turn, add any trait that has been evolved over time, 3e to activate', 'Double strand DNA breaks (DNA pol IV) - immune to salt, uv, and radiation stress, 4e to activate', 'Sporulate - Use all Carbon and all Energy to sit a turn out - adds +15 to all environment rolls', 
                                              'Endosymbiosis - resistance to all environment stresses +10, C generation -2, e generation -1, lose three traits, irreversible']
            return '\n\n'.join(random.choices(self.traits, k=13))
        

        if any(word in user_input.lower() for word in ['roll', 'rolls', 'die', 'dye', 'dice']):
            self.roll1 = random.randint(1, 20)
            self.roll2 = random.randint(1,20)
            print('If you roll higher than a', self.roll2, 'you may proceed')
            print('your roll is', self.roll1)
            if self.roll1 >= self.roll2:
                return 'Hazah! You May Proceed!'
            if self.roll1 <= self.roll2:
                return 'Womp. You may not proceed'



    def generate_response(self, user_input):
        self.add('user', user_input)

        rule_filtered_response = self.rules(user_input)


        context = " ".join(f"{entry['role']}: {entry['message']}" for entry in self.chat_history[-10:])  # 'f' specifies an f-string, which allows embedding variables inside a string using {}
        
        full_prompt = f"{context}\nUser: {user_input}\nCellbot:"

        if rule_filtered_response:
            self.add('Cellbot', rule_filtered_response)
            return rule_filtered_response
        
        try:
            response = self.model.generate_content(full_prompt)
            response_text = response.text if hasattr(response, 'text') else response.candidates[0].content # checks if gemini's response has a 'text' attribute and, otherwise creates an alternative response
            
            self.add('Cellbot', response_text)
            return response_text
        
        except Exception as e:
            print(f'Boop bop beep Error Occurred: {e}')
            return None


#Calling the Class and Defining the System Parameter___________________________________________________________________________
bot = Cellbot()
bot.add('System', 'You are a dundgeons and dragons dungeonmaster for a microbiology themed version of the game. Keep Responses medium-short')
bot.add('System', 'If asked to create an environment or begin, give a synopsis of an environment and the conditions in that environment that effects some combination of oxygen, macromolecules, and carbon source. Start with all resources are available')
bot.add('System', 'Set a challenge score between 10 and 20 for most relevant variable out of this list: organic carbon, oxygen concentration, light availability, general stress')
bot.add('System', 'Do not ask questions of the user')



#Conversation___________________________________________________________________________________________________________________
print("Welcome to Cell-O-Rama! \n")
gamertag = input('Please Enter Your Username: ')

while True:
    user_input = input(gamertag + ':' + ' ', )
    if any(word in user_input.lower() for word in ['exit', 'quit', 'blorp', 'bye']):
        print('Sounds good!  See ya!')
        break

    else:
        response = bot.generate_response(user_input)
        print('CellBot: ', response)


# print(bot.history())

