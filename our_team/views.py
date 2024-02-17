from django.shortcuts import render
from our_team.models import Our_team, Author

def our_team(request):
    our_team = Our_team.objects.all()
    author = Author.objects.all()
    return render(request, 'team.html', {'our_team': our_team, 'author': author})
