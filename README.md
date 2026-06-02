# xioo® KlickTipp Guides

Öffentliche statische xioo® Seiten für problemorientierte KlickTipp-Guides.

## Repository-Zweck

Dieses Repository enthält nur KlickTipp-bezogene öffentliche Seiten.

Andere Partnerprogramme, Produktkandidaten, Backlogs und interne Bewertungen gehören nicht in dieses Repository. Für andere aktive Partnerprogramme werden eigene öffentliche Repositories genutzt.

## Struktur

```text
/
  index.html
  follow-up-prozess/
    index.html
  assets/
    css/
      styles.css
    js/
      analytics.js
    img/
      README.md
  rechtliches/
    impressum.html
    datenschutz.html
  robots.txt
```

## Regeln

1. Keine privaten xioo®-Dokumente in dieses Repository kopieren.
2. Keine Digistore24- oder KlickTipp-Account-Screenshots veröffentlichen.
3. Keine Zahlungs-, Login-, Steuer- oder KYC-Daten speichern.
4. Keine nicht ausdrücklich nutzbaren Werbemittel hochladen.
5. Keine Garantien zu Umsatz, DSGVO, Zustellbarkeit oder Conversion formulieren.
6. Nicht den Eindruck erwecken, xioo® sei offizieller KlickTipp-Support.
7. Keine weiteren Partnerprogramme in diesem Repository ergänzen.
8. Unbekannte öffentliche Daten nur als klar erkennbare Platzhalter eintragen.
9. Cloudflare Web Analytics nur mit bewusst gesetztem Site-Token aktivieren.

## Design-Richtung

Das Layout ist sachlich und rasterbasiert:

1. klare schwarze und weiße Flächen,
2. dezente blaue Akzente,
3. große, direkte Überschriften,
4. wenige, stabile Inhaltsmodule,
5. kleine Affiliate-Offenlegung im Footer.

Die Gestaltung ist an moderne Enterprise-Websites und Rasterprinzipien angelehnt, verwendet aber keine fremden Markenbestandteile.

## Messung

Die Seiten sind für Cloudflare Web Analytics vorbereitet.

Aktueller Platzhalter:

```html
<meta name="xioo-cloudflare-web-analytics-token" content="CLOUDFLARE_WEB_ANALYTICS_TOKEN">
```

Solange dieser Platzhalter in den Seiten steht, lädt `assets/js/analytics.js` kein Cloudflare-Beacon. Nach dem Anlegen einer Website in Cloudflare Web Analytics wird nur der Platzhalter durch den echten Site-Token ersetzt.

Cloudflare Web Analytics misst Seitenaufrufe, Referrer und technische Leistungswerte. Query-Strings werden nach Cloudflare-Dokumentation derzeit nicht als auswertbare Pfade protokolliert. Deshalb werden einzelne X-Posts nicht allein über `?utm_content=post_01` getrennt ausgewertet.

Praktische Messlogik für den ersten KlickTipp-Test:

1. Cloudflare Web Analytics für Seitenaufrufe und Referrer,
2. X für Reichweite, Antworten und Interaktionen,
3. Digistore24 für Verkäufe und Provisionen,
4. bei Bedarf eigene Kampagnenpfade statt reiner UTM-Parameter.

## GitHub Pages

Empfohlene Einstellung:

```text
Settings -> Pages -> Deploy from a branch -> main -> /root
```
