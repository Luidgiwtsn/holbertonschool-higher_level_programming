#!/usr/bin/python3
"""Module qui définit une fonction pour lever une exception NameError."""


def raise_exception_msg(message=""):
    """Lève une exception NameError avec un message.

    Args:
        message (str): Le message à inclure dans l'exception.
                      Par défaut une chaîne vide.

    Raises:
        NameError: Lève toujours cette exception avec le message donné.
    """
    raise NameError(message)
