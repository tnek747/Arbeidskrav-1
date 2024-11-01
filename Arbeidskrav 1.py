#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:43:36 2024

@author: Kent KoKe
"""
""" Grunnvariabler"""
km=10000
elbil_forsikring=5000
bensin_forsikring=7500
kwh_km=0.2
kr_kwh=2.00
bensin_km=1.0
elbil_bom=0.1
bensin_bom=0.3

"""Ellbil variabler"""
elbil_kr_km = kwh_km * kr_kwh
elbil_total_km = km * elbil_kr_km
elbil_total_bom = km * elbil_bom

"""bensinbilvariabler"""
bensin_total_bensin=km*bensin_km
bensin_total_bom=bensin_bom*km

"""elbil"""

elbil_årlig_kost = elbil_forsikring + elbil_total_bom + elbil_total_km + elbil_total_km
print("elbilkost pr år:")
print(elbil_årlig_kost)

"""bensin"""
bensin_årlig_kost = bensin_forsikring + bensin_total_bom + bensin_total_bensin
print("bensinkost pr år")
print(bensin_årlig_kost)
