from django.conf.urls import url
from rest_framework import routers
from django.conf.urls import include
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todos', views.TodoViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
