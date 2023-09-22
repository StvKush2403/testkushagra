from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
    path('index',views.index_f),
    path('test',views.teste_f),
    path('abc',views.abc),
    path('kush',views.kush),
    path('shiva',views.shiva),
    path('testupdatefunction',views.testupdatefunction),
    path('practiseupdatefunc',views.practiseupdatefunc),
    path('kushagrainsert',views.kushagrainsert),
    path('abcinsert',views.abcinsert),
    path('testupdate',views.testupdate),
    path('fetchall',views.fetchall),
    path('yash',views.yash),
    path('sam',views.sam),
    path('tom',views.tom),
    path('raj',views.raj),

]