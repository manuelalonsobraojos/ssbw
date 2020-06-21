from django.urls import path, include
from rest_framework import routers
from . import views

router_visit = routers.DefaultRouter()
router_visit.register(r'visitas', views.VisitaViewSet)

router_visit_like = routers.DefaultRouter()
router_visit_like.register(r'visitas/likes', views.VisitaLikesViewSet)

router_comment = routers.DefaultRouter()
router_comment.register(r'comentarios', views.ComentarioViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('visit/<int:visit_id>', views.getVisit, name='getVisit'),
    path('add_visit', views.addVisit, name='addVisit'),
    path('new_visit', views.newVisitView, name='newVisitView'),
    path('edit_visit_form/<int:visit_id>', views.editVisitView, name='editVisitView'),
    path('edit_visit/<int:visit_id>', views.editVisit, name='editVisit'),
    path('delete_visit/<int:visit_id>', views.deleteVisit, name='deleteVisit'),
    path('increment_likes', views.incrementLikes, name='incrementLikes'),
    path('decrement_likes', views.decrementLikes, name='decrementLikes'),
    path('register_comment', views.registerComment, name='registerComment'),
    path('api/', include(router_visit.urls)),
    path('api/', include(router_visit_like.urls)),
    path('api/', include(router_comment.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]