from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import RedirectURLMixin
from .models import Trainee
from .forms import TraineeModelForm


class TraineeListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Trainee
    template_name = 'trainee_list.html'
    context_object_name = 'trainees'
    paginate_by = 10


class TraineeDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Trainee
    template_name = 'trainee_detail.html'
    context_object_name = 'trainee'
    pk_url_kwarg = 'id'


class TraineeCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Trainee
    form_class = TraineeModelForm
    template_name = 'add_trainee_v2.html'
    success_url = reverse_lazy('trainee_list')


class TraineeDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Trainee
    template_name = 'trainee_confirm_delete.html'
    success_url = reverse_lazy('trainee_list')
    context_object_name = 'trainee' 
    pk_url_kwarg = 'id'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('trainee_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(RedirectURLMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('trainee_list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return self.get_redirect_url() or self.success_url
