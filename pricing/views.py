from django.shortcuts import render
from pricing.models import Our_plans, Pricing

def pricing(request):
    our_plans = Our_plans.objects.all()
    pricing = Pricing.objects.all()
    return render(request, 'pricing.html', {'our_plans': our_plans, 'pricing': pricing})
