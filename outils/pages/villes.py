"""Pages villes pour la taille de haie et l'abattage (5 communes de départ).

Chaque page a son propre texte local : essences, terrain, accès, chantier type,
règles et déchèterie. Ne pas copier un paragraphe d'une page à l'autre.
"""

VILLES = {
    "saint-etienne-de-montluc": ("Saint-Étienne-de-Montluc", "44360"),
    "coueron": ("Couëron", "44220"),
    "saint-herblain": ("Saint-Herblain", "44800"),
    "sautron": ("Sautron", "44880"),
    "orvault": ("Orvault", "44700"),
}
VOISINES = {
    "saint-etienne-de-montluc": ["coueron", "sautron"],
    "coueron": ["saint-etienne-de-montluc", "saint-herblain", "sautron"],
    "saint-herblain": ["coueron", "orvault", "sautron"],
    "sautron": ["orvault", "saint-herblain", "coueron"],
    "orvault": ["sautron", "saint-herblain"],
}
NOTE_PRIX = '<p class="note">Forfait selon le chantier, TVA non applicable (art. 293 B du CGI). <a href="/tarifs-devis/">Tous les tarifs</a>.</p>'
NOTE_EX = '<p class="note">Exemple représentatif des demandes que l\'on reçoit sur la commune, pas un client précis.</p>'

PAGES = []


def ajoute(service, slug, title, desc, h1, intro, body, faq, band):
    ville, cp = VILLES[slug]
    if service == "haie":
        base, nom_base, prefixe, type_s = "/taille-haie-nantes/", "Taille de haies", "taille-haie-", "Taille de haie"
        autre = ("Abattage d'arbre à " + ville, f"/abattage-arbre-nantes/abattage-arbre-{slug}/")
        conseil = ("Quand tailler une haie ?", "/conseils-jardin/quand-tailler-une-haie/")
    else:
        base, nom_base, prefixe, type_s = "/abattage-arbre-nantes/", "Abattage d'arbre", "abattage-arbre-", "Abattage d'arbre"
        autre = ("Taille de haie à " + ville, f"/taille-haie-nantes/taille-haie-{slug}/")
        conseil = ("Arbre abîmé après une tempête", "/conseils-jardin/arbre-tombe-tempete/")
    path = f"{base}{prefixe}{slug}/"
    voisines = "".join(
        f'      <li><a href="{base}{prefixe}{v}/">{type_s} à {VILLES[v][0]}</a></li>\n' for v in VOISINES[slug])
    elag = f"/elagage-nantes/elagage-{slug}/"
    body += f"""
    <h2>On intervient aussi près de {ville}</h2>
    <ul class="links">
{voisines}      <li><a href="{elag}">Élagage à {ville}</a></li>
      <li><a href="{autre[1]}">{autre[0]}</a></li>
    </ul>
"""
    PAGES.append(dict(
        path=path, title=title, desc=desc, h1=h1, intro=intro, body=body, faq=faq, band=band,
        crumbs=[(nom_base, base), (ville, path)],
        menu=base,
        service=dict(name=f"{type_s} à {ville}", type=type_s, city=ville, cp=cp),
        side=[(f"{nom_base} : la page complète", base), (f"Élagage à {ville}", elag), autre, conseil],
        side_titre=f"Devis gratuit à {ville}",
    ))


# =====================================================================
# TAILLE DE HAIE
# =====================================================================

ajoute("haie", "saint-etienne-de-montluc",
    "Taille de haie à Saint-Étienne-de-Montluc | Jean Ferret",
    "Taille de haies à Saint-Étienne-de-Montluc : haies champêtres des hameaux, thuyas et lauriers du bourg. Ramassage compris, devis gratuit sur photo.",
    "Taille de haies à Saint-Étienne-de-Montluc",
    "On est installés au Gendre Moreau : les haies de la commune, on les connaît bien, des longues haies de bocage des hameaux aux thuyas des lotissements du bourg.",
    f"""
    <h2>Deux sortes de haies sur la commune</h2>
    <p>Dans les hameaux, ce sont surtout des haies champêtres : chênes têtards, noisetiers, aubépines, prunelliers, parfois sur un talus. Elles font souvent plus de 100 m et n'ont pas toujours été entretenues depuis des années.</p>
    <p>Autour du bourg et dans les lotissements, on trouve plutôt des haies de thuyas, de lauriers-palmes et de photinias plantées entre 1980 et 2000. Beaucoup dépassent aujourd'hui 3 m de haut et mangent un mètre de jardin en largeur.</p>

    <h2>Ce qu'on fait</h2>
    <p>Taille des deux faces et du dessus au taille-haie, finition au sécateur si besoin, et nacelle pour les haies trop hautes pour un escabeau. Sur une haie champêtre, on travaille plutôt au lamier ou à la tronçonneuse pour reprendre les branches qui ont pris du volume. Tout est ramassé et emporté.</p>

    <h2>Exemple de chantier type à Saint-Étienne-de-Montluc</h2>
    <p>Une haie champêtre de 120 m le long d'un chemin de hameau, qui avance de 2 m sur le passage : recépage des noisetiers, reprise des côtés, bois des chênes coupé en bûches pour le propriétaire, branchages évacués.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Une haie à reprendre chez vous ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Haies de bocage : ce qu'il faut savoir</h2>
    <p>Une haie champêtre en zone agricole ou naturelle est souvent protégée. L'entretenir ne pose pas de problème, mais l'arracher peut demander une déclaration préalable. Avant de supprimer une haie, on vérifie avec vous ce qui s'applique au terrain. Pour la période, on reprend ces haies en hiver, en dehors de la nidification.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Travaux</th><th>Fourchette, ramassage compris</th></tr>
      <tr><td>Haie de jardin, 30 m deux faces et dessus</td><td>environ 500 €</td></tr>
      <tr><td>Haie champêtre très large, ou haie à abattre</td><td>sur devis, après photo</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Les déchets de taille</h2>
    <p>La commune dépend de la Communauté de communes Estuaire et Sillon pour les déchèteries. Les branchages d'une haie de 30 m remplissent vite une remorque : on les emporte, c'est compris dans le prix. À lire : <a href="/conseils-jardin/quand-tailler-une-haie/">quand tailler une haie</a>.</p>
""",
    [("Venez-vous pour une petite haie à Saint-Étienne-de-Montluc ?",
      "Oui. L'entreprise est sur la commune, donc même une petite haie de jardin vaut le déplacement."),
     ("Peut-on arracher une vieille haie de thuyas ?",
      "Oui. On abat la haie, on rogne les souches si vous voulez replanter ou poser une clôture, et on évacue tout.")],
    "Une haie à tailler à Saint-Étienne-de-Montluc ?")

ajoute("haie", "coueron",
    "Taille de haie à Couëron : thuyas, cyprès | Jean Ferret",
    "Taille de haies à Couëron : thuyas, cyprès de Leyland, lauriers des lotissements et jardins près de la Loire. Deux faces et dessus, déchets emportés.",
    "Taille de haies à Couëron",
    "À Couëron, beaucoup de jardins sont fermés par des haies de résineux plantées pour couper le vent de Loire. Elles poussent vite, et une haie oubliée deux ans devient vite un mur.",
    f"""
    <h2>Les haies de Couëron</h2>
    <p>Dans les lotissements de la Chabossière, de la Métairie ou du Bossis, la haie de thuyas ou de cyprès de Leyland est la règle. Le cyprès de Leyland peut prendre près d'un mètre par an : sans deux tailles annuelles, il dépasse 4 m en quelques saisons.</p>
    <p>Côté Loire et vers les marais, le vent d'ouest dessèche souvent la face exposée des haies, qui roussit. Une taille trop courte de ce côté laisse des trous difficiles à refermer.</p>

    <h2>Comment on travaille</h2>
    <p>On réduit d'abord la hauteur, puis on reprend les faces en gardant une haie un peu plus large en bas qu'en haut : la lumière descend jusqu'au pied et la haie reste garnie. Pour les cyprès de plus de 3 m, la nacelle évite de monter sur des échelles dans la haie.</p>

    <h2>Exemple de chantier type à Couëron</h2>
    <p>Une haie de cyprès de Leyland de 25 m, haute de 5 m, qui fait de l'ombre à la maison voisine : réduction à 2 m en une fois sur le dessus, reprise des deux faces, branchages broyés et emportés.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Votre haie a pris trop de hauteur ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Le bon moment à Couëron</h2>
    <p>Près du fleuve, les sols sont gorgés d'eau une bonne partie de l'hiver. On préfère alors tailler en septembre ou en octobre, quand le terrain porte encore et que la nacelle ne marque pas la pelouse. Au printemps, on vérifie toujours la haie avant de commencer : les merles y nichent beaucoup.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Travaux</th><th>Fourchette, ramassage compris</th></tr>
      <tr><td>30 m de haie, deux faces et dessus</td><td>environ 500 €</td></tr>
      <tr><td>Réduction d'une haie de plus de 4 m</td><td>sur devis, après photo</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Les déchets</h2>
    <p>Les déchèteries de Nantes Métropole sont réservées aux particuliers de la Métropole et limitent les volumes. Pour une grosse taille, le plus simple est de nous laisser tout emporter. Pour comprendre les règles avec le voisin, voir <a href="/conseils-jardin/arbre-du-voisin/">l'arbre ou la haie du voisin</a>.</p>
""",
    [("Peut-on réduire une haie de cyprès de moitié d'un coup ?",
      "En hauteur, oui. Sur les côtés, il faut rester dans la partie verte : le cyprès, comme le thuya, ne repart pas du bois nu."),
     ("Taillez-vous les haies mitoyennes ?",
      "Oui, avec l'accord des deux voisins. On peut tailler les deux faces le même jour et partager le devis.")],
    "Une haie à tailler à Couëron ?")

ajoute("haie", "saint-herblain",
    "Taille de haie à Saint-Herblain | Jean Ferret Paysage",
    "Taille de haies mitoyennes à Saint-Herblain : thuyas, photinias, lauriers, même sans accès au jardin. Ramassage et évacuation compris, devis gratuit.",
    "Taille de haies à Saint-Herblain",
    "À Saint-Herblain, la difficulté est rarement la haie elle-même. C'est l'accès : petits jardins, pas de passage sur le côté de la maison, voisin de l'autre côté.",
    f"""
    <h2>Des haies mitoyennes dans des jardins serrés</h2>
    <p>Dans les quartiers du Tillay, de la Bégraisière, de Preux ou du bourg, les jardins font souvent moins de 400 m². La haie sépare deux terrains, elle fait 2 à 3 m de haut, et on ne peut la tailler côté voisin qu'en passant chez lui.</p>
    <p>On y voit beaucoup de photinias et de lauriers, plantés pour cacher vite le vis-à-vis, et des thuyas plus anciens qui se dégarnissent du bas.</p>

    <h2>Notre façon de faire</h2>
    <p>Matériel léger quand il n'y a pas d'accès : taille-haie sur perche et échafaudage roulant plutôt que nacelle. Bâches au sol pour ne pas laisser de feuilles dans les massifs, ramassage à la main et sortie des déchets par la maison ou le portillon, à la brouette ou en big-bag.</p>

    <h2>Exemple de chantier type à Saint-Herblain</h2>
    <p>Une haie de photinias de 18 m entre deux jardins, haute de 3 m et épaisse de 1,50 m : accord des deux voisins, réduction à 2 m, reprise des deux faces, déchets sortis en big-bag par le garage.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Une haie mitoyenne à reprendre ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Hauteur et voisinage</h2>
    <p>Une haie plantée à moins de 2 m de la limite ne doit pas dépasser 2 m de haut, et le voisin peut demander que les branches qui avancent chez lui soient coupées. Le plus simple reste de se mettre d'accord et de faire les deux côtés ensemble. Tout est expliqué dans notre article sur <a href="/conseils-jardin/arbre-du-voisin/">la haie du voisin</a>.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Travaux</th><th>Fourchette, évacuation comprise</th></tr>
      <tr><td>Haie de 30 m, deux faces et dessus</td><td>environ 500 €</td></tr>
      <tr><td>Petite haie de jardin de ville</td><td>sur devis, souvent moins</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Les déchets verts</h2>
    <p>La déchèterie de Saint-Herblain se trouve au lieu-dit Tougas, réservée aux particuliers de Nantes Métropole. Horaires à vérifier avant d'y aller. Sinon, on repart avec tout.</p>
""",
    [("Faut-il passer chez le voisin pour tailler ?",
      "Pour tailler sa face de la haie, oui, avec son accord. Sans accord, on taille uniquement votre côté et le dessus."),
     ("Pouvez-vous intervenir sans accès voiture au jardin ?",
      "Oui. On travaille avec du matériel portable et on sort les déchets par la maison ou le portillon, en protégeant les passages.")],
    "Une haie à tailler à Saint-Herblain ?")

ajoute("haie", "sautron",
    "Taille de haie à Sautron : lauriers, photinias",
    "Taille de haies à Sautron : lauriers et photinias trop épais, haies doublées de largeur, reprise en deux temps. Déchets emportés, devis gratuit.",
    "Taille de haies à Sautron",
    "À Sautron, le problème le plus courant n'est pas la hauteur mais la largeur : des haies de lauriers ou de photinias qui ont doublé d'épaisseur et grignotent le jardin.",
    f"""
    <h2>Les haies de Sautron</h2>
    <p>Les lotissements des années 1980 et 1990 ont été fermés avec des lauriers-palmes et des photinias, deux arbustes qui poussent vite. Taillés seulement sur le dessus pendant des années, beaucoup font aujourd'hui 2 m d'épaisseur. Autour des propriétés plus anciennes, on trouve aussi des charmilles et des haies mélangées sous les chênes.</p>

    <h2>Reprendre une haie trop large</h2>
    <p>Le laurier-palme et le photinia supportent bien une coupe dans le vieux bois. On peut donc rabattre franchement une face, sans attendre. Pour garder un écran vis-à-vis, on rabat une face la première année et l'autre l'année suivante : la haie reste opaque d'un côté pendant qu'elle repart de l'autre.</p>

    <h2>Exemple de chantier type à Sautron</h2>
    <p>Une haie de lauriers-palmes de 35 m, épaisse de 2 m, qui empêche de passer la tondeuse le long de la clôture : rabattage de la face côté jardin à 60 cm du tronc, dessus remis à 1,80 m, tout le feuillage évacué.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Votre haie déborde sur le jardin ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Période et règles locales</h2>
    <p>Une reprise forte se fait en fin d'hiver, avant la montée de sève et l'arrivée des oiseaux, ou en septembre. Sautron dépend du plan local d'urbanisme de Nantes Métropole, qui peut protéger certaines haies et certains arbres : si on doit arracher une haie entière, on vérifie avec vous avant.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Travaux</th><th>Fourchette, ramassage compris</th></tr>
      <tr><td>Taille d'entretien, 30 m deux faces et dessus</td><td>environ 500 €</td></tr>
      <tr><td>Rabattage d'une haie très épaisse</td><td>sur devis, après photo</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Déchets verts</h2>
    <p>Les feuilles de laurier sont lourdes et se compostent mal. Les déchèteries d'Orvault et de Saint-Herblain sont les plus proches, mais le plus simple est de nous laisser les emporter : c'est compris. À lire aussi : <a href="/conseils-jardin/quand-tailler-une-haie/">quand tailler une haie</a>.</p>
""",
    [("Une haie de laurier repart-elle après une coupe sévère ?",
      "Oui, le laurier-palme repart du bois, même après une coupe forte. Il faut juste accepter une haie moins dense pendant une saison."),
     ("Peut-on remplacer la haie par une clôture ?",
      "Oui. On abat la haie, on enlève les souches et on pose la clôture ou des panneaux claustras dans la foulée.")],
    "Une haie à reprendre à Sautron ?")

ajoute("haie", "orvault",
    "Taille de haie à Orvault : charmilles, ifs | Jean Ferret",
    "Taille de haies à Orvault : charmilles, ifs et buis des propriétés anciennes, thuyas des lotissements. Taille soignée, déchets évacués, devis gratuit.",
    "Taille de haies à Orvault",
    "Orvault a des haies qu'on voit moins ailleurs : charmilles, ifs taillés et vieux buis autour des propriétés anciennes, à côté des thuyas des quartiers plus récents.",
    f"""
    <h2>Des haies de propriété et des haies de lotissement</h2>
    <p>Autour des maisons de maître et des anciennes propriétés, vers le Petit-Chantilly ou la Ferrière, on taille des charmilles, des ifs et des haies de buis parfois centenaires. Ces haies demandent une taille nette et régulière, au cordeau, pour garder leur forme.</p>
    <p>Dans les quartiers pavillonnaires, ce sont des thuyas et des lauriers classiques, souvent montés trop haut.</p>

    <h2>Ce qu'on fait</h2>
    <p>Taille au taille-haie et finition à la main sur les ifs et les charmilles, avec un gabarit pour garder des lignes droites. Sur les thuyas, réduction en hauteur à la nacelle et reprise des faces. Ramassage complet, jusque dans les massifs.</p>

    <h2>Exemple de chantier type à Orvault</h2>
    <p>Une charmille de 50 m en bordure d'allée, haute de 2,50 m, dans une propriété ancienne : taille des deux faces et du dessus au cordeau, finition à la main, feuilles soufflées et emportées.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Une haie à entretenir à Orvault ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Le buis et la pyrale</h2>
    <p>Beaucoup de buis d'Orvault ont été dévorés par la pyrale du buis, une chenille arrivée dans la région il y a une dizaine d'années. Un buis très atteint, gris et sans feuilles, ne repart en général pas. On peut l'arracher et proposer une autre haie basse à la place. Sur un buis encore vert, une taille légère et une surveillance au printemps suffisent.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Travaux</th><th>Fourchette, évacuation comprise</th></tr>
      <tr><td>30 m de haie, deux faces et dessus</td><td>environ 500 €</td></tr>
      <tr><td>Charmille ou if taillé au cordeau</td><td>sur devis, selon la longueur</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Déchets et terrain</h2>
    <p>Dans la vallée du Cens, certains jardins sont en pente : on adapte l'échafaudage et on ramasse en remontant. La déchèterie d'Orvault se trouve sur le site de l'Espérance, réservée aux particuliers de la Métropole. Sinon, on emporte tout. Voir aussi : <a href="/conseils-jardin/quand-tailler-une-haie/">quand tailler une haie</a>.</p>
""",
    [("Quand tailler une charmille ?",
      "Une fois par an suffit en général, fin août ou septembre. Une deuxième taille légère en fin d'hiver garde des lignes très nettes."),
     ("Pouvez-vous arracher une haie de buis malade ?",
      "Oui, arrachage, souches et évacuation compris. On peut ensuite replanter ou poser une bordure.")],
    "Une haie à tailler à Orvault ?")

# =====================================================================
# ABATTAGE
# =====================================================================

ajoute("abattage", "saint-etienne-de-montluc",
    "Abattage d'arbre à Saint-Étienne-de-Montluc | Jean Ferret",
    "Abattage d'arbres à Saint-Étienne-de-Montluc : frênes malades, peupliers des marais, chênes de bocage. Bois laissé en bûches si vous voulez, devis gratuit.",
    "Abattage d'arbres à Saint-Étienne-de-Montluc",
    "Sur la commune, on abat surtout des frênes atteints par la maladie, des peupliers fragiles près des marais et des arbres trop proches des maisons.",
    f"""
    <h2>Les arbres qu'on abat le plus ici</h2>
    <p>Les frênes sont très touchés par la chalarose, un champignon qui fait sécher les branches du haut, puis tout l'arbre. Un frêne aux trois quarts sec devient cassant et dangereux, surtout au bord d'un chemin ou d'une maison.</p>
    <p>Vers les marais de l'estuaire, les peupliers et les saules poussent vite mais cassent facilement. Dans le bocage, ce sont parfois de vieux chênes creux ou couchés par une tempête.</p>

    <h2>Comment on abat</h2>
    <p>Quand il y a de la place, abattage direct avec une entaille de direction, l'arbre tombe là où on l'a prévu. Près d'un bâtiment ou d'une clôture, démontage par le haut, branche par branche, chaque morceau étant descendu à la corde. Le tronc est ensuite tronçonné au sol.</p>

    <h2>Exemple de chantier type à Saint-Étienne-de-Montluc</h2>
    <p>Trois frênes secs en bordure de prairie, au-dessus d'un chemin de hameau : abattage direct dans la prairie, bois fendu en bûches de 50 cm et rangé sur place pour le propriétaire, branchages évacués.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Un arbre mort ou dangereux chez vous ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Avant d'abattre : ce qu'on vérifie</h2>
    <p>Un arbre dans un jardin s'abat en général sans autorisation. En revanche, près des marais de l'estuaire, classés en zone naturelle protégée, ou pour un arbre repéré au plan d'urbanisme, une démarche en mairie peut être nécessaire. Dans les champs humides, on attend parfois que le terrain sèche pour entrer avec le matériel.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Arbre</th><th>Prix indicatif</th></tr>
      <tr><td>Petit arbre (moins de 5 m)</td><td>à partir de 260 €</td></tr>
      <tr><td>Grand arbre (plus de 10 m)</td><td>à partir de 1 040 €</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Le bois et la souche</h2>
    <p>Ici, beaucoup de clients gardent le bois pour se chauffer : on le coupe à la longueur voulue, et le prix baisse. La souche reste au ras du sol, ou peut être <a href="/dessouchage-nantes/">rognée</a> si vous voulez replanter.</p>
""",
    [("Faut-il abattre un frêne atteint de chalarose ?",
      "Pas toujours. S'il reste bien feuillé, on peut le surveiller. Quand plus de la moitié du houppier est sec, ou s'il est près d'une maison ou d'un passage, il vaut mieux l'abattre."),
     ("Peut-on garder tout le bois ?",
      "Oui. On coupe le tronc et les grosses branches en bûches, laissées sur place. Seuls les branchages sont emportés.")],
    "Un arbre à abattre à Saint-Étienne-de-Montluc ?")

ajoute("abattage", "coueron",
    "Abattage d'arbre à Couëron : pins, cèdres | Jean Ferret",
    "Abattage d'arbres à Couëron : pins et cèdres trop près des maisons, démontage par rétention au-dessus des toits, arbres des bords de Loire. Devis gratuit.",
    "Abattage d'arbres à Couëron",
    "À Couëron, les arbres à abattre sont souvent de grands résineux plantés il y a 50 ans, devenus trop gros pour des jardins de lotissement.",
    f"""
    <h2>Les cas les plus fréquents à Couëron</h2>
    <p>Pins maritimes, pins noirs et cèdres plantés dans les années 1970 dépassent aujourd'hui 15 m. Leurs aiguilles bouchent les gouttières, leurs racines soulèvent les allées, et ils penchent souvent du côté de la maison, là où il y a le plus de lumière.</p>
    <p>Près de la Loire, les sols mous en hiver tiennent moins bien les racines : un arbre qui a commencé à pencher après une tempête doit être regardé vite.</p>

    <h2>Le démontage par rétention</h2>
    <p>Dans un jardin de Couëron, on a rarement la place de faire tomber un pin de 15 m en entier. On grimpe dans l'arbre, on coupe les branches puis le tronc par tronçons, et chaque morceau est retenu par une corde et un frein avant d'être posé au sol. Rien ne tombe sur la toiture, la clôture ou les massifs.</p>

    <h2>Exemple de chantier type à Couëron</h2>
    <p>Un cèdre de 17 m à 3 m d'une maison, dont les branches basses frottent le toit : démontage complet par rétention, tronc découpé en billons, souche rognée pour refaire la pelouse.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Un grand arbre trop près de la maison ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Bords de Loire et zones protégées</h2>
    <p>Une partie de la commune, le long du fleuve et des marais, est en site naturel protégé de l'estuaire de la Loire. Pour un abattage dans ces secteurs, ou pour un arbre repéré au plan local d'urbanisme de Nantes Métropole, on vous dit quoi vérifier en mairie avant de commencer.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Arbre</th><th>Prix indicatif</th></tr>
      <tr><td>Arbre moyen (5 à 10 m)</td><td>à partir de 650 €</td></tr>
      <tr><td>Grand résineux à démonter près d'une maison</td><td>jusqu'à 4 550 €</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Après l'abattage</h2>
    <p>Branches et aiguilles sont évacuées. La souche peut rester au ras du sol ou être <a href="/dessouchage-nantes/">rognée</a>. Si l'arbre a été abîmé par le vent, lisez aussi <a href="/conseils-jardin/arbre-tombe-tempete/">que faire après une tempête</a>.</p>
""",
    [("Un pin qui penche vers la maison est-il dangereux ?",
      "Pas forcément s'il a toujours penché. S'il penche plus qu'avant, si la terre se soulève au pied ou après une tempête, faites-le voir rapidement."),
     ("Peut-on abattre sans accès pour un engin ?",
      "Oui, le démontage par rétention se fait en grimpe, sans nacelle, et tout est sorti à la main.")],
    "Un arbre à abattre à Couëron ?")

ajoute("abattage", "saint-herblain",
    "Abattage d'arbre à Saint-Herblain | Jean Ferret Paysage",
    "Abattage d'arbres à Saint-Herblain : bouleaux, pins et cerisiers trop grands pour les jardins de lotissement, démontage morceau par morceau. Devis gratuit.",
    "Abattage d'arbres à Saint-Herblain",
    "Dans les jardins herblinois, on abat surtout des arbres devenus trop grands pour la parcelle : bouleaux, pins, cerisiers à fleurs ou vieux fruitiers.",
    f"""
    <h2>Des arbres trop grands pour des jardins moyens</h2>
    <p>Les lotissements du Tillay, de la Bégraisière ou de la Solvardière ont été plantés il y a 40 ou 50 ans. Les bouleaux y ont souvent atteint 15 m, avec des branches qui passent au-dessus du toit voisin. Les vieux cerisiers et pruniers dépérissent et perdent du bois mort.</p>
    <p>Il y a aussi des chênes et des cèdres conservés lors de la construction des quartiers, aujourd'hui très proches des façades.</p>

    <h2>Abattre sans faire de dégâts</h2>
    <p>Entre une maison, une clôture et le jardin du voisin, l'abattage se fait presque toujours en démontage : on monte dans l'arbre et on le réduit par le haut. Les morceaux descendent à la corde et sortent par le portillon. Pour les bouleaux, au bois léger et cassant, on prend des sections plus courtes.</p>

    <h2>Exemple de chantier type à Saint-Herblain</h2>
    <p>Deux bouleaux de 14 m dans un jardin de 350 m², au-dessus d'une véranda : démontage en grimpe, sections descendues à la corde, bois et branches sortis à la main par le garage, souches coupées au ras.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Un arbre devenu trop grand ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Voisins et autorisations</h2>
    <p>Si l'arbre est en limite, prévenez le voisin : on aura peut-être besoin de passer chez lui ou de poser une branche dans son jardin. Saint-Herblain dépend du plan local d'urbanisme de Nantes Métropole, qui protège certains arbres et boisements : on vous dit quoi vérifier avant le chantier. Les règles de distance sont expliquées dans <a href="/conseils-jardin/arbre-du-voisin/">l'arbre du voisin</a>.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Arbre</th><th>Prix indicatif</th></tr>
      <tr><td>Petit arbre ou fruitier (moins de 5 m)</td><td>à partir de 260 €</td></tr>
      <tr><td>Arbre moyen (5 à 10 m)</td><td>à partir de 650 €</td></tr>
      <tr><td>Grand arbre collé à la maison</td><td>jusqu'à 4 550 €</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Le bois et la souche</h2>
    <p>Tout est évacué, ou le bois reste en bûches si vous le souhaitez. Pour récupérer la place au sol, on peut <a href="/dessouchage-nantes/">enlever la souche</a> le même jour.</p>
""",
    [("Faut-il l'accord du voisin pour abattre mon arbre ?",
      "Non pour abattre un arbre chez vous. Mais s'il faut passer chez lui ou travailler au-dessus de son terrain, son accord est nécessaire."),
     ("Combien de temps dure un chantier d'abattage ?",
      "Ça dépend de l'arbre et de l'accès. On vous donne une estimation au moment du devis.")],
    "Un arbre à abattre à Saint-Herblain ?")

ajoute("abattage", "sautron",
    "Abattage d'arbre à Sautron : grands chênes | Jean Ferret",
    "Abattage d'arbres à Sautron : grands chênes et châtaigniers malades, arbres morts au-dessus d'une terrasse. Abattage seulement si besoin, devis gratuit.",
    "Abattage d'arbres à Sautron",
    "À Sautron, beaucoup de jardins ont gardé un grand chêne ou un châtaignier. On ne les abat que quand il n'y a pas d'autre solution, et on vous le dit franchement.",
    f"""
    <h2>Abattre ou élaguer ?</h2>
    <p>Un chêne qui perd du bois mort n'est pas forcément condamné : un élagage sanitaire suffit souvent. L'abattage devient nécessaire quand l'arbre est creux à la base, quand des champignons apparaissent au pied, quand il est mort aux trois quarts ou quand il menace la maison. Les châtaigniers de la commune souffrent aussi de la maladie de l'encre, qui fait dépérir les racines.</p>
    <p>On vient voir l'arbre et on vous dit ce qui est raisonnable, y compris quand la réponse est un <a href="/elagage-nantes/elagage-sautron/">élagage</a> plutôt qu'un abattage.</p>

    <h2>Exemple de chantier type à Sautron</h2>
    <p>Un châtaignier de 18 m à moitié sec au fond d'un jardin, au-dessus d'un abri et d'une terrasse : démontage de la couronne par rétention, abattage du fût dans la pelouse une fois la place libre, bois débité en bûches.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Un doute sur un grand arbre ?</p><a class="btn btn-a" href="/tarifs-devis/">Envoyer une photo</a></div>

    <h2>Arbres protégés à Sautron</h2>
    <p>Le plan local d'urbanisme de Nantes Métropole repère certains arbres et boisements à protéger, surtout autour des anciennes propriétés. Avant d'abattre un grand chêne, on vous indique ce qu'il faut vérifier en mairie. Après l'abattage, une replantation peut être demandée.</p>

    <h2>Le matériel</h2>
    <p>Sur les pelouses, on évite les engins lourds : travail en grimpe, ou nacelle sur plaques de protection quand le terrain le permet. Les grosses sections de tronc sont débitées sur place pour être sorties sans abîmer le jardin.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Arbre</th><th>Prix indicatif</th></tr>
      <tr><td>Grand arbre (plus de 10 m)</td><td>à partir de 1 040 €</td></tr>
      <tr><td>Grand chêne ou châtaignier à démonter</td><td>jusqu'à 4 550 €</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>La souche</h2>
    <p>Une souche de chêne met des dizaines d'années à disparaître. Si vous voulez récupérer la place, on la <a href="/dessouchage-nantes/">rogne</a> sous le niveau du sol. Les déchèteries d'Orvault et de Saint-Herblain sont les plus proches, mais les branchages sont emportés avec le prix.</p>
""",
    [("Mon chêne perd des branches, faut-il l'abattre ?",
      "Pas forcément. Le plus souvent, un élagage qui retire le bois mort suffit. On vient voir l'arbre avant de conseiller un abattage."),
     ("Faut-il replanter après l'abattage ?",
      "Si l'arbre est protégé au plan d'urbanisme, une replantation peut être demandée. Sinon, c'est votre choix.")],
    "Un grand arbre à Sautron ?")

ajoute("abattage", "orvault",
    "Abattage d'arbre à Orvault : cèdres, marronniers",
    "Abattage d'arbres à Orvault : cèdres, marronniers et hêtres des propriétés anciennes, terrains en pente du Cens. Démontage sécurisé, devis gratuit.",
    "Abattage d'arbres à Orvault",
    "Orvault a beaucoup de très grands arbres dans des propriétés anciennes. Quand l'un d'eux doit tomber, c'est souvent un chantier technique, au-dessus de bâtiments ou dans une pente.",
    f"""
    <h2>Les grands arbres d'Orvault</h2>
    <p>Cèdres de l'Atlas, marronniers, hêtres pourpres, séquoias parfois : les parcs des maisons anciennes, vers le Petit-Chantilly ou le bourg, ont des arbres de plus de 20 m. Les marronniers souffrent souvent de chancres et de pourriture du tronc, les hêtres supportent mal les étés secs et les sols tassés par les travaux.</p>

    <h2>Un démontage préparé</h2>
    <p>Pour un arbre de cette taille, on prépare le chantier : zone de sécurité, points d'ancrage des cordes, ordre de coupe, endroit où poser les grosses sections. Le tronc est découpé en tronçons assez légers pour être retenus, puis débité au sol. Si un bâtiment est dessous, rien ne tombe librement.</p>

    <h2>Exemple de chantier type à Orvault</h2>
    <p>Un marronnier de 20 m creux à la base, au bord d'une allée de propriété : démontage complet en grimpe, sections retenues à la corde, bois débité et évacué, souche rognée pour refaire l'allée.</p>
    {NOTE_EX}
    <div class="inline-cta"><p>Un très grand arbre à abattre ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Pente, vallée du Cens et protections</h2>
    <p>Le long du Cens, les terrains en pente obligent à travailler en grimpe et à sortir le bois en remontant. Plusieurs boisements de la commune sont classés au plan local d'urbanisme de Nantes Métropole : dans un espace boisé classé, un abattage demande une déclaration en mairie. On vous dit quoi vérifier avant le chantier.</p>

    <h2>Prix indicatifs</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Arbre</th><th>Prix indicatif</th></tr>
      <tr><td>Arbre moyen (5 à 10 m)</td><td>à partir de 650 €</td></tr>
      <tr><td>Grand arbre (plus de 10 m)</td><td>à partir de 1 040 €</td></tr>
      <tr><td>Très grand arbre à démonter au-dessus d'un bâtiment</td><td>jusqu'à 4 550 €</td></tr>
    </table></div>
    {NOTE_PRIX}

    <h2>Bois et déchets</h2>
    <p>Le bois de cèdre et de hêtre peut être laissé en billons ou en bûches. Les branchages sont évacués : la déchèterie d'Orvault, sur le site de l'Espérance, est réservée aux particuliers de la Métropole et limite les volumes. Après une tempête, voir aussi <a href="/conseils-jardin/arbre-tombe-tempete/">les bons réflexes</a>.</p>
""",
    [("Comment savoir si mon marronnier est dangereux ?",
      "Champignons au pied, écorce qui se décolle, cavité dans le tronc, grosses branches sèches : ce sont des signes à faire vérifier. Une photo suffit pour un premier avis."),
     ("Faut-il une autorisation pour abattre un arbre à Orvault ?",
      "Pas pour un arbre ordinaire dans un jardin. Une déclaration en mairie est nécessaire s'il est en espace boisé classé ou protégé au plan d'urbanisme.")],
    "Un arbre à abattre à Orvault ?")
