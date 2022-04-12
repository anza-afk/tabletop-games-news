from flask import Flask, jsonify, render_template, request
from flask_restful import Api, Resource, reqparse
from models import News
from database import Session, migrate

from crud import get_news
from parser import result_news


def create_app(create_db=True):
    app = Flask(__name__)
    
    if create_db:
        migrate()
    return app

app = create_app()
api = Api(app)

class NewsList(Resource):
    def get(self):
        """
        return JSON text of all objects
        """
        with Session() as session:
            news = session.query(News).all()
        return {'News':list(x.json() for x in news)}


api.add_resource(NewsList,'/news/')

app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=5001)