from django.conf.urls import url
from django.contrib import admin
from lists.views import home_page

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', home_page, name='home'),  # <- 추가
]