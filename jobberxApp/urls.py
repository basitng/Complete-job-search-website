from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name='home'),
    path('login/', loginPage, name='login'),
    path('signup/', signupPage, name='signup'),
    path('jobs/', jobPage, name='job'),
    path('saved-jobs/', savedJobsPage, name='saved-jobs'),
    path('forgot-password/', forgotPasswordPage, name='forget-passsword'),
    path('profile/', profilePage, name='profile'),
    path('logout/', logoutFunc, name='logout'),
    path('<pk>/', singlePage, name='singlePage'),
]

