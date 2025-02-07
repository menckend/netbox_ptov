from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views


app_name = 'netbox_ptov'

urlpatterns = [
    path("golabs/", views.golab, name="golab"),
    
    # GNS3Server URLs
    path("gns3servers/", views.GNS3ServerListView.as_view(), name="gns3server_list"),
    path("gns3servers/add/", views.GNS3ServerEditView.as_view(), name="gns3server_add"),
    path("gns3servers/<int:pk>/", views.GNS3ServerView.as_view(), name="gns3server"),
    path("gns3servers/<int:pk>/edit/", views.GNS3ServerEditView.as_view(), name="gns3server_edit"),
    path("gns3servers/<int:pk>/delete/", views.GNS3ServerDeleteView.as_view(), name="gns3server_delete"),
    path(
        "gns3servers/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="gns3server_changelog",
        kwargs={"model": models.GNS3Server},
    ),

    # PtovJob URLs
    path("ptovjobs/", views.ptovjobListView.as_view(), name="ptovjob_list"),
    path("ptovjobs/add/", views.ptovjobEditView.as_view(), name="ptovjob_add"),
    path("ptovjobs/<int:pk>/", views.ptovjobView.as_view(), name="ptovjob"),
    path("ptovjobs/<int:pk>/edit/", views.ptovjobEditView.as_view(), name="ptovjob_edit"),
    path("ptovjobs/<int:pk>/delete/", views.ptovjobDeleteView.as_view(), name="ptovjob_delete"),
    path(
        "ptovjobs/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="ptovjob_changelog",
        kwargs={"model": models.ptovjob},
    ),

    # SwitchToJob URLs
    path("switchtojobs/", views.switchtojobListView.as_view(), name="switchtojob_list"),
    path("switchtojobs/add/", views.switchtojobEditView.as_view(), name="switchtojob_add"),
    path("switchtojobs/<int:pk>/", views.switchtojobView.as_view(), name="switchtojob"),
    path("switchtojobs/<int:pk>/edit/", views.switchtojobEditView.as_view(), name="switchtojob_edit"),
    path("switchtojobs/<int:pk>/delete/", views.switchtojobDeleteView.as_view(), name="switchtojob_delete"),
    path(
        "switchtojobs/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="switchtojob_changelog",
        kwargs={"model": models.switchtojob},
    ),
]
