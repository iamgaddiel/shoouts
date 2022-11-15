import json

from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout, login, authenticate
from django.db import IntegrityError
from django.conf import settings

from core.models import User

from .forms import (
    SignupForm
)


def register(request):
    req = json.loads(request.body.decode('utf-8'))
    password1 = req.get('password1')
    password2 = req.get('password2')

    # only display content only in debug mode
    if settings.DEBUG:
        print(req)

    if password1 != password2:
        return JsonResponse({'error': 'passwords do not match '})

    try:
        data = {
            'first_name': req.get('first_name'),
            'last_name': req.get('last_name'),
            'email': req.get('email'),
            'phone': req.get('phone'),
            'country': req.get('country'),
            'password1': req.get('password1'),
            'password2': req.get('password2'),
            'account_category': req.get('account_category'),
            'zipcode': req.get('zipcode'),
        }
        if not (form := SignupForm(data)).is_valid():
            print(form.errors)
            return JsonResponse({"errors": dict(form.errors.items())}, status=400)

        form.save()

    except IntegrityError as e:
        print(e)
        return JsonResponse({"error": "There is an issue creating user"})

    return JsonResponse({"data": "user created successfully"}, status=201)


def login_view(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        email = req.get('email')
        password = req.get('password')

        if (user := authenticate(request, email=email, password=password)) is None:
            if settings.DEBUG: print('USER NOT FOUND')
            return JsonResponse({'error': "login invalid"})

        print(user, '<---------')
        login(request, user)
    return redirect('core:user_dashboard')
