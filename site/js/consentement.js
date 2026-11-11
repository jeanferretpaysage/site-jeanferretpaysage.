/* Bandeau cookies conforme CNIL + Google Consent Mode v2.
   Tant que GA_ID et ADS_ID sont vides, aucun cookie n'est déposé et aucun bandeau ne s'affiche.
   Pour activer : renseigner l'identifiant Google Analytics (G-XXXX) et/ou Google Ads (AW-XXXX). */
(function () {
  var GA_ID = '';   // ex. 'G-ABC123XYZ'
  var ADS_ID = '';  // ex. 'AW-123456789'
  var CLE = 'jf-cookies', DUREE = 182 * 24 * 3600 * 1000; // choix gardé 6 mois

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { dataLayer.push(arguments); };
  gtag('consent', 'default', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' });

  function lire() { try { var c = JSON.parse(localStorage.getItem(CLE)); return c && Date.now() - c.t < DUREE ? c.v : null; } catch (e) { return null; } }
  function ecrire(v) { try { localStorage.setItem(CLE, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {} }
  var charge = false;
  function activer() {
    gtag('consent', 'update', { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'denied', analytics_storage: 'granted' });
    if (charge) return; charge = true;
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + (GA_ID || ADS_ID); document.head.appendChild(s);
    gtag('js', new Date()); if (GA_ID) gtag('config', GA_ID); if (ADS_ID) gtag('config', ADS_ID);
  }
  function bandeau() {
    if (document.getElementById('jf-cookies')) return;
    var b = document.createElement('div'); b.id = 'jf-cookies'; b.setAttribute('role', 'dialog'); b.setAttribute('aria-label', 'Cookies');
    b.innerHTML = '<p><strong>Cookies</strong> · Avec votre accord, nous mesurons la fréquentation du site et l’efficacité de nos annonces Google. Aucune donnée n’est vendue. <a href="/confidentialite/#cookies">En savoir plus</a></p>'
      + '<div><button type="button" data-c="non">Refuser</button><button type="button" data-c="oui">Accepter</button></div>';
    b.addEventListener('click', function (e) { var v = e.target.getAttribute('data-c'); if (!v) return; ecrire(v); if (v === 'oui') activer(); else gtag('consent', 'update', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' }); b.remove(); });
    var st = document.createElement('style');
    st.textContent = '#jf-cookies{position:fixed;left:12px;right:12px;bottom:76px;z-index:60;max-width:560px;margin:0 auto;background:#fff;color:#1d2a1f;border:1px solid #dde3dc;border-radius:8px;box-shadow:0 6px 24px rgba(0,0,0,.18);padding:14px 16px;font-size:.88rem}'
      + '#jf-cookies p{margin:0 0 10px}#jf-cookies div{display:flex;gap:8px}#jf-cookies button{flex:1;padding:10px;border-radius:6px;font-weight:700;cursor:pointer;border:2px solid #1f4d2e;background:#fff;color:#1f4d2e}'
      + '#jf-cookies button[data-c=oui]{background:#1f4d2e;color:#fff}@media(min-width:900px){#jf-cookies{bottom:16px}}';
    document.head.appendChild(st); document.body.appendChild(b);
  }
  var actif = GA_ID || ADS_ID;
  document.addEventListener('click', function (e) {
    if (!e.target.closest || !e.target.closest('[data-cookies]')) return;
    e.preventDefault();
    if (actif) bandeau(); else alert('Aucun cookie de mesure n’est utilisé sur ce site pour le moment.');
  });
  if (!actif) return;
  var choix = lire();
  if (choix === 'oui') activer(); else if (choix === null) document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', bandeau) : bandeau();
})();
