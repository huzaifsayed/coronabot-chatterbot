from chatterbot import ChatBot

chatbot = ChatBot('CoronaBot')

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/quesans.txt').read().splitlines()
training_data_greetings = open('training_data/greetings.txt').read().splitlines()

training_data = training_data_quesans + training_data_greetings

trainer.train(training_data)