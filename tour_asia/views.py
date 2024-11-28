from django.shortcuts import render
from .models import tour_asia
# Create your views here.
def index(request):
    tour_asia = tour_asia.objects.all()
    context={
        'tour_asia':tour_asia
    }
    return render(request, 'tour_asia/index.html', context)