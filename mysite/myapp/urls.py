from django.urls import path
from myapp.views import index, indexItem, add_item, update_item

app_name = "myapp"


urlpatterns = [
    path("", index),
    path("<int:my_id>/", indexItem, name="detail"),
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item")
]
