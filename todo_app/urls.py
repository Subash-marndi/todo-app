from django.urls import path 
from.import views

urlpatterns =[
    # Add task
    path('add_task/', views.add_task , name = 'add_task'),

    # Mark as done feature
    path('mark_as_done/<int:pk>/', views.mark_as_done ,name = 'mark_as_done'),

    # Mark as undone feature
    path('undo/<int:pk>/',views.undo ,name = 'undo'),
    
    # edit feature
    path('edit/<int:pk>/',views.edit , name= 'edit'),

    # DELETE Feature 
    path('delete/<int:pk>/',views.delete , name= 'delete'),
    
]