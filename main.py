# using flask_restful
from flask import Flask, jsonify
from flask_restful import Resource, Api
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Fluffy',
)
trainer = ListTrainer(bot)
trainer.train(
    [
        'Hello',
        'Hi there!',
        'How are you doing?',
        'I am doing great.',
        'That is good to hear',
        'Thank you',
        'You are welcome.',
    ]
)

app = Flask(__name__)
api = Api(app)
class Square(Resource):
    def get(self, input):
        return jsonify({'result': str(bot.get_response(input))})

api.add_resource(Square, '/bot/<string:input>')
if __name__ == '__main__':
    app.run(debug = True)