"""Menu principal et pied de page identiques sur toutes les pages du site.
Usage : python3 outils/seo/gabarit.py   (depuis la racine du dépôt)
Modifier MENU ou PIED ci-dessous, puis relancer : toutes les pages sont mises à jour.
Le lien de la page en cours garde aria-current="page"."""
import glob, re

MENU = [
    ("/elagage-nantes/", "Élagage"),
    ("/abattage-arbre-nantes/", "Abattage"),
    ("/taille-haie-nantes/", "Haies"),
    ("/dessouchage-nantes/", "Souches"),
    ("/tonte-entretien-jardin-nantes/", "Jardin"),
    ("/cloture-claustra-nantes/", "Clôtures"),
    ("/arbre-tombe-tempete-nantes/", "Tempête"),
    ("/conseils-jardin/", "Conseils"),
    ("/faq/", "FAQ"),
]

SERVICES = [
    ("/elagage-nantes/", "Élagage"),
    ("/abattage-arbre-nantes/", "Abattage d'arbre"),
    ("/arbre-tombe-tempete-nantes/", "Arbre tombé après tempête"),
    ("/taille-haie-nantes/", "Taille et abattage de haies"),
    ("/dessouchage-nantes/", "Enlèvement de souches"),
    ("/tonte-entretien-jardin-nantes/", "Tonte et entretien"),
    ("/creation-pelouse-nantes/", "Création de pelouse"),
    ("/terrassement-nantes/", "Terrassement et mise à niveau"),
    ("/cloture-claustra-nantes/", "Clôtures et claustras"),
]

COMMUNES = [
    ("/elagage-nantes/elagage-saint-etienne-de-montluc/", "Saint-Étienne-de-Montluc"),
    ("/elagage-nantes/elagage-coueron/", "Couëron"),
    ("/elagage-nantes/elagage-saint-herblain/", "Saint-Herblain"),
    ("/elagage-nantes/elagage-sautron/", "Sautron"),
    ("/elagage-nantes/elagage-orvault/", "Orvault"),
    ("/elagage-nantes/elagage-reze/", "Rezé"),
    ("/elagage-nantes/elagage-savenay/", "Savenay"),
    ("/elagage-nantes/elagage-vigneux-de-bretagne/", "Vigneux-de-Bretagne"),
    ("/elagage-nantes/#communes", "Toutes les communes"),
]

INFOS = [
    ("/tarifs-devis/", "Tarifs et devis"),
    ("/contact/", "Contact"),
    ("/faq/", "Questions fréquentes"),
    ("/conseils-jardin/", "Conseils jardin"),
]


def liste(liens):
    return "".join(f'<li><a href="{u}">{n}</a></li>' for u, n in liens)


def menu(courant):
    li = "".join(
        f'    <li><a href="{u}"{" aria-current=\"page\"" if u == courant else ""}>{n}</a></li>\n'
        for u, n in MENU)
    cta = ' aria-current="page"' if courant == "/tarifs-devis/" else ""
    return (f'<nav class="menu" id="menu" aria-label="Menu principal"><ul>\n{li}'
            f'    <li><a class="cta" href="/tarifs-devis/"{cta}>Estimer mon prix</a></li>\n  </ul></nav>')


PIED = f"""<footer class="site-footer"><div class="in">
  <div class="foot-cols">
    <div><h2>Nos services</h2><ul>{liste(SERVICES)}</ul></div>
    <div><h2>Élagage près de chez vous</h2><ul>{liste(COMMUNES)}</ul></div>
    <div><h2>Infos</h2><ul>{liste(INFOS)}</ul></div>
  </div>
  <div class="foot-bas">
    <span>Jean Ferret Paysage · 4 le Gendre Moreau, 44360 Saint-Étienne-de-Montluc · <a href="tel:+33610641947">06 10 64 19 47</a> · lun.-sam. 9h-19h</span>
    <span><a href="/mentions-legales/">Mentions légales</a> · <a href="/confidentialite/">Confidentialité et cookies</a> · <a href="/conditions-generales/">Conditions générales</a></span>
  </div>
</div></footer>"""


def appliquer(f):
    s = open(f, encoding="utf-8").read()
    if 'class="site-footer"' not in s:
        return False
    m = re.search(r'<nav class="menu".*?</nav>', s, re.S)
    courant = None
    if m:
        c = re.search(r'href="([^"]+)"[^>]*aria-current="page"', m.group(0))
        courant = c.group(1) if c else None
        s = s.replace(m.group(0), menu(courant), 1)
    s = re.sub(r'<footer class="site-footer">.*?</footer>', lambda _: PIED, s, count=1, flags=re.S)
    old = open(f, encoding="utf-8").read()
    if s != old:
        open(f, "w", encoding="utf-8").write(s)
        return True
    return False


if __name__ == "__main__":
    n = 0
    for f in sorted(glob.glob("site/**/*.html", recursive=True) + glob.glob("site/**/*.php", recursive=True)):
        n += appliquer(f)
    print(n, "pages mises à jour (menu et pied de page)")
