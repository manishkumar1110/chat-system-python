# Represents a user in the chat system
class User:
    def __init__(self, username):
        self.username = username


# Represents a message sent by a user
class Message:
    # Class variable to keep track of message IDs
    message_counter = 0

    def __init__(self, sender, content):
        # Increase the message counter for every new message
        Message.message_counter += 1

        # Give each message a unique ID
        self.id = Message.message_counter

        # Store the user who sent the message
        self.sender = sender

        # Store the message content
        self.content = content

    # Controls how a Message object is displayed as a string
    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# Represents a chat room
class ChatRoom:
    def __init__(self, room_name):
        # Store the name of the chat room
        self.room_name = room_name

        # List of users currently in the room
        self.users = []

        # List of messages sent in the room
        self.messages = []

    # Add a user to the chat room
    def join_room(self, user):
        self.users.append(user)
        print(f"{user.username} joined the chat room.")

    # Remove a user from the chat room
    def leave_room(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left the chat room.")
        else:
            print(f"{user.username} is not in the chat room.")

    # Send a message if the user is currently in the room
    def send_message(self, user, content):
        if user in self.users:
            # Create a new Message object
            message = Message(user, content)

            # Store the message in the chat room
            self.messages.append(message)

            print("Message sent.")
        else:
            print("User must join the room before sending messages.")

    # Display all messages in the chat room
    def show_history(self):
        print(f"\n--- {self.room_name} Chat History ---")

        # Check if there are no messages
        if len(self.messages) == 0:
            print("No messages yet.")
        else:
            # Display each message
            for message in self.messages:
                print(message)


# Creating users
u1 = User("Manish")
u2 = User("Rahul")

# Creating a chat room
room = ChatRoom("Python Group")

# Users joining the chat room
room.join_room(u1)
room.join_room(u2)

# Sending messages
room.send_message(u1, "Hello everyone!")
room.send_message(u2, "Hi Manish!")
room.send_message(u1, "Let's learn OOP.")

# Viewing chat history
room.show_history()

# User leaving the chat room
room.leave_room(u2)

# Trying to send a message after leaving the room
room.send_message(u2, "Can I still send this?")

# Showing the chat history again
room.show_history()