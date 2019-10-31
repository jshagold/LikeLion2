from django.urls import include, path
from post import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)