from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/overview/', views.about_overview, name='about-overview'),
    path('about/history/', views.about_history, name='about-history'),
    path('about/vismiss/', views.about_vismiss, name='about-vismiss'),
    path('about/dean/', views.about_dean, name='about-dean'),
    path('programs/', views.programs, name='programs'),
    path('admission/', views.admission, name='admission'),
    path('faqs/', views.faqs, name='faqs'),

    path('programs/programsenvi/',views.programsenvi, name='programsenvi'),
    path('programs/programsenvi/enviepm/', views.enviepm, name='enviepm'),
    path('programs/programsenvi/envier/', views.envier, name='envier'),
    path('programs/programsenvi/enviphd/', views.enviphd, name='enviphd'),

    path('programs/programssds/',views.programssds, name='programssds'),
    path('programs/programssds/msds/', views.msds, name='msds'),
    path('programs/programssds/mssds/', views.mssds, name='mssds'),
    path('programs/programssds/dsdsw/',views.dsdsw, name='dsdsw'),
    path('programs/programssds/dsdswo/', views.dsdswo, name='dsdswo'),
    path('programs/programssds/phdsdsw/', views.phdsdsw, name='phdsdsw'),
    path('programs/programssds/phdsdswo/', views.phdsdswo, name='phdsdswo'),

    path('programs/programsds/', views.programsds, name='programsds'),    
    path("programs/programsds/mds", views.mds, name='mds'),

    path('students/', views.students, name='students'),

    path('facultyhome/', views.facultyhome, name='facultyhome'),
    path('facultyhome/faculty', views.faculty, name='faculty'),
    path('facultyhome/staff', views.staff, name='staff'),
    path('facultyhome/affiliates', views.affil, name='affil'),

    path('research/', views.research, name="research"),
    path('research/agendas/', views.agendas, name='agendas'),

    path('resources/', views.resources, name="resources"),
]
