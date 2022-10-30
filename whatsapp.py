import os
from os import startfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pyautogui import click
from keyboard import press
from keyboard import write
import time

def whatsappmsg(name,message):

    os.startfile("C:/Users/DELL/AppData/Local/WhatsApp/WhatsApp.exe")

    time.sleep(20)
    click(x=211, y=140)
    time.sleep(5)
    write(name)
    time.sleep(5)
    click(x=142, y=285)
    time.sleep(1)
    click(x=792, y=992)
    time.sleep(5)
    write(message)
    press('enter')

def whatsappcall(name):
    os.startfile("C:/Users/DELL/AppData/Local/WhatsApp/WhatsApp.exe")

    time.sleep(20)
    click(x=211, y=140)
    time.sleep(5)
    write(name)
    time.sleep(5)
    click(x=142, y=285)
    time.sleep(1)
    click(x=792, y=992)
    time.sleep(5)
    click(x=1728, y=58)

def whatsappvideocall(name):

    os.startfile("C:/Users/DELL/AppData/Local/WhatsApp/WhatsApp.exe")

    time.sleep(20)
    click(x=211, y=140)
    time.sleep(5)
    write(name)
    time.sleep(5)
    click(x=142, y=285)
    time.sleep(1)
    click(x=792, y=992)
    time.sleep(5)
    click(x=1665, y=66)

def whatsappchat(name):

    os.startfile("C:/Users/DELL/AppData/Local/WhatsApp/WhatsApp.exe")

    time.sleep(20)
    click(x=211, y=140)
    time.sleep(5)
    write(name)
    time.sleep(5)
    click(x=142, y=285)
    time.sleep(1)
    click(x=792, y=992)
    time.sleep(5)







