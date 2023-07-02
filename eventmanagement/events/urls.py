"""
    Urls for the Events.

    Event Mangement, 2023

    Author: Jay Chovatiya
"""
from django.urls import path
from events.views import AvailableUserList

urlpatterns = [
    path("available-user/", AvailableUserList.as_view(), name="available-user"),
]