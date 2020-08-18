from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('' , views.homepage,name='home'),
   # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/' , views.login , name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<str:name>/more' , views.more , name='more'),
    path('added/<int:pk>',views.added , name='added'),
    path('mycart' , views.mycart , name='mycart'),
    path('delordered/<int:pk>' , views.delordered , name='delordered'),
    path('buyitem' , views.buyitem , name='buyitem') ,
    path('myorders' ,views.myorders , name='myorders') ,
    path('profile' ,views.profile , name='profile') ,
    path('editprofile' , views.editprofile , name='editprofile')

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)