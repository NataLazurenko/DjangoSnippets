from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin
urlpatterns = [
    path('', views.index_page, name="home"),
    path('admin/', admin.site.urls),
    path('register/',views.register,name="register"),
    path('login/',views.Login, name="login"),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('profile', views.profile, name="profile"),
    path('logout', views.logout_request, name="logout")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
