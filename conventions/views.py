from django.shortcuts import render, get_object_or_404, redirect
from .models import Convention
from django.utils.timezone import now
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def home(request):

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
    comments = con.comments.order_by('-created_at')  # Get related comments
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.con = con
                comment.save()
                return redirect('con_detail', slug=slug)
            else:
                return redirect('login')
    else:
        form = CommentForm()

<<<<<<< HEAD
    context = {
        'con': con,
        'comments': comments,
        'form': form,
    }

    return render(request, 'con_detail.html', context)


def search_view(request):
    query = request.GET.get('q')  
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    min_value = request.GET.get('min_value')
    max_value = request.GET.get('max_value')


    results = Convention.objects.all()
    
    if query:
        results = results.filter(name__icontains=query)
    if start_date:
        results = results.filter(con_date__gte=start_date)
    if end_date:
        results = results.filter(con_date__lte=end_date)

=======

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
>>>>>>> 507e6d1d914bf551225fb5b42d206ae28d950235

    context = {
        'results': results,
        'query': query,
    }
<<<<<<< HEAD
    return render(request, 'search.html', context)


@login_required
def toggle_favorite(request, con_id):
    if request.method == "POST":
        con = get_object_or_404(Convention, id=con_id)
        user = request.user

        favorited = False

        if con in user.favorite_cons.all():
            con.favorited_by.remove(user)
        else:
            con.favorited_by.add(user)
            favorited = True

        return JsonResponse({"favorited": favorited})
    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def my_favorites(request):
    favorites = request.user.favorite_cons.all()
    return render(request, 'my_favorites.html', {'favorites': favorites})
=======
    return render(request, 'search.html', context)
>>>>>>> 507e6d1d914bf551225fb5b42d206ae28d950235
