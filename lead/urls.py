from django.urls import path
from . import views

urlpatterns = [
    path('',views.leading, name=''),
    path('Createtkassign/',views.Createtkassign.as_view(), name="Createtkassign"),
    path('Viewtkassign/',views.Viewtkassign.as_view(),name='Viewtkassign'),
    path('Viewtkassignall/',views.Viewtkassignall.as_view(),name='Viewtkassignall'),
    path("deletetkassign/", views.deletetkassign.as_view(), name='deletetkassign'),
    path("edit_user/", views.edit_user.as_view(), name='edit_user'),
]