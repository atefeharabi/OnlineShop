from django.shortcuts import render
from django.views import View


class Home(View):
    template_name = 'products/home.html'

    def get(self, request):
        return render(request, self.template_name)