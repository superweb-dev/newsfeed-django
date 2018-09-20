from django.urls import include, path

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path(r'', ArticleListView.as_view()),
    path(r'<subject>/<slug:slug>', ArticleDetailView.as_view()),
]