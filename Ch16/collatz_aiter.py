import asyncio
from aioconsole import ainput

BOUND = 10**5


class Collatz:

    def __init__(self):
        self.start = 2

    async def count_steps(self, start_value):
        steps = 0
        n = start_value
        while n > 1:
            if n % 2:
                n = n * 3 + 1
            else:
                n = n // 2
            steps += 1
        return steps

    def __aiter__(self):
        return self

    async def __anext__(self):
        steps = await self.count_steps(self.start)
        self.start += 1
        if self.start == BOUND:
            raise StopAsyncIteration
        return steps


async def length_counter(target):
    count = 0
    # iter = Collatz().__aiter__()
    # running = True
    # while running:
    #     try:
    #         steps = await iter.__anext__()
    #     except StopAsyncIteration:
    #         running = False
    #     else:
    #         if steps == target:
    #             count += 1

    async for steps in Collatz():
        if steps == target:
            count += 1
    return count


async def get_input(prompt):
    while True:
        n = await ainput(prompt)
        try:
            n = int(n)
        except ValueError:
            print("Value must be an integer.")
            continue

        if n <= 0:
            print("Value must be positive.")
        else:
            return n


async def main():
    print("Collatz Sequence Counter")

    target = await get_input("Collatz sequence length to search for: ")
    print(f"Searching in range 1-{BOUND}...")

    # length_counter_task = asyncio.create_task(length_counter(target))
    # guess_task = asyncio.create_task(
    #     get_input("How many times do you think it will appear? ")
    # )

    # count = await length_counter_task
    # guess = await guess_task

    (guess, count) = await asyncio.gather(
        get_input("How many times do you think it will appear? "),
        length_counter(target)
    )

    if guess == count:
        print("Exactly right! I'm amazed.")
    elif abs(guess - count) < 100:
        print(f"You're close! It was {count}.")
    else:
        print(f"Nope. It was {count}.")


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
