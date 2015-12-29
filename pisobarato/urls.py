from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from pisobarato import views
from .views import HomePageView, GetPisos, GetImagenesPiso, HighCharts, GetUsuario

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pisobarato.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^pisos.json', GetPisos.as_view(), name='pisos'),
    url(r'^piso(?P<piso>[a-zA-Z0-9-]+).json/$', GetImagenesPiso.as_view()),
    url(r'^id(?P<id>[a-zA-Z0-9-]+).json/$', GetUsuario.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registroUsuario$', views.registroUsuario, name='registroUsuario'),
    url(r'^addPiso', views.addPiso, name='addPiso'),
    url(r'^login$', login, {'template_name': 'index.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'index.html', }, name="logout"),
    url(r'^highcharts$', HighCharts.as_view(), name='highchart')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
