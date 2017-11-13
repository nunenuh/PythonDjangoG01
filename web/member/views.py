from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse


class TestView(View):
    def get(self, request):
        return HttpResponse('<h1> Test</h1>')

class TestTplView(View):
    def get(self, request):
        template = 'member/index.html'
        data = {
            'kata':'Ini Text dari View',
            'ar': [1,2,3,4],
            'logika': True
        }
        return render(request, template, data)