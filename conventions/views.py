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

