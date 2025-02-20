from django.urls import path

from netbox.tests.dummy_plugin import views


urlpatterns = (
    path('models/', views.DummyModelsView.as_view(), name='dummy_model_list'),
    path('models/add/', views.DummyModelAddView.as_view(), name='dummy_model_add'),
)
