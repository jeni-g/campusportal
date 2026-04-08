from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('eventregister/',views.eventregister,name='eventregister'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('my-events/', views.my_events, name='my_events'),
    path('contact/', views.contact, name='contact'),
]