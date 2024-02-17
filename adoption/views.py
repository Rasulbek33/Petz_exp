from django.shortcuts import render
from adoption.models import Adoption, Adoption_name
from django.shortcuts import get_object_or_404


def adoption(request):
    adoption = Adoption.objects.all()
    adoption_name = Adoption_name.objects.all()
    return render(request, 'adoption.html', {'adoption': adoption, 'adoption_name': adoption_name})

def detail_page(request, id):
    obj = get_object_or_404(Adoption, pk=id)
    return render(request, 'adopt-single.html', {'obj': obj})