import psutil
import os

class MemoryUsage:
    @staticmethod
    # 메모리 사용량 측정 함수
    def get_memory_usage():
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024  # 메모리 사용량(MB 단위)

