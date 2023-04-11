from django.shortcuts import render

from home.selectors.welocme import get_welcome_block
from home.selectors.about_us import get_about_us_block
from home.selectors.contacts import get_contacts
from home.selectors.documents import all_documents
from home.selectors.partners import all_partners


def home_view(request):
    if request.method != 'GET':
        return

    data = {
        'welcome': get_welcome_block(),
        'about_us': get_about_us_block(),
        'partners': all_partners(),
        'documents': all_documents(),
        'contacts': get_contacts()
    }

    return render(request, 'home/view.html', data)
