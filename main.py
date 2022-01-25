# using flask_restful
from flask import Flask, jsonify
from flask_restful import Resource, Api
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    'Fluffy',
)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "chatterbot.corpus.english"
)

app = Flask(__name__)
api = Api(app)

class Fluffy(Resource):
    def get(self, input):
        return jsonify({'result': str(bot.get_response(input))})

api.add_resource(Fluffy, '/<string:input>')
if __name__ == '__main__':
    app.run(debug = True)