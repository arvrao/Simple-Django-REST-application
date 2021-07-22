from django.conf.urls import include, url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from music.models import Student
# from rest_framework.routers import DefaultRouter
# from music import views
from music.views import StudentAPIView, StudentDetail, GenericsAPIView

# urlpatterns = [
# path('student/',  StudentAPIView.as_view(),
# path('detail/<int:id>/',  StudentDetails.as_view())
# ]
# router = DefaultRouter()
# router.register(r'music', views.MusicViewSet)
# router.register(r'music_filter', views.MusicFilter)
# router.register(r'music_genre', views.MusicGenre)
# router.register(r'music_exclude', views.MusicExclude)

#always use path instead of url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('student/',  StudentAPIView.as_view()),
    path('detail/<int:id>/',  StudentDetail.as_view()),
    path('generic/student/<int:id>/',  GenericsAPIView.as_view()),

]
