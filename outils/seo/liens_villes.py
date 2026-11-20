"""Liens vers les pages « service + commune » depuis les pages mères et les pages élagage.
Usage : python3 outils/seo/liens_villes.py   (lancé aussi par outils/pages/gen.py)

- pages mères (haie, abattage, souches, tonte, clôture, terrassement) : liste des communes
  qui ont une page pour ce service ;
- pages élagage de chaque commune : la phrase « on fait aussi » pointe vers les pages
  locales quand elles existent, sinon vers la page mère.
Ne fait rien si tout est déjà à jour."""
import os, re, sys

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(RACINE, "outils", "pages"))
from villes import VILLES, SERVICES, a  # noqa: E402

SITE = os.path.join(RACINE, "site")
ORDRE = list(VILLES)  # Saint-Étienne-de-Montluc d'abord, puis les voisines


def existe(service, slug):
    base, _, prefixe, _, _ = SERVICES[service]
    return os.path.exists(os.path.join(SITE, f"{base}{prefixe}{slug}".strip("/"), "index.html"))


def ecrit(f, s):
    old = open(f, encoding="utf-8").read()
    if s != old:
        open(f, "w", encoding="utf-8").write(s)
        return 1
    return 0


n = 0
# 1) pages mères
TITRES = {"haie": "Taille de haies près de chez vous", "abattage": "Abattage près de chez vous",
          "souche": "Enlèvement de souches près de chez vous", "tonte": "Tonte et entretien près de chez vous",
          "cloture": "Pose de clôture près de chez vous", "terrassement": "Terrassement près de chez vous"}
for service, titre in TITRES.items():
    base, _, prefixe, _, _ = SERVICES[service]
    communes = [v for v in ORDRE if existe(service, v)]
    if not communes:
        continue
    lis = "".join(f'<li><a href="{base}{prefixe}{v}/">{VILLES[v][0]}</a></li>' for v in communes)
    bloc = (f'<!-- villes -->\n    <h2>{titre}</h2>\n    <ul class="towns">{lis}</ul>\n'
            f'    <p>Votre commune n\'est pas dans la liste ? On intervient dans un rayon de 30 km autour de Nantes : '
            f'<a href="/tarifs-devis/">demandez votre devis</a>.</p>\n    <!-- /villes -->')
    f = os.path.join(SITE, base.strip("/"), "index.html")
    s = open(f, encoding="utf-8").read()
    if "<!-- villes -->" in s:
        s = re.sub(r"<!-- villes -->.*?<!-- /villes -->", lambda _: bloc, s, count=1, flags=re.S)
    else:
        # ancienne liste (haie, abattage) : h2 « … près de chez vous » + ul.links
        m = re.search(r'<h2>[^<]*près de chez vous</h2>\s*<ul class="links">.*?</ul>', s, re.S)
        if m:
            s = s.replace(m.group(0), bloc, 1)
        else:
            s = s.replace("    <h2>Questions fréquentes</h2>", "    " + bloc + "\n\n    <h2>Questions fréquentes</h2>", 1)
    n += ecrit(f, s)

# 2) pages élagage des communes : « on fait aussi »
for v in ORDRE:
    f = os.path.join(SITE, "elagage-nantes", f"elagage-{v}", "index.html")
    if not os.path.exists(f):
        continue
    def lien(service, local, general):
        base, _, prefixe, _, _ = SERVICES[service]
        if existe(service, v):
            return f'<a href="{base}{prefixe}{v}/">{local} {a(v)}</a>'
        return f'<a href="{base}">{general}</a>'
    liens = ", ".join([
        '<a href="/elagage-nantes/">Élagage</a>',
        lien("abattage", "abattage", "abattage"),
        lien("haie", "taille de haies", "taille et abattage de haies"),
        lien("souche", "enlèvement des souches", "enlèvement des souches"),
        lien("tonte", "tonte et entretien", "tonte et entretien"),
        lien("cloture", "clôtures et claustras", "clôtures et claustras"),
    ])
    if existe("terrassement", v):
        liens += ", " + lien("terrassement", "terrassement", "terrassement")
    s = open(f, encoding="utf-8").read()
    s = re.sub(r"(on fait aussi : ).*?\.</p>", lambda m: m.group(1) + liens + ".</p>", s, count=1)
    n += ecrit(f, s)

print(n, "pages mises à jour (liens vers les pages communes)")
