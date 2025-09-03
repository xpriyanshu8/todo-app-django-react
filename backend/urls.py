"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')

schema_view = get_schema_view(
    openapi.Info(
        title="Task API",
        default_version='v1',
        description="API for managing tasks",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('tasks/',views.getTask, name ="tasks"),
    #path('tasks/create/',views.createTask, name ="create-tasks"),
    #path('tasks/update/<int:pk>/',views.updateTask, name ="update-tasks"),
    #path('tasks/delete/<int:pk>/',views.deleteTask, name ="delete-tasks"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.registerUser, name="register"),
    path('profile/',views.getProfile,name="profile"),
    path('get/tasks/',views.getTask, name="gettasks"),
    path('add/tasks',views.addTask,name="addtasks"),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
