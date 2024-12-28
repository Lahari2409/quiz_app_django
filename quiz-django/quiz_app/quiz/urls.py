from django.urls import path
from quiz import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing Page
    path('quiz/', views.quiz_page, name='quiz'),  # Quiz Page
    path('result_page/', views.result_page, name='result_page'),  
    path('results/', views.results, name='results'),# Result Page
]
