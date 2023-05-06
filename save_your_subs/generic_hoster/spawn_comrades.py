from typing import Tuple
import threading
from queue import Queue

from . import comrade

COMRAD_COUNT = 1


def spawn_comrades(comrad_count: int = COMRAD_COUNT) -> Queue:
    work_queue: Queue = Queue()

    for i in range(comrad_count):
        image_thread = threading.Thread(target=comrade.comrad_work_schedule, args=(work_queue,))
        image_thread.start()

    return work_queue
