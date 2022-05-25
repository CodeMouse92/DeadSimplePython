def coroutine():
    ret = None
    while True:
        print("...")
        recv = yield ret
        print(f"recv: {recv}")
        ret = recv


co = coroutine()
current = co.send(None)
print(f"current (ret): {current}")

for i in range(10):
    current = co.send(i)
    print(f"current (ret): {current}")

co.close()
