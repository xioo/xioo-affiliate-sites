# xioo KlickTipp Guides

Öffentliche statische xioo Seiten für das KlickTipp-Partnerprogramm.

## Geplanter Repository-Name

Das Repository soll von `xioo-affiliate-sites` auf `xioo-klicktipp-guides` umbenannt werden.

Warum:

1. Das Repo ist kein Sammelrepo für mehrere Partnerprogramme.
2. Öffentlich sichtbar sind nur KlickTipp-bezogene Seiten.
3. Andere Partnerprogramme bekommen bei Freigabe eigene öffentliche Repositories.
4. Interne Kandidaten, Backlogs und Bewertungen bleiben im privaten xioo-Hauptprojekt.

## Status

Entwurfsstand. Noch nicht für produktive Veröffentlichung freigegeben.

Vor Veröffentlichung prüfen:

1. Impressum mit korrekten Angaben ergänzen.
2. Datenschutzhinweis prüfen.
3. echten Digistore24-KlickTipp-Promolink einsetzen.
4. Affiliate-Hinweis im Footer und Plattformkennzeichnung prüfen.
5. Claims gegen KlickTipp-, Digistore24- und Wettbewerbsregeln prüfen.
6. GitHub Pages erst danach aktivieren.
7. `robots.txt` und `noindex` erst nach Freigabe ändern.

## Struktur

```text
/
  index.html
  follow-up-prozess/
    index.html
  assets/
    css/
      styles.css
    img/
      README.md
  rechtliches/
    impressum.html
    datenschutz.html
  legal/
    impressum.html
    datenschutz.html
  robots.txt
```

`legal/` bleibt nur als Weiterleitungskompatibilität für alte Pfade bestehen. Neue rechtliche Seiten liegen unter `rechtliches/`.

## Regeln

1. Keine privaten xioo-Dokumente in dieses Repository kopieren.
2. Keine Digistore24- oder KlickTipp-Account-Screenshots veröffentlichen.
3. Keine Zahlungs-, Login-, Steuer- oder KYC-Daten speichern.
4. Keine nicht freigegebenen Werbemittel hochladen.
5. Keine Garantien zu Umsatz, DSGVO, Zustellbarkeit oder Conversion formulieren.
6. Nicht den Eindruck erwecken, xioo sei offizieller KlickTipp-Support.
7. Keine weiteren Partnerprogramme in diesem Repository ergänzen.
8. Keine Backlog-Seiten, Produktkandidaten oder internen Testnotizen veröffentlichen.

## Design-Richtung

Das Layout ist sachlich und rasterbasiert:

1. klare schwarze und weiße Flächen,
2. dezente blaue Akzente,
3. große, direkte Überschriften,
4. wenige, stabile Inhaltsmodule,
5. kleine Affiliate-Offenlegung im Footer.

Die Gestaltung ist an moderne Enterprise-Websites und Rasterprinzipien angelehnt, verwendet aber keine fremden Markenbestandteile.

## GitHub Pages

Empfohlene Einstellung nach Freigabe:

```text
Settings -> Pages -> Deploy from a branch -> main -> /root
```

Bis alle Pflichtangaben fertig sind, bleibt `robots.txt` auf `Disallow: /` und die Seiten enthalten `noindex`.
