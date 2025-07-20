# Chunking Prompt

**Source File:** ABB_Datenblatt_IRB6650S_MISTRAL  
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
 IRB 6650S 
<|end_chunk_1|><|start_chunk_2|>
## Industrieroboter

![img-0.jpeg](img-0.jpeg)
<|end_chunk_2|><|start_chunk_3|>
## Anwendungsbereiche

Maschinenbedienung
Materialhandhabung
Punktschweißen

Der IRB 6650S ist ein Konsolroboter mit einzigartigem Arbeitsbereich. Er kann vertikale und horizontale Hubbewegungen ausführen und verfügt über eine große Reichweite nach vorne und nach unten.
<|end_chunk_3|><|start_chunk_4|>
## Pressenbedienung

Der IRB 6650S kann große Bleche wie komplette Karosserieseltenwände schnell und präzise handhaben. Er vereint ausgezeichnete Beschleunigungswerte mit exzellentem Ho-rizontal- und Vertikalhub. Diese einzigartige Kombination ermöglicht deutlich kürzere Taktzeiten und dadurch erhöhte Produktionskapazitäten. Der Bereich unterhalb des Roboters bietet zudem ausgezeichnete Möglichkeiten für einen schnellen Werkzeugwechsel.
<|end_chunk_4|><|start_chunk_5|>
## Druckguss

Der große Arbeitsbereich ermöglicht ein problemloses Einsprühen der Formen und eine einfache Materialhandhabung. Für eine längere Lebensdauer sind die Prozesskabel geschützt im Inneren des Roboterarms verlegt.
<|end_chunk_5|><|start_chunk_6|>
## Spritzguss

Der IRB 6650S ist insbesondere für die Bedienung von großen Spritzgießmaschinen mit über 10.000 kN Schließkraft geeignet. Die Flexibilität dieses 6-Achs-Roboters erleichtert Prozessanwendungen wie Beflämmen, Schneiden, Kleben und Montieren.
<|end_chunk_6|><|start_chunk_7|>
## Materialhandhabung

In einer erhöhten Position auf einer Verfahrenste montiert, kann der IRB 6650S dank seiner großen Reichweite nach vorne und unten doppelt so viele eingehende Förderer mit unterschiedlichen Teilen bearbeiten, wie ein traditioneller Roboter in Decken- oder Wandmontage. Im Vergleich zu einem hängenden Roboter auf einer Verfahrenste benötigt der IRB 6650S eine deutlich kürzere Verfahrenste.
<|end_chunk_7|><|start_chunk_8|>
## Punktschweißen

Der IRB 6650S bietet die Möglichkeit, die Roboterdichte in Schweiß- und Framingstationen zu erhöhen. Der Schlüssel dazu ist die Montage der Roboter in unterschiedlichen Höhen. Stan-dard-Roboter vom Typ IRB 6700 können am Boden montiert werden und der IRB 6650S in etwa 1,5 bis 2 m Höhe über dem Boden. Insgesamt wird so eine kompaktere Bauweise der Stationen ermöglicht und der Raum in der Zelle effizient genutzt.
<|end_chunk_8|><|start_chunk_9|>
## Lieferbar mit OmniCore-Steuerung

Die OmniCore-Steuerung bietet eine erstklassige Bewegungssteuerung, 20 Prozent Energieeinsparung, viele Sicherheitsfunktionen sowie unzählige weitere Optionen. Schnellere Leistung und verbesserte Flexibilität ermöglichen eine höhere Produktivität und die Fähigkeit, auf veränderte Marktanforderungen zu reagieren.
<|end_chunk_9|><|start_chunk_10|>
### Page 2
| Spezifikation |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| Roboter- <br> version | Reichweite | Traglast | Schwerpunkt d. Nutzlast | Handgelenk drehmoment |
| IRB 6650S-90 | $3,9 \mathrm{~m}$ | 90 kg | 360 mm | 438 Nm |
| IRB 6650S-125* | $3,5 \mathrm{~m}$ | 125 kg | 360 mm | 526 Nm |
| IRB 6650S-200* | $3,0 \mathrm{~m}$ | 200 kg | 365 mm | 625 Nm |
| Anzahl der Achsen: |  |  | 6 |  |
| Zusatzlast: |  |  | alle Versionen können mit zusätzlichen Lasten versehen werden: 50 kg am Oberarm und 500 kg am Rahmen von Achse 1 |  |
| Schutzart / Ausführung: |  |  | IP67 / Standard, <br> IP67 / Foundry Plus 2 |  |
| Montageart: |  |  | Konsole |  |
| Integrierte Anwenderschnittstelle: |  |  | abhängig vom gewählten Kabelpaket |  |
| Integrierte Druckluftleitungen: |  |  | abhängig vom gewählten Kabelpaket |  |
| Robotersteuerung: |  |  | OmniCore V250XT, OmniCore V400XT, IRC5-Standardsteuerung, IRC5 Panel Mounted Controller |  |
| * optional in LeanID-Ausführung mit geringerer Traglast |  |  |  |  |
| Leistung |  |  |  |  |
| Positionswiederholgenauigkeit: |  |  | $0,13-0,14 \mathrm{~mm}$ |  |
| Bahnwiederholgenauigkeit: |  |  | $0,70-0,90 \mathrm{~mm}$ |  |
|  |  |  | Arbeitsbereich |  |
| Achse 1 |  |  | $+180^{\circ}$ bis $-180^{\circ}$ |  |
| Achse 2 |  |  | $+160^{\circ}$ bis $-40^{\circ}$ |  |
| Achse 3 |  |  | $+70^{\circ}$ bis $-180^{\circ}$ |  |
| Achse 4 |  |  | $+300^{\circ}$ bis $-300^{\circ}$ |  |
| Achse 5 |  |  | $+120^{\circ}$ bis $-120^{\circ}$ |  |
| Achse 6 |  |  | $+360^{\circ}$ bis $-360^{\circ}$ |  |


| Max. Achsgeschwindigkeit |  |  |
| :--: | :--: | :--: |
|  | IRB 6650S-90 | IRB 6650S-125 IRB 6650S-200 |
| Achse 1 | $100^{\circ} / \mathrm{s}$ | $110^{\circ} / \mathrm{s}$ |
| Achse 2 | $90^{\circ} / \mathrm{s}$ | $90^{\circ} / \mathrm{s}$ |
| Achse 3 | $90^{\circ} / \mathrm{s}$ | $90^{\circ} / \mathrm{s}$ |
| Achse 4 | $150^{\circ} / \mathrm{s}$ | $150^{\circ} / \mathrm{s}$ |
| Achse 5 | $120^{\circ} / \mathrm{s}$ | $120^{\circ} / \mathrm{s}$ |
| Achse 6 | $235^{\circ} / \mathrm{s}$ | $235^{\circ} / \mathrm{s}$ |


| Elektrische Anschlüsse |  |
| :-- | :-- |
| Netzspannung: | $200-600 \mathrm{~V}, 50 / 60 \mathrm{~Hz}$ |
| Leistungsaufnahme: | $2,4 \mathrm{~kW}$ |


| Maße / Gewicht |  |
| :-- | :-- |
| Robotergrundfläche: | $1136 \times 864 \mathrm{~mm}$ |
| Gewicht: | $2275 \mathrm{~kg}($ IRB 6650S-90), |
|  | $2250 \mathrm{~kg}($ IRB 6650S-125/220) |


| Betriebsbedingungen |  |
| :-- | :-- |
| Umgebungstemperatur: | $+5^{\circ} \mathrm{C}$ bis $+52^{\circ} \mathrm{C}$ |
| Bei Transport und Lagerung: | $-25^{\circ} \mathrm{C}$ bis $+55^{\circ} \mathrm{C}$ |
| Kurzfristig (max. 24 Stunden): | bis zu $+70^{\circ} \mathrm{C}$ |
| Relative Luftfeuchtigkeit: | $\max .95 \%$ |
| Geräuschpegel: | $\max .73 \mathrm{~dB}(\mathrm{~A})$ |
| Emission: | EMC/EMI-abgeschirmt |
<|end_chunk_10|><|start_chunk_11|>
 Arbeitsbereich 

IRB 6650S-200/3.0
IRB 6650S-125/3.5
IRB 6650S-90/3.9
![img-1.jpeg](img-1.jpeg)
<|end_chunk_11|><|start_chunk_12|>
## ABB AG

Division Robotics
Grüner Weg 6
61169 Friedberg
Telefon: +49 6031 85-0
E-Mail: robotics@de.abb.com
<|end_chunk_12|><|start_chunk_13|>
## Hinweis:

Technische Änderungen der Produkte sowie Änderungen im Inhalt dieses Dokuments behalten wir uns jederzeit ohne Vorankündigung vor. Bei Bestellungen sind die jeweils vereinbarten Beschaffenheiten maßgebend. Die ABB AG übernimmt keinerlei Verantwortung für eventuelle Fehler oder Unvollständigkeiten in diesem Dokument.

Wir behalten uns alle Rechte an diesem Dokument und den darin enthaltenen Gegenständen und Abbildungen vor. Vervielfältigung, Bekanntgabe an Dritte oder Verwertung seines Inhaltes - auch von Teilen - ist ohne vorherige schriftliche Zustimmung durch die ABB AG verboten.<|end_chunk_13|>
</document>

Respond only with the IDs of the chunks where you believe a split should occur. 
YOU MUST RESPOND WITH AT LEAST ONE SPLIT.
