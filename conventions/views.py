from django.shortcuts import render, get_object_or_404
from .models import Convention
from django.utils.timezone import now

def home(request):
    cons = Convention.objects.all()  # Retrieve all artist records

    #Current date 
    today = now().date()

    # Filter 1: Conventions Upcoming by closest Date
    upcoming_cons = Convention.objects.filter(con_date__gte=today).order_by('con_date')

    # Filter 2: Upcoming GENERAL conventions only
    upcoming_gen_cons = Convention.objects.filter(con_date__gte=today, con_type="G").order_by('con_date')

    # Filter 3: Upcoming ANIME Conventions only
    upcoming_ani_cons = Convention.objects.filter(con_date__gte=today, con_type="A").order_by('con_date')

    # Filter 4: Upcoming COMIC Conventions only
    upcoming_com_cons = Convention.objects.filter(con_date__gte=today, con_type="C").order_by('con_date')

    # filter 5: Upcoming HORROR conventions only
    upcoming_hor_cons = Convention.objects.filter(con_date__gte=today, con_type="J").order_by('con_date')

    # Filter 6: all conventions by alphabetical
    alphabet_cons = Convention.objects.all().order_by('name')

    context = {
        'upcoming_cons': upcoming_cons,
        'upcoming_gen_cons': upcoming_gen_cons,
        'upcoming_ani_cons': upcoming_ani_cons,
        'upcoming_com_cons': upcoming_com_cons,
        'upcoming_hor_cons': upcoming_hor_cons,
        'alphabet_cons': alphabet_cons,
    }

    return render(request, 'home.html', context)


def getting_started(request):
    return render(request, 'gettingstarted.html')


def con_detail(request, slug):
    con = get_object_or_404(Convention, slug=slug)
    return render(request, 'con_detail.html', {'con': con})


def search_view(request):
    query = request.GET.get('q')  # Main search term
    date1 = request.GET.get('con_date')
    date2 = request.GET.get('apply_date')

    results = Convention.objects.all()

    # Apply filters if present
    if query:
        results = results.filter(name__icontains=query)
    if date1:
        results = results.filter(date1__gte=date1)
    if date2:
        results = results.filter(date2__lte=date2)

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search.html', context)