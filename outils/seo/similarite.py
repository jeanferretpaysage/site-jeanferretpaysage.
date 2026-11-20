"""Texte commun entre pages communes (objectif < 40 %).
Usage : python3 outils/seo/similarite.py
Compare le texte du contenu principal (hors menu, pied de page, barre latérale) par
séquences de 5 mots : part des séquences d'une page qu'on retrouve dans l'autre."""
import glob, itertools, re
pages = sorted(set(glob.glob("site/*/*-*/index.html")) | set(glob.glob("site/elagage-nantes/*/index.html")))
pages = [p for p in pages if "conseils-jardin" not in p]
def mots(f):
    s = open(f, encoding="utf-8").read()
    m = re.search(r"<main>(.*?)<aside", s, re.S).group(1)
    t = re.sub(r"<[^>]+>", " ", m).lower()
    return re.findall(r"[a-zà-ÿœ0-9']+", t)
def sh(w):
    return {" ".join(w[i:i + 5]) for i in range(len(w) - 4)}
S = {p: sh(mots(p)) for p in pages}
res = sorted(((len(S[a] & S[b]) / min(len(S[a]), len(S[b])), a, b) for a, b in itertools.combinations(pages, 2)), reverse=True)
print(len(pages), "pages comparées")
for r, a, b in res[:10]:
    print(f"{r:.0%}  {a[5:-11]}  /  {b[5:-11]}")
print("au-dessus de 40 % :", sum(r >= .4 for r, *_ in res))
