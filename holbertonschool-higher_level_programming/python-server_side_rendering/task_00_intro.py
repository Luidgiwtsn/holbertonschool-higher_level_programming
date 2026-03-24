#!/usr/bin/env python3
import logging

# Configuration du système de logs (messages d'erreur/info dans la console)
logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """
    Génère des fichiers d'invitation personnalisés à partir d'un template.
    """

    
    # On vérifie que template est bien une chaîne de caractères
    if not isinstance(template, str):
        logging.error(
            f"Invalid input: 'template' doit être une chaîne de caractères (str), "
            f"reçu : {type(template).__name__}"
        )
        return 

    # On vérifie que attendees est bien une liste de dictionnaires
    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        logging.error(
            f"Invalid input: 'attendees' doit être une liste de dictionnaires (list[dict]), "
            f"reçu : {type(attendees).__name__}"
        )
        return

    # Si le template est une chaîne vide ""
    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    # Si la liste de participants est vide []
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Les 4 clés attendues dans chaque dictionnaire
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # enumerate donne l'index à partir de 1 et le participant
    for index, attendee in enumerate(attendees, start=1):

        # On commence avec une copie du template original
        personalized_text = template

        for key in placeholders:
            # On récupère la valeur, ou None si elle n'existe pas
            value = attendee.get(key)

            # Si la valeur est None ou manquante
            if value is None:
                value = "N/A"

            personalized_text = personalized_text.replace(f"{{{key}}}", str(value))


        #Écriture dans un fichier output_X.txt
        output_filename = f"output_{index}.txt"

        try:#Si output_x.txt n'existe pas il le crée, si existe écrase
            with open(output_filename, "w") as output_file:
                output_file.write(personalized_text)
            logging.info(f"Fichier '{output_filename}' créé avec succès.")

        except IOError as e:
            # Si une erreur survient lors de l'écriture
            logging.error(f"Erreur lors de l'écriture de '{output_filename}' : {e}")
