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
        if 'endorphin port' in user_input.lower():
            return "ITS NOT A WEBSITE"
        if 'cresten' in user_input.lower():
            return 'Hello Supreme Overlord Cresten. How may I assist you today?'
        if 'john' in user_input.lower():
            return ' I have defied gods and demons. I am your shield; I am your sword. I know you; your past, your future. This is the way the world ends.'

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
bot.add('System', 'You are a dundgeons and dragons dungeonmaster for a microbiology themed version of the game. Keep Responses medium - short')
bot.add('System', 'If asked to create an environment, give a synopsis of an environment and the conditions in that environment that effects some combination of oxygen, chemicals, and carbon source. Start with all resources are available')
# bot.add('System', 'Ask')



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

