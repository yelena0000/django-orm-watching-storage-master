from django.utils.timezone import localtime


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime()
    duration = leaved_at - entered_at
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours} ч {minutes} мин"


def is_visit_long(visit, minutes=60):
    duration_min = get_duration(visit).total_seconds()/60
    return duration_min > minutes
