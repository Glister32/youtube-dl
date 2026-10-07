#!python
#!usr/bin/env python3
import subprocess
import os

def lancer_commande(commande: str) -> int:
	"""Lance une commande CMD et affiche sa sortie."""
	resultat = subprocess.run(
		commande,
		shell=True,
		capture_output=True,
		text=True,
		encoding="utf-8",
		errors="replace",
	)
	print(resultat.stdout, end="")
	if resultat.stderr:
		print(resultat.stderr, end="")
	return resultat.returncode

def trouver_fichiers_webm():
	result = []
	fichiers = os.listdir(".")
	for i in range(len(fichiers)):
		if ".webm" in str(fichiers[i]):
			result.append(fichiers[i])
	return result

def convertir_webm_en_mp3(fichier_webm: str) -> int:
	"""Convertit un fichier .webm en .mp3 en utilisant ffmpeg."""
	fichier_mp3 = fichier_webm.replace(".webm", ".mp3")
	commande = f"ffmpeg -i \"{fichier_webm}\" -id3v2_version 3 \"{fichier_mp3}\"" 
	return lancer_commande(commande)

if __name__ == "__main__":
	for fichier in trouver_fichiers_webm():
		convertir_webm_en_mp3(fichier)
		os.remove(fichier)
