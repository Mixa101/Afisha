from django.urls import path
from .views import RegisterView, login_view, ConfirmUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', login_view),
    path('confirm/', ConfirmUserView.as_view()),
]
