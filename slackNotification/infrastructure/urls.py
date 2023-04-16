from django.urls import path

from slackNotification.infrastructure import views

urlpatterns = [
    path("sales/kafka/", views.kafka_sales_init, name="kafka_sales_init"),
]
