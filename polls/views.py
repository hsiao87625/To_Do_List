from django.shortcuts import render
from . import models

# 建立一個任務的列表
def home(request):
    missions = models.Mission.objects.all()
    return render(request, 'polls/new_mission.html', {'missions':missions})

def new_mission(request):
    mission = request.POST.get('mission')
    models.Mission.objects.create(mission=mission)
    missions = models.Mission.objects.all()
    mission_list = {
        'missions':missions,
        }
    return render(request, 'polls/new_mission.html', mission_list)

def delete_mission(request, mission):
    models.Mission.objects.get(mission=mission).delete()
    missions = models.Mission.objects.all()
    return render(request, 'polls/new_mission.html', {'missions':missions})