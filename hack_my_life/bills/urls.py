from django.urls import path,re_path
from bills import views

# Template Tagging
app_name = 'bills'

urlpatterns = [
    re_path(r'^category/list/$',         views.CategoryListView.as_view(),       name='categories'),
    re_path(r'^payment_method/list/$',   views.PaymentMethodListView.as_view(),  name='payment_methods'),
    re_path(r'^payment_provider/list/$', views.PaymentProviderListView.as_view(),name='payment_providers'),
    re_path(r'^schedule/list/$',         views.ScheduleListView.as_view(),       name='schedules'),

    re_path(r'^creditor/list/$',         views.CreditorListView.as_view(),       name='creditors'),
    re_path(r'^creditor/create/$',       views.CreditorCreateView.as_view(),     name='creditor_create'),
       path('creditor/<int:pk>/',        views.CreditorDetailView.as_view(),     name='creditor_detail'),
       path('creditor/update/<int:pk>/', views.CreditorUpdateView.as_view(),     name='creditor_update'),
       path('creditor/delete/<int:pk>/', views.CreditorDeleteView.as_view(),     name='creditor_delete'),


       path('payment_method/<int:pk>/',  views.PaymentMethodDetailView.as_view(),name='payment_method_detail'),
]
