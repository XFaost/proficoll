from django.db import models
from django.core.cache import cache

CACHE_TIMEOUT = 60 * 5


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_to_cache()

    def delete(self, *args, **kwargs):
        self.clear_cache()
        super(SingletonModel, self).delete(*args, **kwargs)

    @classmethod
    def clear_cache(cls):
        cache.delete(cls.__name__)

    def set_to_cache(self):
        cache.set(self.__class__.__name__, self, CACHE_TIMEOUT)

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_to_cache()
        return cache.get(cls.__name__)
