from dependency_injector.wiring import inject, Provide
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from slackNotification import Container
from slackNotification.application.service.NotifySalesUseCase import NotifySalesUseCase
from slackNotification.infrastructure.SalesConsumer import SalesConsumer


# Create your views here.
@inject
@csrf_exempt
def kafka_sales_init(
        request: HttpRequest,
        consumer: SalesConsumer = Provide[Container.sales_consumer]
):
    print("starting kafka for sales")
    consumer.consume()
    data = {
        'event': 'started'
    }
    return JsonResponse(data)
