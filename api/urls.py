from django.urls import path
from .views import GroupViewSet,UserViewSet
urlpatterns = [
	path('user/', UserViewSet.as_view({
                                        'get': 'list',
                                        'post': 'create'
                                    }), name='user-list'),

    path('user/<int:pk>/',UserViewSet.as_view({'get': 'retrieve',
                                    'put': 'update',
                                    'patch': 'partial_update',
                                    'delete': 'destroy'}),name='user-detail'),

	path('group/', GroupViewSet.as_view({
                                        'get': 'list',
                                        'post': 'create'
                                    }), name='group-list'),

    path('group/<int:pk>/',GroupViewSet.as_view({'get': 'retrieve',
                                    'put': 'update',
                                    'patch': 'partial_update',
                                    'delete': 'destroy'}),name='group-detail'),


]
