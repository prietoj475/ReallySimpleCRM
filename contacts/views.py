from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from .models import Contact
from .form import ContactForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class ContactsListView(generic.ListView):
    context_object_name = 'contact_list'
    template_name = 'contacts/listcontacts.html'

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user).order_by('first_name')
        return queryset

@method_decorator(login_required, name='dispatch')
class ContactsDetailView(generic.DetailView):
    context_object_name = 'contact'
    template_name = 'contacts/detailcontacts.html'

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user).order_by('first_name')
        return queryset

@method_decorator(login_required, name='dispatch')
class ContactsCreateView(generic.CreateView):
    form_class = ContactForm
    template_name = 'contacts/createcontacts.html'
    success_url = reverse_lazy('contacts:listcontacts')

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user).order_by('first_name')
        return queryset

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ContactsUpateView(generic.UpdateView):
    form_class = ContactForm
    template_name = 'contacts/updatecontacts.html'

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user).order_by('first_name')
        return queryset

    def get_success_url(self):
        return reverse_lazy('contacts:detailcontacts', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class ContactsDeleteView(generic.DeleteView):
    template_name = 'contacts/deletecontacts.html'
    success_url = reverse_lazy('contacts:listcontacts')

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user).order_by('first_name')
        return queryset