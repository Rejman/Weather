from django.shortcuts import render
from .models import Trial
import datetime

def index(request):
    trials = Trial.objects.all()
    now = datetime.datetime.now().strftime("%d-%m-%Y")
    yearsSet = set()
    for trial in trials:
        yearsSet.add(int(trial.year))
    years = []
    for year in yearsSet:
        years.append(year)
    years.sort()

    return render(request, 'weather/index.html', {'years': years, 'now':now})

def year(request, year):
    trials = Trial.objects.filter(year=year)
    
    months = []
    temperatures = []
    falls = []
    for trial in trials:
        months.append(trial.month)
        temperatures.append(float(trial.temp))
        falls.append(trial.fall)

    context = {
        'months':months,
        'temperatures':temperatures,
        'falls':falls,
        'year':year
        }
        
    return render(request, 'weather/year.html', context)

#def prediction(request):
#    now = datetime.datetime.now().strftime("%m")
#    trials = Trial.objects.all()
#    
#    temperatures = []
#    falls = []
#    for trial in trials:
#        temperatures.append(float(trial.temp))
#        falls.append(trial.fall)

    
    
#    return render(request, 'weather/prediction.html', {'now':now})
    

    
