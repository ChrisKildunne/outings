from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("home/", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),
    path("events/", views.events_index, name="index"),
    path("events/create/", views.EventCreate.as_view(), name="events_create"),
    path("events/<int:pk>/update/", views.EventUpdate.as_view(), name="events_update"),
    path("events/<int:pk>/delete/", views.EventDelete.as_view(), name="events_delete"),
    path("events/<int:event_id>/", views.events_detail, name="detail"),
    path("events/sport", views.filter_sport, name="filter_sport"),
    path("events/<int:event_id>/add_comment/", views.add_comment, name="add_comment"),
]
