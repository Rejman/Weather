from django.urls import path

from . import views
app_name="weather"
urlpatterns = [

    # /weather/
    path('', views.index, name='index'),
    # /weather/2011/
    path('<int:year>', views.year, name='year'),
    # /weather/??
    #path('', views.prediction, name="prediction"),



]
