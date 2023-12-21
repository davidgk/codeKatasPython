
class Subscriber:
    def __init__(self, label):
        self.label = label
        self.messages = []

    def subscribe(self, message):
        # maybe some process
        self.messages.append(message)
        return "ok"


class PersonalQueueFIFO:
    def __init__(self):
        self.subscribers = []
        self.topics = {"A": [], "B":  [], "fails": []}

    def addSubscribers(self, subscribers):
        for subscriber in subscribers:
            self.subscribers.append(subscriber)

    def publish(self, message):
        for key in self.topics:
            if key == message.topic:
                self.topics[key].append(message)
                return "ok"
        self.topics['fails'].append(message)
        return "fail"

    def process(self):
        for subscriber in self.subscribers:
            topic = self.topics[subscriber.label]
            if len(topic) > 0:
                result = subscriber.subscribe(topic[0])
                if result != "ok":
                    self.topics["fails"].append(topic[0])
                del topic[0]

    async def run(self):
        self.run = True
        while self.run:
            self.process()

    async def stop(self):
        self.run = False

class Producer:
    def __init__(self, queue: PersonalQueueFIFO):
        self.myQueue = queue

    def sendMessage(self, message):
        result = self.myQueue.publish(message)
        if result is "ok":
            return "OK"


class MessageTopic:
    def __init__(self, topic, message):
        self.topic = topic
        self.message = message


