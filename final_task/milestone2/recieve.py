import asyncio
import websockets
import sys  

async def receive_message():
    uri = "ws://192.168.114.119:81"
    no_exchange_timeout = 30  # Time in seconds to wait for data before stopping

    try:
        async with websockets.connect(uri, ping_interval=10, ping_timeout=5) as websocket:
            print("Connected to ESP32 WebSocket server.")
            while True:
                try:
                    # Wait for a message with a timeout
                    message = await asyncio.wait_for(websocket.recv(), timeout=no_exchange_timeout)
                    print("Message received from ESP32:")
                    print(message)
                except asyncio.TimeoutError:
                    print(f"No exchange for {no_exchange_timeout} seconds. Stopping the program.")
                    sys.exit(0)  # Exit the program
    except Exception as e:
        print(f"Connection lost: {e}. Stopping the program.")
        sys.exit(0)  # Exit the program

if __name__ == "__main__":
    asyncio.run(receive_message())
