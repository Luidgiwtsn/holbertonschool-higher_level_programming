#!/usr/bin/python3
"""Module de tests unitaires pour la fonction max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Classe de test pour la fonction max_integer.
    Chaque méthode teste un scénario spécifique pour garantir la robustesse.
    """

    def test_ordered_list(self):
        """Teste une liste triée d'entiers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Teste une liste non triée d'entiers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Teste une liste où le maximum est au début."""
        self.assertEqual(max_integer([10, 5, 8, 3]), 10)

    def test_empty_list(self):
        """Teste une liste vide (doit retourner None)."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Teste une liste contenant un seul élément."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Teste une liste contenant uniquement des nombres négatifs."""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    def test_mixed_numbers(self):
        """Teste un mélange de nombres positifs et négatifs."""
        self.assertEqual(max_integer([-10, 15, 0, 2]), 15)

    def test_floats(self):
        """Teste une liste contenant des nombres à virgule (floats)."""
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)


if __name__ == '__main__':
    unittest.main()
