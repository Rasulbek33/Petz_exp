from django.shortcuts import render
from our_services.models import Our_Service, About_petz





def our_service(request):
    our_service = Our_Service.objects.all()
    about_petz = About_petz.objects.all()
    return render(request, 'services.html', {'our_service': our_service, 'about_petz': about_petz})
