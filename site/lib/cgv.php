<?php
// Conditions générales de vente : une seule source pour le devis PDF et la page du site.
const ASSUREUR   = ''; // nom et adresse de l'assureur RC pro, à compléter
const MEDIATEUR  = ''; // nom, adresse et site du médiateur de la consommation, à compléter
const CGV_VERSION = 'Version du 11/11/2026';

function cgv() {
  $assur = ASSUREUR !== '' ? 'souscrite auprès de ' . ASSUREUR . ', couvrant l\'activité en France' : 'couvrant son activité';
  $med = MEDIATEUR !== ''
    ? 'En cas de litige non résolu par une réclamation écrite préalable, le client peut recourir gratuitement au médiateur de la consommation : ' . MEDIATEUR . '.'
    : 'En cas de litige non résolu par une réclamation écrite préalable, le client peut recourir gratuitement à un médiateur de la consommation, dont les coordonnées figurent sur jeanferretpaysage.fr.';
  return [
    ['1. Objet', 'Les présentes conditions s\'appliquent aux travaux réalisés par Jean Ferret Paysage (Jean Ferret, entrepreneur individuel, SIREN ' . SIREN . ', ' . ADRESSE . ') : élagage, abattage, taille et abattage de haies, enlèvement de souches, tonte, création de pelouse, terrassement, pose de clôtures et de claustras. Toute acceptation d\'un devis vaut acceptation de ces conditions.'],
    ['2. Devis', 'Le devis est gratuit et valable ' . VALIDITE_JOURS . ' jours. Lorsqu\'il est établi en ligne, il repose sur les informations et photos fournies par le client. Le prix est confirmé lors d\'une visite gratuite avant les travaux. Si l\'état réel du chantier diffère (dimensions, accès, état de l\'arbre, réseaux), un devis rectificatif est proposé ; il ne s\'applique qu\'après accord du client, qui peut aussi renoncer sans frais.'],
    ['3. Acceptation', 'Le contrat est conclu dès l\'acceptation du devis par le client : en ligne avec le bouton « Bon pour accord », ou par le renvoi du devis daté et signé avec la mention « Bon pour accord ».'],
    ['4. Prix', 'Les prix sont forfaitaires, en euros, nets : TVA non applicable, article 293 B du CGI. Sauf mention contraire, ils comprennent la main-d\'œuvre, le matériel de l\'entreprise (nacelle, tronçonneuses, broyeur) et, si indiqué, l\'évacuation des déchets verts. La fourniture des matériaux (clôtures, panneaux, semences) et la location de matériel spécifique ne sont comprises que si elles figurent au devis.'],
    ['5. Exécution des travaux', 'La date d\'intervention est fixée d\'un commun accord. Elle peut être décalée en cas d\'intempéries, de vent fort ou de sol détrempé, pour des raisons de sécurité, sans pénalité de part et d\'autre. Le client assure l\'accès au chantier, signale les réseaux enterrés ou aériens connus (eau, gaz, électricité, téléphone) et prévient ses voisins si besoin. Les travaux sur un arbre ou une haie protégés (plan local d\'urbanisme, site classé, espace boisé) nécessitent l\'accord préalable des autorités : l\'entreprise informe le client, qui réalise la démarche en tant que propriétaire. Conformément à la réglementation sur la protection des oiseaux, certaines tailles de haies peuvent être reportées pendant la période de nidification.'],
    ['6. Déchets verts', 'Lorsque l\'évacuation est prévue au devis, branches, feuillage et bois sont emportés et le chantier est laissé propre. Si le client garde les déchets ou le bois, ils sont laissés sur place à l\'endroit convenu.'],
    ['7. Paiement', 'Le paiement est dû à la fin des travaux, à réception de la facture, par virement, chèque ou espèces dans la limite légale. Aucun acompte n\'est demandé sauf mention contraire au devis. En cas de retard, des pénalités au taux d\'intérêt légal peuvent être appliquées après mise en demeure.'],
    ['8. Droit de rétractation', 'Lorsque le contrat est conclu à distance ou hors établissement, le client consommateur dispose d\'un délai de 14 jours à compter de l\'acceptation pour se rétracter, sans motif ni frais (articles L221-18 et suivants du Code de la consommation). Il suffit d\'envoyer une déclaration claire, par exemple le formulaire ci-joint, par e-mail à ' . DESTINATAIRE . ' ou par courrier. Si le client demande expressément que les travaux commencent avant la fin de ce délai et se rétracte ensuite, il paie la part des travaux déjà réalisée. Une fois les travaux entièrement exécutés à sa demande expresse, il ne peut plus se rétracter.'],
    ['9. Responsabilité et assurance', 'L\'entreprise est titulaire d\'une assurance responsabilité civile professionnelle ' . $assur . '. Elle n\'est pas responsable des dommages causés par un réseau ou un ouvrage enterré non signalé, ni de l\'évolution naturelle d\'un végétal après une taille réalisée selon les règles de l\'art.'],
    ['10. Réclamations et médiation', 'Toute réclamation est adressée par écrit à ' . DESTINATAIRE . ' ou à ' . ADRESSE . '. ' . $med],
    ['11. Données personnelles', 'Les coordonnées du client servent uniquement à établir le devis, réaliser les travaux et facturer. Elles ne sont ni vendues ni cédées. Le client peut y accéder, les corriger ou demander leur suppression en écrivant à ' . DESTINATAIRE . '.'],
    ['12. Droit applicable', 'Les présentes conditions sont soumises au droit français.'],
  ];
}
function formulaire_retractation() {
  return "À l'attention de Jean Ferret Paysage, " . ADRESSE . ", " . DESTINATAIRE . " :\n"
    . "Je vous notifie par la présente ma rétractation du contrat portant sur la prestation de services ci-dessous :\n"
    . "Devis n° : ................................   Accepté le : ................................\n"
    . "Nom du client : ..................................................................................\n"
    . "Adresse du client : ...............................................................................\n"
    . "Date : ..........................   Signature (en cas d'envoi papier) : ................................";
}
