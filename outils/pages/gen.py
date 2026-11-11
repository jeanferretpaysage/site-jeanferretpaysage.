"""Génère les pages du blog « Conseils jardin » et les pages villes haie / abattage.

Usage (depuis la racine du dépôt) :
    python3 outils/pages/gen.py

Le contenu de chaque page est dans blog.py et villes.py, à côté de ce fichier.
Le haut (menu) et le bas (pied de page, barre mobile) sont copiés de la page FAQ,
pour rester identiques au reste du site.
"""
import json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", ".."))
SITE = os.path.join(RACINE, "site")
BASE = "https://jeanferretpaysage.fr"
CSS_V = "20261112a"
sys.path.insert(0, ICI)

modele = open(os.path.join(SITE, "faq", "index.html"), encoding="utf-8").read()
HAUT = re.search(r'<div class="topbar">.*?</header>\n', modele, re.S).group(0)
HAUT = HAUT.replace(' aria-current="page"', "")
BAS = re.search(r"</main>\n.*", modele, re.S).group(0)


def esc(t):
    return t.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def texte(h):
    return re.sub(r"<[^>]+>", "", h)


def page(p):
    url = BASE + p["path"]
    crumbs = [("Accueil", "/")] + p["crumbs"]
    graph = []
    if p.get("article"):
        graph.append({
            "@type": "BlogPosting", "headline": p["h1"], "description": p["desc"],
            "datePublished": p["article"], "dateModified": p["article"],
            "author": {"@type": "Person", "name": "Jean Ferret"},
            "publisher": {"@id": BASE + "/#entreprise"},
            "image": BASE + "/" + p["img"][0] if p.get("img") else BASE + "/img/elagage-platanes-elagueurs-grimpeurs.webp",
            "mainEntityOfPage": url, "inLanguage": "fr-FR"})
    if p.get("service"):
        s = p["service"]
        graph.append({"@type": "Service", "name": s["name"], "serviceType": s["type"],
                      "provider": {"@id": BASE + "/#entreprise"},
                      "areaServed": {"@type": "City", "name": s["city"], "postalCode": s["cp"]},
                      "url": url})
    if p.get("blog_index"):
        graph.append({"@type": "Blog", "name": "Conseils jardin", "url": url,
                      "publisher": {"@id": BASE + "/#entreprise"}, "inLanguage": "fr-FR"})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u}
        for i, (n, u) in enumerate(crumbs)]})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": texte(a)}}
            for q, a in p["faq"]]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

    haut = HAUT
    if p.get("menu"):
        haut = haut.replace(f'<li><a href="{p["menu"]}">', f'<li><a href="{p["menu"]}" aria-current="page">', 1)

    fil = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in crumbs[:-1]) + f"<li>{crumbs[-1][0]}</li>"
    figure = ""
    if p.get("img"):
        src, alt = p["img"]
        figure = (f'    <figure class="illus"><img src="/{src}" alt="{esc(alt)}" width="800" height="600" '
                  f'loading="lazy" decoding="async"></figure>\n')
    faq = ""
    if p.get("faq"):
        faq = '    <h2>Questions fréquentes</h2>\n    <div class="faq">\n' + "".join(
            f"      <details><summary>{q}</summary><p>{a}</p></details>\n" for q, a in p["faq"]) + "    </div>\n"
    side = "".join(f'        <li><a href="{u}">{n}</a></li>\n' for n, u in p["side"])
    meta_date = ""
    if p.get("article"):
        j, m, a = p["article"].split("-")[::-1]
        mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
                "septembre", "octobre", "novembre", "décembre"][int(m) - 1]
        meta_date = f'    <p class="note">Par Jean Ferret, élagueur depuis 40 ans · {int(j)} {mois} {a}</p>\n'

    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title>
<meta name="description" content="{esc(p["desc"])}">
<link rel="canonical" href="{url}">
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

{haut}
<main>
<section class="hero page-hero">
  <div class="in">
    <ol class="crumbs">{fil}</ol>
    <h1>{p["h1"]}</h1>
    <p>{p["intro"]}</p>
    <div class="btns">
      <a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix avec une photo</a>
      <a class="btn btn-o" href="tel:+33610641947">Appeler le 06 10 64 19 47</a>
    </div>
  </div>
</section>

<section><div class="in layout">
  <article class="prose">
{meta_date}{figure}{p["body"].strip()}
{faq}  </article>

  <aside class="side">
    <div class="box">
      <h2>{p.get("side_titre", "Devis gratuit sur photo")}</h2>
      <p>Une photo, on vous rappelle.</p>
      <a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a>
      <a class="btn btn-m" href="tel:+33610641947">06 10 64 19 47</a>
    </div>
    <div class="box">
      <h2>{p.get("side_liens", "À lire aussi")}</h2>
      <ul class="links">
{side}      </ul>
    </div>
  </aside>
</div></section>

<div class="band"><div class="in">
  <div><h2>{p["band"]}</h2><p>Réponse rapide, devis gratuit.</p></div>
  <a class="btn btn-a" href="/tarifs-devis/">Mon devis en 1 minute</a>
</div></div>
{BAS}"""
    dest = os.path.join(SITE, p["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(html)
    # contrôles simples
    alerte = "" if len(p["title"]) <= 60 and 130 <= len(p["desc"]) <= 155 else "  <-- À CORRIGER"
    print(f'{p["path"]}  title {len(p["title"])}  meta {len(p["desc"])}{alerte}')


if __name__ == "__main__":
    import blog, villes
    for p in blog.PAGES + villes.PAGES:
        page(p)
    # balises de partage et sitemap à jour
    import subprocess
    subprocess.run([sys.executable, os.path.join(RACINE, "outils", "seo", "og.py")], cwd=RACINE, check=True)
    subprocess.run([sys.executable, os.path.join(RACINE, "outils", "seo", "sitemap.py")], cwd=RACINE, check=True)
