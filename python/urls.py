from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('lesson_4/', TemplateView.as_view(template_name='lesson_4.html'), name='lesson_4'),
]