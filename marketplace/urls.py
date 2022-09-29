from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('connect_wallet/' , views.connect_wallet , name = 'connect_wallet'),
    path('collect/' , views.collect , name = 'collect'),
    path('create/' , views.create , name = 'create'),
    path('faq/' , views.faq , name = 'faq'),
    # path('register/' , views.register , name = 'register'),
    path('roadmap/' , views.roadmap , name = 'roadmap'),
    path('check_out/', views.check_out, name = 'checkout'),
    path('collect/<int:data_id>/' , views.nft_detail , name = 'detail')
]
