# DIS18-ORKG-Microbiolgy-Observatory
### Arbeitspakete
- [x] Heraussuchen von Bakterien (Datenbank oder Webiste) -> 3 Tage
- [x] Crawler erstellen -> 4 Tage
- [x] Debugging -> 3 Tage
- [x] Optimales Speicherformat für Ergebnisse des API runs finden finden -> 0,5 Tage
- [x] Auf Pubmed via API zugreifen -> 7 Tage
- [ ] Recherche zur Einbettung in ORKG -> 3 Tage
- [ ] Software zur Indexierung der Daten schreiben -> 7 Tage
- [ ] Debugging -> 7 Tage
- [ ] Indexierung aller Ergebnisse -> 1 Tag


### Ressourcen/Tools/etc.

-	VS Code für Python Entwicklung
-	Github für git repo
-	Google Colab (Falls Rechenleistung von eigenen Computern nicht ausreicht)
-	PowerBI/Tableau zur Visualisierung der Ergebnisse
- https://meshb.nlm.nih.gov/record/ui?ui=D001419
- https://www.msdmanuals.com/de-de/heim/infektionen/bakterielle-infektionen-%C3%BCbersicht/%C3%BCbersicht-%C3%BCber-bakterien
- https://flexikon.doccheck.com/de/Klinisch_relevante_Bakterien
### Team-Organisation
- Kommunikation über Discord/Whatsapp


### Zielsetzung für das Projekt “ORKG - Mikrobiologisches Observatorium”

Unser Ziel ist es Mikrobiologische Daten aus Übersichtsartikeln zu extrahieren und darzustellen. Mithilfe eines Crawlers möchten wir Daten über verschiedene Bakterien (Art, Stamm, Familie, Gattung, Ordnung) von einer Datenbank oder einer Webseite analysieren. Mit PubMed möchten wir via API auf, zu jedem der gesammelten Bakterien, Literatur herausziehen und in einem optimalen Speicherformat (z. B. CSV) speichern. PubMed ist eine englisch sprachige Meta-Datenbank mit medizinischen Artikeln, der auf den gesamten Bereich der Biomedizin bezogen ist. Nachdem die Daten analysiert und bereinigt wurde, integrieren wir mithilfe von der Python Bibliothek „Pandas“ den Wissens Graphen. Zum Visualisieren der Zwischenergebnisse wird ein Dashboard erstellt, welches wir mit der Software Tableau Designen Eine Software soll, uns dabei helfen, die Daten zu indexieren, so dass dem Endbenutzer eine effektive Abfrage des Graphen ermöglicht werden kann und zieht Schlüsse aus den vorhandenen Informationen. Der Wissensgraph speichert die Daten einer Domäne als Entität und Beziehungen unter Verwendung eines Graphen Modells, das sich an eine Ontologie hält. Die Knoten des Netzwerkes stellen die Entität dar und die Kanten oder Verbindungen zwischen den Knoten stellen die Beziehungen zwischen den Knoten dar. Zum Ende des nächsten Semesters sollen die von extrahierten Daten bei Open Research Knowledge Graph (ORKG) integriert werden, sodass Literatur und Autor dieser Literatur mit dem jeweiligen Bakterium in Verbindung gebracht werden kann. Mit diesem Projekt erlernen die Gruppenmitglieder nicht nur neue Kompetenzen, es führt außerdem zu einer hoffentlich erheblichen Erweiterung des ORKG. Dieser steht mit 4891 indexierten Papern, was den Umfang angeht, noch in den Startlöchern. Bei erfolgreichem Abschließen des Projekts wäre es möglich, dass die entwickelte Software bei anderen, ähnlichen Projekten Verwendung findet. 

Besprechung, 15.04.2021 - Next Steps:
### Data Cleaning (Flo)
- needs_cleaning.csv: 
- Affiliates entfernen
- Authors: Klammern Vor- und Nachname
- Keywords: leere rausschmeißen und sonst Klammern entfernen, mesh terms abgleichen 
- Title abgleichen  

### Entrez testen (Kai) 
https://www.ncbi.nlm.nih.gov/books/NBK3837/

### Next Steps (Stand 29.04.2021)
- Via Entrez MeSH-Terms aus der NCBI Mesh-Datenbank ziehen
- MeSH-terms and den Dataframe dranhängen
- ORCID der Autoren ziehen

### Nützliche Links für das bearbeiten der csv

- Bedeutungen der Spaltennamen: https://www.nlm.nih.gov/bsd/mms/medlineelements.html
- Dokumentation für Entrez: https://biopython-tutorial.readthedocs.io/en/latest/notebooks/09%20-%20Accessing%20NCBIs%20Entrez%20databases.html

### Fragen für das Expertengespräch:

- Sind Listen in der CSV Datei in Ordnung? 
- Pflichtfelder? 
- Empfehlungen: andere Seiten, Dokumentationen etc.?
  - nope 
- Gibt es ein Sandbox System? 
  - Es gibt eins, nur nicht öffentlich (ausstehend) 
- Mesh Terms/Ontologien: Header, Unterkategoerien etc.?
  - Ontologien = Klassifikationen
- Wie können wir damit umgehen, falls schon z.B. Identifier im ORKG drin sind? (Doppelungen)
- Festgelegte Identifier im ORKG? R - Codes: Werden die von ORKG automatisch festgelegt? 
  - werden automatisch vergeben (Ressource), wird genutzt um Sachen wieder zu finden
- Research field? 
  - muss von uns erstellt werden
  - im ORKG anschauen (ausstehend) 

### Expertengespräch 20.05.2021
- Abstract: Welche Sachen können wir rausnehmen? (Text wird nicht mitreingenommen) 
- ORKG: 
  - Texte müssen vorab interpretiert werden 
  - Mesh Terms werden bisher noch nicht genutzt
  - "Es geht um das Thema ..." "bzgl. Paper" 
  - Abstract wird nicht retrieved
  - Überlegen: "Wie können wir von den Keywords zu den Ontologien gelangen?" 
  - scispacy (TOI überprüfen)
  - Jeder Begriff ein identifier? 
  - Klassen können manuel im ORKG angelegt werden 
  - "Welche Art von Informationen wollen wir in das ORKG bringen?" 
  - Terms von Krankheitsbildern matchen 
  - Daten müssen interpretierbar sein 
- Dokumentation von Beispielen, Use cases etc. 
- z.B. Frage: "Welches Medikament hat Wirkung auf bestimmte Proteine?"
  - Fragestellung finden
- ein hochgeladener Datensatz kann erweitert werden
- Beispiel Bakterien: Was lösen sie aus?, Verbindungen von Bakterien
  - Orte raussuchen in Verbindung zu Bakterien und das auf die Paper beziehen 
  - Antibotika resistenten 
  - https://coxbase.q-gaps.de/webapp/coxviewer (Isolat Beschreibungen) 
- verschiedene Use cases ausprobieren 



Agenda für die Doku:
  - Fragestellung
  - Zielbeschreibung
  - ORKG kurz erklären
  - Flussdiagramm
  - Erklärung der API funktion mit Screenshots
  - Erklärung zur Erstellung der Tabelle
  - Erklärung zur Erstellung der MeSH-Terme
  - Erklärung fertige Tabelle
  - Beschreibung des richtigen Datenformats
  - ORKG API Beschreiben
  - Zukünftige Baustellen auch für andere
  - Offene Quellen Lizenz
