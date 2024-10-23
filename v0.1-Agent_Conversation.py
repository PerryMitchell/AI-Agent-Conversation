import time
from datetime import datetime
import requests
import json
import os
import pyttsx3
from text_to_speech import TextToSpeech

# Change the working directory to this script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Environment Variables
openai_api_env_var = os.environ.get('OPENAI_API_KEY')
groq_api_env_var = os.environ.get('GROQ_API_KEY')


class AIAgent:
    def __init__(self, api_to_use="openai", name="Agenty", openai_model="gpt-3.5-turbo", groq_model="llama-3.1-70b-versatile", ollama_model="llama3", openaiapikey=openai_api_env_var, groqapikey=groq_api_env_var):
        self.api_to_use = api_to_use
        self.openai_model = openai_model
        self.groq_model = groq_model
        self.ollama_model = ollama_model
        self.time_to_sleep_in_between_requests = 0
        self.openaiapikey = openaiapikey
        self.groqapikey = groqapikey
        self.responses = []
        self.name = name
        self.model = ""

        # Setup for each API
        if api_to_use == "openai":
            self.time_to_sleep_in_between_requests = 10
            if not openaiapikey:
                raise ValueError("OpenAI API key is required.")
            self.client = self.init_openai_client(openaiapikey)

        elif api_to_use == "groq":
            self.time_to_sleep_in_between_requests = 10
            if not groqapikey:
                raise ValueError("GROQ API key is required.")

    # OpenAI client initialization
    def init_openai_client(self, api_key):
        from openai import OpenAI
        return OpenAI(api_key=api_key)

    # Query OpenAI API
    def query_openai(self, prompt, max_tokens=4096):
        try:
            response = self.client.chat.completions.create(
                model=self.openai_model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    # Query Groq API
    def query_groq(self, prompt, max_tokens=8000):
        groq_api_url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.groqapikey}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.groq_model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens
        }
        try:
            response = requests.post(groq_api_url, headers=headers, json=payload)
            response.raise_for_status()
            json_response = response.json()
            if 'choices' in json_response and len(json_response['choices']) > 0:
                return json_response['choices'][0]['message']['content']
            return "No response generated."
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
        except json.JSONDecodeError:
            return "Error: Failed to parse the API response as JSON."

    # Query Ollama API
    def query_ollama(self, prompt, max_tokens=16000):
        ollama_url = "http://localhost:11434/api/generate"
        payload = {
            "model": self.ollama_model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens
            }
        }
        try:
            response = requests.post(ollama_url, json=payload)
            response.raise_for_status()
            json_response = response.json()
            if 'response' in json_response:
                return json_response['response']
            return "No response generated."
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
        except json.JSONDecodeError:
            return "Error: Failed to parse the API response as JSON."
    
    def return_name_api_model(self):
        self.name_api_model = f"{self.name}_{self.api_to_use}_{self.model}"
        return self.name_api_model

    def return_name(self):
        return self.name
        

    # Helper method to call the correct API based on user's choice
    def return_api_call(self, prompt):
        if self.api_to_use == "openai":
            self.model = self.openai_model # To insert model into filename
            return self.query_openai(prompt)
        elif self.api_to_use == "groq":
            self.model = self.groq_model # To insert model into filename
            return self.query_groq(prompt)
        elif self.api_to_use == "ollama":
            self.model = self.ollama_model # To insert model into filename
            return self.query_ollama(prompt)

    # Agent logic
    def agent(self, instructions, data):
        prompt = f"""{instructions}: {data}"""
        response = self.return_api_call(prompt)
        self.responses.append({"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "response": response})
        print(f"{self.name} spoke.")
        return response
    
    def history(self):
        for i in range(len(self.responses)):
            print(f"Response {i}:")
            print(self.responses[i])
            print(" ")


print("Program started.")

# Choose a topic of conversation here.
topic = "earths crust displacement theory and any supporting scientific evidence." #input("what would you like to generate a conversation about? ")

#Choose a filename - todo: should be dynamic hence the extra filename variable.
filename = topic

# Amount of back and forths to have in the conversation.
convo_length = 2

# Insatantiate agents.
agentOne = AIAgent(name="Shauna")
agentTwo = AIAgent(name="Gretchin")

#String to keep track of conversation.
conversation_as_string = f"""{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Subject Matter: {topic}"""

# Create the conversation.
# Conversation start.
agentTwo.agent(f"Your name is {agentTwo.return_name()}. Keep this conversation flowing", agentOne.agent(f"Your name is {agentOne.return_name()} Start this conversation off", f"I would like to have a conversation about {topic}"))
conversation_as_string = f"""

    {conversation_as_string} 

    {agentOne.responses[0]["response"]} 

    {agentTwo.responses[0]["response"]}
    
    """
#Conversation.
for i in range(convo_length):
    agentOne.agent(f"Your name is {agentOne.return_name()}. Introduce yourself and keep this conversation flowing, be an expert in any field associated with the subject matter" , agentTwo.responses[-1]["response"])
    agentTwo.agent(f"Your name is {agentTwo.return_name()}. Introduce yourself and be less knowledgeable in the subject matter and act as a segway for your conversational partner to speak about the subject in depth. Make sure to ask pertinent questions in order to keep the conversation flowing." , agentOne.responses[-1]["response"])
    conversation_as_string = conversation_as_string + f"""
                
    {agentOne.name}: {agentOne.responses[i]["response"]}

    {agentTwo.name}: {agentTwo.responses[i]["response"]}

    """

#Save the conversation to file
with open(f"conversations/{filename}_{agentOne.return_name_api_model()}_{agentTwo.return_name_api_model()}.txt", 'w') as file:
    for i in range(convo_length):
        file.write(f"""
        {agentOne.responses[i]["timestamp"]} AgentOne: {agentOne.responses[i]["response"]}

        {agentTwo.responses[i]["timestamp"]} AgentTwo: {agentTwo.responses[i]["response"]}

        """)
    print(f"{filename}_{agentOne.return_name_api_model()}_{agentTwo.return_name_api_model()}.txt was saved.")
        


print("CONVERSATION: ")
print(conversation_as_string)
#TTS-------------------------------------------
# Initialize the TTS engine
engine = pyttsx3.init()

# Set the speech rate (optional)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)  # 150 is a reasonable speed

# Set the voice (optional, you can choose between male/female voices)
voices = engine.getProperty('voices')
# Uncomment one of the following lines depending on the voice preference
engine.setProperty('voice', voices[0].id)  # Male voice
# engine.setProperty('voice', voices[1].id)  # Female voice

# Text to speak
text = """"""

# Save the speech to a .wav file - string, filename
engine.save_to_file(conversation_as_string, f"conversations/{filename}_{agentOne.return_name_api_model()}_{agentTwo.return_name_api_model()}.wav")
print(f"{filename}_{agentOne.return_name_api_model()}_{agentTwo.return_name_api_model()}.wav was saved.")

# Command the engine to speak the text
#engine.say(conversation_as_string)

# Run the speech engine
engine.runAndWait()
