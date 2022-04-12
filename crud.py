from models import News

def save_news(session, title, author, published, content, image):
    new_news = News(
        title=title,
        author=author,
        published=published,
        content=content,
        image=image
    )
    if bool(session.query(News).filter(News.title == title).first()):
        print(f'News {title} already exists!')
        return True
    session.add(new_news)
    session.commit()


def get_news(session, news_list):
    """
    Выполнять по расписанию - 
    парсер новостей и запись их в дб
    """
    for news in news_list:
        save_news(session, *news.values())
    