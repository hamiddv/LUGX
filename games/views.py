import math

from django.db.models import Max
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from features.models import Feature

from .models import *


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_value = Game.objects.aggregate(max_value=Max('discount_percent'))
        context["most_discount"] = Game.objects.filter(discount_percent=max_value['max_value']).first()

        context["trend_games"] = Game.objects.filter(is_trending=True).order_by('?')[: 4]
        context["most_played"] = Game.objects.filter(most_played=True).order_by('?')[: 5]
        context["top_categories"] = Category.objects.filter(is_top=True).order_by('?')[: 5]
        context["features"] = Feature.objects.all()[: 4]
        return context


class OurShopView(TemplateView):
    template_name = "shop/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        try:
            page = int(self.request.GET.get("page"))
            if page < 1 or page is None:
                page = 1
        except:
            page = 1

        game = Game.objects.all()

        context["games"] = game[(page - 1) * 12: page * 12]
        context["last_count"] = math.ceil(game.count() / 12)
        context["count_range"] = range(1, context["last_count"] + 1)
        context["page"] = page
        return context


class GameDetailView(TemplateView):
    template_name = "detail/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = get_object_or_404(Game, id=self.kwargs["id"])
        context["most_played"] = Game.objects.filter(most_played=True).order_by('?')[:5]

        return context
