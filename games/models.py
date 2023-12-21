from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("name"), max_length=128)
    image = models.ImageField(upload_to="media/categories/%y/%m/%d/", verbose_name=_("image"))
    caption = models.TextField(_("caption"), max_length=1024, null=True, blank=True)
    is_top = models.BooleanField(_("is top"), default=True)
    created_date = models.DateTimeField(_("created date"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Game(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name=_("category"))
    name = models.CharField(_("name"), max_length=128)
    caption = models.TextField(_("caption"), max_length=1024)
    description = models.TextField(_("descriptions"), max_length=5024)
    price = models.PositiveIntegerField(_("price"))
    discount_percent = models.PositiveIntegerField(_("discount percent"), null=True, blank=True)
    most_played_image = models.ImageField(
        upload_to="media/games/most_played_image/%y/%m/%d/", verbose_name=_("most played image"),
        help_text="this is for dont resizing the image in site if this game is most played",
        null=True, blank=True
    )
    most_discounted_image = models.ImageField(
        upload_to="media/games/most_discount_image/%y/%m/%d/", verbose_name=_("most discounted image"),
        help_text="this is for dont resizing the image in site if this game is most discounted",
        null=True, blank=True
    )
    detail_image = models.ImageField(
        upload_to="media/games/detail_image/%y/%m/%d/", verbose_name=_("most discounted image"),
        help_text="this is for dont resizing the image in product detail"
    )
    image = models.ImageField(upload_to="media/games/image/%y/%m/%d/")
    game_id = models.CharField(_("game id"), max_length=10)
    is_active = models.BooleanField(_("is active"), default=True)
    most_played = models.BooleanField(_("most played"))
    is_trending = models.BooleanField(_("is trending"))
    created_date = models.DateTimeField(_("created date"), auto_now=True)

    @property
    def discounted_price(self):
        return self.price - (self.price * self.discount_percent / 100)

    @property
    def genres(self):
        return GameGenre.objects.all().filter(game=self)

    @property
    def tags(self):
        return GameTag.objects.all().filter(game=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("game")
        verbose_name_plural = _("game")


class Genre(models.Model):
    name = models.CharField(_("name"), max_length=128)
    created_date = models.DateTimeField(_("created date"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("genre")
        verbose_name_plural = _("genres")


class GameGenre(models.Model):
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE,)
    created_date = models.DateTimeField(_("created date"), auto_now=True)

    class Meta:
        unique_together = [
            ['game', 'genre']
        ]


class Tag(models.Model):
    name = models.CharField(_("name"), max_length=128)
    created_date = models.DateTimeField(_("created date"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class GameTag(models.Model):
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE, )
    created_date = models.DateTimeField(_("created date"), auto_now=True)

    class Meta:
        unique_together = [
            ['game', 'tag']
        ]
