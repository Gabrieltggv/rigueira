import os

from django.utils.timezone import now


def get_upload_path(instance, filename):
    return os.path.join(
        'account/avatars/', now().date().strftime('%Y/%m/%d'), filename
    )
