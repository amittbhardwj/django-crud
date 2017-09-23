from django.conf.urls import  url

from .views import CRUDList, CRUDCreate, CRUDDelete, CRUDUpdate

urlpatterns = [
  url(r'^$', CRUDList.as_view(), name='CRUD_list'),
  url(r'^create$', CRUDCreate.as_view(), name='CRUD_create'),
  url(r'^edit/(?P<pk>\d+)$', CRUDUpdate.as_view(), name='CRUD_edit'),
  url(r'^delete/(?P<pk>\d+)$', CRUDDelete.as_view(), name='CRUD_delete'),
]