from home.models import AboutUsBlockSettings


def get_about_us_block():
    return AboutUsBlockSettings.load()
