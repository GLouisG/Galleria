from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.landing,name='home'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^location/?P<location>\w+/', views.by_location, name='location')
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)