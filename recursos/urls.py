from django.urls import path
from .views import v_list, v_update, v_create, v_delete

urlpatterns = [
    path('', v_list),
    path('create',  v_create),
    path('update/<int:recursos_id>/', v_update),
    path('delete/<int:recursos_id>/', v_delete),

]