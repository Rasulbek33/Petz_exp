from django.shortcuts import render
from django.views.generic import ListView
from our_services.models import Our_Service, About_petz

class Our_serviceView(ListView):
    queryset = Our_Service.objects.order_by('-id')
    paginate_by = 5

    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        data['titles'] =  About_petz.objects.all()
        return data