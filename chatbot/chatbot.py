import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

class Chatbot:
    def __init__(self, api_key, model_name):
        # Configure l'API Gemini
        genai.configure(api_key=api_key)
        
        # Initialise le modèle de langage
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.7,
            google_api_key=api_key,
            convert_system_message_to_human=True
        )
        
        # Configure la mémoire de conversation
        self.memory = ConversationBufferMemory()
        
        # Crée la chaîne de conversation
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=True
        )

    def get_response(self, user_message):
        try:
            # Obtient la réponse du modèle
            response = self.conversation.predict(input=user_message)
            return response
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse: {str(e)}")
            return "Désolé, une erreur s'est produite. Veuillez réessayer."
