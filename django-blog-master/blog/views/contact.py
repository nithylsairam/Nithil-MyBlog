from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
class ContactView(CreateView):
    
    fields = ['body']
    template_name = 'blog/contact.html'
    login_url = reverse_lazy('contact')