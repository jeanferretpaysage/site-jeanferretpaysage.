"""Ajoute les balises de partage (Open Graph) aux pages qui n'en ont pas.
Usage : python3 outils/seo/og.py   (depuis la racine du dépôt)"""
import re, glob, html
BASE = "https://jeanferretpaysage.fr"
DEFAULT_IMG = BASE + "/img/elagage-platanes-elagueurs-grimpeurs.webp"
for f in glob.glob("site/**/index.html", recursive=True):
    s = open(f, encoding="utf-8").read()
    if 'property="og:title"' in s or 'name="robots" content="noindex"' in s:
        continue
    t = re.search(r"<title>(.*?)</title>", s).group(1)
    d = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
    u = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    m = re.search(r'<main>.*?<img src="/?(img/[^"]+)"', s, re.S)
    img = BASE + "/" + m.group(1) if m else DEFAULT_IMG
    typ = "article" if "/conseils-jardin/" in u and not u.endswith("/conseils-jardin/") else "website"
    tags = (f'<meta property="og:type" content="{typ}">\n'
            f'<meta property="og:site_name" content="Jean Ferret Paysage">\n'
            f'<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n'
            f'<meta property="og:url" content="{u}">\n'
            f'<meta property="og:image" content="{img}">\n'
            f'<meta property="og:locale" content="fr_FR">\n')
    s = s.replace(m0 := re.search(r'<link rel="canonical"[^>]*>\n', s).group(0), m0 + tags, 1)
    open(f, "w", encoding="utf-8").write(s)
    print("OG ajouté :", f)
