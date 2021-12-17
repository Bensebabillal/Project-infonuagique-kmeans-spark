import os

from private_storage.storage.files import PrivateFileSystemStorage

from backend.settings.dev import BASE_DIR

my_storage = PrivateFileSystemStorage(
    location=os.path.join(BASE_DIR, 'media/video/private-media/'),
    base_url='/private-documents/'
)
