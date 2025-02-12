import google.generativeai as genai
import os

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
    
    def generate_response(self, user_input):
        self.add('user', user_input)
    
        try: 
            response = self.model.generate_content(user_input)
            self.add('Cellbot', response)

            return response.text
        except:
            print('Beep Boop Bop, Error Occured')
            print('John is the best')

#some change
#Calling the Class___________________________________________________________________________
bot = Cellbot()

ok = bot.generate_response('hi')
output = bot.history()
print(output)
