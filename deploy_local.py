#!/usr/bin/env python3
"""
Script de déploiement local pour tester avant le push
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Échec")
        print(f"Erreur: {e.stderr}")
        return False

def main():
    """Fonction principale de test de déploiement"""
    print("🚀 Test de déploiement local - Concours ESATIC")
    
    # Vérifier que nous sommes dans le bon répertoire
    if not os.path.exists('manage.py'):
        print("❌ Erreur: manage.py non trouvé. Exécutez ce script depuis la racine du projet.")
        sys.exit(1)
    
    # Tests de pré-déploiement
    tests = [
        ("pip install -r requirements.txt", "Installation des dépendances"),
        ("python manage.py check", "Vérification de la configuration Django"),
        ("python manage.py makemigrations --check --dry-run", "Vérification des migrations"),
        ("python manage.py collectstatic --noinput", "Collecte des fichiers statiques"),
        ("python manage.py test", "Exécution des tests")
    ]
    
    success_count = 0
    for command, description in tests:
        if run_command(command, description):
            success_count += 1
    
    print(f"\n📊 Résultats: {success_count}/{len(tests)} tests réussis")
    
    if success_count == len(tests):
        print("🎉 Tous les tests sont passés ! Prêt pour le déploiement.")
        return 0
    else:
        print("⚠️  Certains tests ont échoué. Corrigez les erreurs avant le déploiement.")
        return 1

if __name__ == "__main__":
    sys.exit(main())