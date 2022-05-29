import concurrent.futures
import multiprocessing
import queue
import itertools
import signal
import time

BOUND = 10**5

in_queue = multiprocessing.Queue(100)
exit_event = multiprocessing.Event()


def exit_handler(signum, frame):
    exit_event.set()


signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)


def collatz(n):
    steps = 0
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n = n // 2
        steps += 1
    return steps


def collatz_consumer(target):
    count = 0
    while True:
        if not in_queue.empty():
            try:
                n = in_queue.get(timeout=1)
            except queue.Empty:
                return count

            if collatz(n) == target:
                count += 1

        if exit_event.is_set():
            return count


def range_producer():
    for n in range(2, BOUND):
        if exit_event.is_set():
            return
        try:
            in_queue.put(n, timeout=1)
        except queue.Full:
            exit_event.set()
            return

    while True:
        time.sleep(0.05)
        if in_queue.empty():
            exit_event.set()
            return


def length_counter(target):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(range_producer)
        results = executor.map(
            collatz_consumer,
            itertools.repeat(target, 4)
        )

    return sum(results)


def get_input(prompt):
    while True:
        n = input(prompt)
        try:
            n = int(n)
        except ValueError:
            print("Value must be an integer.")
            continue

        if n <= 0:
            print("Value must be positive.")
        else:
            return n


def main():
    print("Collatz Sequence Counter")

    target = get_input("Collatz sequence length to search for: ")
    print(f"Searching in range 1-{BOUND}...")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_guess = executor.submit(
            get_input,
            "How many times do you think it will appear? "
        )

        count = length_counter(target)

    guess = future_guess.result()

    if guess == count:
        print("Exactly right! I'm amazed.")
    elif abs(guess - count) < 100:
        print(f"You're close! It was {count}.")
    else:
        print(f"Nope. It was {count}.")


if __name__ == "__main__":
    main()
