from django.urls import path
from . import views
urlpatterns = [
    path('',views.main, name='main'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('create_user/',views.CreateUser.as_view(), name="create_user"),
    path("view_user/",views.ViewStaff.as_view(),name='view_user'),
    path("delete_user/", views.delete_user.as_view(), name='delete_user'),
]