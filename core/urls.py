from django.urls import path
from .views import home, example,doughnot,linechart
urlpatterns = [
    path('', home),
    path('example', example),
    path('doughnot', doughnot),
    path('linechart',linechart)
]