from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from people.models import Person
from people.forms import PersonForm
from django.contrib.auth.decorators import user_passes_test

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'phone','job_title', 'bio')
    success_url = reverse_lazy('person_list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'people/person_update_form.html'
    success_url = reverse_lazy('person_list')


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'



