from django.urls import path
from myapp.views import index, indexItem, add_item, update_item, delete_item, ProductListView
from django.views.decorators.cache import cache_page

app_name = "myapp"


urlpatterns = [
    path("", index, name='index'),
    path("", cache_page(60*15)(ProductListView.as_view()), name="index"),
    path("<int:my_id>/",indexItem, name="detail"),
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:my_id>/", delete_item, name="delete_item"),
]
