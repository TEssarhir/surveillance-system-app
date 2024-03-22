# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:40:33 2020

@author: chevrier6
"""
from bitManip import *
from easymodbus.modbusClient import ModbusClient
from easymodbus.modbusClient import convert_registers_to_float


class AutomateException(Exception):
    def __init__(self, message):
        self.message = message


class Armoire5():
    # ici les adresse des mesure commence  a ZERO (pas UN comme en java)

    def __init__(self):
        self.nbCharge = 7  # de 0 a 6
        self.ipAdresse = "100.75.155.115"
        self.adresseMesure = 2
        self.adresseTOR = 32000
        self.adresseMesureSecteur1 = 7  # attention  vraie adresse ()
        self.adresseMesureSecteur2 = 8  # attention  vraie adresse

        self.debutAdrCharge = 9
        self.debutAdrSource = 0

    def okCharge(self, i):
        return 0 <= i <= self.nbCharge - 1 ###########♦ MODIF

    def resetAll(self):
        self.writeTOR(0)

    def resetSource(self):
        for i in range(self.nbCharge):
            self.setSource1(i)

    def resetCharge(self):
        for i in range(self.nbCharge):
            self.unsetCharge(i)

    def setCharge(self, charge: int):
        if not self.okCharge(charge):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        val = self.readTOR()
        val = setBit(val, charge + self.debutAdrCharge)
        self.writeTOR(val)

    def unsetCharge(self, charge):
        if not self.okCharge(charge):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        val = self.readTOR()
        val = clearBit(val, charge + self.debutAdrCharge)
        self.writeTOR(val)

    def toggleCharge(self, charge):
        if not self.okCharge(charge):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        val = self.readTOR()
        val = toggleBit(val, charge + self.debutAdrCharge)
        self.writeTOR(val)

    def setSource1(self, charge):
        if not self.okCharge(charge):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        val = self.readTOR()
        val = clearBit(val, charge + self.debutAdrSource)
        self.writeTOR(val)

    def setSource2(self, charge):
        if not self.okCharge(charge):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        val = self.readTOR()
        val = setBit(val, charge + self.debutAdrSource)
        self.writeTOR(val)

    def togglesource(self, charge):
        if not self.okCharge(charge):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        val = self.readTOR()
        val = toggleBit(val, charge + self.debutAdrSource)
        self.writeTOR(val)

    ################################

    def writeTOR(self, val):
        modbusclient = ModbusClient(self.ipAdresse, 502)
        modbusclient.connect()
        modbusclient.write_single_register(self.adresseTOR, val)
        modbusclient.close()
        # some tempo to wait measure to stabilize
        from time import sleep
        sleep(2.)

    def readTOR(self):
        modbusclient = ModbusClient(self.ipAdresse, 502)
        modbusclient.connect()
        inputRegisters = modbusclient.read_inputregisters(self.adresseTOR, 1)
        modbusclient.close()
        return (int)(inputRegisters[0])

    ###############################################
    def readSecteur1(self):
        addr = self.adresseMesure + (self.adresseMesureSecteur1) * 8
        return self.lireValeurAdresse(addr + 2), self.lireValeurAdresse(addr), self.lireValeurAdresse(
            addr + 4), self.lireValeurAdresse(addr + 6)

    def readSecteur2(self):
        addr = self.adresseMesure + (self.adresseMesureSecteur2) * 8
        return self.lireValeurAdresse(addr + 2), self.lireValeurAdresse(addr), self.lireValeurAdresse(
            addr + 4), self.lireValeurAdresse(addr + 6)

    def readMesureCourant(self, source: int):
        if not self.okCharge(source):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        return self.lireValeur(source, 0)

    def readMesureTension(self, source: int):
        if not self.okCharge(source):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        return self.lireValeur(source, 2)

    def readMesurePactive(self, source: int):
        if not self.okCharge(source):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        return self.lireValeur(source, 4)

    def readMesurePreactive(self, source: int):
        if not self.okCharge(source):
            raise AutomateException("numero charge pas compris entre 0 et 6")
        return self.lireValeur(source, 6)

    def readMesure(self, source):
        return self.readMesureTension(source), self.readMesureCourant(source), self.readMesurePactive(
            source), self.readMesurePreactive(source)

    def lireValeur(self, source, offset):

        addr = self.adresseMesure + (source) * 8 + offset
        return self.lireValeurAdresse(addr)

    def lireValeurAdresse(self, addr):

        modbusclient = ModbusClient(self.ipAdresse, 502)
        modbusclient.connect()
        data = modbusclient.read_holdingregisters(addr, 2)
        modbusclient.close()
        res = convert_registers_to_float(data)

        return res[0]

