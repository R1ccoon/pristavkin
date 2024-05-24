from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.product_list, name='product_list'),
    path('<category_slug>',
         views.product_list,
         name='product_list_by_category'),
    path('<slug>/',
         views.product_detail,
         name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)