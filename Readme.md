# Description
This microservice is a django service and is responsible for sending slacks. It is listening to a kafka broker and, based on the topic, sends a slack to one team or another.

The slack implementation is mocked.

## Run it:

### Using Docker (Recommended)

In the root folder just run:

`docker-compose up`

## Test it

This service will only listen messages, in theory, this shouldn't have any endpoint. BUT:

Here I found a problem. As django is prepared only to get endpoints, it is necessary to do a workaround to have a subscriber always listening for a topic. The workaround that I thought of was to call an endpoint to initiate the kafka subscribers. It is only necessary to call once, and it is not necessary to wait for the response. There is an endpoint by subscriber. In the example, there are two subscribers (sales and engineering) so two endpoints have to be called.

I am sure that there should be another option to do it. Maybe django is not necessary in this microservice, since any endpoint has to be exposed. But since all the configuration, mainly the inversion of control and the injection of dependencies was done in django in the other microservice, I decided to continue in this way.

The endpoints that has to be called are:

* For the sales consumer:
  * `[GET] http://127.0.0.1:8001/notification/sales/kafka/`

Once the kafka is initialized, this will listen to the configured topic. For example, the SalesConsumer will be listening the sales topic and the EngineeringConsumer will be listening the engineering topic. Both of them will start their own use case and the implementation can be different.