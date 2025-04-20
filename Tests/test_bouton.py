import unittest
from  gpiozero.pins.mock import MockFactory
from gpiozero import Button
from model.platine import Platine

Button.pin_factory = MockFactory()

class TestBouton(unittest.TestCase):
    def setUp(self):
        self.bouton_demarrer = 19
        self.bouton_mesure = 26
        self.platine = Platine(self.bouton_demarrer, self.bouton_mesure, "")

    def test_initialisation_bouton(self):
        self.assertEqual(self.platine.boutons["Demarrer"].pin.number, self.bouton_demarrer)
        self.assertEqual(self.platine.boutons["Mesure"].pin.number, self.bouton_mesure)


    def test_execution_bouton_mesure(self):
        self.platine.boutons["Mesure"].is_active = True
        message = self.platine.update()

        
        self.assertEqual({0: 0, 1: 0}, message)
        self.assertIn(0, message)
        self.assertIn(1, message)
        self.assertTrue("ValeurADC" in message[0])
        self.assertTrue("Voltage" in message[1])

        self.platine.boutons["Mesure"].is_active = False

if __name__ == "__main__":
    unittest.main()