from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'WildlifeResearchApp.views.home'),
    url(r'^animal$', 'WildlifeResearchApp.views.listanimals'),
    url(r'^tblAnimal$', 'WildlifeResearchApp.views.tableAnimals'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
