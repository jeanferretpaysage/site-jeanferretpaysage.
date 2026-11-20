"""Abattage d'arbre : 18 communes (en plus des 5 de villes.py).
Un texte propre à chaque commune. Ne pas recopier un paragraphe d'une page à l'autre."""
from villes import ajoute, prix, NOTE_EX

CTA = '<div class="inline-cta"><p>{}</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>'
PETIT = ("Petit arbre (moins de 5 m)", "à partir de 260 €")
MOYEN = ("Arbre moyen (5 à 10 m)", "à partir de 650 €")
GRAND = ("Grand arbre (plus de 10 m)", "à partir de 1 040 €")


def dur(txt):
    return (txt, "jusqu'à 4 550 €")


ajoute("abattage", "bouguenais",
    "Abattage d'arbre à Bouguenais | Jean Ferret Paysage",
    "Abattage d'arbres à Bouguenais : pins des Couëts, peupliers vers Port-Lavigne, arbres sous les couloirs de l'aéroport. Démontage sécurisé, devis gratuit.",
    "Abattage d'arbres à Bouguenais",
    "À Bouguenais, on abat surtout deux sortes d'arbres : les grands pins des jardins des Couëts, et les peupliers vieillissants des terrains bas vers la Loire.",
    f"""
    <h2>Pins des Couëts, peupliers de la Loire</h2>
    <p>Dans les quartiers pavillonnaires, les pins noirs et maritimes plantés à la construction dépassent maintenant 15 m. Leurs racines soulèvent les allées et leurs aiguilles acidifient la pelouse. Vers Port-Lavigne et les prairies humides, les peupliers plantés il y a quarante ans arrivent en fin de vie : bois cassant, branches qui tombent par grand vent.</p>

    <h2>Comment on procède</h2>
    <p>Dans un jardin, démontage en grimpe : branches puis tronc en tronçons, retenus à la corde. En bord de prairie, quand la place le permet, abattage direct avec une entaille de direction, plus rapide et donc moins cher.</p>

    <h2>Exemple de chantier type à Bouguenais</h2>
    <p>Un pin noir de 18 m dans un jardin des Couëts, à 4 m de la maison, dont les racines ont fissuré l'allée du garage : démontage complet par rétention, tronc débité, souche rognée pour refaire l'allée.</p>
    {NOTE_EX}
    {CTA.format("Un pin ou un peuplier à abattre ?")}

    <h2>Avant les travaux : aéroport et urbanisme</h2>
    <p>Une partie de la commune est sous les servitudes de l'aéroport Nantes Atlantique, qui limitent surtout la hauteur des nouvelles plantations et des engins. Pour un abattage classique, ça ne change rien, mais on le vérifie si une grue ou une très grande nacelle est nécessaire. Les arbres repérés au plan local d'urbanisme métropolitain demandent une déclaration.</p>

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Grand pin à démonter près de la maison")], col="Arbre")}

    <h2>Bois et souche</h2>
    <p>Le bois de pin chauffe mal et encrasse les conduits : on l'emporte le plus souvent. La souche peut être <a href="/dessouchage-nantes/">rognée</a> sous le niveau du sol pour replanter ou refaire une allée.</p>
""",
    [("Un pin dont les racines soulèvent l'allée doit-il être abattu ?",
      "Pas toujours, mais couper les grosses racines fragilise l'arbre. Si l'allée doit être refaite, l'abattage est souvent plus sûr."),
     ("Abattez-vous les peupliers en bord de prairie ?",
      "Oui, en abattage direct dans la prairie quand la place le permet, ce qui réduit le prix.")],
    "Un arbre à abattre à Bouguenais ?")


ajoute("abattage", "cordemais",
    "Abattage d'arbre à Cordemais : estuaire, bocage",
    "Abattage d'arbres à Cordemais : saules et frênes fendus près des étiers, pins isolés exposés au vent, chênes morts du bocage. Bois laissé si vous voulez.",
    "Abattage d'arbres à Cordemais",
    "Entre les étiers de l'estuaire et le bocage du nord, les arbres de Cordemais prennent beaucoup de vent. Quand l'un d'eux est fendu ou mort, on l'abat avant qu'il tombe tout seul.",
    f"""
    <h2>Les arbres à risque sur la commune</h2>
    <p>Près des étiers et des fossés de marais, les saules et les frênes poussent vite sur un sol gorgé d'eau. Leurs grosses branches se fendent à la fourche. Les pins isolés, plantés pour abriter les maisons, prennent le vent de plein fouet. Au nord, dans le bocage, ce sont des chênes et des frênes morts ou creux au bord des chemins.</p>

    <h2>Exemple de chantier type à Cordemais</h2>
    <p>Un saule de 12 m fendu en deux à la fourche, au bord d'un étier, dont une moitié menace un abri de jardin : retrait de la partie fendue par rétention, abattage du reste vers le pré, bois coupé en bûches et laissé sur place.</p>
    {NOTE_EX}
    {CTA.format("Un arbre fendu ou mort chez vous ?")}

    <h2>Terrains humides et zones protégées</h2>
    <p>Les marais de l'estuaire sont protégés. Abattre un arbre dans un jardin du bourg ne demande pas d'autorisation ; en bordure de marais ou dans une haie repérée au plan d'urbanisme, une démarche peut être nécessaire. Côté terrain, on attend souvent quelques jours de sec avant d'entrer avec le matériel.</p>

    <h2>Prix indicatifs</h2>
    {prix([PETIT, MOYEN, dur("Arbre fendu au-dessus d'un bâtiment")], col="Arbre")}

    <h2>Le bois</h2>
    <p>Frêne et chêne font un bon bois de chauffage : on le coupe à la longueur de votre poêle. Les branchages sont broyés et emportés vers les déchèteries d'Estuaire et Sillon, ou laissés en paillage si vous voulez.</p>
""",
    [("Un saule fendu peut-il être sauvé ?",
      "Parfois, en retirant la partie fendue et en allégeant le reste. Si la fente descend dans le tronc, il vaut mieux l'abattre."),
     ("Pouvez-vous attendre que le terrain sèche ?",
      "Oui, sauf urgence. Sur sol mouillé, on travaille en grimpe sans engin, ou on décale de quelques jours.")],
    "Un arbre à abattre à Cordemais ?")


ajoute("abattage", "la-chapelle-sur-erdre",
    "Abattage d'arbre à La Chapelle-sur-Erdre | Jean Ferret",
    "Abattage d'arbres à La Chapelle-sur-Erdre : robiniers, pins et chênes sur terrains en pente vers l'Erdre, site protégé, démontage en grimpe. Devis gratuit.",
    "Abattage d'arbres à La Chapelle-sur-Erdre",
    "Vers l'Erdre, les terrains descendent et les grands arbres sont nombreux. Abattre y demande de la méthode, et parfois une démarche, car la vallée est protégée.",
    f"""
    <h2>Les arbres qu'on abat ici</h2>
    <p>Beaucoup de robiniers, qu'on appelle aussi acacias, ont colonisé les pentes vers la rivière : ils drageonnent et font des forêts de rejets. Les pins sylvestres et maritimes des propriétés souffrent des étés secs et meurent parfois en une saison. Dans les quartiers de la Gesvrine et de la Babinière, ce sont plutôt des bouleaux et des cerisiers devenus trop grands.</p>

    <h2>Exemple de chantier type à La Chapelle-sur-Erdre</h2>
    <p>Un pin sylvestre mort de 16 m en haut d'un terrain en pente vers l'Erdre, au-dessus d'un abri à bateau : démontage en grimpe, tronçons retenus et posés sur la pente, bois remonté au treuil vers le haut du terrain.</p>
    {NOTE_EX}
    {CTA.format("Un arbre mort sur un terrain en pente ?")}

    <h2>Le site de l'Erdre</h2>
    <p>La vallée de l'Erdre est un site protégé. Abattre un arbre dans ce périmètre peut demander une déclaration en mairie, en plus des protections du plan local d'urbanisme métropolitain. On vous dit quoi vérifier avant le chantier. Près de la berge, on laisse souvent la souche en place pour que les racines continuent de tenir le sol.</p>

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Grand arbre en pente, sans accès engin")], col="Arbre")}

    <h2>Les robiniers</h2>
    <p>Un robinier abattu repart de la souche et des racines, souvent plus fort. Pour s'en débarrasser, il faut rogner la souche et couper les rejets plusieurs années de suite. Son bois, très dur, fait un excellent bois de chauffage et des piquets imputrescibles.</p>
""",
    [("Faut-il une autorisation pour abattre près de l'Erdre ?",
      "Ça dépend de l'emplacement : la vallée est protégée, et certains arbres sont repérés au plan d'urbanisme. On vérifie avec vous avant."),
     ("Comment se débarrasser d'un acacia qui repart sans cesse ?",
      "Abattage, rognage de la souche, puis coupe des rejets pendant deux ou trois saisons.")],
    "Un arbre à abattre à La Chapelle-sur-Erdre ?")


ajoute("abattage", "la-montagne",
    "Abattage d'arbre à La Montagne : coteau | Jean Ferret",
    "Abattage d'arbres à La Montagne : arbres sur murs de soutènement, jardins en terrasses, rues étroites. Démontage en grimpe, rien ne tombe, devis gratuit.",
    "Abattage d'arbres à La Montagne",
    "Sur le coteau de La Montagne, abattre un arbre, c'est d'abord protéger ce qui est en dessous : un mur, une terrasse, la maison du voisin plus bas.",
    f"""
    <h2>Ce qui rend l'abattage délicat</h2>
    <p>Les jardins en paliers ne laissent jamais la place de faire tomber un arbre. Les rues sont étroites, souvent en pente, et une nacelle ne peut pas se garer. Les arbres poussés près des murs de soutènement, frênes, érables sycomores, robiniers, finissent par pousser le mur avec leurs racines.</p>

    <h2>Notre méthode</h2>
    <p>Tout se fait en grimpe. On démonte l'arbre par le haut, chaque morceau retenu à la corde et posé sur le palier le plus proche. Le tronc est coupé en tronçons courts qu'on peut porter. Pour un arbre collé à un mur fissuré, on laisse une souche haute plutôt que d'arracher les racines qui tiennent peut-être le mur.</p>

    <h2>Exemple de chantier type à La Montagne</h2>
    <p>Un érable sycomore de 14 m poussé au pied d'un mur de soutènement qui commence à se bomber : démontage en grimpe palier par palier, souche coupée au ras sans dessouchage, conseil de faire vérifier le mur par un maçon.</p>
    {NOTE_EX}
    {CTA.format("Un arbre près d'un mur ou d'une maison ?")}

    <h2>Prix indicatifs</h2>
    {prix([PETIT, MOYEN, dur("Arbre en terrasse au-dessus d'une maison")], col="Arbre")}

    <h2>Démarches et déchets</h2>
    <p>Les arbres repérés au plan local d'urbanisme métropolitain demandent une vérification. Pour le stationnement dans les rues étroites, on s'organise avant. La déchèterie de La Montagne, chemin du Pérou, est réservée aux particuliers de la Métropole ; les branchages du chantier partent avec nous.</p>
""",
    [("Faut-il dessoucher un arbre collé à un mur ?",
      "Pas toujours. Les racines peuvent tenir le mur ; les arracher risque de l'abîmer. On coupe souvent au ras et on laisse la souche."),
     ("Comment sortez-vous le bois sans accès ?",
      "En tronçons courts, portés à la main ou descendus à la corde jusqu'à la rue.")],
    "Un arbre à abattre à La Montagne ?")


ajoute("abattage", "lavau-sur-loire",
    "Abattage d'arbre à Lavau-sur-Loire | Jean Ferret",
    "Abattage d'arbres à Lavau-sur-Loire : frênes et peupliers en fin de vie, arbres cassés par le vent de l'estuaire, chemins de marais. Devis gratuit.",
    "Abattage d'arbres à Lavau-sur-Loire",
    "À Lavau, l'estuaire est partout et le vent aussi. Les arbres qu'on abat sont souvent des frênes ou des peupliers qui n'ont pas résisté à un hiver de tempêtes.",
    f"""
    <h2>Ce qu'on rencontre au village</h2>
    <p>Les frênes du bourg et des fossés sont touchés par la chalarose, qui les dessèche par le haut. Les peupliers plantés le long des prairies arrivent en fin de vie. Le vent d'ouest, sans obstacle sur le marais, casse les cimes et déracine les arbres sur sol détrempé.</p>

    <h2>Exemple de chantier type à Lavau-sur-Loire</h2>
    <p>Deux frênes secs aux trois quarts au-dessus d'une ruelle du bourg et d'un toit d'appentis : démontage en grimpe avec rétention au-dessus du toit, ruelle protégée le temps du chantier, bois laissé en bûches au propriétaire.</p>
    {NOTE_EX}
    {CTA.format("Un arbre abîmé par le vent ?")}

    <h2>Travailler au bord du marais</h2>
    <p>Les marais de l'estuaire sont des espaces naturels protégés. Pour un arbre en bordure, on vérifie avant de couper, et on évite le printemps. En hiver, les chemins de marais ne portent souvent pas un véhicule : on travaille avec du matériel porté et on sort le bois quand le terrain le permet.</p>

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Arbre cassé suspendu au-dessus d'un toit")], col="Arbre")}

    <h2>Le bois</h2>
    <p>Le frêne est un très bon bois de chauffage, même sec sur pied. On le coupe à la longueur voulue. Les branchages sont emportés, ou broyés sur place pour pailler. La déchèterie la plus proche est celle de Savenay, horaires à vérifier.</p>
""",
    [("Un frêne sec sur pied est-il dangereux ?",
      "Oui, son bois devient cassant en un ou deux ans. Au-dessus d'un passage ou d'un toit, il faut l'abattre sans attendre."),
     ("Intervenez-vous après une tempête à Lavau ?",
      "Oui. Pour un arbre tombé ou cassé, appelez directement : on vient sécuriser le plus vite possible.")],
    "Un arbre à abattre à Lavau-sur-Loire ?")


ajoute("abattage", "le-pellerin",
    "Abattage d'arbre au Pellerin : peupliers, frênes",
    "Abattage d'arbres au Pellerin : alignements de peupliers en fin de vie, frênes du canal de la Martinière, arbres du coteau. Abattage par étapes possible.",
    "Abattage d'arbres au Pellerin",
    "Au Pellerin, beaucoup de propriétaires ont hérité d'une rangée de peupliers plantés dans les années 1980. Ils arrivent en fin de vie, et c'est souvent nous qu'on appelle.",
    f"""
    <h2>Les alignements de peupliers</h2>
    <p>Le long des fossés et du canal de la Martinière, les peupliers d'alignement ont 35 à 45 ans. Leur bois devient creux et ils perdent de grosses branches. Plutôt que de tout abattre d'un coup, on peut les retirer en deux ou trois hivers, en commençant par les plus atteints, et replanter au fur et à mesure.</p>

    <h2>Sur le coteau</h2>
    <p>Vers Saint-Jean-de-Boisseau, les terrains en coteau ont des châtaigniers et des chênes. Là, on abat plutôt des arbres morts ou dangereux, un par un, souvent en démontage au-dessus d'une maison.</p>

    <h2>Exemple de chantier type au Pellerin</h2>
    <p>Une rangée de sept peupliers le long d'un fossé, dont trois creux à la base : abattage des trois plus atteints vers le pré cet hiver, les quatre autres programmés l'hiver suivant, bois débité et emporté, souches laissées au ras.</p>
    {NOTE_EX}
    {CTA.format("Une rangée de peupliers à retirer ?")}

    <h2>Prix indicatifs</h2>
    {prix([GRAND, ("Alignement de plusieurs arbres", "sur devis, prix par arbre dégressif"), dur("Arbre creux au-dessus d'une maison")], col="Arbre")}

    <h2>Règles et déchets</h2>
    <p>Les bords de Loire et du canal sont des secteurs naturels sensibles : on vérifie les protections avant un abattage. Les branchages sont emportés ; si vous y allez vous-même, les déchèteries de Saint-Jean-de-Boisseau et de La Montagne sont les plus proches.</p>
""",
    [("Faut-il abattre tous les peupliers en même temps ?",
      "Non. On peut étaler sur plusieurs hivers et commencer par les plus dangereux. Le prix par arbre baisse quand on en fait plusieurs."),
     ("Le bois de peuplier se brûle-t-il ?",
      "Mal : il chauffe peu. On l'emporte le plus souvent, sauf si vous voulez le garder pour le petit bois.")],
    "Un arbre à abattre au Pellerin ?")


ajoute("abattage", "le-temple-de-bretagne",
    "Abattage d'arbre au Temple-de-Bretagne | Jean Ferret",
    "Abattage d'arbres au Temple-de-Bretagne : pins et bouleaux trop grands dans les lotissements, chênes de bocage dépérissants. Démontage, devis gratuit.",
    "Abattage d'arbres au Temple-de-Bretagne",
    "Au Temple-de-Bretagne, les lotissements des années 2000 ont été plantés de pins, de bouleaux et de saules. Vingt ans plus tard, ils sont souvent trop grands pour le terrain.",
    f"""
    <h2>Des arbres plantés trop près</h2>
    <p>Un pin planté à 3 m d'une maison semble raisonnable quand il fait 2 m. À 12 m, ses branches touchent le toit et ses racines approchent des fondations. On voit aussi beaucoup de saules pleureurs et de bouleaux qui ont pris tout le jardin. Autour du bourg, quelques vieux chênes de bocage, gardés lors des constructions, dépérissent à cause des terrassements faits à leur pied.</p>

    <h2>Exemple de chantier type au Temple-de-Bretagne</h2>
    <p>Deux pins sylvestres de 12 m plantés à 3 m d'une maison de lotissement, aiguilles dans les gouttières chaque automne : démontage par rétention au-dessus du toit, tronc sorti par le côté du garage, souches rognées pour engazonner.</p>
    {NOTE_EX}
    {CTA.format("Un arbre trop près de la maison ?")}

    <h2>Un vieux chêne qui dépérit</h2>
    <p>Un chêne dont le pied a été tassé ou recouvert de terre lors d'une construction peut mettre dix ans à mourir. Les signes : feuillage clairsemé, branches sèches en haut, champignons au pied. On vient voir avant de conseiller l'abattage : parfois un élagage du bois mort suffit pour quelques années.</p>

    <h2>Prix indicatifs</h2>
    {prix([PETIT, MOYEN, GRAND], col="Arbre")}

    <h2>Après l'abattage</h2>
    <p>Les branchages sont emportés, la commune dépend des déchèteries d'Estuaire et Sillon. Si vous voulez replanter, choisissez une essence qui restera à la taille du jardin, et plantez-la à au moins la moitié de sa hauteur adulte de la maison.</p>
""",
    [("À quelle distance de la maison planter un arbre ?",
      "Au moins la moitié de sa hauteur adulte. Un arbre de 10 m adulte se plante à 5 m minimum."),
     ("Faut-il une autorisation pour abattre un pin de lotissement ?",
      "En général non. Vérifiez seulement le règlement du lotissement et le plan d'urbanisme si l'arbre est repéré.")],
    "Un arbre à abattre au Temple-de-Bretagne ?")


ajoute("abattage", "les-sorinieres",
    "Abattage d'arbre aux Sorinières : jardins | Jean Ferret",
    "Abattage d'arbres aux Sorinières : liquidambars, érables et bouleaux qui soulèvent la pelouse, arbres trop grands en limite. Souche rognée, devis gratuit.",
    "Abattage d'arbres aux Sorinières",
    "Aux Sorinières, les arbres qu'on abat sont rarement dangereux. Ils sont simplement au mauvais endroit : trop près de la maison, de la terrasse ou du voisin.",
    f"""
    <h2>Les essences des lotissements</h2>
    <p>Liquidambars, érables argentés, bouleaux et cerisiers à fleurs ont été plantés en masse dans les quartiers récents de la commune. Le liquidambar et l'érable argenté ont des racines qui courent juste sous la pelouse et soulèvent dallages et bordures. Le bouleau perd ses chatons et ses branches fines dans les gouttières.</p>

    <h2>Exemple de chantier type aux Sorinières</h2>
    <p>Un liquidambar de 11 m dont les racines soulèvent la terrasse et la pelouse : démontage en grimpe, tronc sorti en tronçons par le portillon, rognage de la souche et des grosses racines superficielles pour reposer la terrasse.</p>
    {NOTE_EX}
    {CTA.format("Un arbre qui abîme la terrasse ?")}

    <h2>Lotissement et voisinage</h2>
    <p>Un arbre planté à moins de 2 m de la limite ne doit pas dépasser 2 m de haut. Au-delà, le voisin peut demander qu'il soit réduit ou arraché. Le règlement du lotissement peut aussi prévoir des arbres à garder : vérifiez-le avant de faire abattre un arbre planté par l'aménageur.</p>

    <h2>Prix indicatifs</h2>
    {prix([PETIT, MOYEN, ("Rognage de la souche", "à partir de 260 €")], col="Arbre ou souche")}

    <h2>Les déchets</h2>
    <p>Les déchèteries de Rezé et de Vertou sont les plus proches, réservées aux particuliers de la Métropole. Le bois et les branchages partent avec nous ; le bois peut aussi rester en bûches.</p>
""",
    [("Les racines de mon érable soulèvent la pelouse, que faire ?",
      "Couper les racines affaiblit l'arbre. Si elles abîment une terrasse, l'abattage avec rognage de souche et des racines est souvent la solution."),
     ("Mon voisin peut-il exiger que j'abatte mon arbre ?",
      "S'il est à moins de 2 m de la limite et dépasse 2 m de haut, il peut demander sa réduction ou son arrachage.")],
    "Un arbre à abattre aux Sorinières ?")


ajoute("abattage", "malville",
    "Abattage d'arbre à Malville : chênes, frênes | Jean Ferret",
    "Abattage d'arbres à Malville : chênes morts en prairie, frênes atteints de chalarose, arbres de haies sur talus. Abattage direct si possible.",
    "Abattage d'arbres à Malville",
    "Sur les grands terrains de Malville, on a souvent la place de faire tomber un arbre en entier. C'est plus rapide, et ça se voit sur le prix.",
    f"""
    <h2>Abattage direct ou démontage</h2>
    <p>Quand l'arbre est au milieu d'une prairie ou au bord d'un champ, on l'abat en direct : entaille de direction, trait d'abattage, et il tombe à l'endroit prévu. Près d'une maison ou d'une ligne électrique, on revient au démontage par le haut. Sur la commune, environ un chantier sur deux permet l'abattage direct.</p>

    <h2>Les arbres concernés</h2>
    <p>Chênes morts sur pied dans les prairies, frênes desséchés par la chalarose dans les haies, et parfois des châtaigniers des talus qui penchent sur un chemin. Dans le bourg, ce sont plutôt des arbres de jardin trop grands.</p>

    <h2>Exemple de chantier type à Malville</h2>
    <p>Un chêne mort de 20 m au milieu d'une prairie, avec des branches qui tombent sur la clôture des chevaux : abattage direct dans la prairie, bois débité en bûches de 50 cm, branchages broyés et étalés, souche laissée au ras.</p>
    {NOTE_EX}
    {CTA.format("Un arbre mort dans un pré ?")}

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, ("Grand arbre en abattage direct, sans évacuation", "sur devis, souvent moins")], col="Arbre")}

    <h2>À vérifier</h2>
    <p>Un arbre d'une haie sur talus repérée au plan local d'urbanisme peut demander une déclaration avant d'être abattu. Un arbre isolé en prairie ou dans un jardin, en général non. Malville a une aire de déchets verts gérée par Estuaire et Sillon, mais sur un grand terrain, le broyat peut rester sur place.</p>
""",
    [("Un abattage direct coûte-t-il moins cher ?",
      "Oui, nettement, car il prend beaucoup moins de temps qu'un démontage en grimpe."),
     ("Pouvez-vous laisser le bois en bûches ?",
      "Oui, on le débite à la longueur voulue et on le range sur place.")],
    "Un arbre à abattre à Malville ?")


ajoute("abattage", "reze",
    "Abattage d'arbre à Rezé : Trentemoult, Sèvre | Jean Ferret",
    "Abattage d'arbres à Rezé : petits jardins de Trentemoult sans accès, peupliers et saules de la Sèvre, bouleaux des quartiers. Démontage, devis gratuit.",
    "Abattage d'arbres à Rezé",
    "Abattre un arbre à Rezé, c'est presque toujours abattre dans un petit jardin. Tout sort à la main, et rien ne doit toucher la maison d'à côté.",
    f"""
    <h2>Des chantiers sans place</h2>
    <p>À Trentemoult et à Pont-Rousseau, les jardins font souvent moins de 200 m² et n'ont pas d'accès véhicule. Les arbres qu'on y abat, bouleaux, saules, vieux pruniers, figuiers devenus énormes, sont démontés en grimpe et sortis en morceaux par la maison ou une ruelle. Près de la Sèvre et dans le quartier de la Houssais, ce sont plutôt des peupliers et des frênes sur sol humide.</p>

    <h2>Exemple de chantier type à Rezé</h2>
    <p>Un bouleau de 13 m mort au fond d'un jardin de Pont-Rousseau, entre trois maisons : démontage en grimpe avec rétention, sections de 50 cm portées par le couloir de la maison, bâches au sol, souche coupée au ras.</p>
    {NOTE_EX}
    {CTA.format("Un arbre à abattre dans un petit jardin ?")}

    <h2>Le figuier, un cas courant</h2>
    <p>Le figuier pousse très bien dans les jardins abrités de Rezé et finit par couvrir tout le terrain. Il repart vigoureusement de la souche après l'abattage : pour s'en débarrasser, il faut rogner la souche, sinon il faudra couper les rejets chaque année.</p>

    <h2>Prix indicatifs</h2>
    {prix([PETIT, MOYEN, dur("Grand arbre entre plusieurs maisons, sortie à la main")], col="Arbre")}

    <h2>Démarches et déchets</h2>
    <p>Les arbres repérés au plan local d'urbanisme métropolitain demandent une déclaration. À Trentemoult, on prévoit aussi le stationnement. La déchèterie de Rezé, rue Pierre Legendre, est réservée aux particuliers de la Métropole ; avec nous, tout part avec le chantier.</p>
""",
    [("Comment abattre un arbre sans accès au jardin ?",
      "En démontage en grimpe : l'arbre est coupé en petits morceaux qui sortent à la main par la maison, le garage ou une ruelle."),
     ("Un figuier abattu repousse-t-il ?",
      "Oui, souvent. Pour l'arrêter, il faut rogner la souche sous le niveau du sol.")],
    "Un arbre à abattre à Rezé ?")


ajoute("abattage", "saint-jean-de-boisseau",
    "Abattage d'arbre à Saint-Jean-de-Boisseau | Jean Ferret",
    "Abattage d'arbres à Saint-Jean-de-Boisseau : noyers et châtaigniers trop près des maisons, arbres des chemins creux, terrains humides vers la Loire.",
    "Abattage d'arbres à Saint-Jean-de-Boisseau",
    "Entre le bourg, les chemins creux et les terrains bas vers la Loire, Saint-Jean-de-Boisseau a des arbres de toutes sortes. On abat surtout ceux que la maison a fini par rattraper.",
    f"""
    <h2>Des arbres plus vieux que les maisons</h2>
    <p>Beaucoup de lotissements de la commune ont été construits sur d'anciens vergers et prés. On y trouve des noyers, des châtaigniers et des chênes gardés lors des travaux, aujourd'hui à quelques mètres des façades. Le noyer, en particulier, devient très large et ses feuilles tachent terrasses et voitures.</p>

    <h2>Exemple de chantier type à Saint-Jean-de-Boisseau</h2>
    <p>Un noyer de 15 m dont la couronne recouvre la maison et le jardin voisin : démontage par rétention au-dessus des deux toits, beau tronc gardé en grume pour le propriétaire qui voulait le vendre, branchages emportés.</p>
    {NOTE_EX}
    {CTA.format("Un grand arbre au-dessus de la maison ?")}

    <h2>Vers la Loire</h2>
    <p>Sur les terrains bas qui descendent vers le fleuve, les saules et les peupliers poussent vite sur un sol mou. Après les hivers venteux, on vient souvent abattre un arbre qui a commencé à pencher. Si la motte de racines se soulève, l'abattage ne doit pas attendre.</p>

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Grand arbre au-dessus de deux maisons")], col="Arbre")}

    <h2>Bois et déchets</h2>
    <p>Le bois de noyer et de châtaignier se valorise : bûches, ou grume pour un menuisier. Les branchages sont emportés. La déchèterie de Saint-Jean-de-Boisseau est rue de la Poterie, réservée aux particuliers de la Métropole.</p>
""",
    [("Peut-on vendre le bois d'un noyer abattu ?",
      "Un beau tronc droit de noyer intéresse parfois les menuisiers. On le coupe en grume de bonne longueur pour vous laisser le vendre."),
     ("Un arbre qui penche après le vent doit-il être abattu ?",
      "Si la terre se soulève au pied, oui, et vite. S'il penchait déjà avant, on vient l'évaluer.")],
    "Un arbre à abattre à Saint-Jean-de-Boisseau ?")


ajoute("abattage", "saint-sebastien-sur-loire",
    "Abattage d'arbre à Saint-Sébastien-sur-Loire | Jean Ferret",
    "Abattage d'arbres à Saint-Sébastien-sur-Loire : chênes rouges et noyers des années 1950, bouleaux au-dessus des vérandas, arbres de bord de Loire.",
    "Abattage d'arbres à Saint-Sébastien-sur-Loire",
    "Les jardins sébastiennais des années 1950 et 1960 ont des arbres qui couvrent aujourd'hui deux ou trois parcelles. Les abattre demande de travailler au-dessus de chez tout le monde.",
    f"""
    <h2>Des arbres qui couvrent plusieurs jardins</h2>
    <p>Chênes rouges d'Amérique, noyers, tilleuls et cèdres ont été plantés quand les parcelles étaient plus grandes. Depuis, les terrains ont été divisés, et l'arbre se retrouve au-dessus de trois maisons. Le chêne rouge, qui pousse vite, a souvent des fourches fragiles.</p>

    <h2>Exemple de chantier type à Saint-Sébastien-sur-Loire</h2>
    <p>Un chêne rouge de 22 m avec une fourche fendue, au-dessus de deux jardins voisins : accord des voisins, démontage par rétention avec des points d'ancrage hauts, branches posées dans chaque jardin puis sorties, bois emporté.</p>
    {NOTE_EX}
    {CTA.format("Un arbre au-dessus de plusieurs jardins ?")}

    <h2>Organiser le chantier avec les voisins</h2>
    <p>Quand l'arbre surplombe d'autres jardins, on a besoin de passer chez les voisins ou de poser des branches chez eux. On les prévient avec vous, on protège ce qui doit l'être, et on nettoie chaque jardin en partant. Les arbres repérés au plan local d'urbanisme demandent une vérification avant.</p>

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Très grand arbre au-dessus de plusieurs maisons")], col="Arbre")}

    <h2>Près de la Loire</h2>
    <p>Vers les bords de Loire, les sols mouillés par les crues tiennent moins bien les racines. Les déchèteries de Nantes Métropole sont réservées aux particuliers de la Métropole ; les branchages du chantier partent avec nous.</p>
""",
    [("Qui paie l'abattage d'un arbre qui surplombe plusieurs jardins ?",
      "Le propriétaire de l'arbre. Les voisins doivent seulement laisser l'accès si on en a besoin."),
     ("Une fourche fendue est-elle dangereuse ?",
      "Oui, elle peut s'ouvrir d'un coup par grand vent. Faites-la voir vite, une photo suffit pour un premier avis.")],
    "Un arbre à abattre à Saint-Sébastien-sur-Loire ?")


ajoute("abattage", "sainte-luce-sur-loire",
    "Abattage d'arbre à Sainte-Luce-sur-Loire | Jean Ferret",
    "Abattage d'arbres à Sainte-Luce-sur-Loire : séquoias et cèdres de plus de 20 m côté Thouaré, peupliers vers la Loire, arbres de lotissement. Devis gratuit.",
    "Abattage d'arbres à Sainte-Luce-sur-Loire",
    "Côté Thouaré, certains jardins ont un séquoia ou un cèdre planté dans les années 1960. À plus de 20 m, quand il doit tomber, c'est un vrai chantier de grimpeur.",
    f"""
    <h2>Les très grands résineux</h2>
    <p>Séquoias, cèdres de l'Atlas et sapins de Nordmann plantés à la construction des maisons dépassent souvent 20 m. Ils posent des soucis quand ils sont à moins de 10 m d'une maison, quand leur cime a été cassée par le vent, ou quand un cèdre perd ses grosses branches basses. Leur démontage se prépare : ordre de coupe, zones de dépose, sortie du bois.</p>

    <h2>Le reste de la commune</h2>
    <p>Dans les lotissements récents, on abat plutôt des arbres d'ornement devenus encombrants. Vers la Loire, ce sont des peupliers et des saules fragilisés par les sols détrempés.</p>

    <h2>Exemple de chantier type à Sainte-Luce-sur-Loire</h2>
    <p>Un séquoia de 24 m à 6 m d'une maison des années 1960, cime cassée par un coup de vent : démontage complet en grimpe, sections du fût retenues par un frein, tronc débité au sol, bois emporté.</p>
    {NOTE_EX}
    {CTA.format("Un très grand arbre près de chez vous ?")}

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Résineux de plus de 20 m près d'une maison")], col="Arbre")}

    <h2>Démarches et déchets</h2>
    <p>Certains grands arbres sont repérés au plan local d'urbanisme métropolitain : on vérifie avant. Les déchèteries de Nantes Métropole sont réservées aux particuliers de la Métropole et limitent les volumes ; un séquoia représente plusieurs camions, qu'on gère.</p>
""",
    [("Faut-il abattre un séquoia dont la cime est cassée ?",
      "Pas forcément. Si le reste de l'arbre est sain et loin de la maison, on peut retirer la partie cassée. Près d'une maison, l'abattage est souvent plus raisonnable."),
     ("Combien coûte l'abattage d'un très grand résineux ?",
      "Ça dépend de la hauteur, de l'accès et de ce qu'il y a dessous. Comptez à partir de 1 040 € et jusqu'à 4 550 € pour les cas difficiles.")],
    "Un arbre à abattre à Sainte-Luce-sur-Loire ?")


ajoute("abattage", "savenay",
    "Abattage d'arbre à Savenay : chênes et cyprès",
    "Abattage d'arbres à Savenay : cyprès de Lambert brise-vent cassés, chênes secs au pied du Sillon, arbres des jardins clos du centre. Devis gratuit.",
    "Abattage d'arbres à Savenay",
    "À Savenay, le Sillon de Bretagne coupe la commune en deux : en haut, des jardins clos de murs ; en bas, des prés et des haies. Les abattages ne s'y ressemblent pas.",
    f"""
    <h2>En haut, dans le centre</h2>
    <p>Autour du centre ancien, les jardins sont fermés de murs et les accès passent par des portails étroits. Les cyprès de Lambert et les pins plantés pour couper le vent du large y ont souvent pris 15 m, avec des cimes cassées. On les démonte en grimpe et le bois sort par le portail.</p>

    <h2>En bas, vers les prés</h2>
    <p>Au pied du coteau et vers les marais, les chênes et les frênes des haies sèchent sur pied, souvent après plusieurs étés secs. Là, on a généralement la place d'un abattage direct.</p>

    <h2>Exemple de chantier type à Savenay</h2>
    <p>Trois cyprès de Lambert de 14 m dans un jardin clos du centre, dont deux à la cime cassée : démontage en grimpe, tronçons sortis par un portail de 1,20 m, souches rognées pour replanter une haie plus basse.</p>
    {NOTE_EX}
    {CTA.format("Des cyprès ou un chêne à abattre ?")}

    <h2>Prix indicatifs</h2>
    {prix([PETIT, MOYEN, GRAND], col="Arbre")}

    <h2>Patrimoine et déchets</h2>
    <p>Dans le centre ancien, des règles de patrimoine peuvent s'appliquer aux arbres visibles depuis la rue : on vérifie avec vous. Savenay a une déchèterie gérée par Estuaire et Sillon ; les branchages du chantier partent avec nous.</p>
""",
    [("Un cyprès à la cime cassée doit-il être abattu ?",
      "Il ne refera pas de vraie cime et reste fragile. Dans un jardin habité, l'abattage est souvent le choix le plus sûr."),
     ("Passez-vous par un portail étroit ?",
      "Oui. Tout est découpé en morceaux qu'on peut porter, sans engin dans le jardin.")],
    "Un arbre à abattre à Savenay ?")


ajoute("abattage", "suce-sur-erdre",
    "Abattage d'arbre à Sucé-sur-Erdre : bord d'Erdre",
    "Abattage d'arbres à Sucé-sur-Erdre : aulnes et peupliers de berge, grands arbres des propriétés au bord de l'Erdre, chênes de hameaux. Devis gratuit.",
    "Abattage d'arbres à Sucé-sur-Erdre",
    "À Sucé, beaucoup d'arbres à abattre sont au bord de l'eau. On les fait tomber du bon côté, jamais dans l'Erdre, et on garde les racines qui tiennent la berge.",
    f"""
    <h2>Arbres de berge</h2>
    <p>Aulnes, saules et peupliers bordent les propriétés qui descendent vers l'Erdre. Les aulnes sont parfois touchés par une maladie des racines qui les fait dépérir ; les peupliers deviennent cassants avec l'âge. Un arbre qui penche vers la rivière se démonte par le haut, en ramenant chaque morceau côté terrain.</p>

    <h2>Dans le bourg et les hameaux</h2>
    <p>Les maisons du bourg ont des jardins plus petits, souvent desservis par des allées étroites. Dans les hameaux, on abat surtout des chênes morts et des frênes atteints de chalarose.</p>

    <h2>Exemple de chantier type à Sucé-sur-Erdre</h2>
    <p>Un peuplier de 20 m penché vers l'Erdre au bout d'une propriété, au-dessus d'un ponton : démontage en grimpe, sections ramenées côté jardin à la corde, souche laissée en place pour tenir la berge, bois remonté.</p>
    {NOTE_EX}
    {CTA.format("Un arbre au bord de l'eau ?")}

    <h2>Protections de l'Erdre</h2>
    <p>Les abords de l'Erdre sont protégés : avant un abattage près de la rivière, une démarche peut être nécessaire. On vous dit quoi vérifier en mairie. On évite de travailler en berge au printemps, quand les oiseaux nichent.</p>

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Arbre penché au-dessus de l'eau ou d'un ponton")], col="Arbre")}

    <h2>Déchets</h2>
    <p>Sucé dépend des déchèteries d'Erdre et Gesvres, et celle de la commune est annoncée en travaux : vérifiez avant de vous déplacer. Avec nous, les branchages partent avec le chantier.</p>
""",
    [("Pourquoi laisser la souche au bord de l'Erdre ?",
      "Les racines continuent de tenir la berge pendant des années. Sans elles, la rive s'érode plus vite."),
     ("Un arbre peut-il tomber dans la rivière pendant l'abattage ?",
      "Non, chaque morceau est retenu à la corde et ramené côté terrain.")],
    "Un arbre à abattre à Sucé-sur-Erdre ?")


ajoute("abattage", "treillieres",
    "Abattage d'arbre à Treillières | Jean Ferret Paysage",
    "Abattage d'arbres à Treillières : chênes de bocage gardés dans les lotissements, saules pleureurs envahissants, arbres morts du Gesvres. Devis gratuit.",
    "Abattage d'arbres à Treillières",
    "Quand les lotissements de Treillières ont été construits, on a souvent gardé les chênes du bocage. Trente ans après, certains sont au-dessus de deux ou trois maisons.",
    f"""
    <h2>Le chêne du lotissement</h2>
    <p>Un chêne de bocage conservé au milieu d'un lotissement a vu son environnement changer : sol tassé, racines coupées par les réseaux, arrosage différent. Certains s'adaptent, d'autres dépérissent lentement. Avant de parler d'abattage, on regarde le houppier, le pied et le tronc. Quand il faut l'abattre, c'est en démontage complet.</p>

    <h2>Autres cas fréquents</h2>
    <p>Saules pleureurs plantés près d'une mare devenue pelouse, bouleaux trop proches des maisons, et, le long du Gesvres, frênes et aulnes morts au bord des chemins.</p>

    <h2>Exemple de chantier type à Treillières</h2>
    <p>Un chêne de 19 m dépérissant entre trois jardins de lotissement, avec du bois mort au-dessus d'une aire de jeux : démontage par rétention avec l'accord des voisins, bois débité en bûches, souche coupée au ras.</p>
    {NOTE_EX}
    {CTA.format("Un grand chêne qui inquiète ?")}

    <h2>Haies protégées et réseaux</h2>
    <p>Certains arbres et haies de la commune sont protégés au plan local d'urbanisme : on vérifie avant d'abattre. Si on doit ensuite enlever la souche près d'une maison, on vérifie aussi les réseaux enterrés.</p>

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Grand chêne au-dessus de plusieurs maisons")], col="Arbre")}

    <h2>Déchets</h2>
    <p>Treillières dépend des déchèteries d'Erdre et Gesvres. Le bois de chêne est un très bon bois de chauffage : beaucoup de clients le gardent. Les branchages partent avec nous.</p>
""",
    [("Comment savoir si mon chêne dépérit ?",
      "Feuilles plus petites et plus rares, branches sèches en haut de la couronne, champignons au pied. Une photo en été aide beaucoup."),
     ("Les voisins doivent-ils être d'accord ?",
      "Non pour abattre votre arbre. Mais s'il faut passer chez eux ou poser des branches dans leur jardin, leur accord est nécessaire.")],
    "Un arbre à abattre à Treillières ?")


ajoute("abattage", "vertou",
    "Abattage d'arbre à Vertou : pins et cèdres | Jean Ferret",
    "Abattage d'arbres à Vertou : pins maritimes dépérissants des années 1970, grands arbres en pente vers la Sèvre, arbres en limite de vigne. Devis gratuit.",
    "Abattage d'arbres à Vertou",
    "Les quartiers de Vertou ont beaucoup de pins plantés dans les années 1970. Une partie dépérit aujourd'hui, et un pin mort devient dangereux en quelques mois.",
    f"""
    <h2>Les pins des quartiers</h2>
    <p>Pins maritimes et pins noirs souffrent des étés secs à répétition. Un pin affaibli est vite attaqué par des insectes sous l'écorce, et il peut rougir et mourir en une saison. Son bois sèche alors rapidement et devient cassant. Quand les aiguilles virent au roux sur toute la couronne, il est trop tard pour le sauver.</p>

    <h2>Vers la Sèvre et le vignoble</h2>
    <p>Près de la Sèvre et de la chaussée des Moines, les propriétés en pente ont des cèdres, des chênes et des platanes : là, on démonte en grimpe. Vers le vignoble, les arbres isolés en limite de parcelle s'abattent souvent en direct, côté jardin, pour ne pas toucher les rangs.</p>

    <h2>Exemple de chantier type à Vertou</h2>
    <p>Un pin maritime de 17 m rougi en quelques semaines, au-dessus d'une maison et d'une piscine : démontage par rétention, bâches sur la piscine, tronc débité au sol, souche rognée.</p>
    {NOTE_EX}
    {CTA.format("Un pin qui roussit ?")}

    <h2>Prix indicatifs</h2>
    {prix([MOYEN, GRAND, dur("Pin mort au-dessus d'une maison")], col="Arbre")}

    <h2>Règles et déchets</h2>
    <p>Les bords de la Sèvre et certains secteurs de patrimoine sont protégés : on vérifie avant un abattage. La déchèterie de Vertou est à La Foresterie, allée des Cadets, réservée aux particuliers de la Métropole. Le bois de pin, qui chauffe mal, est emporté.</p>
""",
    [("Mon pin devient roux, peut-on le sauver ?",
      "Si toute la couronne roussit, non. Il faut l'abattre avant que son bois devienne cassant, surtout près d'une maison."),
     ("Pouvez-vous protéger la piscine pendant l'abattage ?",
      "Oui, on bâche et on retient chaque morceau à la corde au-dessus des zones fragiles.")],
    "Un arbre à abattre à Vertou ?")


ajoute("abattage", "vigneux-de-bretagne",
    "Abattage d'arbre à Vigneux-de-Bretagne | Jean Ferret",
    "Abattage d'arbres à Vigneux-de-Bretagne et La Paquelais : chênes foudroyés, frênes malades, arbres de bocage au-dessus des chemins. Bois laissé en bûches.",
    "Abattage d'arbres à Vigneux-de-Bretagne",
    "À Vigneux, on préfère sécuriser un vieil arbre plutôt que l'abattre. Mais un chêne foudroyé ou un frêne sec au-dessus d'un chemin doivent tomber avant de tomber tout seuls.",
    f"""
    <h2>Quand l'abattage s'impose</h2>
    <p>Sur les grands terrains de la commune et de La Paquelais, les arbres isolés attirent la foudre : un chêne foudroyé a souvent une longue fente du haut en bas et peut mourir dans l'année. Les frênes de bocage atteints de chalarose sèchent par le haut. Et les chênes creux au bord des chemins et des routes deviennent dangereux pour ceux qui passent dessous.</p>

    <h2>Exemple de chantier type à Vigneux-de-Bretagne</h2>
    <p>Un chêne de 22 m foudroyé l'été, fendu sur toute la hauteur, au bord du chemin d'accès d'une maison de hameau : démontage de la couronne à la nacelle depuis le chemin, abattage du fût dans le champ, bois débité en bûches et laissé au propriétaire.</p>
    {NOTE_EX}
    {CTA.format("Un arbre foudroyé ou sec ?")}

    <h2>Abattre, ou seulement sécuriser ?</h2>
    <p>Un chêne têtard creux qui ne menace rien peut rester : il abrite chouettes, chauves-souris et insectes. On le sécurise par une taille. On ne conseille l'abattage que quand l'arbre est au-dessus d'une maison, d'un passage ou d'une route, et qu'aucune taille ne suffit.</p>

    <h2>Prix indicatifs</h2>
    {prix([GRAND, ("Abattage direct en champ, bois laissé sur place", "sur devis, souvent moins"), dur("Arbre foudroyé au-dessus d'un bâtiment")], col="Arbre")}

    <h2>Démarches et déchets</h2>
    <p>Les haies bocagères repérées au plan local d'urbanisme demandent une déclaration avant d'abattre un de leurs arbres. Vigneux a une déchèterie d'Erdre et Gesvres, impasse de la Vallée. Sur un grand terrain, les branchages peuvent être broyés et laissés sur place.</p>
""",
    [("Un chêne foudroyé peut-il survivre ?",
      "Parfois, si la fente est superficielle. Si l'écorce se décolle sur une large bande, il meurt souvent dans l'année."),
     ("Pouvez-vous intervenir vite près de Vigneux ?",
      "On est installés à Saint-Étienne-de-Montluc, la commune voisine : pour un arbre dangereux, appelez directement.")],
    "Un arbre à abattre à Vigneux-de-Bretagne ?")
