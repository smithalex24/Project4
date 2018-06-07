from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:trip_id>/', views.show, name='show'),
	path('post_url/', views.post_trip, name='post_trip'),
	path('user/<username>/', views.profile, name='profile'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('search/', views.search_view, name='search'),
	path('delete/<trip_id>', views.delete_view, name='delete'),
	path('signup/', views.signup_view, name='signup'),
	
]