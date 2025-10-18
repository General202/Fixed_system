from django.urls import path
from .views import RegisterView, OfficerLoginView, OfficerLogoutView

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', OfficerLoginView.as_view(), name='login'),
    path('logout/', OfficerLogoutView.as_view(), name='logout'),
]
