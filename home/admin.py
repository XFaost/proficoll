from django.contrib import admin
from django.utils.html import format_html

from core.utils.singleton.singleton_model_admin import SingletonModelAdmin
from home.models import WelcomeBlockSettings, AboutUsBlockSettings, Partner, ContactsBlockSettings


@admin.register(WelcomeBlockSettings)
class WelcomeBlockSettingsAdmin(SingletonModelAdmin):
    pass


@admin.register(AboutUsBlockSettings)
class AboutUsBlockSettingsAdmin(SingletonModelAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'image_view',)

    def image_view(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width:150px;"/>')

    image_view.__name__ = 'Зображення'
    image_view.allow_tags = True


@admin.register(ContactsBlockSettings)
class ContactsBlockSettingsAdmin(SingletonModelAdmin):
    pass
