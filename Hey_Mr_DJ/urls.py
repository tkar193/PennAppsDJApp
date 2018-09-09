from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import login, logout

app_name = "login"

urlpatterns = [
    path('login/', include('login.urls')),
    #path('admin/', admin.site.urls),
]
