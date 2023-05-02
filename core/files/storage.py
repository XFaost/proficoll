import uuid

from django.core.files.storage import FileSystemStorage


class UUIDFileSystemStorage(FileSystemStorage):

    def get_valid_name(self, name):
        ext = name.split('.')[-1]
        name = f'{uuid.uuid4()}.{ext}'
        return super().get_valid_name(name)
