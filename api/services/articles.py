from api import db
from api.models.articles import Article
from api.models.documents import Document
from api.models.libraries import Library
from api.models.users import User


def get_article(article_id=None, to_dict=True):
    if article_id is not None:
        article = db.session.query(Article).get(article_id)
        if article is None:
            return None
        return article.to_dict() if to_dict else article
    return [item.to_dict() if to_dict else item for item in db.session.query(Article).all()]


def create_article(name, article_type, content, user_id, library_id, document_id):
    user = db.session.query(User).get(user_id)
    if user is None:
        raise KeyError(f"Создатель статьи должен существовать")
    library = db.session.query(Library).get(library_id)
    if library is None:
        raise KeyError(f"Библиотека должна существовать")
    document: Document = db.session.query(Document).get(document_id)
    if document is None:
        raise KeyError(f"Документ должен существовать")
    if document.author.id != user.id:
        raise KeyError(f"Вы не автор статьи")
    article = Article()
    article.author = user
    article.library = library
    article.name = name
    article.article_type = article_type
    article.content = content
    document.articles.append(article)

    db.session.add(article)
    db.session.commit()
    return article
