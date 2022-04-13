from app import create_app
from celery import Celery
from celery.schedules import crontab
from database import Session, migrate
from parser import save_news
import requests

celery_app = Celery('parser_run_task', broker='redis://redis:6379/0')
flask_app = create_app()


@celery_app.task
def bgeek_news():
    with flask_app.app_context():
        migrate()
        with requests.Session() as requests_session:
            with Session() as db_session:
                save_news(db_session ,requests_session)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), bgeek_news.s())