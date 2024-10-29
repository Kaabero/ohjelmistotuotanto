import unittest
from statistics_service import StatisticsService
from statistics_service import SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
         
        )
        


    def test_pelaajan_haku_palauttaa_oikean_pelaajan(self):
        pelaaja = self.stats.search("Semenko")

        self.assertAlmostEqual(pelaaja.name, "Semenko")
    
    def test_olemattoman_pelaajan_haku_palauttaa_oikean_pelaajan(self):
        pelaaja = self.stats.search("Samenko")

        self.assertIsNone(pelaaja)

    def test_tiimin_haku_palauttaa_listan_tiimista(self):
        tiimi = self.stats.team("EDM")

        self.assertAlmostEqual(len(tiimi), 3)

    def test_top_points_haku_palauttaa_oikeanlaisen_listan(self):
        lista = self.stats.top(2, SortBy.POINTS)
        topkolme=[]

        for pelaaja in lista:
            topkolme.append(pelaaja.name)


        self.assertEqual(topkolme, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_goals_haku_palauttaa_oikeanlaisen_listan(self):
        lista = self.stats.top(2, SortBy.GOALS)
        topkolme=[]

        for pelaaja in lista:
            topkolme.append(pelaaja.name)


        self.assertEqual(topkolme, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_assists_haku_palauttaa_oikeanlaisen_listan(self):
        lista = self.stats.top(2, SortBy.ASSISTS)
        topkolme=[]

        for pelaaja in lista:
            topkolme.append(pelaaja.name)


        self.assertEqual(topkolme, ["Gretzky", "Yzerman", "Lemieux"])

    
   