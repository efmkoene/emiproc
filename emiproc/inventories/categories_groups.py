"""Mappings to regroup categories together."""
ZH_2_GNFR = {
    # PublicPower
    "GNFR_A": [
        "c2201_BHKW_Emissionen_Kanton",
        "c2301_KHKWKehricht_Emissionen_Kanton",
        "c2302_KHKWErdgas_Emissionen_Kanton",
        "c2303_KHKWHeizoel_Emissionen_Kanton",
    ],
    # Industry
    "GNFR_B": [
        "c3201_Notstromanlagen_Emissionen_Kanton",
        "c3301_Prozessenergie_Emissionen_Kanton",
        "c3401_Metallreinigung_Emissionen_Kanton",
        "c3402_Holzbearbeitung_Emissionen_Kanton",
        "c3403_Malereien_Emissionen_Kanton",
        "c3404_Textilreinigung_Emissionen_Kanton",
        "c3405_Karosserien_Emissionen_Kanton",
        "c3406_Raeuchereien_Emissionen_Kanton",
        "c3407_Roestereien_Emissionen_Kanton",
        "c3408_Druckereien_Emissionen_Kanton",
        "c3409_Laboratorien_Emissionen_Kanton",
        "c3410_Bierbrauereien_Emissionen_Kanton",
        "c3411_Brotproduktion_Emissionen_Kanton",
        "c3412_MedizinischePraxen_Emissionen_Kanton",
        "c3413_Gesundheitswesen_Emissionen_Kanton",
    ],
    # Other stationary combustion (services, residential, agriculture)
    "GNFR_C": [
        "c2101_Oelheizungen_Emissionen_Kanton",
        "c2102_Gasheizungen_Emissionen_Kanton",
        "c2103_HolzheizungenLokalisiert_Emissionen_Kanton",
        "c2104_HolzheizungenDispers_Emissionen_Kanton",
        "c2105_Warmwassererzeuger_Emissionen_Kanton",
    ],
    # Fugitives
    "GNFR_D": [
        "c3416_Tankstellen_Emissionen_Kanton",
    ],
    # Solvents and product use
    "GNFR_E": [
        "c3417_LoesemittelIG_Emissionen_Kanton",
        "c5101_LoesemittelHH_Emissionen_Kanton",
    ],
    # Road transport
    "GNFR_F": [
        "c1301_Personenwagen_Emissionen_Kanton",
        "c1302_Lastwagen_Emissionen_Kanton",
        "c1303_Motorraeder_Emissionen_Kanton",
        "c1304_Linienbusse_Emissionen_Kanton",
        "c1305_Trolleybusse_Emissionen_Kanton",
        "c1306_StartStopTankatmung_Emissionen_Kanton",
        "c1307_Lieferwagen_Emissionen_Kanton",
        "c1308_Reisebusse_Emissionen_Kanton",
    ],
    # Shipping
    "GNFR_G": [
        "c1101_Linienschiffe_Emissionen_Kanton",
        "c1102_PrivaterBootsverkehr_Emissionen_Kanton",
    ],
    # Offroad mobility
    "GNFR_I": [
        "c1201_BahnPersonenverkehr_Emissionen_Kanton",
        "c1202_BahnGueterverkehr_Emissionen_Kanton",
        "c1203_Tramverkehr_Emissionen_Kanton",
        "c1204_Kleinbahnen_Emissionen_Kanton",
        # c31xx are construction stuff
        "c3101_MaschinenHochbau_Emissionen_Kanton",
        "c3102_Bitumen_Emissionen_Kanton",
        "c3103_FarbenBaustelle_Emissionen_Kanton",
        "c3104_MaschinenTiefbau_Emissionen_Kanton",
        "c3105_Strassenbelag_Emissionen_Kanton",
        "c3419_IndustrielleFZ_Emissionen_Kanton",
        "c4101_ForstwirtschaftlicheFZ_Emissionen_Kanton",
        "c4201_LandwirtschaftlicheFZ_Emissionen_Kanton",
    ],
    # Waste
    "GNFR_J": [
        "c2401_Klaerschlammverwertung_Emissionen_Kanton",
        "c3418_Vergaerwerk_Emissionen_Kanton",
        "c3414_Krematorium_Emissionen_Kanton",
        "c5201_Gruenabfallverbrennung_Emissionen_Kanton",
        "c5301_HolzoefenKleingarten_Emissionen_Kanton",
        "c5401_AbfallverbrennungHaus_Emissionen_Kanton",
    ],
    # AgriLivestock
    "GNFR_K": [
        "c4401_Nutztierhaltung_Emissionen_Kanton",
    ],
    # AgriOther
    "GNFR_L": [
        "c4301_Nutzflaechen_Emissionen_Kanton",
    ],
    # Others
    "GNFR_R": [
        "c5501_HausZooZirkustiere_Emissionen_Kanton",
        "c5601_Feuerwerke_Emissionen_Kanton",
        "c5701_Tabakwaren_Emissionen_Kanton",
        "c5801_BrandFeuerschaeden_Emissionen_Kanton",
        "c6101_Waelder_Emissionen_Kanton",
        "c6201_Grasflaechen_Emissionen_Kanton",
        "c6301_Gewaesser_Emissionen_Kanton",
        "c6401_Blitze_Emissionen_Kanton",
    ],
}

CH_2_GNFR = {
    # PublicPower
    "GNFR_A": [
        # Waste incinerator we agreed on nov. 22 to put them in the public power category
        "eipkv",  # Punktquellen KVA (Kehrichtverbrennungsanlagen ) == Waste incinerators
    ],
    # Industry
    "GNFR_B": [
        "eipro",
        "eipwp",  # this is the weitere punktquelle (additional point sources)
        "eipzm",
    ],
    # Other stationary combustion (services, residential, agriculture)
    "GNFR_C": [
        "ehare",
        "ehfho",
        "ehfoe",
        "ehgws",
        "eipdh",
        "eiprd",
        "elfeu",
    ],
    # Fugitives
    "GNRF_D": [
        "eilgk",
        "eivgn",
        "evklm",
        "evtrk",
    ],
    # Solvents and product use
    "GNFR_E": [
        "eilmi",  # Lösungsmittel Industrie
        "ehlmk", # Lösungsmittel Konsumprodukte
    ],
    # Road transport
    "GNFR_F": [
        # "evstr_ch4",
        # "evstr_co",
        # "evstr_co2",
        # "evstr_n2o",
        # "evstr_nh3",
        # "evstr_nmvoc",
        # "evstr_nox",
        # "evstr_so2",
        "evstr",
        "evzon",
    ],
    # Shipping
    "GNFR_G": [
        "evsee",
        "evsfa",
        "evsrh",
    ],
    # Aviation
    "GNFR_H": [
        "evfgva",
        "evfzhr",
    ],
    # Offroad mobility
    "GNFR_I": [
        "ehmgh",
        "eibau",
        "eifrz",
        "eilpf",
        "eipis",
        "elfwm",
        "ellwm",
        "evsch",
        "evsra",
    ],
    # Waste
    "GNFR_J": [
        "eidep",
        "eikla",
        "eikmp",
        "elabf",
        "elver",
    ],
    # AgriLivestock
    "GNFR_K": [
        "elapp",
        "elsto",
    ],
    #  AgriOther
    "GNFR_L": [
        "elfer",
    ],
    # Others
    "GNFR_R": [
        "ehhab",
        "ehhaf",
        "ehhan",
        "enwal",
    ],
}


TNO_2_GNFR = {
    # PublicPower
    "GNFR_A": [
        "A",
    ],
    # Industry
    "GNFR_B": [
        "B",
    ],
    # Other stationary combustion (services, residential, agriculture)
    "GNFR_C": [
        "C",
    ],
    # Fugitives
    "GNFR_D": [
        "D",
    ],
    # Road transport
    "GNFR_F": [
        "F1",
        "F2",
        "F3",
        "F4",
    ],
    # Shipping
    "GNFR_G": [
        "G",
    ],
    # Aviation
    "GNFR_H": [
        "H",
    ],
    # Offroad mobility
    "GNFR_I": [
        "I",
    ],
    # Waste
    "GNFR_J": [
        "J",
    ],
    # AgriLivestock
    "GNFR_K": [
        "K",
    ],
    # AgriOther
    "GNFR_L": [
        "L",
    ],
    # Others
    "GNFR_R": [
        "E",  # E is not in the zh or swiss to we set e to that
    ],
}
