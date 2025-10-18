from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import OfficerRegistrationForm, OfficerAuthenticationForm

# Create your views here.
class RegisterView(View):
    template_name = 'auth/register.html'

    def get(self, request):
        form = OfficerRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OfficerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Реєстрація успішна.")
            return redirect('home')
        return render(request, self.template_name, {'form': form})


class OfficerLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = OfficerAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        # Додаткова перевірка: дозволяємо заходити лише офіцерам
        if not getattr(user, 'is_officer', False):
            messages.error(self.request, "Доступ дозволено тільки працівникам поліції.")
            return redirect('auth:login')
        return super().form_valid(form)


class OfficerLogoutView(LogoutView):
    next_page = reverse_lazy('auth:login')


def index(request):
    return render(request, 'index.html')