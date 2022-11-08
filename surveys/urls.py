from django.urls import include, path

from surveys.views import Create, Edit

urlpatterns = [
    path('create', Create.as_view(), name='create'),
    path('edit/<int:id>', Edit.as_view(), name='edit'),
]
