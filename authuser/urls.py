from django.urls import path
from . import views
 
urlpatterns = [
    path('',views.main, name='main'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('create_user/',views.CreateUser.as_view(), name="create_user"),
    path('view_user/',views.ViewStaff.as_view(),name='view_user'),
    path("delete_user/", views.delete_user.as_view(), name='delete_user'),
    path("edit_user/", views.edit_user.as_view(), name='edit_user'),
    path("login_check/", views.login_check.as_view(), name='login_check'),
]