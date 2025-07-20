# Chunking Prompt

**Source File:** ABB_Datenblatt_IRB7710_7720_MISTRAL  
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
#### Page 1<|end_chunk_0|><|start_chunk_1|>
 IRB 7710, IRB 7720 
<|end_chunk_1|><|start_chunk_2|>
## Industrieroboter

![img-0.jpeg](img-0.jpeg)

Bei den Modellen IRB 7710 und IRB 7720 lag der Entwicklungsschwerpunkt auf einem effizienten modularen Design. Die Modellreihe bietet Energieeinsparungen von bis zu $30 \%$ und liefert gleichzeitig Leistung und Qualität auf Weltklasseniveau. Sie umfasst 16 Varianten mit Traglasten von 280 kg bis 620 kg .
<|end_chunk_2|><|start_chunk_3|>
## Hauptvorteile

1. Produktivität: Die Roboter erreichen eine in ihrer Klasse führende Präzision mit einer Bahngenauigkeit von bis zu 0,6 mm bei hohen Geschwindigkeiten von bis zu $1600 \mathrm{~mm} / \mathrm{s}$.
2. Energieeinsparungen: In Kombination mit der OmniCoreRobotersteuerung verbrauchen die Roboter $30 \%$ weniger Energie.
3. Größere Auswahl: 16 verschiedene Varianten erlauben es, das für die Anforderung exakt passende Modell zu finden.
4. Hohe Verfügbarkeit: Das LeanID-Kabelpaket verhindert effektiv Kabelschwingungen und verringert den Verschleiß. Außerdem vereinfacht es die Offline-Programmierung erheblich.
<|end_chunk_3|><|start_chunk_4|>
## Größere Flexibilität und Auswahl

Hersteller, die ihre Produktion hochfahren, können aus einer breiten Palette von ABB-Robotern aus dieser Schwerlast-Baureihe wählen, um den exakt passenden Roboter für ihre Applikation und Industrie zu finden. Die Roboter können zum Beispiel in der Automobilindustrie, im Bauwesen, in der Intralogistik sowie in der Gießereiindustrie eingesetzt werden.
<|end_chunk_4|><|start_chunk_5|>
## Unerreichte Produktivität und Qualität

Mit dem OmniCore-Robotersteuerung V400XT erreichen die Roboter eine in ihrer Klasse führende Präzision mit einer Bahngenauigkeit von bis zu $0,6 \mathrm{~mm}$, selbst wenn mehrere Roboter mit hohen Geschwindigkeiten von bis zu $1600 \mathrm{~mm} / \mathrm{s}$ laufen. Anwender können von einer bis zu $25 \%$ igen Reduzierung* der Zykluszeiten profitieren, was die Produktivität und Qualität weiter steigert.
<|end_chunk_5|><|start_chunk_6|>
## Energieeinsparungen bis zu 30\%

Das energieeffiziente Design des Roboters in Kombination mit der OmniCore-Energierückgewinnungs-Technologie ermöglicht Energieeinsparungen von bis zu $30 \%$. Das eingebaute Netzteil kann Energie an das Stromnetz zurückgeben.
<|end_chunk_6|><|start_chunk_7|>
## Modulares Design

Die Schwerlastroboter der IRB 77X0-Reihe basieren auf demselben modularen Design wie die anderen Schwerlastroboter von ABB, mit standardisierten Komponenten, einschließlich Sockel, Unterarm und Oberarm. Alle Roboter haben die gleiche Grundfläche, was eine schnellere, bequemere und flexiblere Installation beim Wechsel von Robotern in verschiedenen Produktionslinien ermöglicht.
<|end_chunk_7|><|start_chunk_8|>
## Anwendungsbeispiele

- Montage und Handhabung von sehr schweren Produkten wie z. B. EV-Batterien, Gussteilen oder ganzen Karossen
- Pressenbedienung und Palettieren, z. B. Autotüren, Rahmen, Kisten und Paletten
- Hochpräzise Kontaktanwendungen, z. B. Materialbearbeitung und Rührreibschweißen
<|end_chunk_8|><|start_chunk_9|>
### Page 2
| Spezifikation |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| Roboter- <br> version | Reichweite | Traglast | Schwerpunkt d. Nutzlast | Handgelenkdrehmoment |
| ohne LeanID |  |  |  |  |
| IRB 7710-500/2.85 | 2,85 m | 500 kg | 360 mm | 3027 Nm |
| IRB 7710-430/3.1 | 3,1 m | 430 kg | 360 mm | 3027 Nm |
| IRB 7710-360/3.3 | 3,3 m | 360 kg | 360 mm | 3027 Nm |
| IRB 7710-310/3.5 | 3,5 m | 310 kg | 360 mm | 3027 Nm |
| IRB 7720-620/2.9 | 2,9 m | 620 kg | 400 mm | 4635 Nm |
| IRB 7720-530/3.1 | 3,1 m | 530 kg | 400 mm | 4635 Nm |
| IRB 7720-510/3.3 | 3,3 m | 510 kg | 400 mm | 3027 Nm |
| IRB 7720-450/3.5 | 3,5 m | 450 kg | 400 mm | 3027 Nm |
| mit LeanID |  |  |  |  |
| IRB 7710-400/2.85 LID | 2,85 m | 400 kg | 360 mm | 2994 Nm |
| IRB 7710-390/3.1 LID | 3,1 m | 390 kg | 360 mm | 2994 Nm |
| IRB 7710-325/3.3 LID | 3,3 m | 325 kg | 360 mm | 2994 Nm |
| IRB 7710-280/3.5 LID | 3,5 m | 280 kg | 360 mm | 2994 Nm |
| IRB 7720-560/2.9 LID | 2,9 m | 560 kg | 400 mm | 4586 Nm |
| IRB 7720-480/3.1 LID | 3,1 m | 480 kg | 400 mm | 4586 Nm |
| IRB 7720-400/3.3 LID | 3,3 m | 400 kg | 400 mm | 2994 Nm |
| IRB 7720-400/3.5 LID | 3,5 m | 400 kg | 400 mm | 2994 Nm |
| Anzahl der Achsen: |  |  | 6 |  |
| Zusatzlast: |  |  | alle Versionen ohne Lean-ID können mit zusätzlichen Lasten versehen werden: 50 kg am Oberarm und 550 kg am Rahmen von Achse 1 |  |
| Schutzart / Ausführung: |  |  | IP67 / Standard, IP67 / Foundry Plus 2 |  |
| Montageart: |  |  | Boden |  |
| Robotersteuerung: |  |  | OmniCore V400XT |  |
| Leistung |  |  |  |  |
|  | Positionswiederholgenaulgkeit: |  | Bahnswiederholgenaulgkeit: |  |
| IRB 7710-500/2.85 | 0,06 mm |  | 0,10 mm |  |
| IRB 7710-430/3.1 | 0,10 mm |  | 0,14 mm |  |
| IRB 7710-360/3.3 | 0,07 mm |  | 0,21 mm |  |
| IRB 7710-310/3.5 | 0,06 mm |  | 0,23 mm |  |
| IRB 7720-620/2.9 | 0,06 mm |  | 0,07 mm |  |
| IRB 7720-530/3.1 | 0,05 mm |  | 0,07 mm |  |
| IRB 7720-510/3.3 | 0,05 mm |  | 0,29 mm |  |
| IRB 7720-450/3.5 | 0,06 mm |  | 0,21 mm |  |
| IRB 7710, alle Varianten |  |  |  |  |
|  | Arbeitsbereich |  | Max. Achsgeschwindigkeit |  |
| Achse 1* | $+170^{\circ}$ bis $-170^{\circ}$ |  | $90^{\circ} / \mathrm{s}$ |  |
| Achse 2 | $+85,2^{\circ}$ bis $-65^{\circ}$ |  | $60^{\circ} / \mathrm{s}$ |  |
| Achse 3 | $+130^{\circ}$ bis $-27^{\circ}$ |  | $60^{\circ} / \mathrm{s}$ |  |
| Achse 4 | $+300^{\circ}$ bis $-300^{\circ}$ |  | $100^{\circ} / \mathrm{s}$ |  |
| Achse 5** | $+130^{\circ}$ bis $-130^{\circ}$ |  | $100^{\circ} / \mathrm{s}$ |  |
| Achse 6*** | $+360^{\circ}$ bis $-360^{\circ}$ |  | $160^{\circ} / \mathrm{s}$ |  |


| IRB 7720, alle Varianten |  |  |
| :--: | :--: | :--: |
|  | Arbeitsbereich | Max. Achsgeschwindigkeit |
| Achse 1* | $+170^{\circ}$ bis $-170^{\circ}$ | $75^{\circ} / \mathrm{s}$ |
| Achse 2 | $+85,2^{\circ}$ bis $-65^{\circ}$ | $60^{\circ} / \mathrm{s}$ |
| Achse 3 | $+130^{\circ}$ bis $-27^{\circ}$ | $55^{\circ} / \mathrm{s}$ |
| Achse 4 | $+300^{\circ}$ bis $-300^{\circ}$ | $100^{\circ} / \mathrm{s}$ |
| Achse 5** | $+130^{\circ}$ bis $-130^{\circ}$ | $100^{\circ} / \mathrm{s}$ |
| Achse 6*** | $+360^{\circ}$ bis $-360^{\circ}$ | $160^{\circ} / \mathrm{s}$ |
| *Optional $\pm 220^{\circ}$ ** $\pm 120^{\circ}$ in Lean ID-Ausführung |  | *** $\pm 220^{\circ}$ in Lean ID-Ausführung |


| Elektrische Anschlüsse |  |
| :-- | :-- |
| Netzspannung: | $380-480$ VAC, $50 / 60 \mathrm{~Hz}$ |
| Leistungsaufnahme: | $2,7-3,1 \mathrm{~kW}$ (IRB 7710) |
|  | $2,3-2,8 \mathrm{~kW}$ (IRB 7720) |


| Maße / Gewicht |  |
| :-- | :-- |
| Robotergrundfläche: | $1020 \times 795 \mathrm{~mm}$ |
| Gewicht: | $2130-2690 \mathrm{~kg}$ |


| Betriebsbedingungen |  |
| :-- | :-- |
| Umgebungstemperatur: | $+5^{\circ} \mathrm{C}$ bis $+50^{\circ} \mathrm{C}$ |
| Bei Transport und Lagerung: | $-25^{\circ} \mathrm{C}$ bis $+55^{\circ} \mathrm{C}$ |
| Kurzfristig (max. 24 Stunden): | bis zu $+70^{\circ} \mathrm{C}$ |
| Relative Luftfeuchtigkeit: | max. 95\% |
| Geräuschpegel: | max. 72 dB (A) |
| Emission: | EMC/EMl-abgeschirmt |
<|end_chunk_9|><|start_chunk_10|>
### Page 3<|end_chunk_10|><|start_chunk_11|>
 Arbeitsbereich
<|end_chunk_11|><|start_chunk_12|>
## IRB 7710-500/2.85

![img-1.jpeg](img-1.jpeg)
<|end_chunk_12|><|start_chunk_13|>
## IRB 7710-430/3.1

![img-2.jpeg](img-2.jpeg)
<|end_chunk_13|><|start_chunk_14|>
## IRB 7710-360/3.3

![img-3.jpeg](img-3.jpeg)
<|end_chunk_14|><|start_chunk_15|>
## IRB 7710-310/3.5

![img-4.jpeg](img-4.jpeg)
<|end_chunk_15|><|start_chunk_16|>
 Arbeitsbereich
<|end_chunk_16|><|start_chunk_17|>
## IRB 7710-430/2.85 LID

![img-5.jpeg](img-5.jpeg)
<|end_chunk_17|><|start_chunk_18|>
## IRB 7710-390/3.1 LID

![img-6.jpeg](img-6.jpeg)
<|end_chunk_18|><|start_chunk_19|>
## IRB 7710-325/3.3 LID

![img-7.jpeg](img-7.jpeg)
<|end_chunk_19|><|start_chunk_20|>
## IRB 7710-280/3.5 LID

![img-8.jpeg](img-8.jpeg)
<|end_chunk_20|><|start_chunk_21|>
### Page 4<|end_chunk_21|><|start_chunk_22|>
 Arbeitsbereich
<|end_chunk_22|><|start_chunk_23|>
## IRB 7720-620/2.9

![img-9.jpeg](img-9.jpeg)
<|end_chunk_23|><|start_chunk_24|>
## IRB 7720-530/3.1

![img-10.jpeg](img-10.jpeg)
<|end_chunk_24|><|start_chunk_25|>
## IRB 7720-510/3.3

![img-11.jpeg](img-11.jpeg)
<|end_chunk_25|><|start_chunk_26|>
## IRB 7720-450/3.5

![img-12.jpeg](img-12.jpeg)
<|end_chunk_26|><|start_chunk_27|>
 Arbeitsbereich
<|end_chunk_27|><|start_chunk_28|>
## IRB 7720-560/2.9 LID

![img-13.jpeg](img-13.jpeg)
<|end_chunk_28|><|start_chunk_29|>
## IRB 7720-480/3.1 LID

![img-14.jpeg](img-14.jpeg)
<|end_chunk_29|><|start_chunk_30|>
## IRB 7720-400/3.3 LID

![img-15.jpeg](img-15.jpeg)
<|end_chunk_30|><|start_chunk_31|>
## IRB 7720-400/3.5 LID

![img-16.jpeg](img-16.jpeg)
<|end_chunk_31|><|start_chunk_32|>
### Page 5<|end_chunk_32|><|start_chunk_33|>
## ABB AG

Division Robotics
Grüner Weg 6
61169 Friedberg
Telefon: +49 6031 85-0
E-Mail: robotics@de.abb.com
<|end_chunk_33|><|start_chunk_34|>
## www.abb.de/robotics
<|end_chunk_34|><|start_chunk_35|>
## Hinweis:

Technische Änderungen der Produkte sowie Änderungen im Inhalt dieses Dokuments behalten wir uns jederzeit ohne Vorankündigung vor. Bei Bestellungen sind die jeweils vereinbarten Beschaffenheiten maßgebend. Die ABB AG übernimmt keinerlei Verantwortung für eventuelle Fehler oder Unvollständigkeiten in diesem Dokument.

Wir behalten uns alle Rechte an diesem Dokument und den darin enthaltenen Gegenständen und Abbildungen vor. Vervielfältigung, Bekanntgabe an Dritte oder Verwertung seines Inhaltes - auch von Teilen - ist ohne vorherige schriftliche Zustimmung durch die ABB AG verboten.<|end_chunk_35|>
</document>

Respond only with the IDs of the chunks where you believe a split should occur. 
YOU MUST RESPOND WITH AT LEAST ONE SPLIT.
