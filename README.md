# xioo® KlickTipp Guides

Öffentliche statische xioo® Website für KlickTipp-Guides zu Leadgenerierung, E-Mail-Marketing, Follow-up und CRM-naher Kontaktführung.

## Repository-Zweck

Dieses Repository enthält nur KlickTipp-bezogene öffentliche Seiten.

Andere Partnerprogramme, Produktkandidaten, Backlogs und interne Bewertungen gehören nicht in dieses Repository. Für andere aktive Partnerprogramme werden eigene öffentliche Repositories genutzt.

## Struktur

```text
/
  index.html
  follow-up-prozess/
    index.html
  follow-up-checkliste/
    index.html
  lead-magnet-nachfassen/
    index.html
  webinar-follow-up/
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
  google1d032a5e65392c5c.html
  robots.txt
  sitemap.xml
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
10. Kanonische Kampagnen-URL ist `https://klicktipp.xioo.de/follow-up-prozess/`.
11. Google-Search-Console-Verifikationsdateien bleiben im Root, solange die Property aktiv ist.

## Website- und Design-Richtung

Die Seiten bilden eine zusammenhängende KlickTipp-Guide-Website, nicht einzelne isolierte Landingpages.

Navigationsprinzip:

1. alle öffentlichen Guide-Seiten sind über die obere Hauptnavigation erreichbar,
2. jede Seite hat einen sichtbaren KlickTipp-CTA im Header,
3. jede Seite verweist im Footer auf alle Guides und Rechtstexte,
4. die Startseite bündelt die gesamte Guide-Struktur,
5. Unterseiten bleiben thematisch fokussiert, führen aber in die Gesamtwebsite zurück.

Das Layout ist hochwertig, sachlich und rasterbasiert:

1. klare schwarze und weiße Flächen,
2. dezente blaue Akzente,
3. kompakte Sticky-Navigation mit Markenbereich und primärem CTA,
4. große, direkte Überschriften,
5. wenige, stabile Inhaltsmodule,
6. kleine Affiliate-Offenlegung im Footer.

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

Für kostenlose Kampagnen werden zunächst UTM-Parameter auf der eigenen Landingpage genutzt, zum Beispiel:

```text
https://klicktipp.xioo.de/follow-up-prozess/?utm_source=x&utm_medium=social&utm_campaign=klicktipp_followup&utm_content=post_001
```

Die Sitemap liegt unter:

```text
https://klicktipp.xioo.de/sitemap.xml
```

Die zusätzlichen SEO-Einstiegsseiten führen intern auf die zentrale Follow-up-Seite und auf die übrigen Guides zurück. Die Website bleibt auf KlickTipp als Partnerprogramm verengt und wird nicht um andere Partnerprogramme erweitert.

## Google Search Console

Die HTML-Verifikation für die URL-Präfix-Property `https://klicktipp.xioo.de/` liegt im Root:

```text
https://klicktipp.xioo.de/google1d032a5e65392c5c.html
```

Die Property soll auf die Website-Start-URL zeigen, nicht auf die Sitemap-URL.

## Custom Domain

GitHub Pages ist über diese Subdomain angebunden:

```text
klicktipp.xioo.de
```

Die DNS-Auflösung erfolgt bei IONOS über CNAME:

```text
klicktipp.xioo.de -> xioo.github.io
```

Die kanonische öffentliche URL ist:

```text
https://klicktipp.xioo.de/
```

`Enforce HTTPS` ist in GitHub Pages aktiv. HTTP-Aufrufe werden auf HTTPS umgeleitet.

## GitHub Pages

Empfohlene Einstellung:

```text
Settings -> Pages -> Deploy from a branch -> main -> /root
```
