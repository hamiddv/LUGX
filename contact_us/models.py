from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_("name"), max_length=128)
    surname = models.CharField(_("summary"), max_length=128)
    subject = models.CharField(_("subject"), max_length=128)
    email = models.EmailField(_("email"))
    message = models.TextField("message")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("contact us message")
        verbose_name_plural = _("contact us messages")
