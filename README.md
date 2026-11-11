# Site Jean Ferret Paysage

Site de jeanferretpaysage.fr (élagage, abattage, haies, jardin autour de Nantes).

- `site/` : les fichiers du site, tels qu'ils sont en ligne.
- `outils/maj.php` : copie du script installé chez Ionos dans `/mise-a-jour/`. Une tâche cron Ionos le lance toutes les heures : il télécharge ce dépôt et copie `site/` dans le dossier `/site` de l'hébergement (sans rien supprimer).
- Aucun mot de passe dans ce dépôt.
