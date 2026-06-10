# xioo® KlickTipp Guides

Öffentliche statische xioo® Website für KlickTipp-Guides zu Leadgenerierung, E-Mail-Marketing, Follow-up und CRM-naher Kontaktführung.

## Repository-Zweck

Dieses Repository enthält nur KlickTipp-bezogene öffentliche Seiten.

Andere Partnerprogramme, Produktkandidaten, Backlogs und interne Bewertungen gehören nicht in dieses Repository. Für andere aktive Partnerprogramme werden eigene öffentliche Repositories genutzt.

## Struktur

```text
/
  index.html
  ueber-xioo/
    index.html
  grundlagenkurs/
    index.html
  leads-generieren/
    landingpage-ohne-programmierer/
      index.html
    leadmagnet-automatisch-ausliefern/
      index.html
    optin-formular-starten/
      index.html
    newsletter-empfehlungen/
      index.html
    sms-und-email-leads/
      index.html
  email-marketing/
    newsletter-schneller-erstellen/
      index.html
    betreffzeilen-und-ki-copywriter/
      index.html
    email-zustellbarkeit-verbessern/
      index.html
    newsletter-analytics-verstehen/
      index.html
    dynamische-inhalte-personalisierung/
      index.html
  marketing-crm/
    tags-statt-listenchaos/
      index.html
    kontakte-zentral-organisieren/
      index.html
    segmentierung-nach-interesse/
      index.html
    doppelte-kontakte-vermeiden/
      index.html
    kontakthistorie-und-leadvalue/
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
      social/
        klicktipp-guides-social.png
        grundlagenkurs-social.png
        follow-up-system-social.png
        follow-up-checkliste-social.png
        lead-magnet-social.png
        webinar-follow-up-social.png
  rechtliches/
    impressum.html
    datenschutz.html
  partials/
    header.html
    footer.html
  scripts/
    generate-suite-pages.py
    sync-shared-layout.py
  CNAME
  google1d032a5e65392c5c.html
  robots.txt
  sitemap.xml
  xioo-affiliate-sites/
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
10. Kanonische Kampagnen-URL für den ersten Follow-up-Test ist `https://klicktipp.xioo.de/follow-up-prozess/`.
11. Google-Search-Console-Verifikationsdateien bleiben im Root, solange die Property aktiv ist.
12. Header und Footer werden über `partials/` gepflegt und mit `scripts/sync-shared-layout.py` statisch in alle HTML-Seiten geschrieben.
13. Die 15 Marketing-Suite-Guides werden über `scripts/generate-suite-pages.py` erzeugt und danach mit dem Shared-Layout synchronisiert.
14. Der alte Search-Console-Sitemap-Pfad `xioo-affiliate-sites/sitemap.xml` bleibt als kompatible Kopie der Hauptsitemap bestehen.
15. Strukturierte Daten werden nur für semantische Einordnung genutzt; sie ersetzen keine inhaltliche Qualität und garantieren keine Google-Indexierung.

## Website- und Design-Richtung

Die Seiten bilden eine zusammenhängende KlickTipp-Guide-Website, nicht einzelne isolierte Landingpages.

Navigationsprinzip:

1. alle öffentlichen Guide-Seiten sind über die obere Hauptnavigation erreichbar,
2. die obere Hauptnavigation führt in die Hauptbereiche `Start`, `Grundlagenkurs`, `Leads`, `E-Mail`, `CRM` und `Follow-up`,
3. jede Seite hat einen sichtbaren KlickTipp-CTA im Header,
4. jede Seite verweist im Footer auf alle Guides und Rechtstexte,
5. die Startseite bündelt die gesamte Guide-Struktur,
6. Unterseiten bleiben thematisch fokussiert, führen aber in die Gesamtwebsite zurück.
7. `ueber-xioo/` erklärt Redaktion, Grenzen, Affiliate-Rolle und Prüflogik der Website.

Die neuen Marketing-Suite-Guides sind nach Kundenproblemen sortiert:

1. `leads-generieren/` für Landingpages, Leadmagnete, Opt-in-Formulare, Empfehlungen sowie SMS- und E-Mail-Leads,
2. `email-marketing/` für Newsletter-Erstellung, KI-Copywriting, Zustellbarkeit, Analytics und dynamische Inhalte,
3. `marketing-crm/` für Tags, zentrale Kontakte, Segmentierung, Datenqualität und LeadValue.

Das Layout ist hochwertig, sachlich und rasterbasiert:

1. klare schwarze und weiße Flächen,
2. dezente blaue Akzente,
3. kompakte Sticky-Navigation mit Markenbereich und primärem CTA,
4. große, direkte Überschriften,
5. wenige, stabile Inhaltsmodule,
6. kleine Affiliate-Offenlegung im Footer.

Die Gestaltung ist an moderne Enterprise-Websites und Rasterprinzipien angelehnt, verwendet aber keine fremden Markenbestandteile.

## Modulare Pflege

Die Website bleibt bewusst statisch, damit GitHub Pages ohne Build-System funktioniert und Suchmaschinen Header, Navigation und Footer direkt im ausgelieferten HTML sehen.

Zentrale Layout-Bausteine:

1. `partials/header.html` für Markenbereich, Hauptnavigation und Header-CTA,
2. `partials/footer.html` für Footer-Navigation, Rechtstexte und Affiliate-Hinweis,
3. `scripts/sync-shared-layout.py` für die statische Synchronisierung in alle Seiten.

Marketing-Suite-Seiten:

1. Inhalte und Metadaten der 15 neuen Bereichsseiten liegen in `scripts/generate-suite-pages.py`.
2. Das Skript erzeugt die HTML-Dateien und aktualisiert die Sitemap.
3. Das Skript schreibt zusätzlich eine kompatible Sitemap unter `xioo-affiliate-sites/sitemap.xml`, weil dieser alte Pfad in der Google Search Console eingereicht wurde.
4. Danach muss `scripts/sync-shared-layout.py` ausgeführt werden.

Nach Änderungen an Header oder Footer wird ausgeführt:

```bash
python3 scripts/sync-shared-layout.py
```

Nach Änderungen an den Marketing-Suite-Guides wird ausgeführt:

```bash
python3 scripts/generate-suite-pages.py
python3 scripts/sync-shared-layout.py
```

Das Skript ersetzt die markierten Bereiche zwischen `xioo-shared-header` und `xioo-shared-footer`. Inhalte, Metadaten, SEO-Texte und Seitensektionen bleiben weiterhin direkt in den jeweiligen HTML-Dateien.

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

Kompatibler alter Search-Console-Pfad:

```text
https://klicktipp.xioo.de/xioo-affiliate-sites/sitemap.xml
```

Beide Dateien enthalten denselben URL-Bestand. Die Hauptsitemap bleibt die kanonische Sitemap, der alte Pfad dient nur dazu, den früheren Search-Console-Abruffehler zu entschärfen.

Die zusätzlichen SEO-Einstiegsseiten führen intern auf die zentrale Follow-up-Seite, den Grundlagenkurs-Guide und die übrigen Guides zurück. Die Website bleibt auf KlickTipp als Partnerprogramm verengt und wird nicht um andere Partnerprogramme erweitert.

## Indexierungsverbesserungen

Seit `xioo-0049` wurden zusätzliche Indexierungs- und Qualitätssignale ergänzt:

1. eigene Seite `ueber-xioo/` für redaktionelle Einordnung, Grenzen und Affiliate-Abgrenzung,
2. strukturierte Daten für Startseite, Hauptguides, Marketing-Suite-Guides und Über-Seite,
3. Breadcrumb-, Article-, FAQ- und ItemList-Daten, wo sie zum sichtbaren Inhalt passen,
4. sichtbares xioo-Prüfraster auf den Marketing-Suite-Guides,
5. zusätzliche Entscheidungshilfen auf Startseite, Follow-up-Seite und Grundlagenkurs,
6. Aktualisierung der Sitemap-`lastmod`-Werte auf `2026-06-10`,
7. kompatible Legacy-Sitemap für den alten Search-Console-Pfad.

Wichtig: Diese Änderungen beseitigen technische und inhaltliche Schwächen, garantieren aber keine Indexierung. Die URL-Prüfung und Indexierungsanfrage in Google Search Console bleiben manuelle Folgeschritte.

## Grundlagenkurs-Seite

Die Seite `grundlagenkurs/` bewirbt den KlickTipp Grundlagenkurs als Einstieg in einen strukturierten KlickTipp-Start.

Die Seite adressiert vor allem drei Kundenprobleme:

1. unklarer Start mit KlickTipp,
2. technische und organisatorische Einrichtung als Bremse,
3. Kontakte ohne E-Mail-Strecke, Leadmagnet, Sales-Funnel oder Vertrauensaufbau.

Primärer Partnerlink:

```text
https://www.klicktipp.com/de/support/wissensdatenbank/grundlagenkurs/?a=226599
```

## Social Previews

Die öffentlichen Guide-Seiten nutzen große Linkvorschauen für X und andere Open-Graph-Verbraucher.

Regeln:

1. `twitter:card` steht auf `summary_large_image`,
2. jede inhaltliche Seite hat ein eigenes `og:image` und `twitter:image`,
3. Bild-URLs sind absolute HTTPS-URLs unter `https://klicktipp.xioo.de/assets/img/social/`,
4. Social-Bilder haben 1200 x 630 Pixel,
5. die Sitemap enthält Bildverweise für die sechs inhaltlichen Seiten,
6. keine KlickTipp-Logos, Account-Screenshots oder privaten Werbemittel als Linkbild verwenden.

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
