from django.contrib import admin
from django.urls import path, include

#############################Untuk Media####################################
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


#memanggil fungsi home yg ada didalam file views

from myproject.views import home, about
from myproject.autentikasi import  akun_login

urlpatterns = [
   path('admin/', admin.site.urls),

    path('', home, name= 'home'),
    path('dashboard/', include("berita.urls")),
    path('about/', about, name='about'),

    path('autentikasi/login', akun_login, name="akun_login")
   ]

################################### Untuk media ##########################
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

