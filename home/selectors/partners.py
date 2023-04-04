from home.models import Partner


def all_partners():
    return Partner.objects.all()
