"""Taille de haie : 18 communes (en plus des 5 de villes.py).
Un texte propre à chaque commune. Ne pas recopier un paragraphe d'une page à l'autre."""
from villes import ajoute, prix, NOTE_EX

CTA = '<div class="inline-cta"><p>{}</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>'
H30 = ("30 m de haie, deux faces et dessus", "environ 500 €")


ajoute("haie", "bouguenais",
    "Taille de haie à Bouguenais : Couëts, bourg | Jean Ferret",
    "Taille de haies à Bouguenais : cyprès des Couëts, haies de bocage vers Port-Lavigne, haies le long des rues. Branchages emportés, devis gratuit sur photo.",
    "Taille de haies à Bouguenais",
    "Aux Couëts, la haie sert surtout à se cacher de la rue. Vers la Loire et Port-Lavigne, elle borde des prés et des chemins. Deux métiers différents, qu'on fait tous les deux.",
    f"""
    <h2>Haies de rue aux Couëts et dans le bourg</h2>
    <p>Les quartiers des Couëts et du bourg ont été bâtis en grande partie entre 1960 et 1990. Les haies de cyprès, de thuyas et de troènes y longent souvent le trottoir. Quand elles avancent sur la voie, c'est au propriétaire de les faire reculer, et un piéton avec une poussette ne doit pas avoir à descendre sur la route.</p>

    <h2>Haies champêtres côté Loire</h2>
    <p>Vers Port-Lavigne et les secteurs agricoles du sud de la commune, on trouve des haies d'ormes, de prunelliers et de saules, parfois plantées sur un fossé. On les reprend au lamier ou à la tronçonneuse, en gardant les arbres de haut jet quand ils sont sains.</p>

    <h2>Exemple de chantier type à Bouguenais</h2>
    <p>Une haie de troènes et de cyprès de 40 m le long d'une rue des Couëts, qui déborde de 80 cm sur le trottoir : face rue ramenée à l'aplomb du muret, dessus remis à 1,80 m, branchages chargés et emportés le jour même.</p>
    {NOTE_EX}
    {CTA.format("Votre haie déborde sur la rue ?")}

    <h2>Prix indicatifs à Bouguenais</h2>
    {prix([H30, ("Haie champêtre ou haie sur fossé", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Quand tailler et que faire des déchets</h2>
    <p>Pour une haie de jardin, deux passages par an suffisent : fin d'hiver et septembre. Pour une haie de bocage, on intervient l'hiver, hors période de nidification. Les déchèteries les plus proches sont celles de Rezé, rue Pierre Legendre, et de Saint-Jean-de-Boisseau (horaires à vérifier) ; avec nous, tout est emporté.</p>
""",
    [("Ma haie déborde sur le trottoir, suis-je obligé de la tailler ?",
      "Oui. Les plantations qui avancent sur la voie publique doivent être coupées à l'aplomb de la limite par le propriétaire."),
     ("Faites-vous les haies de saules au bord des fossés ?",
      "Oui, en hiver, au lamier ou à la tronçonneuse. On peut garder le bois si vous en voulez.")],
    "Une haie à tailler à Bouguenais ?")


ajoute("haie", "cordemais",
    "Taille de haie à Cordemais : bocage et brise-vent",
    "Taille de haies à Cordemais : haies brise-vent face à l'estuaire, haies bocagères au nord, thuyas du bourg. Nacelle si besoin, ramassage compris.",
    "Taille de haies à Cordemais",
    "À Cordemais, beaucoup de haies ont un rôle précis : arrêter le vent qui remonte de l'estuaire. On les taille pour qu'elles gardent ce rôle, pas seulement pour qu'elles soient jolies.",
    f"""
    <h2>Des haies qui protègent du vent</h2>
    <p>Entre le bourg et les marais, les maisons sont souvent abritées par des haies de cyprès de Lambert, de chênes verts ou de grands thuyas. Une haie brise-vent fonctionne mieux quand elle laisse passer un peu d'air : trop dense et trop haute, elle crée des tourbillons et prend tout le vent. On la garde fournie, mais pas en mur.</p>
    <p>Au nord de la commune, vers le bocage, les haies sont plus variées : chênes, frênes, noisetiers, houx.</p>

    <h2>Exemple de chantier type à Cordemais</h2>
    <p>Une haie de cyprès de Lambert de 60 m qui abrite une longère, montée à 7 m, avec des branches cassées après l'hiver : réduction du dessus à la nacelle, retrait des branches cassées, faces reprises, bois broyé et emporté.</p>
    {NOTE_EX}
    {CTA.format("Une haie brise-vent à reprendre ?")}

    <h2>La bonne période près des marais</h2>
    <p>Les marais de l'estuaire sont un grand site pour les oiseaux. On taille donc en fin d'été et en automne, ou en hiver pour les haies champêtres, et on évite le printemps. Les terrains bas restent mouillés longtemps : la nacelle ne passe qu'une fois le sol ressuyé.</p>

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie brise-vent de plus de 4 m, à la nacelle", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Les déchets</h2>
    <p>Cordemais dépend de la Communauté de communes Estuaire et Sillon. Une haie brise-vent de 60 m représente plusieurs remorques : on broie sur place et on emporte, c'est compris dans le prix.</p>
""",
    [("Faut-il garder une haie brise-vent très haute ?",
      "Pas forcément. Une haie de 3 à 4 m bien garnie protège déjà un jardin. Au-delà, elle prend beaucoup de vent et casse plus."),
     ("Peut-on tailler un cyprès de Lambert sévèrement ?",
      "Comme le thuya, il ne repart pas du bois sans feuilles. On réduit la hauteur franchement, mais les côtés restent dans le vert.")],
    "Une haie à tailler à Cordemais ?")


ajoute("haie", "la-chapelle-sur-erdre",
    "Taille de haie à La Chapelle-sur-Erdre | Jean Ferret",
    "Taille de haies à La Chapelle-sur-Erdre : lauriers et photinias des lotissements, bambous envahissants, haies de propriété près de l'Erdre. Devis gratuit.",
    "Taille de haies à La Chapelle-sur-Erdre",
    "De la Gesvrine aux propriétés de bord d'Erdre, les haies chapelaines sont très variées. Une particularité ici : beaucoup de haies de bambous, plantées pour aller vite, qui finissent par envahir le jardin.",
    f"""
    <h2>Les haies qu'on rencontre</h2>
    <p>Dans les quartiers récents, autour de la Babinière et de la Gesvrine, ce sont surtout des lauriers-palmes, des photinias et des elaeagnus. Dans les propriétés plus anciennes, en pente vers l'Erdre, on trouve des haies libres de noisetiers, de cornouillers et de viornes, mélangées sous de grands arbres.</p>

    <h2>Le cas des bambous</h2>
    <p>Un bambou traçant, planté sans barrière anti-rhizome, gagne un à deux mètres par an et passe sous la clôture chez le voisin. On peut le tailler en hauteur et en largeur, mais pour l'arrêter il faut couper les rhizomes en bordure, ou l'arracher entièrement. On vous dit franchement ce qui est réaliste selon l'âge de la touffe.</p>

    <h2>Exemple de chantier type à La Chapelle-sur-Erdre</h2>
    <p>Une haie de bambous de 15 m qui a traversé la clôture et pousse dans la pelouse voisine : coupe de toutes les tiges, découpe des rhizomes sur 40 cm de profondeur côté voisin, pose d'une barrière anti-rhizome, déchets évacués.</p>
    {NOTE_EX}
    {CTA.format("Des bambous ou une haie qui déborde ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Bambous à contenir ou à arracher", "sur devis, après photo")], "Fourchette, déchets emportés")}

    <h2>Près de l'Erdre</h2>
    <p>La vallée de l'Erdre est protégée : supprimer une haie en bord de rivière peut demander une démarche, alors que la tailler n'en demande pas. Les déchets verts peuvent aller à la déchèterie de la Gesvrine, rue Ampère, réservée aux habitants de la Métropole (horaires à vérifier). Les tiges de bambou ne se compostent pas bien : on les emporte.</p>
""",
    [("Peut-on se débarrasser définitivement de bambous ?",
      "Oui, mais il faut sortir tous les rhizomes, ce qui revient à un petit terrassement. Sinon, une barrière anti-rhizome bien posée les contient."),
     ("Taillez-vous les haies libres sans leur donner une forme carrée ?",
      "Oui. On éclaircit et on raccourcit les branches trop longues en gardant l'aspect naturel de la haie.")],
    "Une haie à tailler à La Chapelle-sur-Erdre ?")


ajoute("haie", "la-montagne",
    "Taille de haie à La Montagne : jardins en coteau",
    "Taille de haies à La Montagne : haies sur murets et en terrasses, accès étroits, matériel porté à la main. Déchets descendus et emportés, devis gratuit.",
    "Taille de haies à La Montagne",
    "Sur le coteau de La Montagne, la haie est souvent posée en haut d'un muret ou au bord d'une terrasse. La tailler demande surtout de bien se placer, et de penser à la sortie des déchets.",
    f"""
    <h2>Des haies en hauteur</h2>
    <p>Beaucoup de jardins de la commune sont en paliers. Une haie de 2 m en haut d'un mur de 1,50 m fait, vue d'en bas, plus de 3 m. Les essences sont classiques, lauriers, thuyas, troènes, avec du lierre qui grimpe dans les haies anciennes et les alourdit.</p>

    <h2>Comment on s'y prend</h2>
    <p>Pas de nacelle dans les rues étroites du coteau : on travaille sur échafaudage roulant posé sur le palier, ou avec un taille-haie sur perche. Bâches au pied pour que les feuilles ne tombent pas dans le jardin du dessous. Les déchets sont mis en sacs et descendus à la main jusqu'au camion.</p>

    <h2>Exemple de chantier type à La Montagne</h2>
    <p>Une haie de lauriers de 20 m posée en haut d'un mur de soutènement, envahie de lierre, qui retombe sur le jardin du voisin en contrebas : retrait du lierre, réduction de la hauteur et de la face côté voisin, sacs descendus par l'escalier.</p>
    {NOTE_EX}
    {CTA.format("Une haie difficile d'accès ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie sur mur ou sans accès véhicule", "sur devis, souvent un peu plus")], "Fourchette, ramassage compris")}

    <h2>Lierre, murs et déchets</h2>
    <p>Le lierre tient l'humidité contre les murs et pèse lourd dans une haie. On le coupe au pied et on l'arrache des branches. La déchèterie de La Montagne, chemin du Pérou, est réservée aux particuliers de Nantes Métropole (horaires à vérifier). Pour une haie entière, on emporte tout.</p>
""",
    [("Le lierre abîme-t-il ma haie ?",
      "Oui, à la longue il l'étouffe et la rend plus lourde. On le coupe à la base et on retire ce qui est accroché."),
     ("Pouvez-vous tailler sans passer par le jardin du voisin du dessous ?",
      "Souvent oui, avec un taille-haie sur perche depuis votre palier. Pour une face très haute, son accord facilite le travail.")],
    "Une haie à tailler à La Montagne ?")


ajoute("haie", "lavau-sur-loire",
    "Taille de haie à Lavau-sur-Loire | Jean Ferret Paysage",
    "Taille de haies à Lavau-sur-Loire : saules têtards, haies de tamaris et de frênes en bord de marais, taille en hiver. Bois évacué, devis gratuit.",
    "Taille de haies à Lavau-sur-Loire",
    "À Lavau, les haies sont faites pour un pays de marais : saules, frênes, aubépines et tamaris, qui supportent l'eau et le vent. On les entretient en hiver.",
    f"""
    <h2>Les haies du village et des marais</h2>
    <p>Autour du bourg, on taille des haies de tamaris et d'arbustes résistants au vent salé qui remonte l'estuaire. Le long des fossés et des chemins, ce sont des saules têtards et des frênes, conduits depuis des générations. Les jardins du village ont aussi leurs haies de lauriers et de troènes, comme partout.</p>

    <h2>Exemple de chantier type à Lavau-sur-Loire</h2>
    <p>Une ligne de huit saules têtards au bord d'un fossé, pas coupés depuis dix ans, dont les branches commencent à fendre la tête : recépage de toutes les perches en hiver, bois laissé en fagots ou évacué selon le souhait du propriétaire.</p>
    {NOTE_EX}
    {CTA.format("Des têtards ou une haie à reprendre ?")}

    <h2>Tailler en respectant le marais</h2>
    <p>On intervient de novembre à février, quand la faune est la moins dérangée. Les chemins de marais ne portent pas toujours un véhicule en hiver : on porte le matériel et on attend parfois quelques jours de sec. Une haie en bordure de zone naturelle peut être protégée : la tailler ne pose pas de problème, l'arracher demande une vérification.</p>

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Saules têtards, prix par arbre", "sur devis, selon le nombre")], "Fourchette, déchets compris")}

    <h2>Le bois et les déchets</h2>
    <p>Le bois de saule et de frêne fait de bons fagots pour l'allumage. On peut le laisser sur place. Sinon tout est emporté : la déchèterie de Savenay (Estuaire et Sillon) reste la plus proche, horaires à vérifier.</p>
""",
    [("Tous les combien recoupe-t-on un saule têtard ?",
      "Tous les cinq à sept ans environ. Au-delà, les perches deviennent lourdes et la tête risque de se fendre."),
     ("Taillez-vous les tamaris ?",
      "Oui, après la floraison pour les tamaris d'été, ou en fin d'hiver. Ils supportent une taille franche.")],
    "Une haie à tailler à Lavau-sur-Loire ?")


ajoute("haie", "le-pellerin",
    "Taille de haie au Pellerin : bourg et canal | Jean Ferret",
    "Taille de haies au Pellerin : haies de jardins du bourg, haies champêtres du coteau, haies le long du canal de la Martinière. Ramassage compris.",
    "Taille de haies au Pellerin",
    "Au Pellerin, on taille aussi bien la petite haie de troènes d'une maison de quai que la longue haie champêtre d'une propriété du coteau.",
    f"""
    <h2>Trois paysages, trois sortes de haies</h2>
    <p>Dans le bourg, les jardins des maisons de quai sont étroits et fermés par des haies basses ou des murs doublés d'arbustes. Sur le coteau qui monte vers Saint-Jean-de-Boisseau, les propriétés ont des haies champêtres de chênes, de châtaigniers et de noisetiers. Le long du canal de la Martinière, les terrains humides sont bordés de saules et d'aulnes.</p>

    <h2>Notre façon de faire</h2>
    <p>Pour une haie de jardin, taille au taille-haie sur les deux faces et le dessus. Pour une haie champêtre, on raccourcit les branches qui envahissent le chemin ou le champ, on enlève le bois mort et on garde les beaux sujets. Au bord du canal, on travaille hors période de nidification.</p>

    <h2>Exemple de chantier type au Pellerin</h2>
    <p>Une haie champêtre de 80 m le long d'un chemin du coteau, qui gêne le passage d'un tracteur : élagage des branches basses au-dessus du chemin, reprise de la face côté chemin au lamier, bois de chauffage laissé en tas.</p>
    {NOTE_EX}
    {CTA.format("Une haie à reprendre au Pellerin ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie champêtre longue, au mètre", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Déchets verts au Pellerin</h2>
    <p>Les déchèteries de Saint-Jean-de-Boisseau et de La Montagne sont les plus proches, réservées aux particuliers de la Métropole (horaires à vérifier). Brûler ses déchets verts dans le jardin est interdit : on les emporte avec le chantier.</p>
""",
    [("Une haie champêtre doit-elle être taillée chaque année ?",
      "Non. Une reprise tous les deux ou trois ans suffit souvent, sauf le long d'un chemin ou d'une route."),
     ("Peut-on brûler les branches de sa haie ?",
      "Non, le brûlage des déchets verts est interdit. On les emporte, c'est compris dans le prix.")],
    "Une haie à tailler au Pellerin ?")


ajoute("haie", "le-temple-de-bretagne",
    "Taille de haie au Temple-de-Bretagne | Jean Ferret",
    "Taille de haies au Temple-de-Bretagne : haies écran le long de la voie express, eleagnus et thuyas des lotissements. Ramassage compris, devis gratuit.",
    "Taille de haies au Temple-de-Bretagne",
    "Au Temple-de-Bretagne, beaucoup de haies ont été plantées pour se protéger du bruit et de la vue de la route de Vannes. Elles ont bien poussé, parfois trop.",
    f"""
    <h2>Des haies écran</h2>
    <p>Les lotissements proches de la voie express ont souvent une haie épaisse en fond de terrain : eleagnus, lauriers, photinias, parfois doublés de thuyas. Ces haies poussent vite et finissent par prendre deux mètres de large. Une haie ne coupe pas vraiment le bruit, mais elle cache la route et arrête la poussière : on la garde dense en la reprenant régulièrement.</p>

    <h2>Exemple de chantier type au Temple-de-Bretagne</h2>
    <p>Une haie d'eleagnus et de lauriers de 35 m en fond de jardin, côté voie express, haute de 3,50 m et large de 2 m : réduction de la largeur côté jardin, dessus ramené à 2,50 m pour garder l'écran, branchages broyés et emportés.</p>
    {NOTE_EX}
    {CTA.format("Votre haie écran a trop grossi ?")}

    <h2>L'eleagnus, champion de la pousse</h2>
    <p>L'eleagnus fait de longues tiges qui partent dans tous les sens dès le printemps. Deux tailles par an, en juin après la nidification et en septembre, le gardent net. Il accepte une coupe dans le vieux bois, ce qui permet de rattraper une haie négligée en une saison.</p>

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie écran à réduire en largeur", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Déchets et règles</h2>
    <p>La commune dépend des déchèteries d'Estuaire et Sillon. Pour une haie de fond de terrain, le plus simple est de nous laisser tout emporter. Si vous voulez remplacer la haie par une clôture, le plan local d'urbanisme fixe la hauteur et l'aspect : vérifiez en mairie avant.</p>
""",
    [("Une haie arrête-t-elle le bruit de la route ?",
      "Très peu. Elle cache la route et filtre la poussière, mais pour le bruit il faudrait un mur ou un talus."),
     ("Quand tailler un eleagnus ?",
      "Fin juin, après la nidification, puis en septembre. Il supporte bien une taille sévère.")],
    "Une haie à tailler au Temple-de-Bretagne ?")


ajoute("haie", "les-sorinieres",
    "Taille de haie aux Sorinières : photinias, lauriers",
    "Taille de haies aux Sorinières : photinias malades, lauriers et thuyas de lotissement, règles de hauteur à respecter. Déchets emportés, devis gratuit.",
    "Taille de haies aux Sorinières",
    "Aux Sorinières, la plupart des haies ont moins de 25 ans. Elles sont encore jeunes, mais certaines ont déjà un souci : les photinias qui perdent leurs feuilles.",
    f"""
    <h2>Le photinia et ses taches</h2>
    <p>Le photinia « Red Robin » a été planté partout dans les lotissements des Sorinières. Beaucoup souffrent d'une maladie des feuilles, l'entomosporiose : des petites taches rouges, puis les feuilles jaunissent et tombent. La haie se dégarnit par le bas. Une taille qui aère, le ramassage des feuilles malades et un arrosage au pied plutôt que sur le feuillage limitent la casse. Quand la haie est trop atteinte, on peut la remplacer.</p>

    <h2>Une taille dans les règles du lotissement</h2>
    <p>Le règlement de lotissement fixe souvent une hauteur maximale, 1,80 m ou 2 m. On taille à cette hauteur, au cordeau, pour que la haie soit propre côté rue comme côté voisin.</p>

    <h2>Exemple de chantier type aux Sorinières</h2>
    <p>Une haie de photinias de 30 m, dégarnie à la base et tachée, en limite d'un jardin de lotissement : taille d'éclaircie, ramassage soigné des feuilles tombées, évacuation, conseils pour remplacer les sujets morts.</p>
    {NOTE_EX}
    {CTA.format("Votre photinia perd ses feuilles ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Arrachage d'une haie malade, souches comprises", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Les déchets</h2>
    <p>Les feuilles malades ne doivent pas aller au compost du jardin. On les emporte. Si vous y allez vous-même, les déchèteries de Rezé et de Vertou sont les plus proches, réservées aux particuliers de la Métropole (horaires à vérifier).</p>
""",
    [("Mon photinia a des taches rouges, est-il perdu ?",
      "Pas forcément. Si la haie garde la moitié de ses feuilles, une taille d'aération et le ramassage des feuilles malades suffisent souvent."),
     ("Par quoi remplacer une haie de photinias malade ?",
      "Une haie mélangée (charme, troène, viorne, eleagnus) résiste mieux aux maladies qu'une haie d'une seule espèce.")],
    "Une haie à tailler aux Sorinières ?")


ajoute("haie", "malville",
    "Taille de haie à Malville : haies sur talus | Jean Ferret",
    "Taille de haies à Malville : haies bocagères sur talus, chemins creux, thuyas des lotissements du bourg. Lamier ou taille-haie, bois évacué ou laissé.",
    "Taille de haies à Malville",
    "Malville a gardé beaucoup de haies sur talus le long des chemins creux. Entre les hameaux et le bourg, on taille aussi bien ces vieilles haies que des thuyas de lotissement.",
    f"""
    <h2>Les haies sur talus</h2>
    <p>Une haie sur talus retient la terre, l'eau et abrite le bétail. Celles de Malville mêlent chênes, châtaigniers, houx et noisetiers. Avec le temps, les branches avancent au-dessus du chemin et frottent les véhicules. On les reprend à la verticale du talus, au lamier, sans toucher aux racines qui tiennent la terre.</p>

    <h2>Dans le bourg</h2>
    <p>Autour du bourg, les lotissements récents ont des haies de thuyas et de photinias plantées en même temps que les maisons. Elles arrivent à l'âge où elles dépassent 2,50 m : c'est le moment de les ramener à une hauteur qu'on peut entretenir soi-même.</p>

    <h2>Exemple de chantier type à Malville</h2>
    <p>150 m de haie sur talus le long d'un chemin d'accès à un hameau, qui empêche le passage d'un camion de livraison : reprise de la face côté chemin et du dessus, branches de chêne coupées en bûches, broyat laissé au pied du talus.</p>
    {NOTE_EX}
    {CTA.format("Un chemin envahi par la haie ?")}

    <h2>Ce que dit la règle</h2>
    <p>L'entretien d'une haie sur talus est libre. L'arracher, ou araser le talus, peut demander une déclaration, surtout si la haie est repérée au plan local d'urbanisme. On le vérifie avec vous. Pour les haies le long des champs, la taille se fait en dehors du printemps et de l'été.</p>

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie sur talus, longueur importante", "sur devis, au mètre")], "Fourchette, ramassage compris")}

    <h2>Les déchets</h2>
    <p>Malville a une aire de déchets verts gérée par Estuaire et Sillon (horaires à vérifier). Sur un grand terrain, le broyat peut aussi rester sur place en paillage.</p>
""",
    [("Faut-il une autorisation pour tailler une haie sur talus ?",
      "Non, l'entretien est libre. C'est l'arrachage ou la destruction du talus qui peut demander une démarche."),
     ("Peut-on garder le broyat ?",
      "Oui. Étalé au pied des haies ou dans les massifs, il garde l'humidité et limite les mauvaises herbes.")],
    "Une haie à tailler à Malville ?")


ajoute("haie", "reze",
    "Taille de haie à Rezé : Ragon, Pont-Rousseau | Jean Ferret",
    "Taille de haies à Rezé : haies mitoyennes de Pont-Rousseau, lauriers de Ragon, petites haies de Trentemoult sans accès. Ramassage compris, devis gratuit.",
    "Taille de haies à Rezé",
    "À Rezé, les haies sont souvent courtes mais difficiles : un jardin étroit, une maison mitoyenne, et la haie qui sépare deux terrains depuis cinquante ans.",
    f"""
    <h2>Haies de ville et haies de quartier</h2>
    <p>À Pont-Rousseau et autour de la Houssais, les jardins en lanière sont séparés par des haies de troènes, de lauriers-tins ou de fusains, souvent plus vieilles que les propriétaires actuels. Vers Ragon et la Blordière, les maisons des années 1970 ont des haies de thuyas et de lauriers-palmes plus hautes. À Trentemoult, la haie est souvent une simple bordure, mais tout se fait à pied.</p>

    <h2>Travailler dans un jardin en lanière</h2>
    <p>On arrive avec du matériel léger : taille-haie sur batterie, moins bruyant pour les voisins proches, escabeau à trois pieds et bâches. Les déchets sortent en sacs par le couloir ou le garage. Quand la haie est mitoyenne, on propose de faire les deux faces le même jour.</p>

    <h2>Exemple de chantier type à Rezé</h2>
    <p>Une vieille haie de troènes de 25 m entre deux jardins de Pont-Rousseau, haute de 3 m et très dégarnie du bas : rabattage à 1,60 m pour la faire repartir de la base, reprise des deux faces avec l'accord du voisin, déchets sortis par le garage.</p>
    {NOTE_EX}
    {CTA.format("Une haie mitoyenne à reprendre ?")}

    <h2>Prix indicatifs à Rezé</h2>
    {prix([H30, ("Petite haie de ville, accès à pied", "sur devis, souvent moins")], "Fourchette, ramassage compris")}

    <h2>Déchets verts</h2>
    <p>La déchèterie de Rezé est rue Pierre Legendre, réservée aux particuliers de la Métropole (horaires à vérifier). Avec nous, rien à transporter : les déchets partent avec le chantier.</p>
""",
    [("Un vieux troène peut-il être rabattu sévèrement ?",
      "Oui, le troène repart très bien du vieux bois. Rabattu en fin d'hiver, il se regarnit dès l'été."),
     ("Utilisez-vous du matériel silencieux ?",
      "Pour les jardins de ville, on privilégie le taille-haie sur batterie, nettement moins bruyant que le thermique.")],
    "Une haie à tailler à Rezé ?")


ajoute("haie", "saint-jean-de-boisseau",
    "Taille de haie à Saint-Jean-de-Boisseau | Jean Ferret",
    "Taille de haies à Saint-Jean-de-Boisseau : haies de cyprès des chemins creux, photinias des lotissements, haies vives du pays de Retz. Devis gratuit.",
    "Taille de haies à Saint-Jean-de-Boisseau",
    "Saint-Jean-de-Boisseau est à la frontière du pays de Retz : des chemins creux bordés de haies vives, et des lotissements où chaque terrain a sa haie de photinias.",
    f"""
    <h2>Les haies de la commune</h2>
    <p>Les anciens chemins qui descendent vers la Loire sont bordés de haies vives : aubépine, prunellier, sureau, avec des châtaigniers de place en place. Dans les quartiers plus récents, les haies sont surtout en photinias, lauriers et cyprès de Leyland, ces derniers ayant souvent dépassé les 4 m.</p>

    <h2>Réduire un cyprès de Leyland</h2>
    <p>Le cyprès de Leyland pousse très vite. On peut le rabaisser fortement en hauteur, à la nacelle, mais ses côtés ne repartent pas du bois nu : on reste dans le vert. Quand une haie de Leyland est trop large pour le terrain, la seule vraie solution est souvent de l'abattre et de replanter.</p>

    <h2>Exemple de chantier type à Saint-Jean-de-Boisseau</h2>
    <p>Une haie de cyprès de Leyland de 30 m, haute de 6 m, qui coupe le soleil du potager l'après-midi : réduction à 2,50 m à la nacelle, reprise des deux faces dans le vert, broyage et évacuation de plusieurs remorques.</p>
    {NOTE_EX}
    {CTA.format("Une haie trop haute qui fait de l'ombre ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Réduction d'une haie de plus de 4 m", "sur devis, après photo"), ("Abattage de la haie et des souches", "sur devis")], "Fourchette, ramassage compris")}

    <h2>Déchets</h2>
    <p>La déchèterie de Saint-Jean-de-Boisseau, rue de la Poterie, est réservée aux particuliers de la Métropole (horaires à vérifier). Une haie de Leyland réduite de moitié, c'est beaucoup de volume : on broie sur place et on emporte.</p>
""",
    [("Mon voisin peut-il exiger que je réduise ma haie de cyprès ?",
      "Oui, si elle fait plus de 2 m de haut à moins de 2 m de la limite. Il peut aussi demander la coupe des branches qui avancent chez lui."),
     ("Une haie vive de chemin creux se taille-t-elle comme une haie de jardin ?",
      "Non, on la reprend plus librement, en hiver, en gardant sa forme naturelle et les arbres de haut jet.")],
    "Une haie à tailler à Saint-Jean-de-Boisseau ?")


ajoute("haie", "saint-sebastien-sur-loire",
    "Taille de haie à Saint-Sébastien-sur-Loire | Jean Ferret",
    "Taille de haies à Saint-Sébastien-sur-Loire : thuyas mitoyens dégarnis, lauriers des quartiers pavillonnaires, haies des bords de Loire. Devis gratuit.",
    "Taille de haies à Saint-Sébastien-sur-Loire",
    "À Saint-Sébastien, le grand sujet, c'est le thuya mitoyen : planté dans les années 1980, il fait aujourd'hui 4 m et il est vide du bas. Que faire ? On vous aide à choisir.",
    f"""
    <h2>Garder, rabaisser ou remplacer ?</h2>
    <p>Un thuya dégarni du bas ne se regarnira pas : il ne repart pas du bois sans feuilles. On a trois options. Le rabaisser à 2 m et garder les faces vertes, si elles le sont encore. Le doubler par une jeune haie ou un claustra côté jardin. Ou l'abattre et le remplacer par une haie mélangée ou une clôture. On regarde avec vous ce que donne chaque solution.</p>

    <h2>Haies proches de la Loire</h2>
    <p>Vers les bords de Loire, les terrains sont plus humides et les haies plus libres : saules, cornouillers, sureaux. Elles poussent vite et se reprennent en hiver, quand le sol porte.</p>

    <h2>Exemple de chantier type à Saint-Sébastien-sur-Loire</h2>
    <p>Une haie de thuyas mitoyenne de 22 m, haute de 4 m et vide jusqu'à 1,50 m : réduction à 2 m de haut, reprise des faces vertes, pose de panneaux claustras devant la partie dégarnie côté terrasse.</p>
    {NOTE_EX}
    {CTA.format("Votre thuya est vide du bas ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Arrachage d'une haie de thuyas avec souches", "sur devis"), ("Pose de claustras, main-d'œuvre", "à partir de 40 € le mètre")], "Fourchette, déchets emportés")}

    <h2>Les déchets</h2>
    <p>Les déchèteries de Nantes Métropole sont réservées aux habitants de la Métropole, avec des limites de volume. Une haie de thuyas réduite de 2 m, c'est souvent plus d'une remorque : on s'en charge.</p>
""",
    [("Mon thuya est marron d'un côté, va-t-il repartir ?",
      "Si le marron vient d'une taille trop courte, non. Si c'est une sécheresse ponctuelle, il peut reverdir au printemps. Une photo suffit pour un premier avis."),
     ("Pouvez-vous poser une clôture à la place de la haie ?",
      "Oui : arrachage, souches, puis pose de la clôture ou des claustras sur le même tracé.")],
    "Une haie à tailler à Saint-Sébastien-sur-Loire ?")


ajoute("haie", "sainte-luce-sur-loire",
    "Taille de haie à Sainte-Luce-sur-Loire | Jean Ferret",
    "Taille de haies à Sainte-Luce-sur-Loire : premières tailles de haies jeunes, eleagnus et photinias des quartiers récents. Ramassage compris, devis gratuit.",
    "Taille de haies à Sainte-Luce-sur-Loire",
    "Sainte-Luce a beaucoup de quartiers récents, donc beaucoup de haies jeunes. Bien taillées dans leurs premières années, elles restent faciles à vivre pendant trente ans.",
    f"""
    <h2>Former une haie jeune</h2>
    <p>Une haie de 5 à 10 ans se taille un peu plus large en bas qu'en haut, et on ne la laisse pas monter d'un coup : on la fait grimper de 20 ou 30 cm par an jusqu'à la hauteur voulue. C'est ce qui évite les haies vides du pied qu'on voit partout. Dans les quartiers de la commune, les plantations les plus courantes sont l'eleagnus, le photinia, le laurier-tin et l'abélia.</p>

    <h2>Haies plus anciennes</h2>
    <p>Les maisons plus anciennes, vers la Loire ou côté Thouaré, ont des haies de charmes, de lauriers-palmes ou de thuyas. Là, on travaille plutôt en reprise : hauteur, largeur, et parfois un rabattage franc.</p>

    <h2>Exemple de chantier type à Sainte-Luce-sur-Loire</h2>
    <p>Une haie mélangée de 40 m plantée il y a six ans autour d'un jardin neuf, jamais taillée : taille de formation en trapèze, réglage de la hauteur à 1,60 m, ramassage, et un calendrier de taille laissé au propriétaire.</p>
    {NOTE_EX}
    {CTA.format("Une jeune haie à former ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie jeune, taille de formation", "sur devis, souvent moins")], "Fourchette, ramassage compris")}

    <h2>Déchets et règles</h2>
    <p>Une haie qui déborde sur le trottoir doit être taillée par le propriétaire. Les déchèteries de Nantes Métropole sont réservées aux particuliers de la Métropole, horaires à vérifier. Sinon, on emporte tout.</p>
""",
    [("À quel âge faut-il commencer à tailler une haie ?",
      "Dès la deuxième année. Une taille légère chaque année fait une haie dense de la base jusqu'en haut."),
     ("Pouvez-vous passer tous les ans ?",
      "Oui. Beaucoup de clients nous font venir une ou deux fois par an pour la même haie.")],
    "Une haie à tailler à Sainte-Luce-sur-Loire ?")


ajoute("haie", "savenay",
    "Taille de haie à Savenay : haies en pente | Jean Ferret",
    "Taille de haies à Savenay : haies sur les terrains en pente du Sillon, ajoncs et genêts, lauriers des quartiers récents. Déchets remontés et emportés.",
    "Taille de haies à Savenay",
    "Sur le Sillon de Bretagne, une haie se taille rarement sur du plat. À Savenay, la pente change la façon de travailler, et la façon de ramasser.",
    f"""
    <h2>Tailler dans la pente</h2>
    <p>Entre le centre et le bas du coteau, beaucoup de jardins descendent vers l'estuaire. Une haie qui suit la pente doit être taillée en suivant le terrain, pas à l'horizontale, sinon elle paraît bancale. On installe l'échafaudage sur des pieds réglables et on ramasse en remontant, sur bâche.</p>

    <h2>Les essences du Sillon</h2>
    <p>Le sol du coteau est pauvre et sec, souvent rocheux. Les haies anciennes y sont faites d'essences rustiques : chênes, houx, ajoncs, genêts, prunelliers. Dans les lotissements, lauriers, photinias et thuyas souffrent plus des étés secs qu'ailleurs, et une taille trop courte en plein été les fait roussir.</p>

    <h2>Exemple de chantier type à Savenay</h2>
    <p>Une haie de lauriers-palmes de 28 m qui descend le long d'un jardin en pente, haute de 3 m en bas et 2 m en haut : remise à une hauteur régulière qui suit la pente, faces reprises, déchets remontés en big-bags jusqu'à la rue.</p>
    {NOTE_EX}
    {CTA.format("Une haie dans un jardin en pente ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie en forte pente ou sans accès", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Période et déchets</h2>
    <p>Sur un sol sec, on évite de tailler en pleine chaleur : fin d'hiver et septembre restent les meilleurs moments. Savenay a une déchèterie gérée par Estuaire et Sillon (horaires à vérifier). On peut aussi tout emporter.</p>
""",
    [("Pourquoi ma haie roussit après la taille ?",
      "Souvent parce qu'elle a été taillée en pleine chaleur ou trop court. Sur le coteau, mieux vaut tailler en fin d'hiver ou en septembre."),
     ("Pouvez-vous tailler une haie d'ajoncs ?",
      "Oui, au taille-haie ou au lamier, avec des gants épais. L'ajonc se taille juste après sa floraison.")],
    "Une haie à tailler à Savenay ?")


ajoute("haie", "suce-sur-erdre",
    "Taille de haie à Sucé-sur-Erdre | Jean Ferret Paysage",
    "Taille de haies à Sucé-sur-Erdre : haies de propriétés au bord de l'Erdre, haies de hameaux, thuyas du bourg. Bateau ou ponton pas gênants, devis gratuit.",
    "Taille de haies à Sucé-sur-Erdre",
    "À Sucé, beaucoup de haies descendent jusqu'à l'eau. On les taille côté jardin comme côté rivière, en faisant attention à ce qui tombe dans l'Erdre.",
    f"""
    <h2>Des haies au bord de l'eau</h2>
    <p>Les propriétés qui longent l'Erdre ont souvent une haie de séparation qui descend jusqu'à la berge, avec un ponton ou une cale au bout. On travaille sur la pente avec des bâches et des filets pour que rien ne finisse dans la rivière. Les haies de berge, saules et aulnes, se taillent en hiver, en laissant les racines tenir le sol.</p>

    <h2>Dans le bourg et les hameaux</h2>
    <p>Les lotissements autour du bourg ont des haies de thuyas et de lauriers qui ont souvent attendu quelques années de trop. Dans les hameaux, ce sont des haies bocagères de chênes et de noisetiers, plus libres.</p>

    <h2>Exemple de chantier type à Sucé-sur-Erdre</h2>
    <p>Une haie de lauriers de 45 m qui sépare deux propriétés jusqu'à la berge, haute de 4 m côté rivière : réduction à la nacelle depuis le haut du terrain, finition en bas au taille-haie sur perche, filets posés au bord de l'eau, déchets remontés.</p>
    {NOTE_EX}
    {CTA.format("Une haie qui descend jusqu'à l'Erdre ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie en bord de rivière, accès difficile", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Règles et déchets</h2>
    <p>Les abords de l'Erdre sont protégés : tailler ne pose pas de problème, arracher une haie de berge peut demander une démarche. Sucé dépend des déchèteries d'Erdre et Gesvres ; celle de Sucé est annoncée en travaux, vérifiez avant de vous déplacer. Avec nous, les déchets sont emportés.</p>
""",
    [("Laissez-vous tomber des branches dans l'Erdre ?",
      "Non. On pose des filets et des bâches côté berge, et on ramasse tout ce qui tombe près de l'eau."),
     ("Peut-on arracher une haie de bord de rivière ?",
      "Ça demande une vérification en mairie, car les berges de l'Erdre sont protégées. La tailler, en revanche, est libre.")],
    "Une haie à tailler à Sucé-sur-Erdre ?")


ajoute("haie", "treillieres",
    "Taille de haie à Treillières : lotissements | Jean Ferret",
    "Taille de haies à Treillières : thuyas et cyprès des lotissements de 20 à 30 ans, haies bocagères du Gesvres. Réduction en hauteur, ramassage compris.",
    "Taille de haies à Treillières",
    "Treillières a beaucoup grandi dans les années 1990 et 2000. Les haies plantées à ce moment-là arrivent toutes au même âge : celui où elles deviennent trop hautes pour une échelle.",
    f"""
    <h2>Des haies arrivées à 4 mètres</h2>
    <p>Dans les lotissements de Treillières, les haies de thuyas, de cyprès et de lauriers plantées à la construction font souvent 3,50 à 4,50 m. Le propriétaire n'arrive plus à tailler le dessus, et la haie s'élargit chaque année. On la ramène à une hauteur raisonnable en une fois, puis on l'entretient, ou on vous laisse l'entretenir vous-même.</p>

    <h2>Le long du Gesvres</h2>
    <p>Vers le Gesvres et dans les hameaux, les haies bocagères sont plus anciennes : chênes, frênes, aubépines. Elles se reprennent l'hiver, en douceur, en gardant leur rôle pour les oiseaux.</p>

    <h2>Exemple de chantier type à Treillières</h2>
    <p>Une haie de thuyas de 32 m autour d'un jardin de lotissement, haute de 4 m : réduction à 2 m à la nacelle, reprise des trois faces visibles, broyage et évacuation, conseils pour l'entretien annuel.</p>
    {NOTE_EX}
    {CTA.format("Une haie devenue trop haute ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Réduction forte d'une haie de plus de 4 m", "sur devis, après photo")], "Fourchette, ramassage compris")}

    <h2>Déchets verts</h2>
    <p>Treillières dépend des déchèteries d'Erdre et Gesvres ; celle de Vigneux-de-Bretagne est l'une des plus proches (horaires à vérifier). Une réduction de 2 m sur 30 m de thuyas, c'est plusieurs remorques : on s'en occupe.</p>
""",
    [("Peut-on réduire un thuya de moitié en hauteur ?",
      "Oui, en hauteur le thuya le supporte. Le dessus restera un peu plat et brun quelques mois, puis les côtés le recouvrent."),
     ("Pouvez-vous venir chaque année ?",
      "Oui, on peut prévoir un passage par an, en septembre, pour garder la haie à la même hauteur.")],
    "Une haie à tailler à Treillières ?")


ajoute("haie", "vertou",
    "Taille de haie à Vertou : Sèvre et vignoble | Jean Ferret",
    "Taille de haies à Vertou : lauriers-tins près des vignes, propriétés de la Sèvre, thuyas des quartiers. Ramassage compris, devis gratuit sur photo.",
    "Taille de haies à Vertou",
    "Vertou mélange les jardins de bord de Sèvre, les quartiers pavillonnaires et, au sud, les premières vignes. Chaque secteur a ses haies, et ses contraintes.",
    f"""
    <h2>Près des vignes</h2>
    <p>Au sud de la commune, vers le vignoble, les maisons qui touchent une parcelle de vigne ont souvent une haie mélangée de lauriers-tins, de charmes et de cornouillers. Côté vigne, on taille pour ne pas gêner le passage du tracteur entre les rangs, et on ramasse tout pour ne rien laisser dans la parcelle.</p>

    <h2>Bords de Sèvre et quartiers</h2>
    <p>Près de la Sèvre et de la chaussée des Moines, les propriétés en pente ont des haies anciennes de buis, d'ifs ou de lauriers-palmes. Dans les quartiers des années 1970 et 1980, ce sont des thuyas et des lauriers classiques.</p>

    <h2>Exemple de chantier type à Vertou</h2>
    <p>Une haie mélangée de 50 m entre un jardin et une parcelle de vigne, qui déborde d'un mètre côté rangs : reprise de la face côté vigne à l'aplomb de la limite, dessus remis à 2 m, déchets ramassés jusque dans le premier rang.</p>
    {NOTE_EX}
    {CTA.format("Une haie en limite de vigne ou de rivière ?")}

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie longue en limite agricole", "sur devis, au mètre")], "Fourchette, ramassage compris")}

    <h2>Déchets</h2>
    <p>La déchèterie de Vertou se trouve à La Foresterie, allée des Cadets, réservée aux particuliers de la Métropole (horaires à vérifier). Sinon, on emporte tout avec le chantier.</p>
""",
    [("Le viticulteur peut-il me demander de tailler ma haie ?",
      "Oui, comme tout voisin, si les branches avancent sur sa parcelle ou si la haie dépasse 2 m à moins de 2 m de la limite."),
     ("Quand tailler un laurier-tin ?",
      "Après sa floraison, au printemps, en vérifiant l'absence de nids. Une deuxième taille légère en septembre si besoin.")],
    "Une haie à tailler à Vertou ?")


ajoute("haie", "vigneux-de-bretagne",
    "Taille de haie à Vigneux-de-Bretagne | Jean Ferret",
    "Taille de haies à Vigneux-de-Bretagne et La Paquelais : haies bocagères des hameaux, longues haies de propriété, thuyas du bourg. Devis gratuit sur photo.",
    "Taille de haies à Vigneux-de-Bretagne",
    "À Vigneux et à La Paquelais, les terrains sont grands et les haies longues. Ici, une haie de 100 m n'a rien d'exceptionnel. On est juste à côté, à Saint-Étienne-de-Montluc.",
    f"""
    <h2>Des haies longues</h2>
    <p>Les maisons des hameaux sont souvent entourées de haies bocagères sur trois côtés : chênes, châtaigniers, noisetiers, houx. Les propriétaires les laissent pousser plusieurs années, puis ont besoin d'une vraie reprise. Pour ces longueurs, on travaille avec la nacelle depuis le champ ou le chemin, et au lamier pour les faces.</p>

    <h2>Exemple de chantier type à Vigneux-de-Bretagne</h2>
    <p>Une haie bocagère de 130 m autour d'une maison de hameau à La Paquelais, pas reprise depuis six ans : face côté jardin reprise au lamier, branches de chênes au-dessus de la pelouse élaguées, bois de chauffage coupé et rangé, branchages broyés.</p>
    {NOTE_EX}
    {CTA.format("Une longue haie à reprendre ?")}

    <h2>Haies protégées et bonne période</h2>
    <p>Une partie des haies bocagères de la commune est repérée au plan local d'urbanisme. L'entretien est libre ; l'arrachage demande une démarche. On taille ces haies entre novembre et février, en dehors de la nidification, et on garde les vieux arbres creux qui abritent la faune.</p>

    <h2>Prix indicatifs</h2>
    {prix([H30, ("Haie bocagère de plus de 100 m", "sur devis, au mètre")], "Fourchette, ramassage compris")}

    <h2>Déchets verts</h2>
    <p>Vigneux-de-Bretagne a une déchèterie d'Erdre et Gesvres sur la commune, impasse de la Vallée (horaires à vérifier). Sur un grand terrain, le broyat peut rester sur place en paillage.</p>
""",
    [("Une haie bocagère abîmée repart-elle ?",
      "Oui, la plupart des essences du bocage repartent bien après une taille franche en hiver."),
     ("Venez-vous de loin pour Vigneux ?",
      "Non, on est installés à Saint-Étienne-de-Montluc, la commune voisine.")],
    "Une haie à tailler à Vigneux-de-Bretagne ?")
