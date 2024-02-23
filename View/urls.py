
from django.urls import path
from View import views

urlpatterns = [
    path('',views.MyCRUD.as_view(),name='Home'),
    # path('',views.add_show,name='Home'),
    path('Update/<int:id>/',views.UpdateDataView.as_view(),name='update'),
    path('Delete/<int:id>/',views.UserDeleteView.as_view(),name='delete'),

]

