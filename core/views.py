from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, "core/index_page.html")
    