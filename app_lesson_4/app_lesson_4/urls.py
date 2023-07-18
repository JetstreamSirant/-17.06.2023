from django.urls import path
from lesson_4.views import Lesson4View

urlpatterns = [
    path('lesson_4/', Lesson4View.as_view(), name='lesson_4'),
]