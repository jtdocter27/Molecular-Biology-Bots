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
            self.traits = ['Modified Lipid Layer Confers +1 Temperature Resistance', 'Cell Wall Defense Upgrade +2, -1C and 1e to use', 'Sporulate! Use all Carbon and all Energy to sit a turn out', 'Histone Coiling creates resistance to DNA damage +3, requires 1 C and 1E to activate', 'Crispr-Cas: Can generate any trait you want but must delete after one use']
            return random.choice(self.traits)
        

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
print("Welcome to Cell-O-Rama!")
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

