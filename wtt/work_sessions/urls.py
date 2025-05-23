from django.urls import path

from .views import WorkSessionViewSet, WorkSessionLabelViewSet

urlpatterns = [
    path('', WorkSessionViewSet.as_view({'get': 'list', 'post': 'create'}), name='work-session-list'),
    path('<uuid:pk>/', WorkSessionViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='work-session'),
    path('<uuid:pk>/end/', WorkSessionViewSet.as_view({'post': 'end'}), name='work-session-end'),

    path('labels/', WorkSessionLabelViewSet.as_view({'get': 'list', 'post': 'create'}), name='work-session-label-list'),
    path('labels/<uuid:pk>/', WorkSessionLabelViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='work-session-label'),
]
