# Scrap Email

Ce projet permet d'extraire des adresses email depuis des sites web, de nettoyer ces adresses puis d'envoyer des emails de prospection.

## Nettoyage des emails

Le script `clean_emails.py` possède une fonction `clean_email` qui retire les numéros de téléphone ou autres caractères parasites pouvant précéder ou suivre l'adresse.

Pour nettoyer un fichier CSV contenant une colonne `emails` :

```bash
python clean_emails.py --input chemin/vers/fichier.csv --output resultat.csv
```

## Tests

Des tests unitaires vérifient la fonction de nettoyage. Ils s'exécutent avec `pytest` :

```bash
pytest
```
