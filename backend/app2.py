# from google.cloud import pubsub_v1
# import os

# # Authentication with service account
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# project_id = "vp33-400500"
# topic_id = "ICA3"

# # Initialize a Publisher Client
# publisher = pubsub_v1.PublisherClient()
# topic_path = publisher.topic_path(project_id, topic_id)

# def send_message(message):
#     # Publish a message to the Pub/Sub topic
#     future = publisher.publish(topic_path, message.encode("utf-8"))
#     print(f"Published message with ID: {future.result()}")

# if __name__ == "__main__":
#     send_message("Hello, this is a test message from app2!")
