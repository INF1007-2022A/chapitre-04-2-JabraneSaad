#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	PremierPrénom = name[:name.find("-")]
	return PremierPrénom.title()

def get_random_sentence(animals, adjectives, fruits):
	return f"Aujourd’hui,j’ai vu un {animals[random.randrange(0, len(animals)-1)]} s’emparer d’un panier {adjectives[random.randrange(0, len(adjectives)-1)]} plein de {fruits[random.randrange(0, len(fruits)-1)]}"

def encrypt(text, shift):
	new_text = []
	for letter in text.upper():
		if letter.isalpha():
			new_text.append(chr((ord(letter) % 90) + 65))
		else :
			new_text.append(letter)

	return new_text

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
