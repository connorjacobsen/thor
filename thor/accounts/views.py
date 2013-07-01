from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from accounts.forms import UserCreationForm

@csrf_protect
def login(request):
    c = { }
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)

@csrf_protect
def auth_view(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')    
    user = auth.authenticate(email=email, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/succinctly/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

@csrf_protect
def loggedin(request):
    return render_to_response('accounts/loggedin.html', {'email': request.user.email})

def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('accounts/logged_out.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    args = {}
    args.update(csrf(request)) # csrf token

    args['form'] = UserCreationForm() # blank UserCreationForm

    return render_to_response('accounts/register.html', args)

def register_success(request):
    return render_to_response('accounts/register_success.html')