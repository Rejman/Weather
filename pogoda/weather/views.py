from django.shortcuts import render
from .models import Trial
import datetime

def index(request):
    trials = Trial.objects.all()
    now = datetime.datetime.now().strftime("%m")
    
    yearsSet = set()
    for trial in trials:
        yearsSet.add(int(trial.year))
    years = []
    for year in yearsSet:
        years.append(year)
    years.sort()

    trials = Trial.objects.filter(month=int(now))
    months = {
        "01":["Styczeń", 31],
        "02":["Luty", 30],
        "03":["Marzec", 31],
        "04":["Kwiecień", 30],
        "05":["Maj", 31],
        "06":["Czerwiec", 30],
        "07":["Lipiec", 31],
        "08":["Sierpień", 31],
        "09":["Wrzesień", 30],
        "10":["Październik", 31],
        "11":["Listopad", 30],
        "12":["Grudzień",31],
    }
    now = months[now]
    temperatures = []
    falls = []
    for trial in trials:
        temperatures.append(float(trial.temp))
        falls.append(trial.fall)

    temperature = round(sum(temperatures)/len(temperatures),1)
    f = sum(falls)/len(falls)
    fall = round((f/now[1])*100)
    
    context={
        'fall':fall,
        'temperature':temperature,
        'years': years,
        'now':now[0],
        'temperatures':temperatures,
        'falls':falls
        }

    return render(request, 'weather/index.html', context)

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


    

    
