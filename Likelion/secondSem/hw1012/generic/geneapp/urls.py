from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from geneapp import views

urlpatterns = [
    path('post/', views.SnippetList.as_view()),
    path('post/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
