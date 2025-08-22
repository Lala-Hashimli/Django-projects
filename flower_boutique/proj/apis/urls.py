from django.urls import path
from .views import FlowersAPIViews, FlowersDetailsAPIViews


urlpatterns = [
    path("flowers/", FlowersAPIViews.as_view(), name="flowers"),
    path("flowers/<int:flower_id>/", FlowersDetailsAPIViews.as_view(), name="flower_details")
]