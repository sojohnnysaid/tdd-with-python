from django.contrib import admin
from django.urls import path, include
from lists import views as list_views
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_views.home_page, name='home'),
    path('lists/', include('lists.urls')),
    path('accounts/', include(accounts_urls)),
]
