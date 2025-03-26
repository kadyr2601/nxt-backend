from django.urls import path
from .views import FlatHomePageView, CreateFeedbackView

urlpatterns = [
    path('homepage', FlatHomePageView.as_view()),
    path('feedback', CreateFeedbackView.as_view()),
]
