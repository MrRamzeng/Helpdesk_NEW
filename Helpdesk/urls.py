from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from Helpdesk import settings
from help.views import ticket, manuals, manual
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('manuals/', manuals, name='manuals'),
    path('manual/<int:manual_id>/', manual, name='manual'),
    path('tickets/', ticket, name='tickets'),
    path('', RedirectView.as_view(url = '/tickets/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
