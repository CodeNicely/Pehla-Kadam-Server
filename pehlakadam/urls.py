"""pehlakadam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

import xadmin
from django.conf.urls import url
from django.contrib import admin
from xadmin.plugins import xversion
from campaign.views import campaign
from gallery.views import gallery_image,gallery_video
xversion.register_models()

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^campaign/', campaign),
    url(r'^image/', gallery_image),
    url(r'^video/', gallery_video),
    url(r'^video/', gallery_video),


]
