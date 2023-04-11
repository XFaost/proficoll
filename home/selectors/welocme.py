from home.models import WelcomeBlockSettings


def get_welcome_block():
    return WelcomeBlockSettings.load()
