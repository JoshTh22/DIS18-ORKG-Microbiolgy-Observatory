# DIS18-ORKG-Microbiolgy-Observatory
### Arbeitspakete
- [ ] Heraussuchen von Bakterien (Datenbank oder Webiste) -> 3 Tage
- [ ] Crawler erstellen -> 4 Tage
- [ ] Debugging -> 3 Tage
- [ ] Optimales Speicherformat für Ergebnisse des API runs finden finden -> 0,5 Tage
- [ ] Auf Pubmed via API zugreifen -> 7 Tage
- [ ] Recherche zur Einbettung in ORKG -> 3 Tage
- [ ] Software zur Indexierung der Daten schreiben -> 7 Tage
- [ ] Debugging -> 7 Tage
- [ ] Indexierung aller Ergebnisse -> 1 Tag


### Ressourcen/Tools/etc.

-	VS Code für Python Entwicklung
-	Github für git repo
-	Google Colab (Falls Rechenleistung von eigenen Computern nicht ausreicht)
-	PowerBI/Tableau zur Visualisierung der Ergebnisse

### Team-Organisation
- Kommunikation über Discord/Whatsapp


Zielsetzung für das Projekt “ORKG - Mikrobiologisches Observatorium”

Unser Ziel ist es Mikrobiologische Daten aus Übersichtsartikeln zu extrahieren und darzustellen. Mithilfe eines Crawlers möchten wir Daten über verschiedene Bakterien (Art, Stamm, Familie, Gattung, Ordnung) von einer Datenbank oder einer Webseite analysieren. Mit PubMed möchten wir via API auf, zu jedem der gesammelten Bakterien, Literatur herausziehen und in einem optimalen Speicherformat (z. B. CSV) speichern. PubMed ist eine englisch sprachige Meta-Datenbank mit medizinischen Artikeln, der auf den gesamten Bereich der Biomedizin bezogen ist. Nachdem die Daten analysiert und bereinigt wurde, integrieren wir mithilfe von der Python Bibliothek „Pandas“ den Wissens Graphen. Eine Software soll uns dabei helfen, die Daten zu indexieren, so dass dem Endbenutzer eine effektive Abfrage des Graphen ermöglicht werden kann und zieht Schlüsse aus den vorhandenen Informationen. Der Wissensgraph speichert die Daten einer Domäne als Entität und Beziehungen unter Verwendung eines Graphen Modells, das sich an eine Ontologie hält. Die Knoten des Netzwerkes stellen die Entität dar und die Kanten oder Verbindungen zwischen den Knoten stellen die Beziehungen zwischen den Knoten dar. Zum Ende des nächsten Semsters sollen die von extrahierten Daten bei Open Research Knowledge Graph integriert werden, sodass Literatur und Autor dieser Literatur mit dem jeweiligen Bakterium in Verbindung gebracht werden kann. Mit diesem Projekt erlernen die Gruppenmitglieder nicht nur neue Kompetenzen, es führt außerdem zu einer hoffentlich erheblichen Erweiterung des ORKG, welcher vom Umfang her noch in den Startlöchern steht.
