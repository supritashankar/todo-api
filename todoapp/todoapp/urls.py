from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'todoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^todos/', include('todos.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
