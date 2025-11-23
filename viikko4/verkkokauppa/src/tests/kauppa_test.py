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

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()
        
        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
    # tehdään toteutus saldo-metodille
    def varasto_saldo(self,tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 15
            if tuote_id == 3:
                return 0

    # tehdään toteutus hae_tuote-metodille
    def varasto_hae_tuote(self,tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 10)
            if tuote_id == 3:
                return Tuote(3, "kananmuna", 7)
        
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
        
    def test_kutsutaan_pankkia_oikealla_tilinumerolla_ja_summalla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
        
    def test_kutsutaan_pankkia_oikealla_tilinumerolla_ja_summalla_kahdella_eri_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.lisaa_koriin(2) 
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 15)
        
    def test_kutsutaan_pankkia_oikealla_tilinumerolla_ja_summalla_kahdella_samalla_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2) 
        self.kauppa.lisaa_koriin(2) 
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 20)
    
    def test_kun_toinen_tuote_on_loppu_saldoon_perustuva_hinta_toimii(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.lisaa_koriin(3) 
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
    
    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2) 
        self.kauppa.tilimaksu("matti", "54321")
        
        self.pankki_mock.tilisiirto.assert_called_with("matti", ANY, "54321", ANY, 10)
    
    def test_jokaiselle_maksulle_pyydetaan_uusi_viite(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.viitegeneraattori_mock.uusi.assert_called()
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2) 
        self.kauppa.tilimaksu("matti", "54321")
        
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)
    
    def test_tuotteen_poistaminen_toimii(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.lisaa_koriin(2) 
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 10)