"""Blog « Conseils jardin » : la page d'accueil du blog et les articles."""

DATE = "2026-11-12"
BLOG = ("Conseils jardin", "/conseils-jardin/")

ARTICLES = [
    ("/conseils-jardin/quand-tailler-une-haie/", "Quand tailler une haie ?",
     "Les bonnes périodes selon la haie (thuyas, lauriers, photinias, champêtre) et les règles sur les nids d'oiseaux."),
    ("/conseils-jardin/prix-elagage-nantes/", "Prix d'un élagage à Nantes",
     "Ce qui fait varier le prix : hauteur, accès, déchets. Les fourchettes que l'on pratique, sans surprise."),
    ("/conseils-jardin/arbre-du-voisin/", "L'arbre du voisin dépasse chez moi",
     "Distances, branches, racines, feuilles : ce que dit le Code civil et comment régler ça à l'amiable."),
    ("/conseils-jardin/arbre-tombe-tempete/", "Arbre tombé ou abîmé après une tempête",
     "Les bons réflexes, l'assurance, et quand un arbre penché devient dangereux."),
]

SIDE_BLOG = [(t, u) for u, t, _ in ARTICLES]

PAGES = []

# ---------------------------------------------------------------- accueil du blog
cartes = "".join(
    f'    <h2><a href="{u}">{t}</a></h2>\n    <p>{d} <a href="{u}">Lire l\'article</a></p>\n'
    for u, t, d in ARTICLES)
PAGES.append(dict(
    path="/conseils-jardin/",
    title="Conseils jardin et arbres près de Nantes | Jean Ferret",
    desc="Conseils d'un élagueur nantais : quand tailler une haie, prix d'un élagage, arbre du voisin, arbre tombé après une tempête. Réponses claires et concrètes.",
    h1="Conseils jardin et arbres",
    intro="Les questions qu'on me pose le plus souvent sur les chantiers, avec des réponses simples. Pour un cas précis, le plus rapide reste d'envoyer une photo.",
    crumbs=[BLOG],
    blog_index=True,
    menu="/conseils-jardin/",
    body=cartes + """
    <div class="inline-cta"><p>Vous ne trouvez pas votre réponse ?</p><a class="btn btn-a" href="/tarifs-devis/">Envoyer une photo</a></div>
    <p>Voir aussi la <a href="/faq/">FAQ</a> et la page des <a href="/tarifs-devis/">tarifs</a>.</p>
""",
    side=[("Élagage à Nantes", "/elagage-nantes/"), ("Taille de haies", "/taille-haie-nantes/"),
          ("Abattage d'arbre", "/abattage-arbre-nantes/"), ("Tarifs et devis", "/tarifs-devis/")],
    side_liens="Nos services",
    band="Une question sur un arbre ou une haie ?",
))

# ---------------------------------------------------------------- 1. quand tailler une haie
PAGES.append(dict(
    path="/conseils-jardin/quand-tailler-une-haie/",
    title="Quand tailler une haie ? Les bonnes périodes | Jean Ferret",
    desc="Thuyas, lauriers, photinias, haie champêtre : à quelle période tailler, ce qu'il faut éviter au printemps et ce que dit la loi sur les nids d'oiseaux.",
    h1="Quand tailler une haie ?",
    intro="Deux périodes reviennent pour presque toutes les haies : la fin de l'hiver et la fin de l'été. Le détail dépend de l'essence, et du printemps, à cause des oiseaux.",
    crumbs=[BLOG, ("Quand tailler une haie", "/conseils-jardin/quand-tailler-une-haie/")],
    article=DATE,
    img=("img/taille-haie-nantes-haie-conifere-taille-haie.webp",
         "Haie de conifères en cours de taille avec un taille-haie posé au sol (photo d'illustration)"),
    body="""
    <h2>La règle simple : fin d'hiver et fin d'été</h2>
    <p>Dans la région nantaise, la plupart des haies se taillent bien à deux moments. En fin d'hiver, de février à la mi-mars, la végétation n'est pas encore repartie et on voit bien la forme de la haie. En fin d'été, de fin août à octobre, la grosse pousse de printemps est faite et la haie reste propre jusqu'à l'hiver.</p>
    <p>Une haie de jardin bien entretenue se contente souvent d'une taille par an, en septembre. Les haies qui poussent vite, comme le laurier-palme ou le photinia, en demandent deux.</p>

    <h2>Haie par haie</h2>
    <h3>Thuyas et cyprès</h3>
    <p>Fin d'hiver et septembre. Le point à retenir : un thuya ne repousse pas sur le bois nu. Si on coupe trop profond, dans la partie brune sans aiguilles, le trou reste. Une haie de thuyas trop haute se reprend donc en hauteur sans problème, mais en épaisseur avec beaucoup de prudence.</p>
    <h3>Laurier-palme</h3>
    <p>Il pousse vite et supporte bien les tailles fortes. Une taille en fin d'hiver pour reprendre la forme, une autre en septembre. Le taille-haie déchiquette les grandes feuilles, ce qui fait jaunir les bords : sur une haie très visible, une finition au sécateur est plus propre.</p>
    <h3>Photinia</h3>
    <p>Après la floraison, puis en septembre. Chaque taille relance les jeunes pousses rouges qui font tout son intérêt.</p>
    <h3>Haie champêtre (charme, noisetier, aubépine, prunellier)</h3>
    <p>Plutôt en hiver, hors gel. On évite de tout couper la même année : une haie champêtre reprise en deux hivers garde des fleurs et des fruits pour les oiseaux et repart mieux.</p>

    <h2>Le printemps et les nids d'oiseaux</h2>
    <p>De la mi-mars à la fin juillet, les oiseaux nichent dans les haies. L'Office français de la biodiversité recommande d'éviter les tailles pendant cette période.</p>
    <p>Pour un particulier, il n'y a pas d'interdiction nationale de tailler sa haie au printemps. En revanche, détruire un nid ou des œufs d'une espèce protégée est interdit toute l'année (article L411-1 du Code de l'environnement), et la plupart des oiseaux des jardins sont protégés : merle, mésange, rouge-gorge, pinson. Un arrêté préfectoral ou municipal peut aussi encadrer les tailles localement.</p>
    <p>Pour les agriculteurs, les règles de la PAC interdisent de tailler les haies du 16 mars au 15 août. C'est souvent de là que vient l'idée d'une interdiction générale.</p>
    <p>En pratique : une petite taille d'entretien au printemps reste possible si on vérifie la haie avant. S'il y a un nid occupé, on attend. Les grosses reprises se gardent pour l'automne et l'hiver.</p>

    <h2>Haie trop haute : jusqu'où peut-on descendre ?</h2>
    <p>Une haie de plus de 2 m plantée à moins de 2 m de la limite peut être réduite à la demande du voisin (article 671 du Code civil). Sur des thuyas de 4 ou 5 m, on peut descendre d'un coup à 2 m, mais le dessus restera dégarni un moment. Sur un laurier, on peut descendre beaucoup plus franchement : il repart du bois.</p>
    <div class="inline-cta"><p>Votre haie est trop haute ou trop large ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Combien coûte une taille de haie ?</h2>
    <p>Pour 30 m de haie taillée sur les deux faces et le dessus, avec ramassage et évacuation, comptez environ 500 €. Le prix change surtout avec la hauteur, l'épaisseur et l'accès à l'arrière de la haie. Le détail est sur la page <a href="/taille-haie-nantes/">taille de haies</a>.</p>
    <p>À lire aussi : <a href="/conseils-jardin/arbre-du-voisin/">l'arbre ou la haie du voisin dépasse chez moi</a>.</p>
""",
    faq=[
        ("Peut-on tailler une haie en avril ou en mai ?",
         "Oui pour une taille légère, à condition de vérifier qu'aucun oiseau n'y niche. Les tailles fortes se font plutôt en fin d'été ou en hiver."),
        ("Quand tailler une haie de thuyas ?",
         "En fin d'hiver puis en septembre, sans jamais couper dans le bois sans aiguilles, qui ne repousse pas."),
        ("Le voisin peut-il m'obliger à tailler ma haie ?",
         "Oui si elle dépasse 2 m de haut à moins de 2 m de la limite, ou si ses branches avancent chez lui (articles 671 et 673 du Code civil)."),
    ],
    side=[("Taille de haies près de Nantes", "/taille-haie-nantes/")] + SIDE_BLOG[1:],
    band="Une haie à reprendre ?",
))

# ---------------------------------------------------------------- 2. prix élagage
PAGES.append(dict(
    path="/conseils-jardin/prix-elagage-nantes/",
    title="Prix d'un élagage à Nantes en 2026 | Jean Ferret",
    desc="Combien coûte un élagage à Nantes ? Fourchettes selon la hauteur de l'arbre, ce qui fait monter le prix, l'évacuation des branches et comment payer moins.",
    h1="Prix d'un élagage à Nantes",
    intro="Le prix d'un élagage dépend surtout de trois choses : la hauteur de l'arbre, l'accès et ce qu'on fait des branches. Voici nos fourchettes, évacuation comprise.",
    crumbs=[BLOG, ("Prix d'un élagage", "/conseils-jardin/prix-elagage-nantes/")],
    article=DATE,
    img=("img/elagage-nantes-elagueur-encorde-grand-arbre.webp",
         "Élagueur encordé dans un grand arbre (photo d'illustration)"),
    body="""
    <h2>Nos fourchettes de prix</h2>
    <div class="table-wrap"><table class="prices">
      <tr><th>Hauteur de l'arbre</th><th>Prix indicatif, évacuation comprise</th></tr>
      <tr><td>Moins de 5 m</td><td>200 à 650 €</td></tr>
      <tr><td>5 à 10 m</td><td>460 à 1 170 €</td></tr>
      <tr><td>10 à 15 m</td><td>910 à 1 560 €</td></tr>
      <tr><td>Plus de 15 m</td><td>1 560 à 4 550 €</td></tr>
    </table></div>
    <p class="note">Forfait selon le chantier, TVA non applicable (art. 293 B du CGI). Devis gratuit, le prix est fixé avant de commencer.</p>

    <h2>Pourquoi un tel écart dans une même ligne ?</h2>
    <p>Deux arbres de 8 m ne demandent pas le même travail. Un tilleul isolé au milieu d'une pelouse, accessible à la nacelle, se fait vite. Le même tilleul au fond d'un jardin de ville, sans accès, au-dessus d'une véranda, demande de grimper, de descendre chaque branche à la corde et de tout sortir à la main. Le prix suit ce temps de travail.</p>
    <p>Ce qui fait monter le prix :</p>
    <ul>
      <li>pas d'accès pour la nacelle, donc travail en grimpe ;</li>
      <li>une maison, une toiture, une ligne électrique ou une route sous l'arbre ;</li>
      <li>un arbre malade ou du bois mort, qui oblige à plus de précautions ;</li>
      <li>un gros volume de branches à évacuer.</li>
    </ul>

    <h2>Élagage, taille douce, réduction : de quoi parle-t-on ?</h2>
    <p>Un élagage n'est pas forcément une coupe sévère. Le plus souvent, on retire le bois mort, on dégage une toiture ou on éclaircit le houppier pour laisser passer le vent et la lumière. Une réduction de hauteur coûte plus cher qu'un simple nettoyage, parce qu'il y a plus de coupes et plus de branches. L'étêtage, qui coupe tout le haut d'un coup, abîme l'arbre et on le déconseille.</p>

    <h2>Comment payer moins cher</h2>
    <ul>
      <li>Garder le bois : coupé en bûches et laissé sur place, il réduit le volume à évacuer.</li>
      <li>Grouper les travaux : un élagage et une taille de haie le même jour évitent un deuxième déplacement.</li>
      <li>Ne pas attendre : un arbre entretenu tous les 3 à 5 ans coûte moins cher qu'un arbre repris après 20 ans.</li>
      <li>Se mettre d'accord avec le voisin quand l'arbre est en limite : on peut partager le chantier.</li>
    </ul>
    <div class="inline-cta"><p>Le plus simple : une photo de l'arbre.</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Et l'abattage ?</h2>
    <p>Quand un arbre est mort, dangereux ou trop près de la maison, l'abattage coûte à partir de 260 € pour un petit arbre, et jusqu'à 4 550 € pour un grand arbre à démonter morceau par morceau. Le détail est sur la page <a href="/abattage-arbre-nantes/">abattage d'arbre</a>. Tous les prix sont sur la page <a href="/tarifs-devis/">tarifs et devis</a>.</p>
    <p>Pas de crédit d'impôt pour l'élagage : ces travaux n'entrent pas dans les services à la personne.</p>
""",
    faq=[
        ("Combien coûte l'élagage d'un arbre de 10 m ?",
         "Entre 460 et 1 170 € chez nous, évacuation des branches comprise. Le prix exact dépend de l'accès et de ce qu'il y a sous l'arbre."),
        ("L'évacuation des branches est-elle comprise ?",
         "Oui, nos prix comprennent le ramassage et l'évacuation des déchets verts. Si vous gardez le bois, le prix baisse."),
        ("Le devis est-il payant ?",
         "Non. Envoyez une photo de l'arbre, on vous donne une estimation, puis un prix ferme après visite si besoin."),
    ],
    side=[("Élagage à Nantes", "/elagage-nantes/"), ("Tous les tarifs", "/tarifs-devis/")] + [SIDE_BLOG[0]] + SIDE_BLOG[2:],
    band="Un arbre à élaguer ?",
))

# ---------------------------------------------------------------- 3. arbre du voisin
PAGES.append(dict(
    path="/conseils-jardin/arbre-du-voisin/",
    title="Arbre du voisin qui dépasse : vos droits | Jean Ferret",
    desc="Branches, racines, feuilles, arbre trop près de la limite : ce que dit le Code civil, qui paie l'élagage et comment régler ça sans conflit avec le voisin.",
    h1="L'arbre du voisin dépasse chez moi : que faire ?",
    intro="C'est l'une des questions qu'on nous pose le plus. Le Code civil est assez clair, et la plupart des cas se règlent par une discussion et un devis partagé.",
    crumbs=[BLOG, ("Arbre du voisin", "/conseils-jardin/arbre-du-voisin/")],
    article=DATE,
    body="""
    <h2>Les distances de plantation</h2>
    <p>Sauf règlement ou usage local différent, l'article 671 du Code civil fixe deux distances par rapport à la limite de propriété :</p>
    <ul>
      <li>2 m minimum pour un arbre ou une haie qui dépasse 2 m de haut ;</li>
      <li>50 cm minimum pour les plantations qui restent sous 2 m.</li>
    </ul>
    <p>La distance se mesure depuis le centre du tronc, la hauteur depuis le sol. Si la règle n'est pas respectée, le voisin peut demander que l'arbre soit réduit à 2 m ou arraché (article 672).</p>

    <h2>L'exception des 30 ans</h2>
    <p>Un arbre trop haut ou trop près de la limite depuis plus de 30 ans ne peut plus être contesté pour sa hauteur ou sa distance : c'est la prescription trentenaire. Les 30 ans se comptent à partir du moment où l'arbre a dépassé la hauteur autorisée, pas à partir de sa plantation. Le propriétaire qui l'invoque doit pouvoir le prouver (photos anciennes, témoignages).</p>
    <p>Attention : cette prescription ne protège pas les branches qui dépassent.</p>

    <h2>Les branches qui dépassent</h2>
    <p>Le voisin peut toujours exiger que les branches qui avancent sur son terrain soient coupées à la limite (article 673). Ce droit ne se perd jamais, même pour un arbre centenaire. Les frais sont à la charge du propriétaire de l'arbre.</p>
    <p>En revanche, on ne coupe pas soi-même les branches du voisin, même celles qui sont chez soi : il faut lui demander, puis passer par un conciliateur ou le juge s'il refuse.</p>

    <h2>Les racines, les ronces et les fruits</h2>
    <p>Les racines, ronces et brindilles qui passent chez vous, vous pouvez les couper vous-même, à la limite. Prudence sur les grosses racines : en couper une peut déstabiliser l'arbre, et c'est le propriétaire qui coupe qui en serait responsable.</p>
    <p>Les fruits tombés naturellement chez vous vous appartiennent. Ceux qui sont encore sur la branche restent au voisin.</p>

    <h2>Et les feuilles ?</h2>
    <p>Les feuilles mortes ne suffisent pas, en général, à obliger un voisin à élaguer. Les juges ne retiennent un trouble anormal du voisinage que dans des cas marqués : gouttières bouchées en permanence, perte importante de lumière, arbre dangereux.</p>
    <div class="inline-cta"><p>Besoin d'un devis à montrer à votre voisin ?</p><a class="btn btn-a" href="/tarifs-devis/">Estimer mon prix</a></div>

    <h2>Comment régler ça sans conflit</h2>
    <ol>
      <li>En parler de vive voix, photo à l'appui. Beaucoup de voisins ne voient pas ce qui dépasse de leur côté.</li>
      <li>Proposer un devis : un élagueur peut travailler des deux côtés le même jour, ce qui coûte moins cher que deux chantiers.</li>
      <li>Si rien ne bouge, envoyer un courrier recommandé qui rappelle l'article 673.</li>
      <li>Ensuite, passer par un conciliateur de justice (gratuit). Cette étape est obligatoire avant de saisir le tribunal pour ce type de litige.</li>
    </ol>

    <h2>Arbre de la commune ou haie au bord de la route</h2>
    <p>Une haie privée qui déborde sur la voie publique doit être taillée par son propriétaire. Le maire peut l'exiger et, après une mise en demeure restée sans effet, faire faire les travaux aux frais du propriétaire. Pour un arbre communal qui dépasse chez vous, adressez-vous d'abord à la mairie.</p>
    <p class="note">Ces informations sont générales. Pour un litige en cours, un conciliateur de justice ou un professionnel du droit vous dira ce qui s'applique à votre cas.</p>
    <p>À lire aussi : <a href="/conseils-jardin/quand-tailler-une-haie/">quand tailler une haie</a>, et la page <a href="/elagage-nantes/">élagage à Nantes</a>.</p>
""",
    faq=[
        ("Puis-je couper moi-même les branches du voisin qui dépassent chez moi ?",
         "Non. Vous pouvez exiger qu'il les coupe (article 673 du Code civil), mais pas les couper vous-même. Les racines, en revanche, vous pouvez les couper à la limite."),
        ("Qui paie l'élagage des branches qui dépassent ?",
         "Le propriétaire de l'arbre. Rien n'empêche de partager les frais à l'amiable, surtout si les deux côtés sont taillés le même jour."),
        ("Mon voisin a un arbre de plus de 2 m à 1 m de la limite, que faire ?",
         "Vous pouvez demander qu'il soit réduit à 2 m ou arraché, sauf s'il dépasse cette hauteur depuis plus de 30 ans."),
    ],
    side=[("Élagage à Nantes", "/elagage-nantes/"), ("Taille de haies", "/taille-haie-nantes/")] + SIDE_BLOG[:2] + [SIDE_BLOG[3]],
    band="Un arbre en limite de propriété ?",
))

# ---------------------------------------------------------------- 4. tempête
PAGES.append(dict(
    path="/conseils-jardin/arbre-tombe-tempete/",
    title="Arbre tombé après une tempête : que faire ? | Jean Ferret",
    desc="Arbre tombé, branche cassée ou arbre penché après un coup de vent près de Nantes : les bons réflexes de sécurité, l'assurance et le dégagement du terrain.",
    h1="Arbre tombé ou abîmé après une tempête",
    intro="Après un gros coup de vent, on reçoit beaucoup d'appels pour des arbres couchés ou des branches suspendues. Voici dans quel ordre faire les choses, et ce qu'il ne faut surtout pas faire seul.",
    crumbs=[BLOG, ("Arbre tombé après une tempête", "/conseils-jardin/arbre-tombe-tempete/")],
    article=DATE,
    img=("img/abattage-arbre-nantes-entaille-tronconneuse.webp",
         "Tronc en cours de découpe à la tronçonneuse (photo d'illustration)"),
    body="""
    <h2>D'abord, la sécurité</h2>
    <ul>
      <li>Éloignez tout le monde de l'arbre et des branches suspendues : une branche cassée peut tomber des heures après le vent.</li>
      <li>Si l'arbre touche un fil électrique ou téléphonique, n'approchez pas et appelez Enedis au 09 726 750 44 (dépannage, 7j/7).</li>
      <li>Si l'arbre bloque la route, prévenez la mairie ou les secours.</li>
      <li>Ne montez pas dans un arbre abîmé et ne tronçonnez pas un tronc sous tension : le bois couché est en contrainte et peut se libérer d'un coup. C'est la cause de nombreux accidents graves chaque hiver.</li>
    </ul>

    <h2>Ensuite, les photos et l'assurance</h2>
    <p>Avant de toucher à quoi que ce soit, photographiez l'arbre, les dégâts et les alentours. Déclarez le sinistre à votre assureur dans les délais de votre contrat, souvent quelques jours.</p>
    <p>La garantie tempête des contrats habitation couvre en général les dégâts causés aux bâtiments par un arbre tombé. Le dégagement et l'évacuation de l'arbre ne sont pas toujours pris en charge, surtout quand il n'a rien abîmé. Lisez votre contrat ou demandez à votre assureur, et gardez la facture de l'élagueur.</p>
    <p>Si votre arbre tombe chez le voisin, c'est en principe votre assurance qui intervient. Si l'arbre était visiblement malade ou mort avant la tempête, votre responsabilité peut être engagée.</p>

    <h2>Arbre penché, fendu ou déraciné : est-il encore sûr ?</h2>
    <p>Certains signes doivent vous alerter, même si l'arbre est encore debout :</p>
    <ul>
      <li>la terre soulevée d'un côté du pied, ou des racines arrachées ;</li>
      <li>une fente dans le tronc ou à la fourche des grosses branches ;</li>
      <li>un arbre qui penche plus qu'avant la tempête ;</li>
      <li>une grosse branche cassée restée accrochée dans le houppier.</li>
    </ul>
    <p>Dans ces cas, faites-le voir par un élagueur. Selon l'état de l'arbre, une taille de sécurité suffit, ou il faut l'abattre.</p>
    <div class="inline-cta"><p>Un arbre abîmé chez vous ?</p><a class="btn btn-a" href="/tarifs-devis/">Envoyer une photo</a></div>

    <h2>Comment on dégage un arbre tombé</h2>
    <p>On commence par sécuriser les branches suspendues, puis on découpe l'arbre couché en libérant les tensions dans le bon ordre. Sur une toiture, les morceaux sont retenus à la corde et descendus un par un. Le bois peut être coupé en bûches et laissé sur place, le reste est évacué. Il reste ensuite la souche, qu'on peut rogner pour récupérer le terrain.</p>
    <p>Après une grosse tempête, les demandes arrivent toutes en même temps. On traite d'abord les arbres dangereux pour les personnes et les maisons, puis le reste dans l'ordre des appels.</p>

    <h2>Éviter le prochain dégât</h2>
    <p>Les arbres qui tombent sont souvent des arbres jamais entretenus, avec du bois mort ou un houppier trop lourd, ou des arbres aux racines abîmées par des travaux. Un contrôle et un élagage tous les quelques années, avant l'hiver, limitent beaucoup les risques. Sur les bords de Loire et dans l'estuaire, très exposés au vent d'ouest, c'est encore plus utile.</p>
    <p>À lire aussi : <a href="/abattage-arbre-nantes/">abattage d'arbre dangereux</a>, <a href="/dessouchage-nantes/">enlèvement des souches</a> et <a href="/conseils-jardin/prix-elagage-nantes/">prix d'un élagage</a>.</p>
""",
    faq=[
        ("L'assurance paie-t-elle l'évacuation d'un arbre tombé ?",
         "Ça dépend du contrat. Les dégâts aux bâtiments sont en général couverts par la garantie tempête. Le dégagement de l'arbre ne l'est pas toujours : vérifiez auprès de votre assureur."),
        ("Mon arbre est tombé chez le voisin, qui paie ?",
         "En principe votre assurance responsabilité civile ou habitation. Prévenez-la rapidement avec des photos."),
        ("Puis-je découper moi-même un arbre tombé ?",
         "Un petit arbre au sol, oui avec prudence. Un gros tronc en tension, un arbre sur une toiture ou près d'un fil électrique, non : faites appel à un professionnel."),
    ],
    side=[("Abattage d'arbre", "/abattage-arbre-nantes/"), ("Élagage à Nantes", "/elagage-nantes/")] + SIDE_BLOG[:3],
    band="Un arbre abîmé par le vent ?",
))
