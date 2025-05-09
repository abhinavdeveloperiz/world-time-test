from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WorldClock
import pytz
import json

def world_clock_view(request):
    return render(request, 'world_clock.html',)

@csrf_exempt
def get_user_time(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_timezone = data.get('timezone', 'UTC')
        world_clock = WorldClock.objects.first()

        if world_clock:
            try:
                target_timezone = pytz.timezone(user_timezone)
                user_time = world_clock.uk_time.astimezone(target_timezone)
                formatted_time = user_time.strftime('%I:%M %p')
                return JsonResponse({'time': formatted_time, 'timezone': user_timezone})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'No UK time set'}, status=404)
