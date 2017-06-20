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


from login.views import login
from django.conf import settings
from django.conf.urls.static import static
from about_us.views import about_us
from welcome.views import welcome
from splash_screen.views import splash_screen
from contact_us.views import contact_us
from feedback.views import feedback
from join_us.views import join_us
from story.views import stories,like,share
from admin_panel.views import home
xversion.register_models()

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^home/',home),
    url(r'^campaign/', campaign),
    url(r'^gallery_image/', gallery_image),
    url(r'^gallery_video/', gallery_video),
    url(r'^like/', like),
    url(r'^share/', share),
    url(r'^stories/',stories),
    url(r'^login/', login),
    url(r'^splash_screen/', splash_screen),
    url(r'^welcome/', welcome),
    url(r'^about_us/', about_us),   
    url(r'^contact_us/',contact_us),
    url(r'^feedback/',feedback),
    url(r'^join_us/',join_us),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)