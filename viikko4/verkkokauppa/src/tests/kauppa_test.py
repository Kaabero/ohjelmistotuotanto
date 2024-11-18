import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
    

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_ja_summalla(self):

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

  
        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 5)

    def test_ostettaessa_kahta_eri_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_ja_summalla(self):

        varasto_mock = Mock()


        varasto_mock.saldo.side_effect = [10,12]
        varasto_mock.hae_tuote.side_effect = [Tuote(1, "maito", 5), Tuote(2, "mehu", 6)]

        kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

  
        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 11)

    def test_ostettaessa_kaksi_samaa_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_ja_summalla(self):


        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

  
        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 10)

    def test_yrittaessa_ostaa_varastossa_oleva_tuote_ja_loppu_oleva_tuote_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_ja_summalla(self):
 
        varasto_mock = Mock()

        varasto_mock.saldo.side_effect = [10, 0]
        varasto_mock.hae_tuote.side_effect = [Tuote(1, "maito", 5), Tuote(2, "mehu", 5)]

        kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

  
        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 5)

    def test_uusi_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
 
        varasto_mock = Mock()

        varasto_mock.saldo.side_effect = [10, 10, 10, 10]
        varasto_mock.hae_tuote.side_effect = [Tuote(1, "maito", 5), Tuote(2, "mehu", 5), Tuote(2, "banaani", 10), Tuote(2, "suklaa", 10)]

        kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

  
        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 10)

        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(3)
        kauppa.lisaa_koriin(4)
        kauppa.tilimaksu("risto", "56789")

        self.pankki_mock.tilisiirto.assert_called_with("risto", 42, "56789", kauppa._kaupan_tili, 20)
    
    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):

        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
 
        varasto_mock = Mock()

        varasto_mock.saldo.side_effect = [10, 10, 10, 10]
        varasto_mock.hae_tuote.side_effect = [Tuote(1, "maito", 5), Tuote(2, "mehu", 5), Tuote(2, "banaani", 10), Tuote(2, "suklaa", 10)]

        kauppa = Kauppa(varasto_mock, self.pankki_mock, viitegeneraattori_mock)

  
        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("risto", "56789")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)

        kauppa.aloita_asiointi()
  
        kauppa.lisaa_koriin(4)
        kauppa.tilimaksu("matti", "13579")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 3)

    def test_ostoskorista_poistetun_tuotteen_hinta_ei_tule_mukaan_maksutapahtumaan(self):
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "mehu", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)

        kauppa.poista_korista(1)

        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 5)

        

   
