from django.views import View
from django.http import HttpResponse

class Lesson4View(View):
    def get(self, request):
        return HttpResponse("Домашка по 4 занятию")