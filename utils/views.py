from private_storage.views import PrivateStorageView

from utils.storage import my_storage


class MyStorageView(PrivateStorageView):
    storage = my_storage

    def can_access_file(self, private_file):
        # This overrides PRIVATE_STORAGE_AUTH_FUNCTION
        return True
