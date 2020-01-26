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


class TestAction_card(TestCase):
    def setUp(self):
        # Data setup
        self.players = testUtility.GetPlayers()
        self.nV = testUtility.GetVictoryCards(self.players)
        self.nC = testUtility.GetCurses(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        # Pick n cards from the box to be in the supply
        self.supply = testUtility.GetSupply(self.box, 10, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player("Annie")
        self.player.actions = 1
        self.player.buys = 1
        self.player.purse = 0

    def test_init(self):
        self.setUp()
        cost = 4
        actions = 2
        cards = 2
        buys = 2
        coins = 2

        # instantiate the Action Card object and add card into player hand
        self.card = Dominion.Action_card(self.player.name, cost, actions, cards, buys, coins)

        # verify that the class variables have the expected values
        self.assertEqual('Annie', self.card.name)
        self.assertEqual("action", self.card.category)
        self.assertEqual(cost, self.card.cost)
        self.assertEqual(actions, self.card.actions)
        self.assertEqual(cards, self.card.cards)
        self.assertEqual(buys, self.card.buys)
        self.assertEqual(coins, self.card.coins)

    def test_use(self):
        self.test_init()
        prior_hand = self.player.hand
        self.player.hand.append(self.card)
        self.card.use(self.player, self.trash)
        self.assertEqual(self.player.played[-1], self.card)
        self.assertEqual(self.player.hand, prior_hand)

    def test_augment(self):
        self.test_init()
        self.card.augment(self.player)
        self.assertEqual(self.player.actions, 3)
        self.assertEqual(self.player.buys, 3)
        self.assertEqual(self.player.purse, 2)
        self.assertEqual(len(self.player.hand), 7)

class TestPlayer(TestCase):
    def setUp(self):
        # Data setup
        self.players = testUtility.GetPlayers()
        self.nV = testUtility.GetVictoryCards(self.players)
        self.nC = testUtility.GetCurses(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        # Pick n cards from the box to be in the supply
        self.supply = testUtility.GetSupply(self.box, 10, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player("Annie")

    def test_init(self):
        self.setUp()
        cost = 3
        actions = 2
        cards = 0
        buys = 0
        coins = 0

        # instantiate the Action Card object and add card into player hand
        self.card = Dominion.Action_card(self.player.name, cost, actions, cards, buys, coins)

        # verify that the class variables have the expected values
        self.assertEqual('Annie', self.card.name)
        self.assertEqual("action", self.card.category)
        self.assertEqual(cost, self.card.cost)
        self.assertEqual(actions, self.card.actions)
        self.assertEqual(cards, self.card.cards)
        self.assertEqual(buys, self.card.buys)
        self.assertEqual(coins, self.card.coins)

    def test_draw(self):
        self.test_init()
        len_prior_hand = len(self.player.hand)
        self.player.draw()
        self.assertEqual(len(self.player.hand), len_prior_hand + 1)

    def test_action_balance(self):
        self.test_init()
        self.player.hand.append(self.card)
        self.assertEqual(self.player.action_balance(), 70*1/11)
        self.player.hand.append(self.card)
        self.assertEqual(self.player.action_balance(), 70*2/12)

    def test_cardsummary(self):
        self.test_init()
        self.assertEqual(self.player.cardsummary(), {'Copper': 7, 'Estate': 3, 'VICTORY POINTS': 3})
        self.player.hand.append(self.card)
        self.assertEqual(self.player.cardsummary(), {'Copper': 7, 'Estate': 3, 'Annie': 1, 'VICTORY POINTS': 3})


    def test_calcpoints(self):
        self.test_init()
        self.assertEqual(self.player.calcpoints(), 3)
        garden = Dominion.Gardens()
        self.player.hand.append(garden)
        self.assertEqual(self.player.calcpoints(), 4)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.player.hand.append(garden)
        self.assertEqual(self.player.calcpoints(), 3 + 20)
