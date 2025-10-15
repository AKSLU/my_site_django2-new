from django.shortcuts import render
from .models import Client, Meet, Note
from django.utils.dateparse import parse_date
from datetime import date, timedelta
from django.utils.timezone import now

def create_client_view(request):
    context = {}
    if request.method == "POST":
        try:
            client = Client.objects.create(
                name=request.POST.get("name"),
                surname=request.POST.get("surname"),
                telephone=request.POST.get("telephone"),
                age=request.POST.get("age"),
                pol=request.POST.get("pol"),
            )
            context['success'] = True

            context['form_data'] = {
                'name': request.POST.get("name"),
                'surname': request.POST.get("surname"),
                'telephone': request.POST.get("telephone"),
                'age': request.POST.get("age"),
                'pol': request.POST.get("pol"),
            }
        except Exception as e:
            context['error'] = str(e)
            context['form_data'] = request.POST
    else:
        context['form_data'] = {}

    return render(request, 'create_client.html', context)


def create_meet_view(request):
    context = {}
    if request.method == "POST":
        try:
            date = parse_date(request.POST.get("date"))
            Meet.objects.create(
                title=request.POST.get("title"),
                date=date
            )
            context['success'] = True
            context['form_data'] = {
                'title': request.POST.get("title"),
                'date': request.POST.get("date"),
            }
        except Exception as e:
            context['error'] = str(e)
            context['form_data'] = request.POST
    else:
        context['form_data'] = {}

    return render(request, 'create_meet.html', context)


def create_note_view(request):
    context = {}
    if request.method == "POST":
        try:
            date = parse_date(request.POST.get("date"))
            Note.objects.create(
                name=request.POST.get("name"),
                date=date,
                main_text=request.POST.get("main_text")
            )
            context['success'] = True
            context['form_data'] = {
                'name': request.POST.get("name"),
                'date': request.POST.get("date"),
                'main_text': request.POST.get("main_text"),
            }
        except Exception as e:
            context['error'] = str(e)
            context['form_data'] = request.POST
    else:
        context['form_data'] = {}

    return render(request, 'create_note.html', context)

def upcoming_meets_widget_view(request):
    today = date.today()
    week_later = today + timedelta(days=7)
    month_later = today + timedelta(days=30)

    today_meets = Meet.objects.filter(date=today)
    week_meets = Meet.objects.filter(date__gt=today, date__lte=week_later)
    month_meets = Meet.objects.filter(date__gt=week_later, date__lte=month_later)

    context = {
        'today_meets': today_meets,
        'week_meets': week_meets,
        'month_meets': month_meets,
    }
    return render(request, 'upcoming_meets_widget.html', context)

def dashboard_view(request):
    clients = Client.objects.count()
    meets_today = Meet.objects.filter(date=date.today()).count()
    total_notes = Note.objects.count()

    context = {
        'clients': clients,
        'meets_today': meets_today,
        'total_notes': total_notes,
    }
    return render(request, 'dashboard.html', context)


def list_clients_view(request):
    clients = Client.objects.all()
    return render(request, 'list_clients.html', {'clients': clients})


def list_meets_view(request):
    meets = Meet.objects.all()
    return render(request, 'list_meets.html', {'meets': meets})


def list_notes_view(request):
    notes = Note.objects.all()
    return render(request, 'list_notes.html', {'notes': notes})
