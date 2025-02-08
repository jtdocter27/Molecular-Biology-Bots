import google.generativeai as genai
import os

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY') #creates the API KEY from the global environment
genai.configure(api_key=GOOGLE_API_KEY) #opens the bot

model = genai.GenerativeModel('gemini-2.0-flash') #initializes the model 

response = model.generate_content("Set the stage for a dundgeons and dragons game",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 300,
        "top_p": 0.9,
        "top_k": 40,
    },
    safety_settings=[
        {"category": "HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    ]
)

#temperature: Randomness: Higher the number, more creative 
#max_output_tokens: Response Length
#top_p: Another randomness control, number is the probability of words going together - low number would be a random, nonsensical output. 
#top_k: Another randomness control, lower k values make responses more predictable and less creative, higher k means more diverse responses k=1 means most robotic, k = 10 picks form the top 10 most likely word, k = 50+ is much more wild
#safety settings: 

print(response.text)

#Looks like function calling and game state are the two ways to build cell-0-rama. 
    #Will need to sit down with cresten to understand how the flow of the game works and then program it in 