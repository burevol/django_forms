from django.urls import path

from .views import CategoryView, QuestionView

urlpatterns = [
    path('', CategoryView.as_view(), name='categories'),
    path('category/<int:pk>', QuestionView.as_view(), name='question')
]