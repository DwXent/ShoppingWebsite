from django.urls import path
from .views.home import  Index
from .views.signup import Signup
from .views.login import Login
from .views.home import ceo
from .views.home import company
from .views.home import help


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login') ,
    path('ceo', ceo),
     path('company', company),
     path('help', help)
]
