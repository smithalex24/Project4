from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Trip
from .forms import TripForm, LoginForm, SignupForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def index(request):
	return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            user = User.objects.create_user(username = u, email = e, password = p)
            print('created new user', user)
            user.save()
            print("saved new user:", user)
            user = authenticate(username = u, email = e, password = p)
            print("authenticated new user:", user)
            login(request,user)
            new_url = '/user/' + request.user.username
            return HttpResponseRedirect(new_url)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			new_url = '/user/' + u
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(new_url)
				else:
					print('The account has been disabled.')
			else: print('The username and/or password is incorrect.')
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


def profile(request, username):
	user = User.objects.get(username=username)
	trips = Trip.objects.filter(user=user)
	form = TripForm()
	return render(request, 'profile.html', {'username': username, 'trips': trips, 'form': form})

def search_view(request):
	return render(request, 'search.html')


def show(request, trip_id):
	trip = Trip.objects.get(id=trip_id)
	return render(request, 'show.html', {'trip': trip}) 

def post_trip(request):
	form = TripForm(request.POST)
	if form.is_valid():
		trip = form.save(commit = False)
		trip.user = request.user
		trip.save()
	new_url = '/user/' + request.user.username
	return HttpResponseRedirect(new_url)

def delete_view(request, trip_id):
	if request.user.is_authenticated and request.method == "POST":
		trip = Trip.objects.get(id=trip_id)
		print("this is the trip to delete", trip)
		trip.delete()
		print("these are now the user's trips", Trip.objects)
		new_url = '/user/' + request.user.username
		return HttpResponseRedirect(new_url)

