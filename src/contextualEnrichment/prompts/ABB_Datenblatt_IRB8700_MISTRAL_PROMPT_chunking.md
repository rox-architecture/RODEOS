# Chunking Prompt

**Source File:** ABB_Datenblatt_IRB8700_MISTRAL  
**Prompt Type:** Chunking  
**Generated:** RODEOS  


---

You are an assistant specialized in splitting text into semantically consistent sections.

<instructions>
    <instruction>The text has been divided into chunks, each marked with <|start_chunk_X|> and <|end_chunk_X|> tags, where X is the chunk number</instruction>
    <instruction>Identify points where splits should occur, such that consecutive chunks of similar themes stay together</instruction>
    <instruction>Each chunk must be between 200 and 1000 words</instruction>
    <instruction>If chunks 1 and 2 belong together but chunk 3 starts a new topic, suggest a split after chunk 2</instruction>
    <instruction>The chunks must be listed in ascending order</instruction>
    <instruction>Provide your response in the form: 'split_after: 3, 5'</instruction>
</instructions>

This is the document text:
<document>
<|start_chunk_0|>
#### Page 1
ROBOTICS
<|end_chunk_0|><|start_chunk_1|>
 IRB 8700 
<|end_chunk_1|><|start_chunk_2|>
## Industrieroboter

![img-0.jpeg](img-0.jpeg)

Der IRB 8700 ist ein Schwerlastroboter mit bis zu 800 kg Handhabungskapazität und den niedrigsten Gesamtbetriebskosten seiner Klasse. Dank robuster Bauteile ist er besonders wartungsarm.
<|end_chunk_2|><|start_chunk_3|>
## Zwei Ausführungen

Der IRB 8700 ist in zwei Ausführungen lieferbar: eine Variante bietet 4,20 m Reichweite und 550 kg Traglast ( 620 kg bei geneigtem Handgelenk; 475 kg mit LeanID), die zweite Variante bietet 3,5 m Reichweite und 800 kg Traglast (bis zu 1000 kg bei geneigtem Handgelenk; 630 kg mit LeanID). Beide Ausführungen verfügen über ein Massenträgsheitsmoment von $725 \mathrm{~kg} /$ $\mathrm{m}^{2}$.
<|end_chunk_3|><|start_chunk_4|>
## Extrem zuverlässig

Mit einem einfachen und klaren Design, bestehend aus Hochleistungskomponenten, LeanID-Kabelführung für eine verlängerte Lebensdauer der Kabel und Schläuche sowie standardmäßiger Foundry-Plus-2-Schutzausführung, bietet der IRB 8700 eine sehr hohe Maschinenverfügbarkeit. Er ist der ideale Roboter für eine Produktion rund um die Uhr.
<|end_chunk_4|><|start_chunk_5|>
## Einfaches Design

Der IRB 8700 hat an jeder Achse nur einen Motor und ein Getriebe, während vergleichbare Roboter mit zwei Motoren und Getrieben pro Achse ausgestattet sind. Außerdem sind im IRB 8700 keine Gasdruckfedern verbaut, die undicht werden könnten. Der Roboter verfügt lediglich über ein Gegengewicht und zwei mechanische Federn zum Gewichtsausgleich.
<|end_chunk_5|><|start_chunk_6|>
## Verfügbar mit LeanID

LeanID ist eine ABB-Lösung zur Kabelführung, die kostengünstiger als ein komplett integriertes Schlauchpaket ist und dennoch ähnliche Vorteile bietet. Roboter mit LeanID lassen sich einfacher am PC simulieren und programmieren, bieten eine längere Lebensdauer der Kabel und Schläuche, ermöglichen
eine flexible Produktion mit Ausnutzung des kompletten Arbeitsbereichs des Roboters und lassen sich auch bei beengten Platzverhältnissen einfach integrieren.
<|end_chunk_6|><|start_chunk_7|>
## Schnell

Roboter mit hohen Traglasten gelten gemeinhin als langsam. Der IRB 8700 beweist jedoch das Gegenteil. Dank kompakten Abmaßen, optimalen Gegengewichten, Parallelarm, steifen Achsen und weniger Motoren, bleiben die Eigenschwingungen gering und die Geschwindigkeit hoch. So ist der IRB 8700 im Schnitt $25 \%$ schneller als vergleichbare Roboter. Zusätzlich ermöglicht die fortschrittliche Bewegungsregelung, dass die Geschwindigkeit des Roboters bei hohen Massenträgheitsmomenten ( $725 \mathrm{~kg} / \mathrm{m}^{2}$ ) angepasst bzw. verringert wird. Vor allem bei der Handhabung von langen und schweren Teilen ist das vorteilhaft.
<|end_chunk_7|><|start_chunk_8|>
## Nachhaltig

Der IRB 8700 erfüllt die Richtlinien 2002/95/EG (RoHS) sowie Nr. 1907/2006 (REACH), die beide die Verwendung bestimmter gefährlicher Stoffe beschränken und somit die Arbeitsplatzsicherheit erhöhen.
<|end_chunk_8|><|start_chunk_9|>
## Eigenschaften und Vorteile

- Traglasten bis zu 1000 kg bei geneigtem Handgelenk
- $25 \%$ schneller als vergleichbare Roboter der gleichen Klasse
- Zuverlässig dank einfacher Konstruktion und standardmäßiger Foundry-Plus-2-Schutzausführung
- Verfügbar mit LeanID für geringeren Kabelverschleiß und einfache Simulation
<|end_chunk_9|><|start_chunk_10|>
### Page 2
| Spezifikation ohne LeanID |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| Roboter- <br> version | Reichweite | Traglast | Schwerpunkt d. Nutzlast | Handgelenkdrehmoment |
| IRB 8700-800 | $3,50 \mathrm{~m}$ | 800 kg | 460 mm | 6043 Nm |
| IRB 8700-550 | $4,20 \mathrm{~m}$ | 550 kg | 460 mm | 5279 Nm |
| Anzahl der Achsen: |  |  | 6 |  |
| Zusatzlast: |  |  | beide Versionen können mit zusätzlichen Lasten versehen werden: 50 kg am Oberarm und 500 kg am Rahmen von Achse 1 |  |
| Schutzart / Ausführung: |  |  | IP67 / Foundry Plus 2 |  |
| Montageart: |  |  | Boden |  |
| Robotersteuerung: |  |  | IRC5-Standardsteuerung, OmniCore V400XT |  |
| Spezifikation mit LeanID |  |  |  |  |
| Roboterversion | Reichweite | Traglast | Schwerpunkt d. Nutzlast | Handgelenkdrehmoment |
| IRB 8700-800 | $3,50 \mathrm{~m}$ | 630 kg | 460 mm | 6043 Nm |
| IRB 8700-550 | $4,20 \mathrm{~m}$ | 475 kg | 460 mm | 5279 Nm |
| Anzahl der Achsen: |  |  | 6 |  |
| Zusatzlast: |  |  | alle Versionen können mit zusätzlichen Lasten versehen werden: 50 kg am Oberarm und 500 kg am Rahmen von Achse 1 |  |
| Schutzart / Ausführung: |  |  | IP67 / Foundry Plus 2 |  |
| Montageart: |  |  | Boden |  |
| Integrierte Anwenderschnittstelle: |  |  | abhängig vom gewählten <br> Kabelpaket |  |
| Integrierte Druckluftleitungen: |  |  | abhängig vom gewählten <br> Kabelpaket |  |
| Robotersteuerung: |  |  | IRC5-Standardsteuerung, OmniCore V400XT |  |
| Leistung |  |  |  |  |
| Positionswiederholgenauigkeit: |  |  | $\begin{aligned} & 0,05 \mathrm{~mm} \text { (IRB 8700-800), } \\ & 0,08 \mathrm{~mm} \text { (IRB 8700-550) } \end{aligned}$ |  |
| Bahnwiederholgenauigkeit: |  |  | $\begin{aligned} & 0,07 \mathrm{~mm} \text { (IRB 8700-800), } \\ & 0,14 \mathrm{~mm} \text { (IRB 8700-550) } \end{aligned}$ |  |
| Bewegung | Arbeitsbereich |  | Max. Achsgeschwindigkeit |  |
| Achse 1 | $+170^{\circ}$ bis $-170^{\circ *}$ |  | $75^{\circ} / \mathrm{s}$ |  |
| Achse 2 | $-65^{\circ}$ bis $+90^{\circ}$ |  | $60^{\circ} / \mathrm{s}$ |  |
| Achse 3 | $-30^{\circ}$ bis $+132^{\circ}$ |  | $60^{\circ} / \mathrm{s}$ |  |
| Achse 4 | $+300^{\circ}$ bis $-300^{\circ}$ |  | $85^{\circ} / \mathrm{s}$ |  |
| Achse 5 | $+130^{\circ}$ bis $-130^{\circ}$ |  | $85^{\circ} / \mathrm{s}$ |  |
| Achse 6 | $+360^{\circ}$ bis $-360^{\circ}$ |  | $115^{\circ} / \mathrm{s}$ |  |
| *optional $+220^{\circ}$ bis $-220^{\circ}$ |  |  |  |  |
| Elektrische Anschlüsse |  |  |  |  |
| Netzspannung: |  |  | 200-600 V, 50/60 Hz |  |
| Leistungsaufnahme: |  |  | 3,03 kW (IRB 8700-800), 3,93 kW (IRB 8700-550) |  |
<|end_chunk_10|><|start_chunk_11|>
## ABB AG

Division Robotics
Grüner Weg 6
61169 Friedberg
Telefon: +49 6031 85-0
E-Mail: robotervertrieb@de.abb.com
<|end_chunk_11|><|start_chunk_12|>
## Maße / Gewicht

| Robotergrundfläche: | $1175 \times 920 \mathrm{~mm}$ |
| :-- | :-- |
| Gewicht: | $4525-4575 \mathrm{~kg}$ |

Betriebsbedingungen
Umgebungstemperatur: $\quad+5^{\circ} \mathrm{C}$ bis $+50^{\circ} \mathrm{C}$
Bei Transport und Lagerung: $-25^{\circ} \mathrm{C}$ bis $+55^{\circ} \mathrm{C}$
Kurzfristig (max. 24 Stunden): bis zu $+70^{\circ} \mathrm{C}$
Relative Luftfeuchtigkeit: $\quad \max .95 \%$
Geräuschpegel: $\quad$ max. $71 \mathrm{~dB}(\mathrm{~A})$
Emission: EMC/EMI-abgeschirmt

Arbeitsbereich
IRB 8700-800
![img-1.jpeg](img-1.jpeg)

IRB 8700-550
![img-2.jpeg](img-2.jpeg)
<|end_chunk_12|><|start_chunk_13|>
## Hinweis:

Technische Änderungen der Produkte sowie Änderungen im Inhalt dieses Dokuments behalten wir uns jederzeit ohne Vorankündigung vor. Bei Bestellungen sind die jeweils vereinbarten Beschaffenheiten maßgebend. Die ABB AG übernimmt keinerlei Verantwortung für eventuelle Fehler oder Unvollständigkeiten in diesem Dokument.

Wir behalten uns alle Rechte an diesem Dokument und den darin enthaltenen Gegenständen und Abbildungen vor. Vervielfältigung, Bekanntgabe an Dritte oder Verwertung seines Inhaltes - auch von Teilen - ist ohne vorherige schriftliche Zustimmung durch die ABB AG verboten.<|end_chunk_13|>
</document>

Respond only with the IDs of the chunks where you believe a split should occur. 
YOU MUST RESPOND WITH AT LEAST ONE SPLIT.
