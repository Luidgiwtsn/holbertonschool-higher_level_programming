#!/usr/bin/env python3
from task_00_intro import generate_invitations


with open('template.txt', 'r') as file:
    template_content = file.read()

# Liste des participants
attendees = [
    {"name": "Alice", "event_title": "Python Conference",    "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob",   "event_title": "Data Science Workshop","event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie","event_title": "AI Summit",           "event_date": None,         "event_location": "Boston"}
]

# Appel de la fonction principale
generate_invitations(template_content, attendees)

# Tests des cas d'erreur
print("\n--- Test : template vide ---")
generate_invitations("", attendees)

print("\n--- Test : liste vide ---")
generate_invitations(template_content, [])

print("\n--- Test : type invalide pour template ---")
generate_invitations(123, attendees)

print("\n--- Test : type invalide pour attendees ---")
generate_invitations(template_content, "pas une liste")
