from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt

from .models import Contact
from .forms import ContactForm


class ContactUsView(CreateView):
    template_name = "contact-us/index.html"
    form_class = ContactForm
    success_url = '.'
    model = Contact

    # def form_valid(self, form):
    #     print(form)
    #     form.save()
    #
    #     return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context["form"] = ContactForm()
    #
    #     return context

