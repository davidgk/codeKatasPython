from example import Subscriber, PersonalQueueFIFO, Producer, MessageTopic


async def test_should_the_shipper_receive_the_message_from_the_producer_when_is_created():
    subscriberA = Subscriber("A")
    subscriberB = Subscriber("B")
    myPersonalQueue = PersonalQueueFIFO()

    myPersonalQueue.addSubscribers([subscriberA, subscriberB])
    myPersonalQueue.run()
    producer = Producer(myPersonalQueue)

    message = MessageTopic("A", "mi Message is For A")
    producer.sendMessage(message)
    # # this should keep going.. , for the sake of example I do it manually
    # myPersonalQueue.process()

    assert len(subscriberA.messages) == 1
    assert subscriberA.messages[0].message == "mi Message is For A"
    assert len(subscriberB.messages) == 0
    await myPersonalQueue.stop()


def test_should_the_queue_save_in_fails_when_topic_not_exists():
    subscriberA = Subscriber("A")
    myPersonalQueue = PersonalQueueFIFO()

    myPersonalQueue.addSubscribers([subscriberA])
    producer = Producer(myPersonalQueue)

    message = MessageTopic("X", "mi Message is For A")
    producer.sendMessage(message)
    # this should keep going.. , for the sake of example I do it manually
    myPersonalQueue.process()

    assert len(subscriberA.messages) == 0
    assert len(myPersonalQueue.topics['fails']) == 1


def test_should_keep_in_the_topic_when_the_subscriber_is_not_configured():
    subscriberB = Subscriber("B")
    myPersonalQueue = PersonalQueueFIFO()

    myPersonalQueue.addSubscribers([subscriberB])
    producer = Producer(myPersonalQueue)

    message = MessageTopic("A", "mi Message is For A")
    producer.sendMessage(message)
    # this should keep going.. , for the sake of example I do it manually
    myPersonalQueue.process()

    assert len(subscriberB.messages) == 0
    assert len(myPersonalQueue.topics['A']) == 1


