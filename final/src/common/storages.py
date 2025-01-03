from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage, S3StaticStorage


class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = "media"


class StaticStorage(S3StaticStorage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = "static"
