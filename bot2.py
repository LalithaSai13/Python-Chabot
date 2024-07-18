from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("Marcella")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train ("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations" )
  
response = chatbot.get_response('What is your Number')
print(response)
 
response = chatbot.get_response('Who are you?')
print(response)
trainer = ListTrainer(chatbot)

trainer.train(["Hi", "Welcome, friend 🤗"])
trainer.train(["What is chatbot used for?","A chatbot is used for automated conversation and assistance."])
trainer.train(["tell me another joke","Why don't scientists trust atoms? Because they make up everything!"])
exit_conditions = (":q", "quit", "exit","bye") 
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"Marcella: {chatbot.get_response(query)}")


