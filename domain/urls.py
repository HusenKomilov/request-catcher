from django.urls import path
from domain import views

urlpatterns = [
    path("", views.RequestsCatcherView.as_view()),
    path("<path:path>", views.RequestsCatcherView.as_view())
]
