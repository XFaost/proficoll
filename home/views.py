from django.shortcuts import render

from home.selectors.contacts import get_contacts
from home.selectors.documents import all_documents
from home.selectors.partners import all_partners


def home_view(request):
    if request.method != 'GET':
        return

    data = {
        'partners': all_partners(),
        'documents': all_documents(),
        'contacts': get_contacts()
    }

    return render(request, 'home/view.html', data)
