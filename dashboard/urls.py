from django.contrib import admin
from django.urls import path,include
from dashboard.views import home,dashboard,get_data,ChartData,updateIssue,PieData


#Navigation URls
urlpatterns = [
    path('',home, name='Home'),
    path('dashboard',dashboard.as_view(),name='dashboard'),
    path('visualdata',get_data,name ='api-data'),
    path('visualchartdata',ChartData.as_view()),
    path('piechartdata',PieData.as_view()),
    path('update/<str:pk>/',updateIssue.as_view(),name = 'update')
   
]