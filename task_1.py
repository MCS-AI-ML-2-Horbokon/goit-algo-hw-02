from typing import Literal
from uuid import UUID, uuid4
from time import sleep
from queue import Queue


class Request:
    id: UUID
    status: Literal["new", "completed"]

    def __init__(self) -> None:
        self.id = uuid4()
        self.status = "new"
        print(f"Created: {self.id}")

    def process(self):
        self.status = "completed"
        print(f"Completed: {self.id}")


queue = Queue()

def generate_request():
    request = Request()
    queue.put(request)

def process_request():
    if queue.qsize() > 0:
        request = queue.get()
        request.process()
    else:
        print("Queue is empty")

def main():
    try:
        while True:
            generate_request()
            process_request()
            sleep(1)
    except KeyboardInterrupt:
        process_request() # empty


if __name__ == "__main__":
    main()
