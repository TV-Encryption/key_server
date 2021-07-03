from django.db import models
from django.utils.translation import pgettext_lazy

# Create your models here.


class Key(models.Model):
    key_ref = models.UUIDField(primary_key=True)
    key = models.CharField(max_length=512)
    init_vector = models.CharField(max_length=512)
    expire_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.key_ref)

    class Meta:
        verbose_name = pgettext_lazy("model name", "key")
        verbose_name_plural = pgettext_lazy("model name", "keys")
