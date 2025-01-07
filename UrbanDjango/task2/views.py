from django.shortcuts import render
from django.views.generic import TemplateView

class TemplatesClass(TemplateView):
    template_name = "second_task/class_template.html"

def index(request):
    return render(request, "second_task/func_template.html")

# Create your views here.
