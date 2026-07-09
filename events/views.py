import calendar
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Event
from .forms import EventForm


def event_calendar(request):
    today = date.today()
    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))

    # 月の範囲外対応（前月・翌月への移動）
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    cal = calendar.Calendar(firstweekday=6)  # 日曜始まり
    month_days = cal.monthdatescalendar(year, month)

    events_in_month = Event.objects.filter(
        start_datetime__year=year, start_datetime__month=month
    )

    events_by_day = {}
    for event in events_in_month:
        day = event.start_datetime.date()
        events_by_day.setdefault(day, []).append(event)

    weeks = []
    for week in month_days:
        week_data = []
        for day in week:
            week_data.append({
                "date": day,
                "in_month": day.month == month,
                "events": events_by_day.get(day, []),
                "is_today": day == today,
            })
        weeks.append(week_data)

    prev_month = month - 1
    prev_year = year
    if prev_month < 1:
        prev_month = 12
        prev_year -= 1

    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1

    context = {
        "weeks": weeks,
        "year": year,
        "month": month,
        "prev_year": prev_year,
        "prev_month": prev_month,
        "next_year": next_year,
        "next_month": next_month,
    }
    return render(request, "events/calendar.html", context)


def event_list(request):
    events = Event.objects.all()
    return render(request, "events/list.html", {"events": events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "events/detail.html", {"event": event})


@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect("events:detail", pk=event.pk)
    else:
        form = EventForm()
    return render(request, "events/create.html", {"form": form})
