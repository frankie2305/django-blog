from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', extra_context={ 'title': 'Log in', 'alert': 'Please log in to access this page.', 'legend': 'Log in', 'submit': 'Log in', 'choice': 'Sign up' }), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', extra_context={ 'title': 'Log out', 'choice': 'Log in again' }), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html', success_url = reverse_lazy('users:password_change_done'), extra_context={ 'title': 'Change password', 'legend': 'Change password', 'submit': 'Change' }), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html', extra_context={ 'title': 'Password change done', 'choice': 'Go back to homepage' }), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', success_url = reverse_lazy('users:password_reset_done'), extra_context={ 'title': 'Reset password', 'legend': 'Reset password', 'submit': 'Request' }), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html', extra_context={ 'title': 'Password reset done', 'choice': 'Go back to homepage' }), name='password_reset_done'),
]
