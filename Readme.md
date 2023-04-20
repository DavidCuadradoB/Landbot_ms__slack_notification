# Description
This microservice is a django service and is responsible for sending slacks. It is listening to a kafka broker and, based on the topic, sends a slack to one team or another.

The slack implementation is mocked.

## Run it:

### Using Docker (Recommended)

In the root folder just run:

`docker-compose up`

## Test it

This service will only listen messages, in theory, this shouldn't have any endpoint. BUT:

In this point I found a problem. As django is set up only to get endpoints, it is necessary to make a workaround to have a subscriber always listening to a topic. The solution I came up with was to call an endpoint to start the kafka subscribers. You only need to call these once, and you don't need to wait for the response. There is one endpoint per subscriber. In the test, there are two subscribers (sales and engineering) so two endpoints need to be called.

I'm sure there must be another way to do this. Maybe django is not needed in this microservice because there is no endpoint to expose. But since all the configuration, mainly control inversion and dependency injection, was done in django in the other microservice, I decided to go with it.

The endpoints that has to be called are:

* For the sales consumer:
  * `[GET] http://127.0.0.1:8002/notification/sales/kafka/`

Once the Kafka is initialised, it will listen to the configured topic. For example, the SalesConsumer will listen to the Sales topic and the EngineeringConsumer will listen to the Engineering topic. Both will run
use case and the implementation can be different.

## TODO

There are some things that, given more time, I would like to finish:

* Add more validations. The event should be validated, maybe the description is incorrect but, since there are not any requirements about it, I decided focus on other stuff

* More tests: Integration tests are missing, I would like to add at least one test that tests the whole use case. It was a bit difficult to do it with Python and I preferred to spend more time on other issues. Also, the validations mentioned before should have unit tests. Kafka's implementation and the Slack's implementation has no testing, I should think a bit about how to test it.

As I said, I decided to leave this pending and dedicate myself more to other topics. My goal is to get the queuing system up and running and I had some problems with the communication between dockers. My apologies for not having it 100% finished, time is what it was and I had to prioritise.
