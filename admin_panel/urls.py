from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	home_stories,
	home_feedback,
	home_joinus,
	change_status,
	)


urlpatterns = [
	url(r'^$', home_stories, name='stories'),
	url(r'^feedback/$', home_feedback, name='feedback'),
	url(r'^joinus/$', home_joinus, name='joinus'),
	url(r'^change_status/$',change_status , name='change_status'),

]