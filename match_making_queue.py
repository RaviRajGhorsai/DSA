"""

Complete the matchmake function that simulates users joining and leaving the matchmaking queue. The function should take a queue instance and a user tuple containing a name and action (either "join" or "leave"):

user = ('Bob', 'join')
user = ('Alice', 'leave')

For each call to matchmake:

If the action is "leave", search the queue for the user and remove them if they are in the queue.
If the action is "join", push the user's name onto the queue.
Lastly, check if the queue has at least 4 users in it. If so, pop the first 2 users from the queue and return the following string:
"{user1} matched {user2}!"

Where user1 is the first user popped and user2 is the second user popped.

If there were less than 4 users in the queue, return the following string: "No match found"


"""

from my_queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:

    name, action = user

    if action == "join":
        queue.push(user[0])

    elif action == "leave":
        queue.search_and_remove(name)

    if queue.size() == 4:
        user1 = queue.pop()
        user2 = queue.pop()

        return f"{user1} matched {user2}"

    return "No match was found."
