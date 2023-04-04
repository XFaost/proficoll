from home.models import ContactsBlockSettings


def get_contacts():
    return ContactsBlockSettings.load()
