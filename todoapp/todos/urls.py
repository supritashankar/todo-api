from django.conf.urls import url
from rest_framework import routers
from django.conf.urls import include
from . import views
from todos.views import TodoView, TodoDetailView
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^todos', TodoView.as_view()),
    url(r'^(?P<todo_id>[0-9]+)/$', TodoDetailView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
