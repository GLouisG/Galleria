from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.landing,name='home'),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)