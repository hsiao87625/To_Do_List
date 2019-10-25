from django.shortcuts import render
from . import models

# 建立一個任務的列表
def home(request):
    return render(request, 'base.html')

def new_mission(request):
    mission = request.POST.get('mission')
    print(mission)
    models.Mission.objects.create(mission=mission)

    mission_list = {
        'mission':mission,
        }
    return render(request, 'polls/new_mission.html', mission_list)