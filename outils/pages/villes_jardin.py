"""Tonte, clôture, terrassement et souches : 5 grosses communes
(Saint-Étienne-de-Montluc, Couëron, Saint-Herblain, Orvault, Rezé).
Un texte propre à chaque page. Ne pas recopier un paragraphe d'une page à l'autre."""
from villes import ajoute, prix, NOTE_EX

CTA = '<div class="inline-cta"><p>{}</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>'
TONTE = ("500 m², tonte, bordures, ramassage et évacuation", "300 €")
CLOT = ("Pose de clôture souple ou rigide, main-d'œuvre", "à partir de 40 € le mètre")
S_PETITE = ("Petite souche (hors location de la rogneuse)", "à partir de 260 €")
S_GROSSE = ("Grosse souche, matériel selon le chantier", "jusqu'à 2 600 €")
TERR = ("Mise à niveau, nivellement, remblai", "forfait après visite")


# =====================================================================
# SAINT-ÉTIENNE-DE-MONTLUC
# =====================================================================

ajoute("tonte", "saint-etienne-de-montluc",
    "Tonte de pelouse à Saint-Étienne-de-Montluc | Jean Ferret",
    "Tonte et entretien de jardin à Saint-Étienne-de-Montluc : grands terrains des hameaux, herbe haute, passages réguliers. Ramassage et évacuation compris.",
    "Tonte et entretien de jardin à Saint-Étienne-de-Montluc",
    "Dans les hameaux de la commune, un terrain de 2 000 m² n'a rien de rare. Quand on n'a plus le temps ou la force de le tondre, on peut passer, et on est déjà sur place.",
    f"""
    <h2>Des terrains plus grands qu'ailleurs</h2>
    <p>Autour du bourg, les jardins de lotissement font 400 à 700 m². Dans les hameaux, on tond souvent des terrains de 1 500 à 3 000 m², avec des fossés, des arbres isolés et un bout de pré. Pour ces surfaces, on vient avec une tondeuse autoportée et une débroussailleuse pour les bords de fossé.</p>

    <h2>Herbe haute après un hiver humide</h2>
    <p>Les terres de la commune sont lourdes et restent mouillées longtemps près des marais. Au printemps, l'herbe pousse d'un coup alors qu'on ne peut pas encore passer sans marquer le terrain. Résultat : une première tonte sur de l'herbe à 30 cm. On la fait en deux passages, le premier haut, pour ne pas étouffer la pelouse.</p>

    <h2>Exemple de chantier type à Saint-Étienne-de-Montluc</h2>
    <p>Un terrain de 2 200 m² autour d'une longère, pas tondu depuis six semaines au mois de mai : tonte en deux passages, bords des fossés à la débroussailleuse, herbe ramassée et emportée, puis un passage tous les quinze jours jusqu'à l'été.</p>
    {NOTE_EX}
    {CTA.format("Un grand terrain à entretenir ?")}

    <h2>Prix indicatifs</h2>
    {prix([TONTE, ("Grand terrain de hameau, herbe haute", "forfait selon photo")], "Prix", "Terrain")}

    <h2>Que devient l'herbe ?</h2>
    <p>On l'emporte, c'est compris. La commune dépend des déchèteries d'Estuaire et Sillon ; sur un grand terrain, on peut aussi laisser l'herbe fine sur place (mulching) quand la tonte est régulière, ce qui nourrit la pelouse.</p>
""",
    [("Tondez-vous les grands terrains de plus de 2 000 m² ?",
      "Oui, avec une tondeuse autoportée. Le prix se fait au forfait selon la surface et la hauteur de l'herbe."),
     ("Peut-on prévoir un passage régulier ?",
      "Oui, tous les quinze jours au printemps, puis selon la pousse en été et en automne.")],
    "Un jardin à tondre à Saint-Étienne-de-Montluc ?")


ajoute("cloture", "saint-etienne-de-montluc",
    "Clôture à Saint-Étienne-de-Montluc : pose | Jean Ferret",
    "Pose de clôture à Saint-Étienne-de-Montluc : grillage souple pour grands terrains, panneaux rigides du bourg, clôture pour chiens ou chevaux. Dès 40 €/m.",
    "Pose de clôture à Saint-Étienne-de-Montluc",
    "Clore un terrain de hameau ou un jardin de lotissement, ce n'est pas le même chantier. On pose les deux, depuis le Gendre Moreau, à quelques minutes.",
    f"""
    <h2>Grillage souple pour les grands terrains</h2>
    <p>Pour fermer 150 m de terrain en campagne, le grillage souple sur poteaux reste le plus économique. On tend le grillage avec des fils de tension, et on renforce les angles et les poteaux de départ. Pour un chien qui creuse, on enterre le bas du grillage de 20 cm ou on pose une bordure.</p>

    <h2>Panneaux rigides dans le bourg</h2>
    <p>Dans les quartiers du bourg, les clients choisissent plutôt des panneaux rigides, parfois avec des lames d'occultation. C'est plus net et plus solide. On aligne la clôture au cordeau et on règle la hauteur des poteaux sur un terrain qui n'est jamais parfaitement plat.</p>

    <h2>Exemple de chantier type à Saint-Étienne-de-Montluc</h2>
    <p>Un terrain de hameau de 3 000 m² à fermer pour deux chiens : 180 m de grillage souple de 1,50 m sur poteaux, bas enterré côté chemin, portillon et portail de 3 m pour la voiture.</p>
    {NOTE_EX}
    {CTA.format("Un terrain à clôturer ?")}

    <h2>Prix indicatifs</h2>
    {prix([CLOT, ("Portail, portillon, lames d'occultation", "sur devis, selon le matériel")], "Prix indicatif", "Prestation")}

    <h2>Règles à vérifier</h2>
    <p>Le plan local d'urbanisme intercommunal fixe la hauteur et l'aspect des clôtures, avec des règles différentes en zone agricole et dans le bourg. Une déclaration préalable peut être demandée. Si une vieille haie doit partir avant la pose, on s'en charge aussi : arrachage, souches, nivellement.</p>
""",
    [("Faut-il une déclaration pour poser une clôture ?",
      "Selon la commune et la zone, oui. Renseignez-vous en mairie avant le chantier, on vous dit quoi demander."),
     ("Fournissez-vous le grillage ?",
      "On peut le fournir ou poser le vôtre. Le prix de 40 € le mètre correspond à la pose seule.")],
    "Une clôture à poser à Saint-Étienne-de-Montluc ?")


ajoute("terrassement", "saint-etienne-de-montluc",
    "Terrassement à Saint-Étienne-de-Montluc | Jean Ferret",
    "Terrassement et mise à niveau à Saint-Étienne-de-Montluc : terres argileuses humides, jardins après construction, chemins et accès. Devis gratuit.",
    "Terrassement et mise à niveau à Saint-Étienne-de-Montluc",
    "Sur la commune, les terres sont souvent lourdes et mouillées une bonne partie de l'année. Une mise à niveau réussie, ici, commence par le choix du bon moment.",
    f"""
    <h2>Les sols de la commune</h2>
    <p>Entre le bourg et les marais de l'estuaire, le sol est argileux : il colle l'hiver, durcit et se fend l'été. Un terrain nivelé sur de l'argile mouillée se tasse mal et garde des flaques. On travaille donc de fin août à octobre, ou au printemps quand la terre s'émiette dans la main.</p>

    <h2>Ce qu'on fait le plus</h2>
    <p>Mise à niveau d'un jardin après la construction d'une maison, avec les bosses laissées par les engins. Comblement d'un creux où l'eau stagne. Petit chemin d'accès stabilisé jusqu'à un abri ou un garage. Préparation d'un terrain pour une <a href="/creation-pelouse-nantes/">pelouse</a>.</p>

    <h2>Exemple de chantier type à Saint-Étienne-de-Montluc</h2>
    <p>Un jardin de maison neuve du bourg, 500 m² de terre retournée avec des gravats de chantier en surface : ramassage des gravats, apport de terre végétale, nivellement avec une légère pente pour écarter l'eau de la maison.</p>
    {NOTE_EX}
    {CTA.format("Un terrain à remettre à plat ?")}

    <h2>Prix indicatifs</h2>
    {prix([TERR, ("Apport de terre végétale", "selon le volume")], "Prix", "Travaux")}

    <h2>Avant de creuser</h2>
    <p>Dès qu'on approche des réseaux enterrés (eau, électricité, assainissement), une déclaration de travaux auprès des exploitants est obligatoire. Pour des remblais importants, le plan local d'urbanisme peut demander une démarche : on vérifie avec vous.</p>
""",
    [("Pourquoi l'eau stagne-t-elle dans mon jardin ?",
      "Souvent à cause d'un sol argileux tassé et d'un creux. Une mise à niveau avec une légère pente et un sol décompacté règle la plupart des cas."),
     ("Évacuez-vous les gravats de chantier ?",
      "Oui, on les ramasse et on les emporte avant de niveler.")],
    "Un terrain à niveler à Saint-Étienne-de-Montluc ?")


ajoute("souche", "saint-etienne-de-montluc",
    "Dessouchage à Saint-Étienne-de-Montluc | Jean Ferret",
    "Enlèvement de souches à Saint-Étienne-de-Montluc : souches de frênes malades, vieilles haies de thuyas, rognage ou extraction. Dès 260 €, devis gratuit.",
    "Enlèvement de souches à Saint-Étienne-de-Montluc",
    "Beaucoup de frênes ont été abattus sur la commune ces dernières années à cause de la chalarose. Il reste les souches, parfois une dizaine sur un même terrain.",
    f"""
    <h2>Les souches qu'on enlève le plus</h2>
    <p>Souches de frênes en bordure de prairie ou de jardin, souvent alignées le long d'une ancienne haie. Souches de thuyas après l'arrachage d'une haie de lotissement. Et vieilles souches de chênes, coupées il y a longtemps, qui gênent un projet de pelouse ou d'abri.</p>

    <h2>Rogner ou extraire ?</h2>
    <p>Pour semer une pelouse, le rognage suffit : la rogneuse broie la souche à 20 ou 30 cm sous le sol. Pour construire, poser une dalle ou replanter au même endroit, on extrait la souche et les grosses racines. Sur un terrain mouillé, on attend que le sol porte la machine.</p>

    <h2>Exemple de chantier type à Saint-Étienne-de-Montluc</h2>
    <p>Huit souches de frênes de 30 à 50 cm le long d'une ancienne haie en bordure de jardin : rognage de toutes les souches dans la même journée, rebouchage avec les copeaux et de la terre, surplus de copeaux emporté.</p>
    {NOTE_EX}
    {CTA.format("Des souches à faire disparaître ?")}

    <h2>Prix indicatifs</h2>
    {prix([S_PETITE, S_GROSSE, ("Plusieurs souches sur un même terrain", "prix dégressif")], "Prix indicatif", "Souche")}

    <h2>Après le dessouchage</h2>
    <p>Les copeaux se tassent en quelques mois : prévoyez un peu de terre en plus avant de semer. On peut enchaîner avec un <a href="/terrassement-nantes/terrassement-saint-etienne-de-montluc/">nivellement du terrain</a> dans le même chantier.</p>
""",
    [("Une souche de frêne repousse-t-elle ?",
      "Oui, le frêne fait des rejets pendant quelques années. Le rognage les arrête."),
     ("Rognez-vous plusieurs souches le même jour ?",
      "Oui, et le prix par souche baisse quand il y en a plusieurs sur le même terrain.")],
    "Des souches à enlever à Saint-Étienne-de-Montluc ?")


# =====================================================================
# COUËRON
# =====================================================================

ajoute("tonte", "coueron",
    "Tonte de pelouse à Couëron | Jean Ferret Paysage",
    "Tonte et entretien de jardin à Couëron : pelouses humides près de la Loire, lotissements de la Chabossière, passages réguliers. Herbe emportée.",
    "Tonte et entretien de jardin à Couëron",
    "À Couëron, la pelouse pousse vite et reste longtemps humide, surtout côté Loire. Une tonte au bon moment évite le gazon arraché et les ornières.",
    f"""
    <h2>Des pelouses sur sol humide</h2>
    <p>Près de la Loire et des marais, le sol garde l'eau jusqu'en avril. Tondre trop tôt sur un terrain gorgé d'eau laisse des traces de roues et arrache le gazon. On choisit les jours où le sol est ressuyé, quitte à décaler de quelques jours. Ces pelouses ont aussi tendance à se remplir de mousse à l'ombre des haies de cyprès.</p>

    <h2>Dans les lotissements</h2>
    <p>À la Chabossière, au Bossis ou à la Métairie, les jardins de 400 à 600 m² se tondent en moins d'une heure. Beaucoup de clients nous demandent un passage régulier pendant la saison, avec les bordures et le ramassage des feuilles à l'automne.</p>

    <h2>Exemple de chantier type à Couëron</h2>
    <p>Un jardin de 600 m² en lotissement, propriétaires absents trois semaines en juin : deux tontes avec bordures, taille légère des massifs, ramassage, herbe emportée, et un passage en octobre pour les feuilles.</p>
    {NOTE_EX}
    {CTA.format("Un jardin à tondre à Couëron ?")}

    <h2>Prix indicatifs</h2>
    {prix([TONTE, ("Ramassage des feuilles à l'automne", "forfait selon le jardin")], "Prix", "Terrain")}

    <h2>L'herbe et les feuilles</h2>
    <p>Les déchèteries de Nantes Métropole sont réservées aux particuliers de la Métropole. Avec nous, tontes et feuilles partent avec le chantier, rien ne reste en tas au fond du jardin.</p>
""",
    [("Pourquoi ne pas tondre quand le sol est mouillé ?",
      "La tondeuse marque le terrain et arrache le gazon. Mieux vaut attendre un ou deux jours secs."),
     ("Ramassez-vous les feuilles à l'automne ?",
      "Oui, en même temps que la dernière tonte ou lors d'un passage dédié.")],
    "Un jardin à entretenir à Couëron ?")


ajoute("cloture", "coueron",
    "Clôture et claustra à Couëron : vent de Loire",
    "Pose de clôture et de claustras à Couëron : panneaux brise-vue qui tiennent au vent de Loire, poteaux scellés, grillage rigide. Pose dès 40 € le mètre.",
    "Pose de clôture et de claustras à Couëron",
    "À Couëron, une clôture pleine prend le vent de la Loire comme une voile. Bien posée, elle tient vingt ans ; mal scellée, elle se couche au premier coup de vent.",
    f"""
    <h2>Brise-vue et vent d'ouest</h2>
    <p>Les panneaux pleins et les claustras occultants sont très demandés pour cacher le vis-à-vis. Mais face au vent d'ouest qui remonte l'estuaire, ils subissent une forte poussée. On scelle les poteaux plus profond, on rapproche les poteaux sur les côtés exposés, et on conseille parfois des lames ajourées qui laissent passer un peu d'air.</p>

    <h2>Grillage et panneaux rigides</h2>
    <p>Pour une limite entre deux jardins, le panneau rigide vert ou gris reste la solution la plus simple. On peut y ajouter des lames d'occultation ou le doubler d'une haie.</p>

    <h2>Exemple de chantier type à Couëron</h2>
    <p>Une clôture de 22 m de panneaux occultants en bois composite en fond de jardin, côté ouest, dont trois panneaux s'étaient couchés après une tempête : dépose, nouveaux poteaux scellés plus profond, repose des panneaux, et ajout d'un poteau intermédiaire sur la partie la plus exposée.</p>
    {NOTE_EX}
    {CTA.format("Une clôture à poser ou à redresser ?")}

    <h2>Prix indicatifs</h2>
    {prix([CLOT, ("Claustras et panneaux occultants, fourniture", "sur devis")], "Prix indicatif", "Prestation")}

    <h2>Avant de poser</h2>
    <p>Couëron dépend du plan local d'urbanisme de Nantes Métropole, qui fixe la hauteur des clôtures selon les quartiers. Une déclaration préalable peut être demandée, en particulier en limite de rue. En bord de marais, des règles plus strictes peuvent s'appliquer.</p>
""",
    [("Mes panneaux brise-vue se couchent avec le vent, que faire ?",
      "Il faut des poteaux plus profonds et plus rapprochés, ou des panneaux un peu ajourés qui prennent moins le vent."),
     ("Quelle hauteur de clôture à Couëron ?",
      "Elle dépend du quartier et du côté (rue ou voisin). Le plan local d'urbanisme métropolitain le précise : vérifiez en mairie.")],
    "Une clôture à poser à Couëron ?")


ajoute("terrassement", "coueron",
    "Terrassement à Couëron : terrains humides | Jean Ferret",
    "Terrassement et mise à niveau à Couëron : terrains humides près de la Loire, zones inondables à vérifier, nivellement pour pelouse ou terrasse.",
    "Terrassement et mise à niveau à Couëron",
    "À Couëron, avant de remblayer un terrain près de la Loire, on vérifie s'il est en zone inondable. Le reste du temps, on nivelle, on comble et on prépare les sols.",
    f"""
    <h2>Zone inondable : ce qui change</h2>
    <p>Une partie de la commune, le long de la Loire et des marais, est couverte par un plan de prévention des risques d'inondation. Dans ces secteurs, apporter de la terre pour surélever un terrain peut être limité ou interdit, pour ne pas gêner l'écoulement des crues. On regarde la carte avec vous avant de prévoir un remblai.</p>

    <h2>Ce qu'on fait ailleurs sur la commune</h2>
    <p>Dans les quartiers hauts, les chantiers sont plus classiques : remise à niveau après des travaux, terrassement d'une zone de terrasse ou d'abri, comblement d'une ancienne mare, préparation d'un terrain avant une pelouse.</p>

    <h2>Exemple de chantier type à Couëron</h2>
    <p>Une ancienne mare de 30 m² comblée de longue date, qui se tasse et forme une cuvette dans la pelouse : décapage, apport de terre compactée par couches, nivellement avec le reste du jardin, semis.</p>
    {NOTE_EX}
    {CTA.format("Un creux ou une cuvette dans le jardin ?")}

    <h2>Prix indicatifs</h2>
    {prix([TERR, ("Comblement d'un creux ou d'une mare", "selon le volume de terre")], "Prix", "Travaux")}

    <h2>La bonne période</h2>
    <p>Les sols près du fleuve sont détrempés de novembre à mars. On travaille plutôt de mai à octobre, quand les engins ne s'enfoncent pas. Avant de creuser, on fait la déclaration de travaux près des réseaux enterrés.</p>
""",
    [("Peut-on surélever un terrain en zone inondable ?",
      "Souvent non, ou de façon très limitée. Le plan de prévention des risques d'inondation le précise ; on le vérifie avant."),
     ("Pourquoi mon ancienne mare comblée se creuse-t-elle ?",
      "Le remblai d'origine n'a pas été tassé par couches. Il faut le reprendre et le compacter correctement.")],
    "Un terrain à niveler à Couëron ?")


ajoute("souche", "coueron",
    "Dessouchage à Couëron : souches de pins | Jean Ferret",
    "Enlèvement de souches à Couëron : souches de pins et de cèdres aux racines traçantes, haies de cyprès arrachées, rognage sous la pelouse. Dès 260 €.",
    "Enlèvement de souches à Couëron",
    "Les grands résineux abattus dans les jardins de Couëron laissent des souches larges, avec des racines qui courent sous toute la pelouse.",
    f"""
    <h2>Pins, cèdres et cyprès</h2>
    <p>Une souche de pin ou de cèdre de 60 cm de diamètre a des racines qui partent à plusieurs mètres, juste sous la surface. Après l'abattage, la pelouse reste bosselée. On rogne la souche, puis on suit les grosses racines superficielles pour les broyer aussi. Pour une haie de cyprès de Leyland arrachée, il y a une souche tous les 60 à 80 cm : on les fait toutes d'un coup.</p>

    <h2>Exemple de chantier type à Couëron</h2>
    <p>La souche d'un cèdre de 70 cm abattu l'année précédente, avec trois grosses racines qui soulèvent la pelouse : rognage à 30 cm sous le sol, broyage des racines sur 3 m, rebouchage, terre ajoutée et pelouse ressemée.</p>
    {NOTE_EX}
    {CTA.format("Une souche de résineux à enlever ?")}

    <h2>Prix indicatifs</h2>
    {prix([S_PETITE, S_GROSSE, ("Haie de cyprès : souches en ligne", "sur devis, au mètre")], "Prix indicatif", "Souche")}

    <h2>Un sol un peu acide après</h2>
    <p>Les aiguilles de pin et de cèdre ont acidifié le sol pendant des années. Après le rognage, on mélange les copeaux à de la terre neuve, et un peu de chaux aide la pelouse à repartir. Près de la Loire, on attend que le sol ressuie pour faire entrer la rogneuse.</p>

    <h2>Avant de rogner</h2>
    <p>On vérifie les réseaux enterrés : eau, électricité, gaz. Près d'un réseau, une déclaration de travaux est obligatoire avant de creuser.</p>
""",
    [("Faut-il aussi enlever les racines ?",
      "Pour une pelouse plate, on broie les grosses racines superficielles autour de la souche. Les racines profondes se décomposent seules."),
     ("Rognez-vous les souches d'une haie de cyprès ?",
      "Oui, toutes les souches en ligne, pour pouvoir replanter ou poser une clôture sur le même tracé.")],
    "Des souches à enlever à Couëron ?")


# =====================================================================
# SAINT-HERBLAIN
# =====================================================================

ajoute("tonte", "saint-herblain",
    "Tonte de pelouse à Saint-Herblain | Jean Ferret Paysage",
    "Tonte et entretien de petits jardins à Saint-Herblain : sans accès sur le côté, tondeuse qui passe par la maison, bordures et ramassage compris.",
    "Tonte et entretien de jardin à Saint-Herblain",
    "À Saint-Herblain, le jardin se trouve souvent derrière la maison, sans passage sur le côté. On vient avec du matériel qui passe par le garage ou le couloir.",
    f"""
    <h2>Des jardins sans accès</h2>
    <p>Au Tillay, à la Bégraisière, à Preux ou au bourg, beaucoup de maisons mitoyennes ont leur jardin à l'arrière. On utilise une tondeuse compacte qui passe dans un couloir de 60 cm, des bâches pour traverser la maison, et des sacs pour sortir l'herbe. Rien n'est laissé dans le garage.</p>

    <h2>Un entretien complet</h2>
    <p>Sur ces petites surfaces, la tonte ne prend pas longtemps : on en profite pour les bordures, le désherbage des allées, la taille des arbustes qui débordent et le soufflage de la terrasse. C'est souvent ce que demandent les clients qui partent ou qui ne peuvent plus jardiner.</p>

    <h2>Exemple de chantier type à Saint-Herblain</h2>
    <p>Un jardin de 250 m² derrière une maison mitoyenne de la Bégraisière, accessible seulement par le garage : tonte, bordures, taille des rosiers et du laurier qui déborde, terrasse soufflée, déchets sortis en sacs.</p>
    {NOTE_EX}
    {CTA.format("Un petit jardin sans accès ?")}

    <h2>Prix indicatifs</h2>
    {prix([TONTE, ("Petit jardin, entretien complet", "forfait selon photo, souvent moins")], "Prix", "Terrain")}

    <h2>Déchets verts</h2>
    <p>La déchèterie de Saint-Herblain, à Tougas, est réservée aux particuliers de Nantes Métropole (horaires à vérifier). Avec nous, l'herbe et les tailles partent avec le chantier.</p>
""",
    [("Votre tondeuse passe-t-elle dans un couloir ?",
      "Oui, on a une tondeuse compacte pour les jardins accessibles seulement par la maison ou un passage étroit."),
     ("Pouvez-vous faire plus que la tonte ?",
      "Oui : bordures, désherbage des allées, taille des arbustes, nettoyage de la terrasse.")],
    "Un jardin à entretenir à Saint-Herblain ?")


ajoute("cloture", "saint-herblain",
    "Clôture à Saint-Herblain : brise-vue, rigide | Jean Ferret",
    "Pose de clôture à Saint-Herblain : panneaux rigides et brise-vue entre jardins mitoyens, petites longueurs, pose sans accès engin. Dès 40 € le mètre.",
    "Pose de clôture à Saint-Herblain",
    "Entre deux jardins herblinois, la clôture fait souvent 15 ou 20 m. Petite longueur, mais beaucoup d'attentes : se protéger du vis-à-vis sans fâcher le voisin.",
    f"""
    <h2>Se cacher du vis-à-vis</h2>
    <p>Dans les quartiers serrés, la demande la plus fréquente est un brise-vue de 1,80 m entre deux terrasses. On pose des panneaux rigides avec lames d'occultation, des panneaux bois ou des claustras composites. Tout se fait à la main : poteaux scellés au béton gâché sur place, matériel passé par le portillon.</p>

    <h2>Mitoyenneté : se mettre d'accord</h2>
    <p>Une clôture posée chez vous, en retrait de la limite, est à vous seul. Posée sur la limite, elle est mitoyenne et demande l'accord du voisin, qui peut en partager le coût. On conseille de décider ensemble de la hauteur et de la couleur, et de garder une trace écrite.</p>

    <h2>Exemple de chantier type à Saint-Herblain</h2>
    <p>Un vieux grillage de 18 m entre deux jardins, doublé d'une haie de thuyas morte : arrachage des thuyas et des souches, dépose du grillage, pose de panneaux rigides gris avec lames d'occultation sur 6 m côté terrasse.</p>
    {NOTE_EX}
    {CTA.format("Une clôture entre deux jardins ?")}

    <h2>Prix indicatifs</h2>
    {prix([CLOT, ("Lames d'occultation, claustras", "sur devis, selon le matériel")], "Prix indicatif", "Prestation")}

    <h2>Règles locales</h2>
    <p>Saint-Herblain applique le plan local d'urbanisme de Nantes Métropole, qui fixe la hauteur des clôtures et peut demander une déclaration préalable. Côté rue, les règles sont souvent plus strictes qu'entre voisins. Vérifiez avant de commander le matériel.</p>
""",
    [("Faut-il l'accord du voisin pour poser une clôture ?",
      "Pas si elle est entièrement chez vous. Sur la limite, elle devient mitoyenne et son accord est nécessaire."),
     ("Pouvez-vous enlever l'ancienne haie avant ?",
      "Oui : arrachage, souches, nivellement, puis pose de la clôture dans le même chantier.")],
    "Une clôture à poser à Saint-Herblain ?")


ajoute("terrassement", "saint-herblain",
    "Terrassement à Saint-Herblain : petits jardins | Jean Ferret",
    "Terrassement et mise à niveau à Saint-Herblain : jardins remblayés de gravats, zones de terrasse, accès étroits avec mini-engin. Devis gratuit sur photo.",
    "Terrassement et mise à niveau à Saint-Herblain",
    "Beaucoup de jardins herblinois ont été remblayés à la construction avec ce qui traînait sur le chantier. Quarante ans après, on retrouve briques et gravats sous la pelouse.",
    f"""
    <h2>Des sols de remblai</h2>
    <p>Dans les lotissements des années 1970 et 1980, la terre végétale a souvent été enlevée puis remplacée par du remblai. Résultat : une pelouse maigre, qui jaunit vite l'été, et des cailloux qui remontent. On décape, on trie ou on évacue les gravats, et on remet 15 à 20 cm de bonne terre.</p>

    <h2>Accès étroits</h2>
    <p>Quand le jardin est derrière la maison, on travaille avec un mini-engin qui passe dans 90 cm, ou à la brouette pour les plus petits accès. La terre arrive en big-bags devant la maison et part par le même chemin.</p>

    <h2>Exemple de chantier type à Saint-Herblain</h2>
    <p>Un jardin de 300 m² avec une pelouse pleine de cailloux et une bosse au fond : décapage, évacuation de deux bennes de gravats, apport de terre végétale, nivellement, et préparation pour une <a href="/creation-pelouse-nantes/">nouvelle pelouse</a>.</p>
    {NOTE_EX}
    {CTA.format("Une pelouse pleine de cailloux ?")}

    <h2>Prix indicatifs</h2>
    {prix([TERR, ("Évacuation de gravats", "selon le volume")], "Prix", "Travaux")}

    <h2>Réseaux et autorisations</h2>
    <p>Dans un jardin de ville, les réseaux (eau, gaz, électricité, assainissement) passent souvent sous la pelouse. On fait la déclaration de travaux avant de creuser. Une mise à niveau simple ne demande pas d'autorisation ; un remblai important peut en demander une.</p>
""",
    [("Pourquoi ma pelouse jaunit-elle si vite l'été ?",
      "Souvent parce qu'il n'y a que quelques centimètres de terre sur du remblai. Un apport de terre végétale règle le problème."),
     ("Pouvez-vous travailler sans accès engin ?",
      "Oui, avec un mini-engin qui passe dans un portillon, ou à la brouette pour les plus petits jardins.")],
    "Un terrain à reprendre à Saint-Herblain ?")


ajoute("souche", "saint-herblain",
    "Dessouchage à Saint-Herblain : rognage | Jean Ferret",
    "Enlèvement de souches à Saint-Herblain : rogneuse étroite qui passe par le portillon, souches de bouleaux et de fruitiers sous la pelouse. Dès 260 €.",
    "Enlèvement de souches à Saint-Herblain",
    "Une souche au milieu d'un petit jardin, c'est un obstacle permanent pour la tondeuse. À Saint-Herblain, on l'enlève même quand le seul accès est un portillon de 70 cm.",
    f"""
    <h2>Une rogneuse qui passe partout</h2>
    <p>Pour les jardins sans accès, on loue une rogneuse compacte qui passe dans un portillon de 70 cm. Elle broie la souche sous le niveau du sol, sans abîmer le reste de la pelouse. Les copeaux servent à reboucher, le surplus part en sacs.</p>

    <h2>Les souches les plus courantes</h2>
    <p>Bouleaux, cerisiers, pruniers et pommiers des jardins de lotissement, coupés au ras il y a quelques années. Souches de thuyas après l'arrachage d'une haie mitoyenne. Et souches d'arbres abattus récemment, que le client veut enlever dans la foulée.</p>

    <h2>Exemple de chantier type à Saint-Herblain</h2>
    <p>Deux souches de bouleaux de 40 cm au milieu d'une pelouse de 200 m², accès par un portillon étroit : rognage à 25 cm sous le sol avec une petite rogneuse, rebouchage, terre et semis à l'endroit des souches.</p>
    {NOTE_EX}
    {CTA.format("Une souche gêne la tondeuse ?")}

    <h2>Prix indicatifs</h2>
    {prix([S_PETITE, ("Souche près d'une terrasse ou d'un mur", "sur devis, après photo")], "Prix indicatif", "Souche")}

    <h2>Avant le rognage</h2>
    <p>Dans les jardins herblinois, les canalisations passent souvent près des arbres. On vérifie leur tracé et on fait la déclaration de travaux si besoin. Les copeaux en trop peuvent aussi pailler vos massifs.</p>
""",
    [("Une rogneuse passe-t-elle par un portillon ?",
      "Oui, il existe des rogneuses compactes qui passent dans 70 cm."),
     ("Peut-on garder les copeaux ?",
      "Oui, ils font un bon paillage au pied des arbustes. Le reste est emporté.")],
    "Une souche à enlever à Saint-Herblain ?")


# =====================================================================
# ORVAULT
# =====================================================================

ajoute("tonte", "orvault",
    "Tonte et entretien de parc à Orvault | Jean Ferret",
    "Tonte et entretien de jardin à Orvault : grands parcs de propriétés anciennes, pelouses en pente vers le Cens, feuilles des grands arbres. Devis gratuit.",
    "Tonte et entretien de jardin à Orvault",
    "Orvault a beaucoup de grandes propriétés avec des parcs et de vieux arbres. Leur entretien, c'est de la tonte au printemps et des montagnes de feuilles à l'automne.",
    f"""
    <h2>Grands parcs et pelouses en pente</h2>
    <p>Vers le Petit-Chantilly, la Ferrière ou le bourg, les propriétés ont des pelouses de 2 000 m² et plus, souvent en pente vers la vallée du Cens. Sur la pente, on tond en travers, avec une tondeuse adaptée, et on passe la débroussailleuse au pied des talus et des murets.</p>

    <h2>Les feuilles des grands arbres</h2>
    <p>Chênes, hêtres, marronniers : à l'automne, une seule propriété peut produire plusieurs remorques de feuilles. Laissées sur la pelouse, elles l'étouffent en quelques semaines. On les ramasse au souffleur et à la tondeuse ramasseuse, en un ou deux passages selon la chute.</p>

    <h2>Exemple de chantier type à Orvault</h2>
    <p>Une propriété avec 2 500 m² de pelouse en pente sous des chênes et un marronnier : tonte toutes les deux semaines d'avril à juin, puis deux passages de ramassage des feuilles en novembre, tout emporté.</p>
    {NOTE_EX}
    {CTA.format("Un grand jardin à entretenir ?")}

    <h2>Prix indicatifs</h2>
    {prix([TONTE, ("Parc de plus de 1 000 m² ou en pente", "forfait selon photo")], "Prix", "Terrain")}

    <h2>Déchets verts</h2>
    <p>La déchèterie d'Orvault, sur le site de l'Espérance, est réservée aux particuliers de la Métropole et limite les volumes. Pour un parc, mieux vaut nous laisser tout emporter, ou garder une partie des feuilles en compost.</p>
""",
    [("Tondez-vous les pelouses en pente ?",
      "Oui, avec le matériel adapté. On tond en travers de la pente pour la sécurité et pour ne pas arracher le gazon."),
     ("Pouvez-vous ramasser les feuilles d'un grand parc ?",
      "Oui, au souffleur et à la tondeuse ramasseuse. Tout est emporté.")],
    "Un jardin à entretenir à Orvault ?")


ajoute("cloture", "orvault",
    "Clôture à Orvault : propriétés et lotissements",
    "Pose de clôture à Orvault : clôtures de propriété le long des allées, grillage doublé de haie, panneaux rigides des quartiers récents. Dès 40 €/m posé.",
    "Pose de clôture à Orvault",
    "À Orvault, une clôture doit souvent rester discrète : longer une allée de propriété, s'effacer derrière une haie, ou s'aligner avec celles du quartier.",
    f"""
    <h2>Clôtures de propriété</h2>
    <p>Autour des maisons anciennes, on pose surtout des clôtures discrètes : grillage vert à mailles soudées, doublé d'une haie ou posé derrière un muret. L'idée est de fermer le terrain, pour un chien ou pour la sécurité, sans que la clôture se voie depuis l'allée.</p>

    <h2>Terrains en pente</h2>
    <p>Le long de la vallée du Cens, le terrain descend. Les panneaux rigides se posent en escalier, chaque panneau décalé du précédent, alors que le grillage souple peut suivre la pente. On choisit avec vous ce qui rend le mieux.</p>

    <h2>Exemple de chantier type à Orvault</h2>
    <p>Une propriété de 4 000 m² à fermer pour un chien, le long d'une allée bordée de charmilles : 140 m de grillage vert de 1,20 m posé derrière la charmille pour rester invisible, portillon en bas du terrain.</p>
    {NOTE_EX}
    {CTA.format("Un terrain à fermer discrètement ?")}

    <h2>Prix indicatifs</h2>
    {prix([CLOT, ("Portillon ou portail", "sur devis, selon le modèle")], "Prix indicatif", "Prestation")}

    <h2>À vérifier en mairie</h2>
    <p>Orvault applique le plan local d'urbanisme de Nantes Métropole. Dans certains secteurs boisés ou de patrimoine, l'aspect de la clôture est encadré, et une déclaration préalable peut être nécessaire. Le règlement de lotissement peut aussi imposer un modèle.</p>
""",
    [("Peut-on poser une clôture derrière une haie existante ?",
      "Oui, c'est même la solution la plus discrète. On dégage juste ce qu'il faut pour planter les poteaux."),
     ("Comment poser une clôture rigide sur un terrain en pente ?",
      "En escalier : chaque panneau est décalé en hauteur du précédent pour suivre le terrain.")],
    "Une clôture à poser à Orvault ?")


ajoute("terrassement", "orvault",
    "Terrassement à Orvault : terrains en pente | Jean Ferret",
    "Terrassement à Orvault : terrains en pente de la vallée du Cens, création de paliers et de zones planes, talus à reprendre. Devis gratuit sur photo.",
    "Terrassement et mise à niveau à Orvault",
    "Sur les pentes de la vallée du Cens, un jardin plat est un luxe. On crée des zones planes pour une terrasse, une pelouse ou un potager, en gardant la pente stable.",
    f"""
    <h2>Créer du plat dans la pente</h2>
    <p>La solution la plus courante est le palier : on prend la terre en haut, on la remet en bas, et on stabilise le talus entre les deux. Pour un talus haut, on prévoit un muret ou des gabions. Sans soutien, un talus raide en terre argileuse finit par glisser après un hiver pluvieux.</p>

    <h2>L'eau de ruissellement</h2>
    <p>Sur un terrain en pente, l'eau descend vers le bas et s'arrête au premier obstacle, souvent la maison ou la terrasse. Chaque mise à niveau prévoit une légère pente pour l'écarter, parfois une petite tranchée drainante.</p>

    <h2>Exemple de chantier type à Orvault</h2>
    <p>Un jardin en pente de 12 % derrière une maison, où les enfants ne pouvaient pas jouer : création d'un palier plat de 80 m² avec la terre du haut du terrain, talus engazonné entre les deux, drain au pied du talus.</p>
    {NOTE_EX}
    {CTA.format("Un jardin en pente à aménager ?")}

    <h2>Prix indicatifs</h2>
    {prix([TERR, ("Muret ou gabions de soutien", "sur devis")], "Prix", "Travaux")}

    <h2>Avant les travaux</h2>
    <p>Certains secteurs d'Orvault sont en espaces boisés classés ou protégés au plan local d'urbanisme : un terrassement près des arbres peut y être encadré, et creuser au pied d'un grand arbre l'abîme. On vérifie aussi les réseaux avant de creuser.</p>
""",
    [("Un talus en terre tient-il tout seul ?",
      "S'il est en pente douce et engazonné, oui. Plus raide, il faut un muret ou des gabions pour qu'il ne glisse pas."),
     ("Peut-on niveler près d'un grand arbre ?",
      "Avec prudence. Couper les racines ou ajouter de la terre au pied d'un arbre peut le faire dépérir.")],
    "Un terrain à aménager à Orvault ?")


ajoute("souche", "orvault",
    "Dessouchage à Orvault : grosses souches | Jean Ferret",
    "Enlèvement de grosses souches à Orvault : marronniers, cèdres et hêtres abattus dans les propriétés, souches d'allée, rognage ou extraction. Devis gratuit.",
    "Enlèvement de souches à Orvault",
    "Les très grands arbres d'Orvault laissent de très grosses souches. Un marronnier de 20 m, c'est parfois 1,20 m de diamètre au ras du sol.",
    f"""
    <h2>Les grosses souches</h2>
    <p>Pour une souche de plus d'un mètre, on loue une rogneuse puissante, sur chenilles quand le terrain est en pente. Le rognage prend plusieurs heures et produit un gros volume de copeaux. Pour une souche dans une allée de propriété, on rogne plus profond pour pouvoir refaire l'allée par-dessus.</p>

    <h2>Garder la souche, parfois</h2>
    <p>Dans un parc, une vieille souche loin des passages peut rester : elle se décompose lentement et abrite insectes et champignons. On conseille de l'enlever quand elle gêne un projet, quand elle est au milieu d'une pelouse ou quand elle fait des rejets.</p>

    <h2>Exemple de chantier type à Orvault</h2>
    <p>La souche d'un marronnier de 1,10 m de diamètre, au bord d'une allée gravillonnée : rognage à 40 cm de profondeur avec une rogneuse sur chenilles, évacuation des copeaux, rebouchage en grave compactée pour l'allée.</p>
    {NOTE_EX}
    {CTA.format("Une très grosse souche à enlever ?")}

    <h2>Prix indicatifs</h2>
    {prix([S_PETITE, S_GROSSE], "Prix indicatif", "Souche")}

    <h2>Pente et protections</h2>
    <p>Dans la vallée du Cens, une rogneuse sur chenilles passe là où une machine sur roues glisserait. Dans un espace boisé classé, retirer une souche peut être lié à une replantation demandée : on vérifie avec vous.</p>
""",
    [("Faut-il toujours enlever une souche ?",
      "Non. Loin des passages, une souche peut rester et se décomposer. On l'enlève quand elle gêne ou fait des rejets."),
     ("Peut-on refaire une allée sur une souche rognée ?",
      "Oui, si on rogne assez profond et qu'on rebouche en grave compactée plutôt qu'avec les copeaux.")],
    "Une souche à enlever à Orvault ?")


# =====================================================================
# REZÉ
# =====================================================================

ajoute("tonte", "reze",
    "Tonte de pelouse à Rezé : jardins de ville | Jean Ferret",
    "Tonte et entretien de jardin à Rezé : jardins en lanière de Pont-Rousseau, petites cours de Trentemoult, accès à pied. Herbe emportée, devis gratuit.",
    "Tonte et entretien de jardin à Rezé",
    "À Rezé, les jardins sont souvent longs et étroits, ou minuscules comme à Trentemoult. On vient à pied s'il le faut, et on repart avec tout.",
    f"""
    <h2>Jardins en lanière et cours de Trentemoult</h2>
    <p>À Pont-Rousseau et autour de la Houssais, les jardins font 6 à 8 m de large pour 30 à 40 m de long. La tonte est rapide, mais les bordures sont nombreuses. À Trentemoult, il n'y a pas d'accès véhicule : on porte la tondeuse, et parfois on travaille au coupe-bordure seulement, car la pelouse fait quelques mètres carrés.</p>

    <h2>Près de la Sèvre</h2>
    <p>Les terrains proches de la Sèvre et de la Loire restent humides l'hiver, et la pelouse se remplit de mousse sous les arbres. Un passage de scarificateur au printemps et une tonte plus haute en été la gardent verte.</p>

    <h2>Exemple de chantier type à Rezé</h2>
    <p>Un jardin en lanière de 300 m² à Pont-Rousseau, avec allée centrale et massifs de chaque côté : tonte, bordures de l'allée, désherbage, taille des arbustes qui débordent, déchets sortis par le couloir.</p>
    {NOTE_EX}
    {CTA.format("Un jardin de ville à entretenir ?")}

    <h2>Prix indicatifs</h2>
    {prix([TONTE, ("Petite cour ou jardin sans accès", "forfait selon photo")], "Prix", "Terrain")}

    <h2>Déchets verts</h2>
    <p>La déchèterie de Rezé est rue Pierre Legendre, réservée aux particuliers de la Métropole (horaires à vérifier). Avec nous, les tontes sont emportées.</p>
""",
    [("Venez-vous pour une toute petite pelouse ?",
      "Oui, souvent avec d'autres travaux : taille, désherbage, nettoyage. On fait un forfait selon le jardin."),
     ("Ma pelouse est pleine de mousse, que faire ?",
      "Scarifier au printemps, tondre moins court et éclaircir les arbres qui font de l'ombre.")],
    "Un jardin à entretenir à Rezé ?")


ajoute("cloture", "reze",
    "Clôture à Rezé : brise-vue et claustras | Jean Ferret",
    "Pose de clôture à Rezé : claustras et brise-vue pour jardins de ville, clôtures sur muret côté rue, pose sans accès véhicule. Dès 40 € le mètre posé.",
    "Pose de clôture et de claustras à Rezé",
    "À Rezé, on pose surtout des clôtures courtes et soignées : un claustra pour cacher une terrasse, une clôture sur muret côté rue, un brise-vue entre deux jardins en lanière.",
    f"""
    <h2>Claustras pour petits jardins</h2>
    <p>Dans un jardin en lanière, quelques mètres de claustras bien placés suffisent à créer un coin terrasse à l'abri des regards. On pose des panneaux bois, composite ou métal, fixés sur poteaux scellés ou sur platines quand il y a une dalle.</p>

    <h2>Côté rue, sur muret</h2>
    <p>Beaucoup de maisons de Pont-Rousseau ou de Ragon ont un muret bas côté rue. On fixe la clôture dessus, avec des poteaux chevillés ou des platines, en respectant la hauteur totale prévue par le plan d'urbanisme.</p>

    <h2>Exemple de chantier type à Rezé</h2>
    <p>Une terrasse de maison de ville à Trentemoult, exposée aux regards de la ruelle : 7 m de claustras bois de 1,80 m fixés sur platines, matériel porté à pied depuis le quai, ancien grillage évacué.</p>
    {NOTE_EX}
    {CTA.format("Une terrasse à protéger des regards ?")}

    <h2>Prix indicatifs</h2>
    {prix([CLOT, ("Claustras sur platines, fourniture", "sur devis")], "Prix indicatif", "Prestation")}

    <h2>Règles à Rezé</h2>
    <p>Rezé applique le plan local d'urbanisme de Nantes Métropole. À Trentemoult et dans les secteurs de patrimoine, l'aspect des clôtures est encadré et une déclaration préalable peut être nécessaire. Vérifiez en mairie avant de choisir le modèle.</p>
""",
    [("Peut-on poser une clôture sur une dalle ?",
      "Oui, avec des poteaux sur platines vissées dans la dalle, sans creuser."),
     ("Faut-il une autorisation à Trentemoult ?",
      "C'est un secteur de patrimoine : une déclaration préalable est souvent demandée. Renseignez-vous en mairie avant.")],
    "Une clôture à poser à Rezé ?")


ajoute("terrassement", "reze",
    "Terrassement à Rezé : jardins et terrasses | Jean Ferret",
    "Terrassement et mise à niveau à Rezé : préparation de terrasses, jardins en zone inondable de la Loire et de la Sèvre, accès étroits. Devis gratuit.",
    "Terrassement et mise à niveau à Rezé",
    "À Rezé, on prépare surtout des zones de terrasse et on remet à niveau des jardins de ville. Près de la Loire et de la Sèvre, on vérifie d'abord la carte des crues.",
    f"""
    <h2>Préparer une terrasse</h2>
    <p>Avant de poser une terrasse en bois ou en dalles, il faut décaisser, poser un géotextile et une couche de grave compactée, avec une légère pente pour l'eau. C'est la partie qu'on fait : le support propre et plat sur lequel le poseur de terrasse, ou vous, pourra travailler.</p>

    <h2>Zones inondables</h2>
    <p>Trentemoult, les bords de Sèvre et certains secteurs bas sont en zone inondable. Surélever un jardin y est encadré par le plan de prévention des risques d'inondation : on ne remblaie pas sans avoir vérifié. Un simple nivellement sans apport de terre reste en général possible.</p>

    <h2>Exemple de chantier type à Rezé</h2>
    <p>Une zone de 25 m² au fond d'un jardin de la Houssais, pour une future terrasse bois : décaissement de 20 cm à la main et au mini-engin, terre évacuée en big-bags, géotextile, grave compactée et réglée.</p>
    {NOTE_EX}
    {CTA.format("Une terrasse à préparer ?")}

    <h2>Prix indicatifs</h2>
    {prix([TERR, ("Décaissement et grave pour terrasse", "selon la surface")], "Prix", "Travaux")}

    <h2>Accès et réseaux</h2>
    <p>Dans les jardins sans accès, la terre sort en big-bags par le couloir ou la ruelle. Avant de creuser, on fait la déclaration de travaux auprès des réseaux, souvent nombreux sous les jardins de ville.</p>
""",
    [("Posez-vous aussi la terrasse ?",
      "On prépare le support : décaissement, géotextile, grave compactée. La pose du bois ou des dalles peut se faire ensuite par vous ou un poseur."),
     ("Peut-on remblayer un jardin à Trentemoult ?",
      "C'est une zone inondable : le remblai y est très encadré. On vérifie le plan de prévention avant.")],
    "Un terrain à reprendre à Rezé ?")


ajoute("souche", "reze",
    "Dessouchage à Rezé : souches de fruitiers | Jean Ferret",
    "Enlèvement de souches à Rezé : vieux fruitiers, figuiers qui repoussent, souches dans les jardins sans accès de Trentemoult. Rognage dès 260 €.",
    "Enlèvement de souches à Rezé",
    "Les jardins rezéens ont souvent eu un verger avant d'être un jardin de ville. Il en reste des souches de vieux pommiers, de pruniers, et des figuiers qui repoussent sans fin.",
    f"""
    <h2>Fruitiers et figuiers</h2>
    <p>Une souche de pommier ou de poirier se rogne facilement. Le figuier et le prunier, eux, font des rejets tout autour de la souche pendant des années. Pour les arrêter, on rogne la souche et on suit les racines qui portent des rejets. Pour un figuier ancien, il faut parfois deux passages à un an d'écart.</p>

    <h2>Sans accès</h2>
    <p>À Trentemoult et dans beaucoup de jardins de Pont-Rousseau, la machine doit passer par la maison ou une ruelle. On utilise une rogneuse compacte, et on protège sols et seuils pendant le passage.</p>

    <h2>Exemple de chantier type à Rezé</h2>
    <p>La souche d'un vieux figuier qui refait des rejets chaque printemps dans un jardin de Trentemoult : rognage à 30 cm, broyage des racines porteuses de rejets, rebouchage, copeaux en trop sortis en sacs par la ruelle.</p>
    {NOTE_EX}
    {CTA.format("Une souche qui repousse ?")}

    <h2>Prix indicatifs</h2>
    {prix([S_PETITE, ("Figuier ou prunier avec rejets", "sur devis, après photo")], "Prix indicatif", "Souche")}

    <h2>Avant de rogner</h2>
    <p>On vérifie les canalisations et réseaux enterrés, nombreux dans les jardins de ville. Près d'un réseau, la déclaration de travaux est obligatoire.</p>
""",
    [("Comment arrêter les rejets d'un figuier ?",
      "En rognant la souche et les grosses racines qui portent les rejets. Un deuxième passage l'année suivante est parfois utile."),
     ("La rogneuse passe-t-elle par la maison ?",
      "Oui, une rogneuse compacte passe dans un couloir ou un portillon. On protège les sols.")],
    "Une souche à enlever à Rezé ?")
