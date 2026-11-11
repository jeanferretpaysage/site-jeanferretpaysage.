"""Regénère site/sitemap.xml à partir des pages indexables (sans noindex).
Usage : python3 outils/seo/sitemap.py"""
import glob, os, re, subprocess, datetime
urls = []
for f in sorted(glob.glob("site/**/index.html", recursive=True)):
    s = open(f, encoding="utf-8").read()
    if 'content="noindex"' in s:
        continue
    u = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", f], capture_output=True, text=True).stdout.strip()
    if not d or subprocess.run(["git", "diff", "--quiet", "HEAD", "--", f]).returncode or subprocess.run(["git","ls-files","--error-unmatch",f],capture_output=True).returncode:
        d = datetime.date.today().isoformat()
    urls.append((u.count("/"), u, d))
urls.sort(key=lambda x: (x[0] > 4, x[0], x[1] != "https://jeanferretpaysage.fr/", x[1]))
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
xml += "".join(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for _, u, d in urls)
xml += "</urlset>\n"
open("site/sitemap.xml", "w").write(xml)
print(len(urls), "adresses dans le sitemap")
