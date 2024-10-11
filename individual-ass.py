#Q77.

from collections import deque

undo_stack = []

registration_queue = deque()

event_details = []

def add_event(event_name):
    event_details.append(event_name)
    print(f"Event '{event_name}' added to the event list.")

def register_event(event_name, participant_name):
    if event_name in event_details:
        registration_queue.append((event_name, participant_name))
        undo_stack.append((event_name, participant_name))
        print(f"Participant '{participant_name}' registered for event '{event_name}'.")
    else:
        print(f"Event '{event_name}' not found.")


def undo_registration():
    if undo_stack:
        event_name, participant_name = undo_stack.pop()
        if (event_name, participant_name) in registration_queue:
            registration_queue.remove((event_name, participant_name))
            print(f"Undo registration: Participant '{participant_name}' removed from event '{event_name}'.")
        else:
            print("No registration found in the queue to undo.")
    else:
        print("No registration to undo.")


def process_registration():
    if registration_queue:
        event_name, participant_name = registration_queue.popleft()
        print(f"Processing registration: Participant '{participant_name}' is registered for event '{event_name}'.")
    else:
        print("No registrations to process.")


add_event("Tech Conference")
add_event("Music Festival")

register_event("Tech Conference", "Assumpta")
register_event("Music Festival", "Aliane")






process_registration()

undo_registration()

process_registration()
