from django.urls import path
from . import views

urlpatterns = [
    path('lead1',views.leading, name='lead1'),
    path('Createtkassign/',views.Createtkassign.as_view(), name="Createtkassign"),
    path('Viewtkassign',views.Viewtkassign.as_view(),name='Viewtkassign'),
    path("deletetkassign", views.deletetkassign.as_view(), name='deletetkassign'),
    # path("edit_user/", views.edit_user.as_view(), name='edit_user'),
]