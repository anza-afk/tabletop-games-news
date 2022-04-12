from flask import Flask
from flask_restful import Api, Resource
from models import News
from database import Session, migrate


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
            news = session.query(News).order_by(News.published.asc()).limit(10)
        return {'News':list(x.json() for x in news)}


api.add_resource(NewsList,'/news/')

app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=5001)
