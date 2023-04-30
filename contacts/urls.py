from django.urls import path
from .views import ContactsListView, ContactsDetailView, ContactsCreateView, ContactsUpateView, ContactsDeleteView

app_name = 'contacts'

urlpatterns = [
    path('', ContactsListView.as_view(), name = 'listcontacts'),
    path('<int:pk>/', ContactsDetailView.as_view(), name = 'detailcontacts'),
    path('create/', ContactsCreateView.as_view(), name = 'createcontacts'),
    path('<int:pk>/update/', ContactsUpateView.as_view(), name = 'updatecontacts'),
    path('<int:pk>/delete/', ContactsDeleteView.as_view(), name = 'deletecontacts'),

]
