from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetCompleteView,
    PasswordResetDoneView
)


from .views import (
    Index
)

app_name = 'core'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    # path('login', LoginView(), new)
]
