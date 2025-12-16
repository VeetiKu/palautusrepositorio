from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def luo_peli(valinta: str):
    pelit = {
        "a": KPSPelaajaVsPelaaja,
        "b": KPSTekoaly,
        "c": KPSParempiTekoaly,
    }

    luokka = pelit.get(valinta)
    return luokka() if luokka else None