from django.urls import path
from . import views

urlpatterns = [
    path('index',views.add,name='add'),
    # path('detail',views.details, name='details'),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('cbvindex',views.TaskListView.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.TaskdeleteView.as_view(), name='cbvdelete'),

]