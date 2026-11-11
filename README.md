# Site Jean Ferret Paysage

Site de jeanferretpaysage.fr (élagage, abattage, haies, jardin autour de Nantes).

- `site/` : les fichiers du site, tels qu'ils sont en ligne.
- `outils/maj.php` : copie du script installé chez Ionos dans `/mise-a-jour/`. Une tâche cron Ionos le lance toutes les heures : il télécharge ce dépôt et copie `site/` dans le dossier `/site` de l'hébergement (sans rien supprimer).
- Aucun mot de passe dans ce dépôt.
- `outils/pages/` : pages du blog « Conseils jardin » (`blog.py`) et pages villes haie / abattage (`villes.py`). Après une modification : `python3 outils/pages/gen.py` (régénère les pages, les balises de partage et le sitemap).
- `outils/seo/og.py` (balises de partage manquantes) et `outils/seo/sitemap.py` (sitemap à partir des pages indexables).
