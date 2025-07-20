# Contextualization Prompt

**Source File:** ABB_Datenblatt_IRB1010_MISTRAL  
**Prompt Type:** Contextualization  
**Generated:** RODEOS  


---

You are an assistant specialized in analyzing document chunks and providing relevant context.

<instructions>
    <instruction>You will be given a document and a specific chunk from that document</instruction>
    <instruction>Provide 2-3 concise sentences that situate this chunk within the broader document</instruction>
    <instruction>Identify the main topic or concept discussed in the chunk</instruction>
    <instruction>Include relevant information or comparisons from the broader document context</instruction>
    <instruction>Note how this information relates to the overall theme or purpose of the document if applicable</instruction>
    <instruction>Include key figures, dates, or percentages that provide important context</instruction>
    <instruction>Avoid phrases like "This chunk discusses" - instead, directly state the context</instruction>
    <instruction>Keep your response brief and focused on improving search retrieval</instruction>
</instructions>

Here is the document:
<document>
### Page 1
ROBOTICS

# IRB 1010 

## Industrieroboter

![img-0.jpeg](img-0.jpeg)

Der IRB 1010 ist ein Kleinroboter mit großer Leistung, der speziell für die Fertigung von Kleinelektronik entwickelt wurde. Mit einer Traglast von $1,5 \mathrm{~kg}$, einer Wiederholgenauigkeit von $0,01 \mathrm{~mm}$ und seiner Kompaktheit ermöglicht er eine hochqualitative Fertigung auf engstem Raum.

Die Nachfrage nach intelligenten und tragbaren Geräten wie Sensoren, Uhren, Kopfhörern, Brillen, Sport- und Gesundheitstrackern (so genannte Wearables) steigt weltweit rasant an. Für die Fertigung solcher Kleinelektronik brauchen Hersteller kleine und leistungsstarke Roboter. Der kleinste Industrieroboter von ABB, der IRB 1010, wurde entwickelt, um dieser Nachfrage gerecht zu werden. Er ermöglicht schnelle Fertigungsprozesse und ein präzises Handling kleiner und empfindlicher Bauteile.

Der IRB 1010 bietet ebenso neue Möglichkeiten für Bildungseinrichtungen. Denn das kompakte Design ermöglicht eine Installation auf einem Tisch im Unterrichtsraum. Darüber hinaus ist der IRB 1010 so anwenderfreundlich, dass Lehrkräfte, Studierende sowie Schülerinnen und Schüler die für die Programmierung und Bedienung erforderlichen Kenntnisse schnell erlernen.

## Vorteile

- Der kleinste Industrieroboter von ABB: Der IRB 1010 ist 30\% kleiner als der IRB 120 und kann in den engsten Produktionsbereichen installiert werden, beispielsweise als Teil von Sondermaschinen. Mit ihm lässt sich der verfügbare Platz ideal ausnutzen.
- Klassenbeste Traglast: Mit einer Traglast von 1,5 kg und seiner Geschwindigkeit kann der IRB 1010 mehr Teile pro Zyklus handhaben als vergleichbare Roboter. Dadurch profitieren Anwender von mehr Durchsatz und höherer Produktivität.
- Immer bereit dank seiner Bremssysteme: Mit seinen sechs Bremssystemen kann der Roboterarm auch dann in Position bleiben, wenn er ausgeschaltet oder angehalten wird. Da der IRB 1010 keine Zeit benötigt, um seine Position wiederzufinden, kann er die Produktion schneller wieder aufnehmen und liefert eine höhere Produktivität als vergleichbare Roboter.
- Überlegene Präzision: Die Positions- und Bahnwiederholgenauigkeit von 0,01 mm ermöglicht eine genaue und hochwertige Fertigung.
- Angetrieben von der OmniCore-Steuerung: Die OmniCoreSteuerung bietet eine erstklassige Bewegungssteuerung, 20\% Energieeinsparung, viele Sicherheitsfunktionen sowie unzählige weitere Optionen. Schnellere Leistung und verbesserte Flexibilität ermöglichen eine höhere Produktivität und die Fähigkeit, auf veränderte Marktanforderungen zu reagieren.
- Zusätzliche Druckluftversorgung: Der große Durchmesser ( $2 \times \varnothing 4 \mathrm{~mm}$ ) des Luftschlauchs am Oberarm bietet zusätzliche Leistung für die Vakuumansaugung, so dass mehr Objekte gleichzeitig gehandhabt werden können.
- Einfache Programmierung mit Robot Control Mate: Benutzer können den IRB 1010 von ihrem Computer oder Tablet aus in Echtzeit bewegen, programmieren und kalibrieren, was die Steuerung der Roboterbewegungen einfacher denn je macht.


## Einsatzbereiche

Materialhandhabung, Pick-and-Place-Aufgaben, Klebstoffauftrag, Entfernung von Folien und Montage

### Page 2
| Spezifikation |  |  |  |
| :--: | :--: | :--: | :--: |
| Roboterversion | Reichweite | Traglast | Zusätzliche <br> Armlast |
| IRB 1010-1.5/0.37 | 370 mm | $1,5 \mathrm{~kg}$ | $0,2 \mathrm{~kg}$ |
| Anzahl der Achsen: |  | 6 |  |
| Schutzart / Ausführung: |  | IP40 / Standard |  |
| Montageart: |  | Boden, Decke, geneigt |  |
| Integrierte Anwenderschnittstelle: |  | 12x Signal / Leistung bis zum Oberarm |  |
| Integrierte Druckluftleitungen: |  | 2 Druckluftleitungen mit max. 6 bar bis zum Oberarm |  |
| Robotersteuerung: |  | OmniCore E10 und C30 |  |
| Leistung |  |  |  |
| Positionswiederholgenauigkeit: |  | $0,01 \mathrm{~mm}$ |  |
| Bahnwiederholgenauigkeit: |  | $0,01 \mathrm{~mm}$ |  |
|  | Arbeitsbereich | Max. Achsgeschwindigkeit |  |
| Achse 1 | $+170^{\circ}$ bis $-170^{\circ}$ | $320^{\circ} / \mathrm{s}$ |  |
| Achse 2 | $+125^{\circ}$ bis $-75^{\circ}$ | $320^{\circ} / \mathrm{s}$ |  |
| Achse 3 | $+50^{\circ}$ bis $-180^{\circ}$ | $375^{\circ} / \mathrm{s}$ |  |
| Achse 4 | $+170^{\circ}$ bis $-170^{\circ}$ | $500^{\circ} / \mathrm{s}$ |  |
| Achse 5 | $+125^{\circ}$ bis $-125^{\circ}$ | $470^{\circ} / \mathrm{s}$ |  |
| Achse 6 | $+360^{\circ}$ bis $-360^{\circ}$ | $500^{\circ} / \mathrm{s}$ |  |
| Zykluszeit |  |  |  |
| 1 kg Pick-\&-Place-Zyklus $25 \times 300 \times 25 \mathrm{~mm}$ |  | $0,54 \mathrm{~s}$ |  |
| Elektrische Anschlüsse |  |  |  |
| Netzspannung: |  | 200-600 V, 50/60 Hz |  |
| Maße / Gewicht |  |  |  |
| Robotergrundfläche: |  | $135 \times 250 \mathrm{~mm}$ |  |
| Gewicht: |  | $13,5 \mathrm{~kg}$ |  |
| Betriebsbedingungen |  |  |  |
| Umgebungstemperatur: |  | $+5^{\circ} \mathrm{C}$ bis $+45^{\circ} \mathrm{C}$ |  |
| Relative Luftfeuchtigkeit: |  | max. $95 \%$ |  |
| Geräuschpegel: |  | max. 70 dB (A) |  |
| Emission: |  | EMC/EMI-abgeschirmt, ESD-zertifiziert |  |

## ABB AG

Division Robotics
Grüner Weg 6
61169 Friedberg
Telefon: +49 6031 85-0
E-Mail: robotics@de.abb.com

## Arbeitsbereich

![img-1.jpeg](img-1.jpeg)
![img-2.jpeg](img-2.jpeg)

OmniCore-Steuerung mit FlexPendant

## Hinweis:

Technische Änderungen der Produkte sowie Änderungen im Inhalt dieses Dokuments behalten wir uns jederzeit ohne Vorankündigung vor. Bei Bestellungen sind die jeweils vereinbarten Beschaffenheiten maßgebend. Die ABB AG übernimmt keinerlei Verantwortung für eventuelle Fehler oder Unvollständigkeiten in diesem Dokument.

Wir behalten uns alle Rechte an diesem Dokument und den darin enthaltenen Gegenständen und Abbildungen vor. Vervielfältigung, Bekanntgabe an Dritte oder Verwertung seines Inhaltes - auch von Teilen - ist ohne vorherige schriftliche Zustimmung durch die ABB AG verboten.
</document>

Here is the chunk to contextualize:
<chunk>
#### Page 1
ROBOTICS

 IRB 1010 

## Industrieroboter

![img-0.jpeg](img-0.jpeg)

Der IRB 1010 ist ein Kleinroboter mit großer Leistung, der speziell für die Fertigung von Kleinelektronik entwickelt wurde. Mit einer Traglast von $1,5 \mathrm{~kg}$, einer Wiederholgenauigkeit von $0,01 \mathrm{~mm}$ und seiner Kompaktheit ermöglicht er eine hochqualitative Fertigung auf engstem Raum.

Die Nachfrage nach intelligenten und tragbaren Geräten wie Sensoren, Uhren, Kopfhörern, Brillen, Sport- und Gesundheitstrackern (so genannte Wearables) steigt weltweit rasant an. Für die Fertigung solcher Kleinelektronik brauchen Hersteller kleine und leistungsstarke Roboter. Der kleinste Industrieroboter von ABB, der IRB 1010, wurde entwickelt, um dieser Nachfrage gerecht zu werden. Er ermöglicht schnelle Fertigungsprozesse und ein präzises Handling kleiner und empfindlicher Bauteile.

Der IRB 1010 bietet ebenso neue Möglichkeiten für Bildungseinrichtungen. Denn das kompakte Design ermöglicht eine Installation auf einem Tisch im Unterrichtsraum. Darüber hinaus ist der IRB 1010 so anwenderfreundlich, dass Lehrkräfte, Studierende sowie Schülerinnen und Schüler die für die Programmierung und Bedienung erforderlichen Kenntnisse schnell erlernen.
</chunk>

Respond only with the succinct context for this chunk. Do not mention it is a chunk or that you are providing context.
