"""Define URL pattern for learning_logs"""

from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # page that show all topics
    path('topics/', views.topics, name='topics'),
    # page for single topic
    path('topics/<int:topic_id>/',views.topic, name='topic'),
    # page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page for edditing entry
    path('edit_entry/<int:edit_entry>/', views.edit_entry, name='edit_entry')
]