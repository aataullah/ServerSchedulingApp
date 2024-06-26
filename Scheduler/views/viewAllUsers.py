from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

import Scheduler
from Scheduler.models import Employee, User


class AllUsers(View):
    def get(self, request):
        allUsers = User.objects.all()
        form = AuthenticationForm
        message = request.session.get("message")
        request.session.delete("message")
        if message == None:
            message = ""
        return render(request, 'Scheduler/allUser.html', {'userList': allUsers, 'message': message})
