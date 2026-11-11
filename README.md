# Site Jean Ferret Paysage

Site de jeanferretpaysage.fr (élagage, abattage, haies, jardin autour de Nantes).

- `site/` : les fichiers du site, tels qu'ils sont en ligne.
- Chaque modification de `site/` est envoyée automatiquement sur Ionos (dossier `/site`) par `.github/workflows/mise-en-ligne.yml`.
- Les accès SFTP Ionos sont dans les secrets du dépôt, jamais dans les fichiers.
