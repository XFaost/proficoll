from home.models import Document


def all_documents():
    return Document.objects.all()

