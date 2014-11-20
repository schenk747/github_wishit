from django.conf.urls import patterns, url

from wishit import views

urlpatterns = patterns('', 
		url(r'^$', views.index, name='index'),
		url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='details'),
		url(r'^results/(?P<pk>\d+)/$', views.ResultsView.as_view(), name='results'),
		url(r'^text/(?P<gift_id>\d+)$', views.texts, name='texts'),
		url(r'^update_text/(?P<gift_id>\d+)$', views.update_texts, name='update_texts'),
		url(r'^home', views.home, name='home'),
		url(r'^login', views.login_user, name='login'),
		url(r'^logout', views.logout_user, name='logout'),
		url(r'^update_wishlist', views.update_wishlist, name="update_wl"),
		url(r'^delete_gift', views.delete_gift, name="delete_g"),
		url(r'^update_gift', views.update_gift, name="update_g"),
		url(r'^register', views.register, name="register"),
)
