from django.urls import path
from . import views

urlpatterns = [
    path('api/create_client', views.create_client_view, name='create_client'),
    path('api/create_meet', views.create_meet_view, name='create_meet'),
    path('api/create_note', views.create_note_view, name='create_note'),

    path('clients/', views.list_clients_view, name='list_clients'),
    path('meets/', views.list_meets_view, name='list_meets'),
    path('notes/', views.list_notes_view, name='list_notes'),

    path('meets/upcoming/', views.upcoming_meets_widget_view, name='upcoming_meets'),
    path('', views.dashboard_view, name='dashboard'),
]
