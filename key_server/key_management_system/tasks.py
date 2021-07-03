from django.utils import timezone

from config import celery_app

from .models import Key


@celery_app.task()
def delete_expired_keys():
    """Deletes the keys which have expired"""
    today = timezone.now()
    Key.objects.filter(expire_date__lte=today).delete()
