"""Génère la page /contact/.

Usage (depuis la racine du dépôt) :
    python3 outils/pages/contact.py

Le haut et le bas de page viennent de la page FAQ (comme gen.py).
Le NAP (nom, adresse, téléphone) doit rester identique à celui de l'accueil.
"""
import json, os, re, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", ".."))
SITE = os.path.join(RACINE, "site")
BASE = "https://jeanferretpaysage.fr"
CSS_V = "20261112a"

modele = open(os.path.join(SITE, "faq", "index.html"), encoding="utf-8").read()
HAUT = re.search(r'<div class="topbar">.*?</header>\n', modele, re.S).group(0)
HAUT = HAUT.replace(' aria-current="page"', "")
BAS = re.search(r"</main>\n.*", modele, re.S).group(0)

TITLE = "Contact élagueur Nantes · Jean Ferret Paysage"
DESC = ("Joindre Jean Ferret, élagueur à Saint-Étienne-de-Montluc : 06 10 64 19 47, "
        "du lundi au samedi 9h-19h. Devis gratuit sur photo, Nantes et 30 km autour.")
URL = BASE + "/contact/"

ENTREPRISE = {
    "@type": "LocalBusiness",
    "@id": BASE + "/#entreprise",
    "name": "Jean Ferret Paysage",
    "url": BASE + "/",
    "logo": BASE + "/img/logo-512.png",
    "image": BASE + "/img/elagage-platanes-elagueurs-grimpeurs.webp",
    "telephone": "+33610641947",
    "address": {"@type": "PostalAddress", "streetAddress": "4 le Gendre Moreau", "postalCode": "44360",
                "addressLocality": "Saint-Étienne-de-Montluc", "addressCountry": "FR"},
    "geo": {"@type": "GeoCoordinates", "latitude": 47.276, "longitude": -1.781},
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "opens": "09:00", "closes": "19:00"}],
    "areaServed": [{"@type": "GeoCircle",
                    "geoMidpoint": {"@type": "GeoCoordinates", "latitude": 47.218, "longitude": -1.553},
                    "geoRadius": "30000"}],
    "contactPoint": {"@type": "ContactPoint", "telephone": "+33610641947", "contactType": "customer service",
                     "areaServed": "FR", "availableLanguage": "French"},
}

FAQ = [
    ("Quel est le moyen le plus rapide pour avoir un prix ?",
     "Envoyer une photo du chantier avec le formulaire ci-dessus ou sur la page "
     "<a href=\"/tarifs-devis/\">Tarifs et devis</a>. Jean voit la hauteur, l'accès et le volume, "
     "et vous rappelle avec une fourchette de prix."),
    ("Le devis est-il payant ?",
     "Non. Le devis est gratuit et sans engagement, sur photo ou après passage sur place si le chantier le demande."),
    ("Je n'arrive pas à vous joindre, que faire ?",
     "Jean est souvent dans un arbre ou sur la nacelle. Laissez un message avec votre nom, votre commune et "
     "le type de travaux, ou envoyez le formulaire : il rappelle dès qu'il redescend."),
    ("Vous déplacez-vous dans ma commune ?",
     "Oui si elle est à moins de 30 km de Nantes environ : Saint-Étienne-de-Montluc, Couëron, Saint-Herblain, "
     "Orvault, Sautron, Rezé, Vertou, Savenay, Treillières, La Chapelle-sur-Erdre et les communes voisines. "
     "En cas de doute, appelez."),
]

COMMUNES = [
    ("Saint-Étienne-de-Montluc", "/elagage-nantes/elagage-saint-etienne-de-montluc/"),
    ("Couëron", "/elagage-nantes/elagage-coueron/"),
    ("Saint-Herblain", "/elagage-nantes/elagage-saint-herblain/"),
    ("Sautron", "/elagage-nantes/elagage-sautron/"),
    ("Orvault", "/elagage-nantes/elagage-orvault/"),
    ("Vigneux-de-Bretagne", "/elagage-nantes/elagage-vigneux-de-bretagne/"),
    ("Cordemais", "/elagage-nantes/elagage-cordemais/"),
    ("Savenay", "/elagage-nantes/elagage-savenay/"),
    ("Le Temple-de-Bretagne", "/elagage-nantes/elagage-le-temple-de-bretagne/"),
    ("Treillières", "/elagage-nantes/elagage-treillieres/"),
    ("La Chapelle-sur-Erdre", "/elagage-nantes/elagage-la-chapelle-sur-erdre/"),
    ("Rezé", "/elagage-nantes/elagage-reze/"),
    ("Bouguenais", "/elagage-nantes/elagage-bouguenais/"),
    ("Le Pellerin", "/elagage-nantes/elagage-le-pellerin/"),
    ("Vertou", "/elagage-nantes/elagage-vertou/"),
    ("Nantes", "/elagage-nantes/elagueur-nantes-jardins-de-ville/"),
]


def texte(h):
    return re.sub(r"<[^>]+>", "", h)


def main():
    graph = [
        ENTREPRISE,
        {"@type": "ContactPage", "@id": URL, "url": URL, "name": TITLE, "description": DESC,
         "inLanguage": "fr-FR", "about": {"@id": BASE + "/#entreprise"},
         "mainEntity": {"@id": BASE + "/#entreprise"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Contact", "item": URL}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": texte(a)}}
            for q, a in FAQ]},
    ]
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    faq = "".join(f"      <details><summary>{q}</summary><p>{a}</p></details>\n" for q, a in FAQ)
    communes = ", ".join(f'<a href="{u}">{n}</a>' for n, u in COMMUNES)

    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{URL}">
<link rel="preload" href="/fonts/montserrat.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/style.css?v={CSS_V}">
<link rel="icon" href="/img/logo.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>

{HAUT}
<main>
<section class="hero page-hero">
  <div class="in">
    <ol class="crumbs"><li><a href="/">Accueil</a></li><li>Contact</li></ol>
    <h1>Contacter Jean Ferret, élagueur près de Nantes</h1>
    <p>Un arbre à élaguer, une haie à reprendre, une souche à enlever ? Le plus simple : appelez, ou envoyez une photo pour un devis gratuit.</p>
    <div class="btns">
      <a class="btn btn-a" href="tel:+33610641947">Appeler le 06 10 64 19 47</a>
      <a class="btn btn-o" href="/tarifs-devis/">Estimer mon prix avec une photo</a>
    </div>
  </div>
</section>

<section><div class="in contact">
  <div class="coords">
    <div class="sec-head" style="margin-bottom:8px"><span class="eyebrow">Coordonnées</span><h2>Jean Ferret Paysage</h2></div>
    <div><strong>Téléphone</strong><a href="tel:+33610641947">06 10 64 19 47</a><br><span class="note">Pas de réponse ? Jean est sans doute dans un arbre : laissez un message, il rappelle.</span></div>
    <div><strong>Horaires</strong>Du lundi au samedi, de 9h à 19h</div>
    <div><strong>Adresse</strong>4 le Gendre Moreau, 44360 Saint-Étienne-de-Montluc<br><span class="note">Pas d'accueil sur place : Jean vient chez vous.</span></div>
    <div><strong>Zone d'intervention</strong>Nantes et 30 km autour, en priorité l'ouest de l'agglomération : {communes}.</div>
    <div><strong>Devis gratuit</strong><a href="/tarifs-devis/">Estimez votre prix en 3 clics</a>, ou remplissez le formulaire.</div>
  </div>
  <form class="devis" action="/devis.php" method="post" enctype="multipart/form-data">
    <input type="hidden" name="source" value="page-contact">
    <label class="hp" aria-hidden="true">Ne pas remplir<input type="text" name="site_web" tabindex="-1" autocomplete="off"></label>
    <label>Prénom et nom<input name="nom" autocomplete="name" required></label>
    <label>Téléphone<input type="tel" name="telephone" autocomplete="tel" required></label>
    <label>E-mail (facultatif)<input type="email" name="email" autocomplete="email"></label>
    <label>Commune<input name="commune" autocomplete="address-level2" required></label>
    <label>Travaux<select name="travaux"><option>Élagage</option><option>Abattage</option><option>Haie</option><option>Souche</option><option>Tonte ou pelouse</option><option>Terrassement</option><option>Clôture ou claustra</option><option>Autre question</option></select></label>
    <label>Déchets verts<select name="dechets"><option>Évacuation par Jean Ferret</option><option>Je garde les déchets</option></select></label>
    <label class="full">Photos (jusqu'à 5)<input type="file" name="photos[]" accept="image/*" multiple></label>
    <label class="full">Votre message<textarea name="message" rows="4" placeholder="Hauteur de l'arbre, longueur de haie, accès pour la nacelle, déchets à évacuer…"></textarea></label>
    <p class="full rgpd">Vos informations servent uniquement à répondre à votre demande. <a href="/confidentialite/">Confidentialité</a></p>
    <button class="btn btn-a full" type="submit">Envoyer ma demande</button>
  </form>
</div></section>

<section><div class="in prose">
    <h2>Questions avant d'appeler</h2>
    <div class="faq">
{faq}    </div>
    <p>Voir aussi : <a href="/elagage-nantes/">élagage</a>, <a href="/abattage-arbre-nantes/">abattage</a>, <a href="/taille-haie-nantes/">taille de haie</a>, <a href="/dessouchage-nantes/">dessouchage</a> et <a href="/faq/">toutes les questions fréquentes</a>.</p>
</div></section>

<div class="band"><div class="in">
  <div><h2>Une photo suffit pour commencer</h2><p>Réponse rapide, devis gratuit.</p></div>
  <a class="btn btn-a" href="/tarifs-devis/">Mon devis en 1 minute</a>
</div></div>
{BAS}"""
    # anti-robots : durée de remplissage, comme sur l'accueil
    html = html.replace('<script src="/js/consentement.js', """<script>
(function(){var t=Date.now();document.querySelectorAll('form[action$="devis.php"]').forEach(function(f){var i=document.createElement('input');i.type='hidden';i.name='duree';f.appendChild(i);f.addEventListener('submit',function(){i.value=String(Date.now()-t)});});})();
</script>
<script src="/js/consentement.js""", 1)
    dest = os.path.join(SITE, "contact", "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(html)
    ok = len(TITLE) <= 60 and 130 <= len(DESC) <= 155
    print(f"/contact/  title {len(TITLE)}  meta {len(DESC)}{'' if ok else '  <-- À CORRIGER'}")


if __name__ == "__main__":
    main()
    subprocess.run([sys.executable, os.path.join(RACINE, "outils", "seo", "og.py")], cwd=RACINE, check=True)
    subprocess.run([sys.executable, os.path.join(RACINE, "outils", "seo", "sitemap.py")], cwd=RACINE, check=True)
