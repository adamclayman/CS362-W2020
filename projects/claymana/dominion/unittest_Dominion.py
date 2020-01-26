from unittest import TestCase
import testUtility
import Dominion


class TestCard(TestCase):
    def setUp(self):
        # Data setup
        self.players = testUtility.GetPlayers()
        self.nV = testUtility.GetVictoryCards(self.players)
        self.nC = testUtility.GetCurses(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        # Pick n cards from the box to be in the supply
        self.supply = testUtility.GetSupply(self.box, 5, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player("Annie")

    def test_init(self):
        self.setUp()
        cost = 1
        buypower = 5

        # instantiate the Card object
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        # verify that the class variables have the expected values
        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        pass
