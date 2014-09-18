""" 	File: Player.py
	Author: Brian Mansfield
	This file represents the player object, which defines player
	state and behavior.

"""

health = 100
coins = 0
upgrades = []
invincible = false;

print health

def decrementPlayerHealth(amountToDecrement):
	health -= amountToDecrement

def incrementPlayerHealth(amountToIncrement):
	health += amountToIncrement

def becomeInvincible():
	invincible = true
