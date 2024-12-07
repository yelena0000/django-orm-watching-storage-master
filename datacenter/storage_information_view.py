from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from .models import get_duration, format_duration


def storage_information_view(request):

    not_leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for person in not_leaved:
        entered_at = localtime(person.entered_at)
        duration = format_duration(get_duration(person))

        non_closed_visits.append({
            'who_entered': str(person.passcard),
            'entered_at': str(entered_at),
            'duration': duration
        })

    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
