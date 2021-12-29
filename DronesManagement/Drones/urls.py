from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

#router.register(r'Drones', views.DroneViewSet)
#router.register(r'Commands', views.CommandViewSet)
#router.register(r'RegisterDrone', views.RegisterDrone)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('LoadingDrone/', views.LoadingDrone.as_view()),
    path('RegisterDrone/',views.RegisterDrone.as_view()),
    path('CheckAvailableDrone/',views.CheckAvailableDrone.as_view()),
    path('CheckDroneBattery/<str:id>',views.CheckDroneBattery.as_view()),
    path('CheckLoadedMedication/<str:id>', views.CheckLoadedMedication.as_view()),



#path('cart-items/<int:id>', CartItemViews.as_view())
]

