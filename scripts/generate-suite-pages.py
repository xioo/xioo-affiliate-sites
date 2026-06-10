#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LASTMOD = "2026-06-10"
SITE = "https://klicktipp.xioo.de"
SOCIAL_IMAGE = f"{SITE}/assets/img/social/klicktipp-guides-social.png?v=20260602-2"

AREAS = {
    "leads": {
        "label": "Leads generieren",
        "nav": "Leads",
        "dir": "leads-generieren",
        "hero": "hero-leads",
        "partner": "https://www.klicktipp.com/de/marketing-suite/leads-generieren/?a=226599",
        "cta": "Lead-Funktionen ansehen",
        "source": "https://www.klicktipp.com/de/marketing-suite/leads-generieren/",
        "image": "https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=1400&q=85",
        "image_alt": "Team plant eine Leadgenerierungskampagne an einem digitalen Arbeitsplatz",
    },
    "email": {
        "label": "E-Mail-Marketing",
        "nav": "E-Mail",
        "dir": "email-marketing",
        "hero": "hero-email",
        "partner": "https://www.klicktipp.com/de/marketing-suite/email-marketing/?a=226599",
        "cta": "E-Mail-Marketing ansehen",
        "source": "https://www.klicktipp.com/de/marketing-suite/email-marketing/",
        "image": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1400&q=85",
        "image_alt": "Arbeitsplatz für E-Mail-Marketing mit Laptop und Notizen",
    },
    "crm": {
        "label": "Marketing CRM",
        "nav": "CRM",
        "dir": "marketing-crm",
        "hero": "hero-crm",
        "partner": "https://www.klicktipp.com/de/marketing-suite/marketing-crm/?a=226599",
        "cta": "Marketing CRM ansehen",
        "source": "https://www.klicktipp.com/de/marketing-suite/marketing-crm/",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1400&q=85",
        "image_alt": "Dashboard mit Kundendaten und Marketingauswertung",
    },
}

PAGES = [
    {
        "area": "leads",
        "slug": "landingpage-ohne-programmierer",
        "title": "Landingpage ohne Programmierer mit KlickTipp planen",
        "meta": "Guide für kleine Anbieter: Landingpage, Opt-in und Leadstrecke mit KlickTipp planen, ohne sofort Entwickler, Designer oder eigene Technik zu brauchen.",
        "hero": "Baue Deine erste Lead-Landingpage ohne Technikchaos.",
        "lead": "Wenn Du Leads gewinnen willst, brauchst Du nicht zuerst ein großes Website-Projekt. Du brauchst eine klare Seite, ein klares Angebot und einen nächsten Schritt.",
        "intro": "KlickTipp positioniert seinen Landingpage-Builder als Weg, um responsive Seiten, Opt-in-Formulare und KI-unterstützte Texte zusammenzubringen. Diese Seite zeigt Dir, wie Du daraus einen einfachen Leadprozess machst.",
        "problems": [
            ("Du wartest auf Technik.", "Die Idee für Dein Angebot ist da, aber Website, Formular und Follow-up hängen an zu vielen Einzelaufgaben."),
            ("Deine Seite sammelt keine Kontakte.", "Besucher lesen, klicken vielleicht kurz und verschwinden wieder, weil kein klarer nächster Schritt sichtbar ist."),
            ("Dein Freebie steht allein.", "Ein Leadmagnet bringt wenig, wenn danach keine E-Mail-Strecke und keine Segmentierung folgen."),
        ],
        "steps": [
            "Wähle genau ein Problem, das Deine Zielgruppe sofort erkennt.",
            "Formuliere ein kurzes Nutzenversprechen und eine klare Handlung.",
            "Verbinde Opt-in, Danke-Seite und erste E-Mail-Strecke.",
            "Markiere die Herkunft des Leads mit einem Tag.",
            "Miss, ob Besucher wirklich zum Formular kommen und sich eintragen.",
        ],
        "klicktipp": [
            "Landingpage-Builder für schnelle Seitenentwürfe",
            "Opt-in-Formulare direkt im Leadprozess",
            "KI-gestützte Textideen als Startpunkt",
            "Leadmagnet-Auslieferung über anschließende E-Mails",
            "Tags für Quelle, Interesse und nächsten Schritt",
        ],
    },
    {
        "area": "leads",
        "slug": "leadmagnet-automatisch-ausliefern",
        "title": "Leadmagnet automatisch ausliefern und nachfassen",
        "meta": "Guide für Freebies, PDFs und Checklisten: So wird ein Leadmagnet mit KlickTipp zum Startpunkt einer sinnvollen E-Mail-Strecke.",
        "hero": "Lass Deinen Leadmagneten nicht als toten Download enden.",
        "lead": "Ein PDF, eine Checkliste oder ein Video ist nur der Anfang. Wert entsteht, wenn danach eine gute Begrüßung, Einordnung und ein nächster Schritt folgen.",
        "intro": "KlickTipp kann Leadgewinnung, Opt-in und E-Mail-Marketing verbinden. Für Dich zählt: Der Kontakt soll den Leadmagnet bekommen und danach verstehen, warum Dein Angebot relevant ist.",
        "problems": [
            ("Der Download wird manuell verschickt.", "Das kostet Zeit und führt dazu, dass Kontakte ungleich behandelt werden."),
            ("Nach dem Freebie passiert nichts.", "Der Lead hat Interesse gezeigt, bekommt aber keinen klaren Pfad zur nächsten Entscheidung."),
            ("Du weißt nicht, welcher Leadmagnet wirkt.", "Ohne Tags und Messung bleibt unklar, welche Themen später zu Gesprächen oder Verkäufen führen."),
        ],
        "steps": [
            "Definiere, welches konkrete Problem Dein Leadmagnet löst.",
            "Erstelle ein Opt-in mit klarer Erwartung und sauberer Einwilligung.",
            "Sende den Leadmagnet automatisch und ohne Verzögerung aus.",
            "Plane drei Folge-E-Mails: Nutzen, Beispiel, nächster Schritt.",
            "Tagge Thema, Quelle und Reaktion für spätere Segmentierung.",
        ],
        "klicktipp": [
            "Automatisierter Versand nach Opt-in",
            "Kampagnen für mehrstufiges Nachfassen",
            "Tags für Leadmagnet-Thema und Quelle",
            "Newsletter oder Kampagne als nächste Kommunikationsform",
            "Analytics für E-Mail-Öffnungen und Klicks",
        ],
    },
    {
        "area": "leads",
        "slug": "optin-formular-starten",
        "title": "Opt-in-Formular starten: Besucher in Kontakte verwandeln",
        "meta": "Guide für den ersten Opt-in-Prozess mit KlickTipp: Formular, Einwilligung, Bestätigung, Tag und erste E-Mail-Strecke sinnvoll verbinden.",
        "hero": "Mach aus anonymen Besuchern einen eigenen Kontaktbestand.",
        "lead": "Wenn Deine Website keine Kontakte gewinnt, bleibt jeder Besucher ein Zufall. Ein gutes Opt-in-Formular macht Interesse messbar und anschlussfähig.",
        "intro": "KlickTipp stellt Formulare, Opt-in-Prozesse und nachgelagerte Kampagnen in einen gemeinsamen Ablauf. Entscheidend ist, dass Du nicht nur ein Formular einbaust, sondern den gesamten nächsten Schritt planst.",
        "problems": [
            ("Deine Website hat keinen Einstieg.", "Besucher finden Inhalte, aber keinen einfachen Grund, ihre E-Mail-Adresse zu hinterlassen."),
            ("Dein Formular ist isoliert.", "Nach dem Absenden fehlt die Bestätigung, die Einordnung und eine Folgekommunikation."),
            ("Du sammelst ohne Segmentierung.", "Alle Kontakte landen gleich in der Liste, obwohl Quelle und Interesse unterschiedlich sind."),
        ],
        "steps": [
            "Platziere das Formular an einer Stelle mit klarer Problemnähe.",
            "Erkläre in einem Satz, was der Kontakt erhält.",
            "Nutze einen passenden Bestätigungs- und Danke-Prozess.",
            "Vergib Tags für Quelle und Thema.",
            "Starte danach eine kurze Begrüßungsstrecke.",
        ],
        "klicktipp": [
            "Opt-in-Formulare für eigene Kontaktgewinnung",
            "Single- oder Double-Opt-in je nach Einsatzfall",
            "Weiterleitung nach Formularabsendung",
            "Tags für Formularquelle und Interesse",
            "Automatisierte Kampagnen nach Eintragung",
        ],
    },
    {
        "area": "leads",
        "slug": "newsletter-empfehlungen",
        "title": "Newsletter-Empfehlungen als Leadquelle nutzen",
        "meta": "Guide für Empfehlungsmarketing mit KlickTipp: Bestehende Leser nutzen, um neue passende Kontakte für Newsletter und Angebote zu gewinnen.",
        "hero": "Nutze Deine bestehende Liste als seriöse Leadquelle.",
        "lead": "Empfehlungen sind oft glaubwürdiger als kalte Reichweite. Der Unterschied liegt darin, ob Du sie systematisch auslöst und sauber nachfasst.",
        "intro": "KlickTipp nennt E-Mail-Empfehlungsmarketing als Leadgenerierungsbaustein. Für xioo zählt daraus eine einfache Idee: Zufriedene Leser sollen passende Menschen auf Deinen besten Einstieg hinweisen können.",
        "problems": [
            ("Gute Leser empfehlen Dich nicht aktiv.", "Gute Leser mögen Deine Inhalte, bekommen aber keinen einfachen Anlass zum Weiterleiten."),
            ("Empfehlungen sind nicht messbar.", "Du erkennst nicht, welche Inhalte neue Kontakte auslösen."),
            ("Neue Kontakte bekommen keinen passenden Einstieg.", "Empfohlene Leser brauchen eine andere Begrüßung als kalte Besucher."),
        ],
        "steps": [
            "Wähle einen Newsletter mit hohem Nutzwert als Empfehlungsanker.",
            "Baue eine klare Empfehlungseinladung in die E-Mail ein.",
            "Verlinke auf eine passende Lead-Landingpage.",
            "Tagge neue Kontakte nach Empfehlungsquelle.",
            "Begrüße empfohlene Kontakte mit Kontext und nächstem Schritt.",
        ],
        "klicktipp": [
            "E-Mail-Empfehlungsmarketing als Leadquelle",
            "Segmentierung nach Herkunft",
            "Landingpages für empfohlene Kontakte",
            "Kampagnen für Begrüßung und Vertiefung",
            "Analytics zur Bewertung von Empfehlungsimpulsen",
        ],
    },
    {
        "area": "leads",
        "slug": "sms-und-email-leads",
        "title": "SMS und E-Mail-Leads sinnvoll kombinieren",
        "meta": "Guide für E-Mail plus SMS mit KlickTipp: Wann zusätzliche Sichtbarkeit sinnvoll ist und wie Leads ohne Druck weitergeführt werden.",
        "hero": "Mehr Sichtbarkeit für wichtige Kontakte, ohne aufdringlich zu werden.",
        "lead": "Nicht jeder Kontakt reagiert auf E-Mail allein. SMS kann ein zusätzlicher Kanal sein, wenn Anlass, Einwilligung und Nutzen klar sind.",
        "intro": "KlickTipp bewirbt SMS als Ergänzung zum E-Mail-Marketing. Für einen seriösen Prozess bedeutet das: SMS nur dort einsetzen, wo der Kontakt einen klaren Vorteil davon hat.",
        "problems": [
            ("Wichtige Hinweise gehen unter.", "Ein Webinarstart, Termin oder Ablauf kann in der Inbox übersehen werden."),
            ("Du nutzt SMS ohne Kontext.", "Dann wirkt der Kanal schnell hart, teuer oder störend."),
            ("Telefonnummern werden nicht sinnvoll eingeordnet.", "Ohne Tags und Anlass ist SMS kein Prozess, sondern nur ein weiterer Versandkanal."),
        ],
        "steps": [
            "Bestimme, welcher Anlass wirklich eine SMS rechtfertigt.",
            "Hole die passende Einwilligung und Erwartung ein.",
            "Kombiniere E-Mail für Inhalt und SMS für kurze Erinnerung.",
            "Tagge Kontakte nach Kanalpräferenz und Anlass.",
            "Prüfe Abmeldungen, Antworten und Reaktionen getrennt.",
        ],
        "klicktipp": [
            "SMS-Marketing als Ergänzung zum E-Mail-Prozess",
            "Kampagnen mit mehreren Kontaktpunkten",
            "Tags für Kanalpräferenz und Reaktion",
            "Antwortübersicht und Feedbacksignale",
            "Segmentierung für relevante Nachrichten",
        ],
    },
    {
        "area": "email",
        "slug": "newsletter-schneller-erstellen",
        "title": "Newsletter schneller erstellen mit KlickTipp",
        "meta": "Guide für kleine Anbieter: Newsletter schneller planen, schreiben und versenden, ohne jedes Mal bei Null zu starten.",
        "hero": "Versende bessere Newsletter, ohne jedes Mal neu anzufangen.",
        "lead": "Ein Newsletter scheitert selten an der Idee allein. Er scheitert an zu vielen kleinen Schritten: Thema, Aufbau, Text, Bild, Link und Versand.",
        "intro": "KlickTipp stellt E-Mail-Builder, Designvorlagen und KI-Funktionen in den Mittelpunkt. Daraus wird ein schnellerer Prozess, wenn Du wiederkehrende Newsletter-Bausteine definierst.",
        "problems": [
            ("Jeder Newsletter dauert zu lange.", "Du verlierst Energie in Layout, Formulierung und Struktur."),
            ("Dein Versandrhythmus bricht ab.", "Ohne Vorlage wird jede Ausgabe zur Einzelproduktion."),
            ("Der Newsletter hat keinen nächsten Schritt.", "Leser bekommen Inhalt, aber keine klare Handlung."),
        ],
        "steps": [
            "Lege ein wiederholbares Newsletter-Format fest.",
            "Nutze eine Vorlage als Layout-Basis statt leeres Dokument.",
            "Plane Betreff, Einstieg, Hauptnutzen und CTA getrennt.",
            "Verlinke auf eine passende Landingpage oder Antwortmöglichkeit.",
            "Bewerte Öffnungen und Klicks, bevor Du das Format änderst.",
        ],
        "klicktipp": [
            "Drag-and-drop-E-Mail-Builder",
            "Newsletter-Designvorlagen",
            "KI-Unterstützung für Inhalte und Betreff",
            "Dynamische Inhalte für relevantere Nachrichten",
            "E-Mail-Analytics für die Auswertung",
        ],
    },
    {
        "area": "email",
        "slug": "betreffzeilen-und-ki-copywriter",
        "title": "Betreffzeilen und KI-Copywriter für E-Mail-Marketing nutzen",
        "meta": "Guide für bessere E-Mail-Texte: Wie Du KI-Unterstützung in KlickTipp sinnvoll einsetzt, ohne Deine Zielgruppe aus dem Blick zu verlieren.",
        "hero": "Beende Schreibblockaden, aber behalte Deine Stimme.",
        "lead": "KI kann Dir Entwürfe liefern. Verkaufen wird Dein Newsletter aber erst, wenn Problem, Ton, Beweis und nächster Schritt zusammenpassen.",
        "intro": "KlickTipp bewirbt KI-generierte Inhalte und Betreffzeilen. Der praktische Nutzen entsteht, wenn Du der KI klare Aufgaben gibst und die Ausgabe kritisch prüfst.",
        "problems": [
            ("Du schiebst den Versand wegen Texten auf.", "Betreff und Einstieg fühlen sich nie fertig genug an."),
            ("KI-Texte klingen austauschbar.", "Ohne klare Vorgabe entstehen generische Mails statt relevanter Kommunikation."),
            ("Der Text verkauft zu hart.", "Zu viel Druck beschädigt Vertrauen, besonders bei warmen Kontakten."),
        ],
        "steps": [
            "Definiere das konkrete Leserproblem vor dem Text.",
            "Erstelle mehrere Betreffvarianten und wähle die klarste.",
            "Prüfe jeden KI-Entwurf auf Wahrhaftigkeit und Ton.",
            "Baue einen nächsten Schritt ein, der zum Interesse passt.",
            "Lerne aus Klicks und Antworten, nicht nur aus Öffnungen.",
        ],
        "klicktipp": [
            "KI-Copywriter für E-Mail-Entwürfe",
            "Betreffzeilen-Ideen für bessere Einstiege",
            "Vorlagen für wiederkehrende Versandformate",
            "Personalisierung mit Kontaktinformationen",
            "Analytics für Themen- und CTA-Bewertung",
        ],
    },
    {
        "area": "email",
        "slug": "email-zustellbarkeit-verbessern",
        "title": "E-Mail-Zustellbarkeit verbessern: erst sichtbar werden",
        "meta": "Guide zur Zustellbarkeit im E-Mail-Marketing: Warum saubere Kontakte, relevante Inhalte und technische Basis vor schönen Layouts kommen.",
        "hero": "Die beste E-Mail hilft nicht, wenn sie nicht gesehen wird.",
        "lead": "Zustellbarkeit ist kein einzelner Schalter. Der Effekt entsteht aus Technik, Listenqualität, Relevanz, Versandverhalten und sauberem Umgang mit Empfängern.",
        "intro": "KlickTipp hebt Zustellbarkeit und Versandperformance stark hervor. Für Deine Praxis heißt das: erst Grundlagen sauber halten, dann Kampagnen skalieren.",
        "problems": [
            ("Deine Liste wird passiver.", "Viele Empfänger öffnen nicht mehr oder reagieren kaum noch."),
            ("Du sendest an falsche Kontakte.", "Doppelte, alte oder uninteressierte Empfänger belasten die Wahrnehmung Deiner E-Mails."),
            ("Du optimierst nur am Design.", "Gute Gestaltung ersetzt keine relevante Nachricht und keine saubere Datenbasis."),
        ],
        "steps": [
            "Arbeite mit bestätigten und erwartungsklaren Eintragungen.",
            "Segmentiere aktive und passive Kontakte.",
            "Reaktiviere oder entferne Kontakte mit dauerhaft geringer Reaktion.",
            "Nutze klare Absender, Betreffzeilen und Inhalte.",
            "Prüfe technische und inhaltliche Signale regelmäßig zusammen.",
        ],
        "klicktipp": [
            "Zustellbarkeitsfokus im E-Mail-Marketing",
            "Tags für aktive und passive Empfänger",
            "SmartTags und Verhaltenssignale",
            "Empfängerzentrierte Datenpflege",
            "Analytics für Öffnungen, Klicks und Entwicklung",
        ],
    },
    {
        "area": "email",
        "slug": "newsletter-analytics-verstehen",
        "title": "Newsletter-Analytics verstehen und besser entscheiden",
        "meta": "Guide für E-Mail-Analytics mit KlickTipp: Öffnungen, Klicks, Themen und Zielgruppenverhalten strukturiert auswerten.",
        "hero": "Sende nicht blind weiter. Lerne aus jeder Kampagne.",
        "lead": "E-Mail-Marketing wird besser, wenn Du nicht nur sendest, sondern auswertest: Welche Themen ziehen? Welche Links werden geklickt? Wo bricht Interesse ab?",
        "intro": "KlickTipp beschreibt Analytics als Grundlage für datenbasierte Entscheidungen. Für Dich zählt ein kleines Messsystem, das Du nach jedem Versand wirklich nutzt.",
        "problems": [
            ("Du misst nur oberflächlich.", "Eine Öffnungsrate allein erklärt nicht, ob Dein Angebot verstanden wurde."),
            ("Du vergleichst falsche Mails.", "Jede E-Mail hat ein anderes Ziel und braucht eigene Bewertung."),
            ("Du ziehst keine Konsequenzen.", "Daten helfen nur, wenn sie Themen, Segmente oder nächste Schritte verändern."),
        ],
        "steps": [
            "Definiere vor dem Versand ein Ziel pro E-Mail.",
            "Unterscheide Öffnung, Klick, Antwort und Kaufnähe.",
            "Vergleiche ähnliche Newsletter-Formate miteinander.",
            "Tagge Kontakte nach relevanten Klicks.",
            "Plane die nächste E-Mail auf Basis der stärksten Signale.",
        ],
        "klicktipp": [
            "E-Mail- und Newsletter-Analytics",
            "Auswertung von Öffnungen und Klicks",
            "Tags nach Linkinteresse",
            "Berichte für Kampagnenentwicklung",
            "Segmentierung für Folgekommunikation",
        ],
    },
    {
        "area": "email",
        "slug": "dynamische-inhalte-personalisierung",
        "title": "Dynamische Inhalte und Personalisierung richtig nutzen",
        "meta": "Guide für relevantere E-Mails mit KlickTipp: Tags, Segmente, dynamische Inhalte und Personalisierung sinnvoll einsetzen.",
        "hero": "Schicke nicht allen dieselbe E-Mail, wenn Interesse unterschiedlich ist.",
        "lead": "Personalisierung ist mehr als ein Vorname. Relevanz entsteht, wenn Inhalt, Timing und Angebot zum Verhalten des Kontakts passen.",
        "intro": "KlickTipp verbindet E-Mail-Marketing mit Tags, dynamischen Inhalten und CRM-Daten. Das kann besonders dann stark sein, wenn Du wenige, aber klare Segmente definierst.",
        "problems": [
            ("Alle Kontakte bekommen dieselbe Nachricht.", "Neue Leads, Käufer und Webinarteilnehmer haben aber unterschiedliche Fragen."),
            ("Personalisierung wirkt künstlich.", "Ein Vorname ohne relevanten Inhalt verbessert keine Beziehung."),
            ("Segmente werden zu kompliziert.", "Zu viele Regeln machen den Prozess schwer wartbar."),
        ],
        "steps": [
            "Starte mit drei Segmenten statt mit zwanzig Sonderfällen.",
            "Nutze Verhalten als Signal: Klick, Download, Webinar, Kauf.",
            "Passe nur die wichtigsten Inhaltsblöcke dynamisch an.",
            "Prüfe, ob der Kontakt die Personalisierung als hilfreich erlebt.",
            "Dokumentiere Tag-Regeln, damit die Logik wartbar bleibt.",
        ],
        "klicktipp": [
            "Tags und SmartTags für Verhalten",
            "Dynamische Inhalte im E-Mail-Marketing",
            "CRM-Daten für relevante Ansprache",
            "Kampagnen nach Interesse und Status",
            "Analytics zur Bewertung personalisierter Inhalte",
        ],
    },
    {
        "area": "crm",
        "slug": "tags-statt-listenchaos",
        "title": "Tags statt Listenchaos im Marketing CRM",
        "meta": "Guide für mehr Ordnung im E-Mail-Marketing: Warum Tags in KlickTipp mehrere Listen ersetzen und Segmentierung einfacher machen können.",
        "hero": "Beende Listenchaos, bevor es Dein Marketing blockiert.",
        "lead": "Wenn derselbe Kontakt in mehreren Listen liegt, wird E-Mail-Marketing schnell unübersichtlich. Tags helfen, einen Kontakt zentral zu führen und trotzdem differenziert anzusprechen.",
        "intro": "KlickTipp beschreibt sein Marketing CRM als tagbasierte Alternative zu parallelen Listen. Für kleine Anbieter ist das ein praktischer Weg, um Ordnung und Relevanz zusammenzubringen.",
        "problems": [
            ("Kontakte liegen doppelt.", "Ein Interessent kann gleichzeitig Webinarteilnehmer, Käufer und Newsletterleser sein."),
            ("Listen erklären kein Verhalten.", "Eine Liste sagt selten, was jemand geklickt, heruntergeladen oder gekauft hat."),
            ("Änderungen werden riskant.", "Wenn Logik über Listen verteilt ist, werden Kampagnen schwer nachvollziehbar."),
        ],
        "steps": [
            "Führe Kontakte zentral statt in parallelen Listen.",
            "Definiere Tags für Quelle, Interesse, Status und Verhalten.",
            "Nutze wenige klare Tag-Gruppen am Anfang.",
            "Dokumentiere, wann ein Tag gesetzt oder entfernt wird.",
            "Baue Kampagnen auf Tags, nicht auf Bauchgefühl.",
        ],
        "klicktipp": [
            "Tagging als CRM-Logik",
            "Beliebig viele Tags pro Kontakt",
            "Segmentierung nach Quelle und Verhalten",
            "Automatisierte Tagging-Bedingungen",
            "Zentrale Datenbasis für Marketing und Follow-up",
        ],
    },
    {
        "area": "crm",
        "slug": "kontakte-zentral-organisieren",
        "title": "Kontakte zentral organisieren mit KlickTipp",
        "meta": "Guide für zentrale Kontaktführung im Marketing: Kontaktdaten, Felder, Tags und Historie mit KlickTipp strukturieren.",
        "hero": "Bring Deine Marketing-Kontakte an einen Ort.",
        "lead": "Kontakte aus Formularen, Webinaren, Gesprächen und Downloads sind nur wertvoll, wenn Du sie wiederfindest, verstehst und sinnvoll weiterführst.",
        "intro": "KlickTipp positioniert das Marketing CRM als zentrale Kontaktbasis. Der Nutzen entsteht, wenn Du nicht alles sammelst, sondern die richtigen Informationen bewusst strukturierst.",
        "problems": [
            ("Daten liegen verstreut.", "Website, E-Mail, Webinar und manuelle Notizen erzählen jeweils nur einen Teil der Geschichte."),
            ("Wichtige Informationen fehlen.", "Ohne Felder und Tags weißt Du später nicht mehr, was den Kontakt interessiert hat."),
            ("Kontakte werden gleich behandelt.", "Bestehende Kunden, neue Leads und passive Leser brauchen unterschiedliche Kommunikation."),
        ],
        "steps": [
            "Lege fest, welche Kontaktinformationen wirklich entscheidungsrelevant sind.",
            "Nutze Stammsatzfelder für stabile Daten.",
            "Nutze Tags für Verhalten, Quelle und Status.",
            "Erstelle einfache Segmente für die nächsten Kampagnen.",
            "Prüfe regelmäßig, ob Daten noch aktuell und nutzbar sind.",
        ],
        "klicktipp": [
            "Zentrale Empfängerdatenbank",
            "Zusätzliche Stammsatzfelder",
            "Tags und SmartTags",
            "Empfänger-SmartImport",
            "Kontakthistorie für nachvollziehbare Änderungen",
        ],
    },
    {
        "area": "crm",
        "slug": "segmentierung-nach-interesse",
        "title": "Segmentierung nach Interesse statt Massenversand",
        "meta": "Guide für bessere Segmentierung mit KlickTipp: Kontakte nach Interesse, Klicks, Downloads und Status sinnvoll gruppieren.",
        "hero": "Sende relevanter, indem Du Interesse sichtbar machst.",
        "lead": "Nicht jeder Kontakt ist gleich weit. Segmentierung hilft Dir, neue Leads, warme Interessenten und bestehende Kunden unterschiedlich anzusprechen.",
        "intro": "KlickTipp bietet Tags, SmartTags und Empfängergruppen für präzisere Kommunikation. Für den Start reichen wenige starke Signale, die wirklich etwas über Interesse aussagen.",
        "problems": [
            ("Du sendest an alle gleich.", "Das spart kurzfristig Zeit, kostet aber Relevanz."),
            ("Interesse wird nicht gespeichert.", "Ein Klick oder Download ist ein Signal, das später wieder nutzbar sein sollte."),
            ("Segmente werden unübersichtlich.", "Ohne klare Regeln entstehen Tags, die niemand mehr versteht."),
        ],
        "steps": [
            "Wähle drei bis fünf relevante Interessenssignale.",
            "Tagge Downloads, Klicks, Webinarteilnahme und Käufe.",
            "Bilde Empfängergruppen für konkrete Folgeaktionen.",
            "Sende nur Nachrichten, die zum Segment passen.",
            "Entferne oder aktualisiere Tags, wenn sich der Status ändert.",
        ],
        "klicktipp": [
            "Tags für Interessenssignale",
            "SmartTags für Verhalten",
            "Empfängergruppen auf Basis von Bedingungen",
            "Tagging-Pixel für Website-Verhalten",
            "Automatisierte Kampagnen nach Segment",
        ],
    },
    {
        "area": "crm",
        "slug": "doppelte-kontakte-vermeiden",
        "title": "Doppelte Kontakte vermeiden und Daten sauber halten",
        "meta": "Guide für sauberere Kontaktdaten mit KlickTipp: doppelte Kontakte, mehrere E-Mail-Adressen und passive Empfänger besser kontrollieren.",
        "hero": "Saubere Daten machen Dein E-Mail-Marketing leichter.",
        "lead": "Doppelte Kontakte, alte Adressen und passive Empfänger erzeugen Kosten, Unschärfe und schlechte Entscheidungen. Datenpflege ist deshalb ein Wachstumshebel.",
        "intro": "KlickTipp beschreibt SmartContact, empfängerzentrierte Abrechnung und Importfunktionen als Wege gegen Datenchaos. Entscheidend ist, dass Du Datenqualität als laufenden Prozess behandelst.",
        "problems": [
            ("Kontakte haben mehrere Adressen.", "Eine Person kann über verschiedene Formulare mit unterschiedlichen E-Mail-Adressen auftauchen."),
            ("Importe erzeugen Unordnung.", "Falsch zugeordnete Felder und fehlerhafte Adressen verschlechtern spätere Kampagnen."),
            ("Passive Kontakte bleiben ewig aktiv.", "Das verfälscht Deine Auswertung und kann Relevanzsignale schwächen."),
        ],
        "steps": [
            "Prüfe, welche Quellen neue Kontakte erzeugen.",
            "Importiere Daten mit klaren Feldzuordnungen.",
            "Nutze Tags für Herkunft und Aktualität.",
            "Unterscheide aktive, passive und reaktivierte Kontakte.",
            "Plane regelmäßige Datenpflege statt einmaliger Aufräumaktion.",
        ],
        "klicktipp": [
            "SmartContact für weniger Redundanzen",
            "Empfänger-SmartImport",
            "Empfängerzentrierte Kontaktlogik",
            "Tags für Datenqualität und Aktivität",
            "Automationen für passive Empfänger",
        ],
    },
    {
        "area": "crm",
        "slug": "kontakthistorie-und-leadvalue",
        "title": "Kontakthistorie und LeadValue für bessere Priorisierung",
        "meta": "Guide für Marketing CRM mit KlickTipp: Kontakthistorie, LeadValue und Tags nutzen, um wertvolle Leads besser zu erkennen.",
        "hero": "Erkenne, welche Kontakte wirklich warm sind.",
        "lead": "Nicht jeder Lead ist gleich wertvoll. Manche lesen, klicken, kaufen oder fragen häufiger. Diese Signale sollten Deine nächsten Aktionen beeinflussen.",
        "intro": "KlickTipp nennt Kontakthistorie und LeadValue als CRM-Funktionen. Für Dich geht es darum, nicht nur Kontakte zu sammeln, sondern Kaufnähe und Relevanz besser einzuschätzen.",
        "problems": [
            ("Du priorisierst nach Gefühl.", "Ohne Historie bleibt unklar, welche Kontakte schon viel Interesse gezeigt haben."),
            ("Wertvolle Leads gehen unter.", "Starke Signale verschwinden zwischen vielen gewöhnlichen Newsletterlesern."),
            ("Follow-up ist nicht passend.", "Ein heißer Lead braucht andere Kommunikation als ein kalter Kontakt."),
        ],
        "steps": [
            "Definiere, welche Signale einen Lead wertvoll machen.",
            "Nutze Tags für Klicks, Downloads, Käufe und Antworten.",
            "Prüfe die Kontakthistorie vor manueller Ansprache.",
            "Baue Segmente für hohe und niedrige Kaufnähe.",
            "Passe E-Mail-Strecken an den Leadstatus an.",
        ],
        "klicktipp": [
            "Kontakthistorie für nachvollziehbare Änderungen",
            "LeadValue zur Wert-Einschätzung",
            "Tags und SmartTags für Verhalten",
            "Segmentierung nach Kaufnähe",
            "Kampagnen für passende nächste Schritte",
        ],
    },
]


def href_to_root(page_path: Path) -> str:
    return "../../"


def page_url(page: dict) -> str:
    area = AREAS[page["area"]]
    return f"{SITE}/{area['dir']}/{page['slug']}/"


def related_pages(page: dict) -> list[dict]:
    return [candidate for candidate in PAGES if candidate["area"] == page["area"] and candidate["slug"] != page["slug"]]


def html_list(items: list[str], ordered: bool = False, class_name: str = "") -> str:
    tag = "ol" if ordered else "ul"
    cls = f' class="{class_name}"' if class_name else ""
    body = "\n".join(f"            <li>{item}</li>" for item in items)
    return f"          <{tag}{cls}>\n{body}\n          </{tag}>"


def json_ld(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=6)


def page_schema(page: dict) -> str:
    area = AREAS[page["area"]]
    url = page_url(page)
    related = [
        f"{SITE}/{area['dir']}/{item['slug']}/"
        for item in related_pages(page)[:3]
    ]
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "@id": f"{url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Start",
                        "item": f"{SITE}/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": area["label"],
                        "item": f"{SITE}/{area['dir']}/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": page["title"],
                        "item": url,
                    },
                ],
            },
            {
                "@type": "Article",
                "@id": f"{url}#article",
                "headline": page["title"],
                "description": page["meta"],
                "inLanguage": "de-DE",
                "url": url,
                "image": SOCIAL_IMAGE,
                "datePublished": "2026-06-03",
                "dateModified": LASTMOD,
                "author": {
                    "@type": "Organization",
                    "name": "xioo",
                    "url": SITE,
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "xioo",
                    "url": SITE,
                },
                "isPartOf": {
                    "@type": "WebSite",
                    "name": "xioo KlickTipp Guides",
                    "url": SITE,
                },
                "about": [area["label"], "KlickTipp", "E-Mail-Marketing"],
                "mentions": related,
            },
            {
                "@type": "FAQPage",
                "@id": f"{url}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "Muss ich dafür schon ein großes System haben?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Nein. Der bessere Start ist ein kleiner, klarer Ablauf. Erst wenn dieser funktioniert, lohnt sich die nächste Automatisierungsstufe.",
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Kann KlickTipp das Problem komplett allein lösen?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "KlickTipp kann wichtige Bausteine bereitstellen. Angebot, Zielgruppe, Texte, Einwilligung, Strategie und Bewertung musst Du trotzdem bewusst festlegen.",
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Warum ist diese Seite ein Guide und nicht nur Werbung?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Weil Du vor dem Klick auf ein Tool verstehen solltest, welcher Prozess dahintersteht. Genau dieser Prozess macht den Einsatz von KlickTipp erst sinnvoll bewertbar.",
                        },
                    },
                ],
            },
        ],
    }
    return json_ld(data)


def render_page(page: dict) -> str:
    area = AREAS[page["area"]]
    root = href_to_root(Path(area["dir"]) / page["slug"] / "index.html")
    related = related_pages(page)
    related_cards = "\n".join(
        f'''        <article class="feature">
          <p class="eyebrow">{area["label"]}</p>
          <h2>{item["title"].split(":")[0]}</h2>
          <p>{item["lead"]}</p>
          <a class="text-link" href="../{item["slug"]}/">Guide lesen</a>
        </article>'''
        for item in related[:3]
    )
    problem_cards = "\n".join(
        f'''        <article class="feature">
          <p class="eyebrow">Problem 0{index}</p>
          <h2>{title}</h2>
          <p>{text}</p>
        </article>'''
        for index, (title, text) in enumerate(page["problems"], 1)
    )
    implementation = [
        ("Anlass", "Welcher konkrete Kontaktmoment soll besser funktionieren?"),
        ("Signal", "Welches Verhalten zeigt Interesse: Formular, Download, Klick, Webinar oder Kauf?"),
        ("Tag", "Wie wird dieses Signal in KlickTipp sichtbar und später nutzbar?"),
        ("Folge", "Welche E-Mail, SMS oder Kampagne ist danach der sinnvollste nächste Schritt?"),
    ]
    implementation_cards = "\n".join(
        f'''        <article class="process-step">
          <span>0{index}</span>
          <h2>{title}</h2>
          <p>{text}</p>
        </article>'''
        for index, (title, text) in enumerate(implementation, 1)
    )
    fit_checks = [
        "Passt, wenn genau dieses Problem regelmäßig auftritt und nicht nur einmalig gelöst werden muss.",
        "Passt nicht, wenn Du noch kein klares Angebot, keine erlaubte Kontaktaufnahme oder keinen sinnvollen nächsten Schritt hast.",
        "Messpunkt: Prüfe nach 14 Tagen, ob Kontakte den nächsten Schritt wirklich auslösen, anklicken oder beantworten.",
    ]
    return f'''<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{page["title"]} | xioo®</title>
    <meta name="description" content="{page["meta"]}">
    <meta name="robots" content="index,follow">
    <link rel="canonical" href="{page_url(page)}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{page["title"]}">
    <meta property="og:description" content="{page["meta"]}">
    <meta property="og:url" content="{page_url(page)}">
    <meta property="og:image" content="{SOCIAL_IMAGE}">
    <meta property="og:image:secure_url" content="{SOCIAL_IMAGE}">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="{page["title"]}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@XiooBerlin">
    <meta name="twitter:title" content="{page["title"]}">
    <meta name="twitter:description" content="{page["meta"]}">
    <meta name="twitter:image" content="{SOCIAL_IMAGE}">
    <meta name="twitter:image:alt" content="{page["title"]}">
    <meta name="xioo-goatcounter-endpoint" content="https://xioo.goatcounter.com/count">
    <script type="application/ld+json">
{page_schema(page)}
    </script>
    <link rel="stylesheet" href="{root}assets/css/styles.css">
    <script defer src="{root}assets/js/analytics.js"></script>
  </head>
  <body class="page-guide page-topic page-{page["area"]}">
    <header class="site-header">
    </header>

    <main>
      <section class="hero {area["hero"]}" aria-label="{page["title"]}">
        <div class="hero-copy">
          <p class="eyebrow">{area["label"]}</p>
          <h1>{page["hero"]}</h1>
          <p class="lead">{page["lead"]}</p>
          <div class="button-row">
            <a class="button" href="{area["partner"]}" rel="sponsored noopener">{area["cta"]}</a>
            <a class="button button-ghost" href="#guide">Guide lesen</a>
          </div>
        </div>
      </section>

      <section class="section section-grid-intro" id="guide">
        <div class="section-kicker">Einordnung</div>
        <div>
          <h2>{page["title"]}</h2>
        </div>
        <div>
          <p>{page["intro"]}</p>
          <p class="source-note">Informationsbasis: KlickTipp Marketing Suite Bereich {area["label"]}. xioo® ist nicht Betreiber, Support oder offizieller Vertreter von KlickTipp.</p>
        </div>
      </section>

      <section class="section feature-grid" aria-label="Kundenprobleme">
{problem_cards}
      </section>

      <section class="section band-section">
        <div>
          <p class="eyebrow">Umsetzungslogik</p>
          <h2>So machst Du daraus einen nutzbaren KlickTipp-Prozess.</h2>
{html_list(page["steps"], ordered=True, class_name="number-list")}
        </div>
      </section>

      <section class="section split-section">
        <div>
          <p class="eyebrow">KlickTipp-Rolle</p>
          <h2>Welche KlickTipp-Bausteine für diesen Fall relevant sind</h2>
{html_list(page["klicktipp"])}
          <a class="button" href="{area["partner"]}" rel="sponsored noopener">{area["cta"]}</a>
        </div>
        <figure class="media-block">
          <img src="{area["image"]}" alt="{area["image_alt"]}">
          <figcaption>Der konkrete Nutzen entsteht nicht durch ein Tool allein, sondern durch einen klaren Ablauf aus Kontakt, Signal und nächstem Schritt.</figcaption>
        </figure>
      </section>

      <section class="section process-grid" aria-label="Mini-Prozess">
{implementation_cards}
      </section>

      <section class="section split-section">
        <div>
          <p class="eyebrow">Grenzen</p>
          <h2>Keine Garantie, aber ein besserer Startpunkt.</h2>
          <p>Dieser Guide verspricht keine automatischen Umsätze, keine garantierte Zustellbarkeit und keine Rechtsberatung. Er hilft Dir, ein konkretes Marketingproblem so zu strukturieren, dass KlickTipp als Werkzeug sinnvoll geprüft werden kann.</p>
        </div>
        <div class="rule-list" aria-label="Prüffragen">
          <h2>Vor dem Start klären</h2>
          <ul>
            <li>Welches Problem soll zuerst gelöst werden?</li>
            <li>Welche Kontakte betrifft dieser Ablauf?</li>
            <li>Welches Signal soll in KlickTipp gespeichert werden?</li>
            <li>Welche nächste Nachricht wäre für den Kontakt wirklich hilfreich?</li>
          </ul>
        </div>
      </section>

      <section class="section band-section">
        <div>
          <p class="eyebrow">xioo-Prüfraster</p>
          <h2>So entscheidest Du, ob dieser KlickTipp-Baustein Priorität hat.</h2>
{html_list(fit_checks)}
        </div>
      </section>

      <section class="section feature-grid" aria-label="Weitere Guides">
{related_cards}
      </section>

      <section class="section band-section">
        <div>
          <p class="eyebrow">Entscheidung</p>
          <h2>Prüfe KlickTipp für diesen Ablauf, wenn Du ihn wiederholbar machen willst.</h2>
          <p>Der nächste sinnvolle Schritt ist nicht, alles auf einmal zu automatisieren. Starte mit genau diesem Problem, einem klaren Kontaktmoment und einer kleinen, messbaren Strecke.</p>
          <a class="button" href="{area["partner"]}" rel="sponsored noopener">{area["cta"]}</a>
        </div>
      </section>

      <section class="section faq-section" aria-label="Häufige Fragen">
        <p class="eyebrow">FAQ</p>
        <h2>Häufige Fragen</h2>
        <details>
          <summary>Muss ich dafür schon ein großes System haben?</summary>
          <p>Nein. Der bessere Start ist ein kleiner, klarer Ablauf. Erst wenn dieser funktioniert, lohnt sich die nächste Automatisierungsstufe.</p>
        </details>
        <details>
          <summary>Kann KlickTipp das Problem komplett allein lösen?</summary>
          <p>KlickTipp kann wichtige Bausteine bereitstellen. Angebot, Zielgruppe, Texte, Einwilligung, Strategie und Bewertung musst Du trotzdem bewusst festlegen.</p>
        </details>
        <details>
          <summary>Warum ist diese Seite ein Guide und nicht nur Werbung?</summary>
          <p>Weil Du vor dem Klick auf ein Tool verstehen solltest, welcher Prozess dahintersteht. Genau dieser Prozess macht den Einsatz von KlickTipp erst sinnvoll bewertbar.</p>
        </details>
      </section>
    </main>

    <footer class="site-footer">
    </footer>
  </body>
</html>
'''


def write_pages() -> None:
    for page in PAGES:
        area = AREAS[page["area"]]
        output_dir = ROOT / area["dir"] / page["slug"]
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(render_page(page), encoding="utf-8")


def write_sitemap() -> None:
    existing = [
        ("/", "1.0", "https://klicktipp.xioo.de/assets/img/social/klicktipp-guides-social.png?v=20260602-2", "KlickTipp Guides für Follow-up, Leads und E-Mail-Marketing"),
        ("/ueber-xioo/", "0.6", "https://klicktipp.xioo.de/assets/img/social/klicktipp-guides-social.png?v=20260602-2", "Über xioo KlickTipp Guides"),
        ("/grundlagenkurs/", "0.9", "https://klicktipp.xioo.de/assets/img/social/grundlagenkurs-social.png?v=20260603-1", "KlickTipp Grundlagenkurs als Start-Guide"),
        ("/follow-up-prozess/", "0.9", "https://klicktipp.xioo.de/assets/img/social/follow-up-system-social.png?v=20260602-2", "Follow-up-System mit KlickTipp aufbauen"),
        ("/follow-up-checkliste/", "0.8", "https://klicktipp.xioo.de/assets/img/social/follow-up-checkliste-social.png?v=20260602-2", "Follow-up-Checkliste für den KlickTipp-Start"),
        ("/lead-magnet-nachfassen/", "0.8", "https://klicktipp.xioo.de/assets/img/social/lead-magnet-social.png?v=20260602-2", "Lead-Magnet mit KlickTipp nachfassen"),
        ("/webinar-follow-up/", "0.8", "https://klicktipp.xioo.de/assets/img/social/webinar-follow-up-social.png?v=20260602-2", "Webinar-Follow-up mit KlickTipp strukturieren"),
    ]
    entries = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    ]
    for path, priority, image, title in existing:
        entries.extend([
            "  <url>",
            f"    <loc>{SITE}{path}</loc>",
            f"    <lastmod>{LASTMOD}</lastmod>",
            "    <changefreq>weekly</changefreq>",
            f"    <priority>{priority}</priority>",
            "    <image:image>",
            f"      <image:loc>{image}</image:loc>",
            f"      <image:title>{title}</image:title>",
            "    </image:image>",
            "  </url>",
        ])
    for page in PAGES:
        entries.extend([
            "  <url>",
            f"    <loc>{page_url(page)}</loc>",
            f"    <lastmod>{LASTMOD}</lastmod>",
            "    <changefreq>weekly</changefreq>",
            "    <priority>0.7</priority>",
            "    <image:image>",
            f"      <image:loc>{SOCIAL_IMAGE}</image:loc>",
            f"      <image:title>{page['title']}</image:title>",
            "    </image:image>",
            "  </url>",
        ])
    for path in ["/rechtliches/impressum.html", "/rechtliches/datenschutz.html"]:
        entries.extend([
            "  <url>",
            f"    <loc>{SITE}{path}</loc>",
            f"    <lastmod>{LASTMOD}</lastmod>",
            "    <changefreq>yearly</changefreq>",
            "    <priority>0.2</priority>",
            "  </url>",
        ])
    entries.append("</urlset>")
    sitemap = "\n".join(entries) + "\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    legacy_dir = ROOT / "xioo-affiliate-sites"
    legacy_dir.mkdir(exist_ok=True)
    (legacy_dir / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def main() -> None:
    write_pages()
    write_sitemap()


if __name__ == "__main__":
    main()
