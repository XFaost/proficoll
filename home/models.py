from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit

from core.utils.singleton.singleton import SingletonModel


class WelcomeBlockSettings(SingletonModel):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    subtitle = models.TextField(max_length=512, verbose_name='Підзаголовок')

    def __str__(self):
        return 'Налаштування головного блоку'

    class Meta:
        verbose_name = '1. Налаштування головного блоку'


class AboutUsBlockSettings(SingletonModel):
    text = models.TextField(max_length=1024, verbose_name='Підзаголовок')

    def __str__(self):
        return 'Налаштування блоку "Про нас"'

    class Meta:
        verbose_name = '2. Налаштування блоку "Про нас"'


class Partner(models.Model):
    name = models.CharField(max_length=64, verbose_name='Ім\'я')

    image = ProcessedImageField(
        upload_to='partners',
        processors=[ResizeToFit(200, 200)],
        format='PNG',
        options={'quality': 60},
        verbose_name='Зображення')
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(200, 200)],
        format='WEBP',
        options={'quality': 60})

    url = models.URLField(verbose_name='Посилання')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнера'
        verbose_name_plural = '3. Партнери'


class Document(models.Model):
    name = models.CharField(max_length=256, verbose_name='Назва')
    file = models.FileField(upload_to='documents.py', verbose_name='Файл')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = '4. Документи'


class ContactsBlockSettings(SingletonModel):
    legal_address = models.CharField(max_length=64, verbose_name='Юридична адреса')
    contact_center_wh = models.CharField(max_length=64, verbose_name='Графік роботи контактного центру')
    administration_wh = models.CharField(max_length=64, verbose_name='Графік роботи адміністрації')
    phone_numbers = models.TextField(verbose_name='Телефони для звернень')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return 'Налаштування блоку "Контактні дані"'

    class Meta:
        verbose_name = '5. Налаштування блоку "Контактні дані"'
