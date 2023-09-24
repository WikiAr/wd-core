"""
from dump.memory import print_memory
"""
import psutil
import os

def print_memory():
    usage = psutil.Process(os.getpid()).memory_info().rss
    print(f'memory usage: psutil {usage / 1024 / 1024} MB')
