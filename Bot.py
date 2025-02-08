#APi Key: AIzaSyA6R_vXh8_a8f62CWyKW6OWDbF2uekfCg8

import google.generativeai as genai
import gradio as gr 
import os



GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY') #creates the API KEY
genai.configure(api_key=GOOGLE_API_KEY) #opens the bot
model = genai.GenerativeModel('gemini-2.0-flash') #initializes the model 


def mansbot(message, history): 
    if 'my elbow hurts' in message.lower():
        return 'tell me about your mom'
    elif 'my girlfriend broke up with me' in message.lower():
        return 'tell me about your mom'
    
    elif 'why am I paying you $200/hour' in message.lower():
        return 'tell me about your mom'

    response = model.generate_content(message)
    return response.text

gr.ChatInterface(fn=mansbot, title='therapy bot', description = '', type = 'messages').launch()

