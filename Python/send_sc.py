import random
from pythonosc import osc_message_builder
from pythonosc import udp_client

# Set up the OSC client
client = udp_client.SimpleUDPClient("127.0.0.1", 57120)

# Loop indefinitely to send numbers
while True:
    # Prompt the user for a number between 1 and 5
    number = int(input("Enter a number between 1 and 5 (or enter 0 to quit): "))

    # If the user entered 0, exit the loop
    if number == 0:
        break

    # Send the OSC message to SuperCollider
    client.send_message("/number", number)
