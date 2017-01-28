from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from finder.models import Matches, Site


def index(request):
    return render(request, 'finder/index.html', {})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if 'http' in q:
            match = Matches.objects.filter(matching__website=q)
            site = Site.objects.filter(matches__in=match)
            site_without_dublicates = list(set(site))
            return render_to_response('finder/search_result.html',
                                      {'matches': site_without_dublicates, 'query': q})
        elif q[0] != '#':
            match = Matches.objects.filter(matching__website__icontains=q)
            site = Site.objects.filter(matches__in=match)
            site_without_dublicates = list(set(site))
            return render_to_response('finder/search_result.html',
                                    {'matches': site_without_dublicates, 'query': q})
        else:
            match = Matches.objects.filter(tags__word__iexact=q)
            site = Site.objects.filter(matches__in=match)
            site_without_dublicates = list(set(site))
            return render_to_response('finder/search_result.html',
                                      {'matches': site_without_dublicates, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def matches(request):
    context_dict = {}
    matches = Matches.objects.all()
    context_dict['matches'] = matches
    return render(request, 'finder/list_matches.html', context=context_dict)
