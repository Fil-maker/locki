from api import db
from api.models.documents import Document
from api.models.libraries import Library
from api.models.users import User


def get_document(document_id=None, to_dict=True):
    if document_id is not None:
        document = db.session.query(Document).get(document_id)
        if document is None:
            return None
        return document.to_dict() if to_dict else document
    return [item.to_dict() if to_dict else item for item in db.session.query(Document).all()]


def create_document(name, user_id, authority_level, library_id):
    user: User = db.session.query(User).get(user_id)
    if user is None:
        raise KeyError(f"Создатель статьи должен существовать")
    library = db.session.query(Library).get(library_id)
    if library is None:
        raise KeyError(f"Библиотека должна существовать")
    for child in user.libraries:
        if child.id == library_id and not child.edit_rights:
            raise KeyError(f"У вас нет прав на редактирование")
    document = Document()
    document.name = name
    document.author = user
    document.authority_level = authority_level
    document.library = library

    db.session.add(document)
    db.session.commit()
    return document
