from google.cloud import pubsub_v1
import os

# Authentication with service account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

project_id = "vp33-400500"
subscription_id = "ICA3_SUB"

# Initialize a Subscriber Client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Callback function to handle messages
def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()  # Acknowledge the message

# Subscribe to the subscription and pull messages
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...")

# Keep the subscriber running
try:
    streaming_pull_future.result()  # Block and wait for messages
except KeyboardInterrupt:
    streaming_pull_future.cancel()
