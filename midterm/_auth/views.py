from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def register(request):
	form = UserCreationForm(data=request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/rmenu')
	return render(request, '_auth/register.html', {'form': form})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = username, password = password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('/rmenu')
		else:
			error = "incorrect username/password"
			return render(request, '_auth/login.html', {'error': error})
	else:
		return render(request, '_auth/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/rmenu')
