#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:43:36 2024

@author: Kent
https://github.com/tnek747/Arbeidskrav-1 
"""

"""Basic var"""
km=10000
elbil_forsikring=5000
bensin_forsikring=7500
trafikkforsikringsavgift=8.38
kwh_km=0.2
kr_kwh=2.00
bensin_km=1.0
elbil_bom=0.1
bensin_bom=0.3


"""trafikkforsikringsavgift"""
tfa =trafikkforsikringsavgift*365

"""EV_var"""
elbil_kr_km = kwh_km * kr_kwh
elbil_total_km = km * elbil_kr_km
elbil_total_bom = km * elbil_bom

"""fossil_car_var"""
bensin_total_bensin=km*bensin_km
bensin_total_bom=bensin_bom*km

"""EV"""

elbil_årlig_kost = elbil_forsikring + elbil_total_bom + elbil_total_km + elbil_total_km + tfa
print("elbilkost pr år:")
print(elbil_årlig_kost)

"""fossil"""
bensin_årlig_kost = bensin_forsikring + bensin_total_bom + bensin_total_bensin + tfa
print("bensinbilkost pr år")
print(bensin_årlig_kost)


    
