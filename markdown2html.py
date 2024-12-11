#!/usr/bin/env python3
import sys
import os

def main():
    # Vérification du nombre d'arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Récupération des noms de fichiers
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérification de l'existence du fichier Markdown
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Si tout est correct, aucune sortie supplémentaire et succès
    sys.exit(0)

if __name__ == "__main__":
    main()
