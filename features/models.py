from django.db import models
from django.utils.translation import gettext_lazy as _


class Feature(models.Model):
    name = models.CharField(_("name"), max_length=50)
    logo = models.ImageField(upload_to="media/features/%y/%m/%d", verbose_name=_("logo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("feature")
        verbose_name_plural = _("features")
