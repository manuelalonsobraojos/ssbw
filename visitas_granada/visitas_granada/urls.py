from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visit/<int:visit_id>', views.getVisit, name='getVisit'),
    path('add_visit', views.addVisit, name='addVisit'),
    path('new_visit', views.newVisitView, name='newVisitView'),
    path('edit_visit_form/<int:visit_id>', views.editVisitView, name='editVisitView'),
    path('edit_visit/<int:visit_id>', views.editVisit, name='editVisit'),
    path('delete_visit/<int:visit_id>', views.deleteVisit, name='deleteVisit'),
]