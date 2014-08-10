from django.conf.urls import patterns, url

from wishit import views

urlpatterns = patterns('', 
		url(r'^$', views.IndexView.as_view(), name='index'),
		url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='details'),
		url(r'^results/(?P<pk>\d+)/$', views.ResultsView.as_view(), name='results'),
		url(r'^text/(?P<gift_id>\d+)$', views.texts, name='texts'),
		url(r'^update_text/(?P<gift_id>\d+)$', views.update_texts, name='update_texts'),
)
