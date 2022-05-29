import asyncio
from aioconsole import ainput

BOUND = 10**5


def collatz(n):
    steps = 0
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n = n / 2
        steps += 1
    return steps


async def length_counter(target):
    count = 0
    for i in range(2, BOUND):
        if collatz(i) == target:
            count += 1
        await asyncio.sleep(0)
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
