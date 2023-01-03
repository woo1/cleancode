class MetricsClient:
    '''타사 지표 전송 클라이언트'''

    def send(self, metric_name, metric_value):
        if not isinstance(metric_name, str):
            raise TypeError("metric_name으로 문자열 타입을 사용해야 한다.")
        if not isinstance(metric_value, str):
            raise TypeError("metric_value으로 문자열 타입을 사용해야 한다.")

        print(f"{metric_name} 전송 값 = {metric_value}")

class WrappedClient:
    def __init__(self):
        self.client = MetricsClient()

    def send(self, metric_name, metric_value):
        return self.client.send(str(metric_name), str(metric_value))

class Process:
    def __init__(self):
        self.client = WrappedClient()

    def run_process(self):
        return 1

    def process_iterations(self, n_iterations):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send(f"iteration.{i}", result)

if __name__ == '__main__':
    process1 = Process()
    process1.process_iterations(10)