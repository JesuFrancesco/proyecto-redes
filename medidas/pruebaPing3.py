from ping3 import ping, verbose_ping

r = ping(dest_addr="8.8.8.8", unit="ms")
print(f"Latencia: {r} ms")