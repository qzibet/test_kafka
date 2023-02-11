from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'fibonacci',
    group_id='my-group',
    bootstrap_servers=['localhost:9092']
)


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        if n < len(self.cache):
            return self.cache[n]

        else:
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


for message in consumer:
    fib_digit = int(message.value)
    fib = Fibonacci()
    print(fib(fib_digit))

