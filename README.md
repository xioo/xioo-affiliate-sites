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
  CNAME
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
9. GoatCounter nur über den zentralen Analytics-Loader einbinden.

## Design-Richtung

Das Layout ist sachlich und rasterbasiert:

1. klare schwarze und weiße Flächen,
2. dezente blaue Akzente,
3. große, direkte Überschriften,
4. wenige, stabile Inhaltsmodule,
5. kleine Affiliate-Offenlegung im Footer.

Die Gestaltung ist an moderne Enterprise-Websites und Rasterprinzipien angelehnt, verwendet aber keine fremden Markenbestandteile.

## Messung

Die Seiten nutzen GoatCounter für einfache Traffic-Messung.

Aktueller Endpoint:

```html
<meta name="xioo-goatcounter-endpoint" content="https://xioo.goatcounter.com/count">
```

`assets/js/analytics.js` lädt darüber das GoatCounter-Skript von `https://gc.zgo.at/count.js`.

GoatCounter misst Seitenaufrufe, Referrer, Pfade und Kampagnenauswertungen. Der Dienst wird genutzt, weil Cloudflare Web Analytics die Hostnames `xioo.github.io` und `klicktipp.xioo.de` im Cloudflare-Konto nicht akzeptiert hat.

Praktische Messlogik für den ersten KlickTipp-Test:

1. GoatCounter für Seitenaufrufe und Referrer,
2. X für Reichweite, Antworten und Interaktionen,
3. Digistore24 für Verkäufe und Provisionen,
4. bei Bedarf eigene Kampagnenpfade statt reiner UTM-Parameter.

## Custom Domain

GitHub Pages ist zusätzlich über diese Subdomain angebunden:

```text
klicktipp.xioo.de
```

Die DNS-Auflösung erfolgt bei IONOS über CNAME:

```text
klicktipp.xioo.de -> xioo.github.io
```

## GitHub Pages

Empfohlene Einstellung:

```text
Settings -> Pages -> Deploy from a branch -> main -> /root
```
