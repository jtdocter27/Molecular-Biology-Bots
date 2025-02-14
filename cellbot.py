import google.generativeai as genai
import os

#export GOOGLE_API_KEY='AIzaSyA6R_vXh8_a8f62CWyKW6OWDbF2uekfCg8'


class Cellbot: 
    def __init__(self): #consructor, sets the initial state of the object (In this case, cellbot) by defining certain attributes. Method == class function
        self.chat_history = []
        self.api_key = os.getenv('GOOGLE_API_KEY')
        
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
        if 'ryan' in user_input.lower():
            return "we need we need we need we need we need we need we need a new place. Also minus 8,000 points"
        if user_input.lower().startswith(''):
            return 'Welcome to Cell-O-Rama! I\'m Cellbot'
        if 'cresten' in user_input.lower():
            return 'Hello supreme overlord Cresten. How may I assist you today?'
       
        
    def generate_response(self, user_input):
        self.add('user', user_input)
    
        rule_filtered_response = self.rules(user_input)

        if rule_filtered_response:
            self.add('Cellbot', rule_filtered_response)
            return rule_filtered_response

        try: 
            response = self.model.generate_content(user_input)
            self.add('Cellbot', response)

            return response.text
        except:
            print('Beep Boop Bop, Error Occured')
            print('John is the best')


#Calling the Class___________________________________________________________________________
bot = Cellbot()

#Conversation___________________________________________________________________________________________________________________
print("Welcome to Cell-O-Rama!")
gamertag = input('Please Enter Your Gametag: ')


while True:
    user_input = input(gamertag + ':' + ' ', )
    response = bot.generate_response(user_input)
    print('Cellbot: ', response)

    if user_input.lower() in ['exit', 'quit', 'blorp', 'bye']: 
        print('Goodbye')
        break


