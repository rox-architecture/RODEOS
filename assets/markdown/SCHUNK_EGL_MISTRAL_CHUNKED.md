# Contextualized Document: SCHUNK_EGL_MISTRAL

**Source:** SCHUNK_EGL_MISTRAL.md  
**Processing:** Semantic Chunking + Contextualization  
**Processed by:** Remote LLM via OpenRouter  
**Prompts saved to:** src/contextualEnrichment/prompts/

This document has been processed to create semantic chunks with contextual information for improved search and retrieval.

---

<chunk_context>The document serves as a product data sheet for the Universalgreifer EGL, detailing its specifications, features, and applications. It introduces the product on the first page, highlighting its significance in automation technology, particularly in flexible and robust gripping solutions. The subsequent pages elaborate on the technical aspects, operational benefits, and integration capabilities of the Universalgreifer EGL, emphasizing its versatility in various industrial environments.</chunk_context>
<chunk>#### Page 1
![img-0.jpeg](img-0.jpeg)

 **Produktdatenblatt**

Universalgreifer EGL

![img-1.jpeg](img-1.jpeg)

### Page 2</chunk>

---

<chunk_context>The Universalgreifer EGL is introduced as a highly flexible and robust servo-electric 2-finger parallel gripper designed for a wide range of applications in both clean and harsh environments. It features a finely adjustable gripping force and a large programmable stroke, allowing for versatile handling of various workpieces. The document emphasizes its integration capabilities with existing control systems via PROFINET or PROFIBUS, highlighting its user-friendly design with standard industrial connectors and USB interfaces for easy configuration and updates.</chunk_context>
<chunk>Flexibel. Robust. Busfähig. 

## Universalgreifer EGL

Servoelektrischer 2-Finger-Parallelgreifer mit feinfühliger Greifkraftregelung und großem Hub

## Einsatzgebiet

Universell einsetzbarer, hochflexibler elektrischer 2-Finger-Parallelgreifer für ein vielfältiges Teilespektrum in sauberen bis rauen Umgebungsbedingungen

## Vorteile - Ihr Nutzen

Stromgeregelte Greifkrafteinstellung von großem Kraftbereich für feinfühliges oder kraftvolles Greifen unterschiedlicher Werkstücke
Großer und frei programmierbarer Hub für flexible Werkstückhandhabung
Komplette Integration der Regel- und Leistungselektronik zum Aufbau eines dezentralen Steuerungssystems
Vielfältige Ansteuerungsmöglichkeiten zur einfachen Einbindung in bestehende Steuerungskonzepte über PROFINET oder PROFIBUS
Anschlussstecker in Industrie-Standard für einen einfachen elektrischen Anschluss
Service-Schnittstelle: USB Host und USB Device für komfortable Parametrierung und Firmwareupdates über USB-Stick oder PC
Drehcodier- und DIP-Schalter für manuelle Feldbusadressierung, Baudrateneinstellung und Servicefunktionen
![img-2.jpeg](img-2.jpeg)</chunk>

---

<chunk_context>The section elaborates on the functional description of the Universalgreifer EGL, detailing the mechanics of its operation, including the DC servomotor's role in driving the gear system and the encoder's function in position tracking. This information is crucial for understanding the device's design, which integrates control and power electronics for decentralized motor control, and highlights the use of a rack-and-pinion mechanism for linear movement. The broader document emphasizes the greifer's versatility and application in various environments, showcasing its robust features such as an electric brake for position retention and a service interface for easy configuration and updates.</chunk_context>
<chunk>### Page 3
 Funktionsbeschreibung 

Der DC-Servomotor treibt über ein Getriebe die Zahnstange der Grundbacke an. Die Position wird über einen Encoder erfasst.
Über die an den Spindelmuttern befestigten Grundbacken
wird die Rotationsbewegung in die Linearbewegung der Grundbacke überführt.
![img-3.jpeg](img-3.jpeg)
(1) Steuerelektronik

Integrierte Regelungs- und Leistungselektronik zur dezentralen Ansteuerung des Servomotors
(2) Encoder
zur Positionsauswertung und Positionierung des Greifers
(3) Elektrische Bremse
für Positionserhaltung bei Stillstand und
Spannungsausfall
(4) Antrieb

DC-Servomotor mit Planetengetriebe
(5) Kinematik

Zahnstangen-Ritzel-Prinzip mit Profilschienenführung für zentrisches Spannen
(6) Servicefenster
mit Kundenschnittstelle für Service-Funktionen, Einstellung der Busadresse, USB-Anbindung und LED-Statusanzeige

### Page 4
 EGL 

## Allgemeine Informationen zur Baureihe

Wirkprinzip: Ritzel-Zahnstangen-Prinzip
Gehäusematerial: Aluminiumlegierung, oberflächenveredelt
Grundbackenmaterial: Stahl
Betätigung: servoelektrisch, über bürstenlosen DC-Servomotor

Gewährleistung: 24 Monate
Lieferumfang: Greifer inklusive Sicherheitsinformationen und Beipack mit Zentrierhülsen für Greifermontage und Fingermontage. Produktspezifische Anleitungen und Software können unter schunk.com/downloads-manuals und schunk.com/downloads-software heruntergeladen werden.
Greifkraft: ist die arithmetische Summe der an jeder Backe wirkenden Einzelkraft, im Abstand P (siehe Zeichnung)
Fingerlänge: wird ab derselben Bezugsfläche wie der Abstand P in Richtung der Hauptachse gemessen.
Wiederholgenauigkeit: ist definiert als Streuung der Endlage bei 100 aufeinanderfolgenden Hüben.

Werkstückgewicht: wird errechnet bei Kraftschluss mit einem Haftreibwert von 0,1 und einer Sicherheit von 2 gegen Rutschen des Werkstücks bei Erdbeschleunigung g. Bei Formschluss ergeben sich deutlich höhere zulässige Werkstückgewichte.
Schließ- und Öffnungszeiten: Minimale Schließ- und Öffnungszeiten sind reine Bewegungszeiten der Grundbacken bzw. Finger bei max. Geschwindigkeit, max. Beschleunigung, ohne Strombegrenzung (Maximalstrom) und Beachtung der maximal zulässigen Massen pro Finger.
Nennströme: dürfen dauerhaft anliegen. Bei allen Strömen oberhalb des Nennstroms bis zum Maximalstrom sind die Hinweise in der jeweiligen Produktdokumentation zu beachten.
Elektrische Bremse: Die eingebaute, elektrische Haltebremse dient der Fixierung und dem Erhalt der Position der Greiferbacken bei Spannungsabfall. Sie kann keine vollständigen Sicherheits- oder Greifkrafterhaltungsfunktionen abdecken.
![img-4.jpeg](img-4.jpeg)

## Anwendungsbeispiel

Hochflexible Handlingeinheit zum Greifen und Transportieren von unterschiedlichen Werkstücken mit zufälliger Lageorientierung

(1) Universalgreifer EGL
(2) Servoelektrische Schwenk-Neigeeinheit PW
(3) Servoelektrisches Drehmodul PR 2
(4) Servoelektrischer Antrieb PDU 2
(5) Linearmodul mit Zahnriemenantrieb Beta</chunk>

---

<chunk_context>This section highlights the additional components and options available for the Universalgreifer EGL, emphasizing its enhanced productivity, functionality, and integration capabilities. It details the integrated control and power electronics that eliminate the need for external control units, and outlines the compatibility with communication standards like PROFINET and PROFIBUS-DP, facilitating seamless integration into existing industrial networks. The mention of the backen interface compatibility with the PGN-plus-P series underscores the versatility and adaptability of the EGL in various applications, aligning with the document's overall focus on advanced automation solutions.</chunk_context>
<chunk>### Page 5
 SCHUNK bietet mehr ... 

Die folgenden Komponenten machen das Produkt noch produktiver - die passende Ergänzung für höchste Funktionalität, Flexibilität, Zuverlässigkeit und Prozesssicherheit.
![img-5.jpeg](img-5.jpeg)

Kommunikationskabel
(1) Weitergehende Informationen zu diesen Produkten finden Sie auf den folgenden Produktseiten oder unter schunk.com.

## Optionen und spezielle Informationen

Die elektrische Ansteuerung des Greifers erfolgt über die komplett integrierte Regelungs- und Leistungselektronik. Somit sind keine zusätzlichen externen Regelungsseinheiten für das Modul notwendig.
Als Kommunikationsarten stehen vielfältige Schnittstellen wie PROFINET oder PROFIBUS-DP zur Verfügung. Damit ist der Aufbau von industriellen Busnetzen gewährleistet und eine einfache Integration in bestehende Steuerungskonzepte möglich. Zur Übertragung von Versorgungsspannung und Datenkommunikation bieten wir diverse Kabel an.
Grundbacken-Schnittstelle: Die Schnittstelle der Grundbacken entspricht der des Universalgreifers PGN-plus-P. Somit kann das umfangreiche Fingerzubehör des PGN-plus-P unter Berücksichtigung der Störkonturen und der geltenden Einsatzgrenzen auch für diesen Greifer genutzt werden.</chunk>

---

<chunk_context>This section provides detailed technical specifications for the Universalgreifer EGL 90, including critical performance metrics such as gripping force, finger length, and maximum load capacities. It highlights the compatibility with various robotic systems (UR 3/5/10/16) and outlines operational parameters like gripping force range (50-600 N), recommended workpiece weight (3 kg), and repeatability (0.05 mm). These specifications are essential for understanding the greifer's capabilities and integration into automated systems, aligning with the document's overall focus on the product's versatility and application in industrial automation.</chunk_context>
<chunk>### Page 6
![img-6.jpeg](img-6.jpeg)

Greifkraft
![img-7.jpeg](img-7.jpeg)

Fingerlänge
![img-8.jpeg](img-8.jpeg)

Dimensionen und max. Belastungen
![img-9.jpeg](img-9.jpeg)
(1) Die angegebenen Momente und Kräfte sind statische Werte, gelten je Grundbacke und dürfen gleichzeitig auftreten. Die Belastungen dürfen zusätzlich zu dem durch die Greifkraft erzeugten Moment auftreten.

 Technische Daten 

| Bezeichnung |  | EGL 90-PN | EOA-UR3510-EGL90 | EOA-UR3510-EGL90-AUB |
| :--: | :--: | :--: | :--: | :--: |
| Ident.-Nr. |  | 1302877 | 1392477 | 1403607 |
| Roboterkompatibilität |  |  | UR 3/5/10/16 | UR 3/5/10/16 |
| Allgemeine Betriebsdaten |  |  |  |  |
| Hub pro Backe | [mm] | 42.5 | 42.5 | 42.5 |
| Min./max. Greifkraft | [N] | 50/600 | 50/600 | 50/600 |
| Empfohlenes Werkstückgewicht | [kg] | 3 | 3 | 3 |
| Max. zulässige Fingerlänge | [mm] | 165 | 165 | 165 |
| Max. zulässige Masse pro Finger | [kg] | 0.5 | 0.5 | 0.5 |
| Wiederholgenauigkeit | [mm] | 0.05 | 0.05 | 0.05 |
| Schließ-/Öffnungszeit | [s] | $0.7 / 0.7$ | $0.7 / 0.7$ | $0.7 / 0.7$ |
| Max. Geschwindigkeit | [mm/s] | 150 | 150 | 150 |
| Max. Beschleunigung | [mm/s $\left.{ }^{2}\right]$ | 2500 | 2500 | 2500 |
| Eigenmasse | [kg] | 1.8 | 2.13 | 2.63 |
| Min./max. Umgebungstemperatur | $\left[{ }^{\circ} \mathrm{C}\right]$ | 5/55 | 5/55 | 5/55 |
| Schutzart IP |  | 46 | 46 | 46 |
| Reinraumklasse ISO 14644-1:2015 |  | 4 | 4 | 4 |
| Abmaße X x Y x Z | [mm] | $112 \times 90 \times 108$ | $112 \times 100.4 \times 121$ | $112 \times 100.4 \times 121$ |
| Elektrische Betriebsdaten |  |  |  |  |
| Reglerelektronik |  | integriert | integriert | integriert |
| Nennspannung | [V DC] | 24 | 24 | 24 |
| Kommunikationsschnittstelle |  | PROFINET | PROFINET | PROFINET |
| Parametrierschnittstelle |  | USB | USB | USB |
| Max. Strom Leistung | [A] | 2.5 | 2.5 | 2.5 |
| Max. Strom Logik | [A] | 0.5 | 0.5 | 0.5 |
| Optionen und deren Eigenschaften |  |  |  |  |
| PROFIBUS-Variante |  | EGL 90-PB |  |  |
| Ident.-Nr. |  | 1325751 |  |  |
| Datenrate | [Mbit/s] | 12 |  |  |

(1) Der maximale Strom der elektrischen Betriebsdaten spezifiziert den Eingangsstrom, der vom Netzteil abgegriffen wird. Die Diagramme Greifkraft, Fingerlänge und Drosselung beziehen sich auf den Motorstrom, der über die SPS-Programmierung angesteuert werden kann.
(2) Das Diagramm Fingerlänge zeigt die max. zulässige Fingerlänge in Abhängigkeit der angesteuerten Backengeschw. bei definierten Motorströmen.

### Page 7
Hauptansicht EGL 90-PN
![img-10.jpeg](img-10.jpeg)

Die Zeichnung zeigt den Greifer in der Grundausführung mit geschlossenen Backen ohne maßliche Berücksichtigung der nachstehend beschriebenen Optionen.
(1) Greiferanschluss
(2) Fingeranschluss
(72) Passung für Zentrierhülse
(80) Tiefe der Zentrierhülsenbohrung im Gegenstück
(90) Servicefenster
(91) M12-Stecker, T-kodiert (Spannungsversorgung)
(92) M12-Buchse PROFINET

### Page 8
 EGL 90 

Universalgreifer

Hauptansicht EOA-UR3510-EGL 90
![img-11.jpeg](img-11.jpeg)

Die Zeichnung zeigt den Greifer in der Grundausführung mit geöffneten Backen ohne maßliche Berücksichtigung der nachstehend beschriebenen Optionen.
(1) Greiferanschluss
(2) Fingeranschluss
(72) Passung für Zentrierhülse
(73) Passung für Zentrierstift
(78) Passung für Zentrierung
80 Tiefe der Zentrierhülsen-
bohrung im Gegenstück
(9) Servicefenster
(91) MI2-Stecker, T-kodiert (Spannungsversorgung)
92 MI2-Buchse PROFINET
93 Lochkreis DIN ISO-9409
94 Durchgangslochbohrung zur Anschraubung</chunk>

---

<chunk_context>This section provides detailed visual representations and technical specifications for the EGL 90 Universalgripper, specifically focusing on the model EOA-UR3510-EGL 90-AUB with attachment jaws. It includes critical information about the maximum allowable overhang and a diagram illustrating the throttling characteristics, which indicates the maximum permissible motor current relative to ambient temperature. Additionally, it highlights the PROFIBUS variant's connection details, emphasizing the integration of communication standards essential for industrial automation. This information is crucial for users seeking to understand the operational limits and connectivity options of the gripper within automated systems.</chunk_context>
<chunk>### Page 9
 Hauptansicht EOA-UR3510-EGL 90-AUB mit Aufsatzbacken 

![img-12.jpeg](img-12.jpeg)

### Page 10
 EGL 90 

Universalgreifer

Maximal zulässige Auskragung
![img-13.jpeg](img-13.jpeg)

Drosselung
![img-14.jpeg](img-14.jpeg)

Das Diagramm Drosselung zeigt den maximal zulässigen Motorstrom in Abhängigkeit von der Umgebungstemperatur.
![img-15.jpeg](img-15.jpeg)

Unzulässiger Bereich

Variante PROFIBUS
![img-16.jpeg](img-16.jpeg)

92 M12-Buchse PROFIBUS
93 M12-Stecker PROFIBUS
Abweichendes Anschlussbild bei Variante PROFIBUS</chunk>

---

<chunk_context>The section focuses on the Zwischenbacke ZBA-EGL 90 and the finger blanks ABR-/SBR-PGZN-plus 80, which are essential components for customizing the gripping functionality of the Universalgreifer EGL. It highlights the materials used—aluminum and steel—and provides identification numbers for these components, emphasizing their role in enhancing the versatility of the gripper. This information is part of a broader discussion on the modularity and customization options available for the EGL series, which is designed for flexible handling in various industrial applications.</chunk_context>
<chunk>### Page 11
## Zwischenbacke ZBA-EGL 90

![img-17.jpeg](img-17.jpeg)

## Fingerrohlinge ABR-/SBR-PGZN-plus 80

![img-18.jpeg](img-18.jpeg)

Die Zeichnung zeigt den Fingerrohling zur kundenspezifischen Nachbearbeitung.

| Bezeichnung | Ident.-Nr. | Material | Lieferumfang |
| :-- | :-- | :-- | :-- |
| Fingerrohling |  |  |  |
| ABR-PGZN-plus 80 | 0300011 | Aluminium (3.4365) | 1 |
| SBR-PGZN-plus 80 | 0300021 | Stahl (1.7131) | 1 |

(1) Greiferanschluss
(2) Fingeranschluss
(3) Passung für Zentrierhülse
(4) ABR-PGZN-plus

Die Zeichnung zuigt den Fingerrohling zur kundenspezifischen Nachbearbeitung.

| Bezeichnung | Ident.-Nr. | Material | Lieferumfang |
| :-- | :-- | :-- | :-- |
| Fingerrohling |  |  |  |
| ABR-PGZN-plus 80 | 0300011 | Aluminium (3.4365) | 1 |
| SBR-PGZN-plus 80 | 0300021 | Stahl (1.7131) | 1 |

(1) Bei der Verwendung von Fingerrohlingen kann es bei einzelnen Greiferbaureihen zu einer Begrenzung des Schließhubs kommen. Bitte prüfen Sie dies im Vorfeld detailliert mithilfe der CAD-Daten und passen Sie die Nachbearbeitung der Finger entsprechend an.

 Anschlusskabel Spannungsversorgung 

![img-19.jpeg](img-19.jpeg)

Die Anschlusskabel dienen dem Anschluss des SCHUNK-Produktes an die Spannungsversorgung.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel Spannungsversorgung - schleppkettentauglich |  |  |  |  |  |  |  |
| KA GLN12T0150-LK-00500-A | 0310262 | 5 | 9.6 | 51 | 15 |  | M12 T-kodiert |
| KA GLN12T0150-LK-01000-A | 0310264 | 10 | 9.6 | 51 | 15 |  | M12 T-kodiert |
| KA WLN12T0150-LK-00500-A | 0310263 | 5 | 9.6 | 47.5 |  | 35 | M12 T-kodiert |
| KA WLN12T0150-LK-01000-A | 0310265 | 10 | 9.6 | 47.5 |  | 35 | M12 T-kodiert |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10 fache des Kabeldurchmessers oder +/- $180^{\circ} / \mathrm{m}$. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.</chunk>

---

<chunk_context>The section on Page 12 details the specifications and options for PROFIBUS communication cables designed for SCHUNK's mechatronic products, emphasizing their compatibility with M12 connectors. It highlights various cable lengths and types, including those suitable for drag chains and torsion applications, which are critical for ensuring reliable data transmission in automated systems. This information supports the document's overall focus on providing comprehensive technical details for integrating SCHUNK's automation solutions, enhancing functionality and connectivity in industrial environments.</chunk_context>
<chunk>### Page 12
 KOL 90 

## Kommunikationskabel PROFIBUS

![img-20.jpeg](img-20.jpeg)

Die Kommunikationskabel sind passend konfektioniert für die mechatronischen SCHUNK-Produkte. Sie verfügen beidseitig über M12-Steckverbinder.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | D3 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | $[\mathrm{m}]$ | $[\mathrm{mm}]$ | $[\mathrm{mm}]$ | $[\mathrm{mm}]$ |  |
| Kommunikationskabel PROFIBUS - schleppkettentauglich |  |  |  |  |  |  |
| KA GGN1204-P8-00150-A | 0349750 | 1.5 | 8 | 47 | 15 | M12 |
| KA GGN1204-P8-00300-A | 0349751 | 3 | 8 | 47 | 15 | M12 |
| KA GGN1204-P8-00500-A | 0349752 | 5 | 8 | 47 | 15 | M12 |
| KA GGN1204-P8-01000-A | 0349753 | 10 | 8 | 47 | 15 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.

## Anschlusssteckverbinder Spannungsversorgung

![img-21.jpeg](img-21.jpeg)

Die Steckverbinder dienen dem Anschluss der SCHUNK Produkte an die Spannungsversorgung. Hierbei kann ein kundenseitiges Kabel verwendet werden. Die Einzellitzen werden mittels Schraubverbindung im Steckverbinder geklemmt.

| Bezeichnung | Ident.-Nr. | D1 [max.] | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusssteckverbinder Spannungsversorgung |  |  |  |  |  |  |
| KBU-M12T-G 4P | 0310260 | 10 | 58 | 20.2 |  | M12 T-kodiert |
| KBU-M12T-W 4P | 1001514 | 10 | 43 | 20.2 | 39 | M12 T-kodiert |

(1) Für das Anschlusskabel wird ein Querschnitt je Einzellitze von min. 1,5 mm2 empfohlen. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.

### Page 13
 Anschlusskabel Kommunikation PROFINET, EtherNet/IP und EtherCAT 

![img-22.jpeg](img-22.jpeg)

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  | Anschluss modulseitig |  |  |
| KA G... | Gerader Steckverbinder |  |  |  |  | 90 Kabelende mit zweitem |
| KA W... | Gewinkelter Steckverbinder |  |  |  |  | Steckverbinder |

Die Kommunikationskabel sind für die mechatronischen Produkte von SCHUNK passend konfektioniert und können für die Kommunikationsschnittstelle PROFINET, EtherNET/IP und EtherCAT verwendet werden. Sie verfügen modulseitig immer über einen M12-Steckverbinder (D-kodiert, Stecker). Die Steckverbinder sind modulseitig gerade (KA G...) oder gewinkelt (KA W...) ausgeführt. Auf der zweiten Seite verfügen die Kabel entweder über einen geraden M12-Steckverbinder (D-kodiert, Stecker) oder einen R/45-Steckverbinder.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-12D04-ET-00500-A | 1505114 | 5 | 6.5 | 47.3 | 14.8 |  | M12 |
| KA GGN12D04-12D04-ET-01000-A | 1505119 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gerade - auf R/45 Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-R/45-ET-00200-A | 1511256 | 2 | 6.5 | 47.3 | 14.8 |  | M12 |
| KA GGN12D04-R/45-ET-00500-A | 1354681 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KA GGN12D04-R/45-ET-01000-A | 1505143 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gewinkelt - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KA WGN12D04-12D04-ET-00500-A | 1354661 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KA WGN12D04-12D04-ET-01000-A | 1505141 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gewinkelt - auf R/45 Stecker, gerade |  |  |  |  |  |  |  |
| KA WGN12D04-R/45-ET-00500-A | 1354688 | 5 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| KA WGN12D04-R/45-ET-01000-A | 1505142 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR GGN12D04-12D04-ET-00500-A | 1505146 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR GGN12D04-12D04-ET-01000-A | 1505147 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gerade - auf R/45 Stecker, gerade |  |  |  |  |  |  |  |
| KAR GGN12D04-R/45-ET-00500-A | 1354677 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR GGN12D04-R/45-ET-01000-A | 1505160 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gewinkelt - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR WGN12D04-12D04-ET-00500-A | 1354674 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR WGN12D04-12D04-ET-01000-A | 1505148 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gewinkelt - auf R/45 Stecker, gerade |  |  |  |  |  |  |  |
| KAR WGN12D04-R/45-ET-00500-A | 1354692 | 5 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| KAR WGN12D04-R/45-ET-01000-A | 1505149 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.</chunk>

---

<chunk_context>The section on Page 14 focuses on the termination of the bus line for the EGL 90 Universalgripper, specifically detailing the use of termination resistors necessary for proper communication within a PROFIBUS network. This information is crucial for ensuring reliable data transmission and system integrity in automated environments, aligning with the document's emphasis on the integration and functionality of SCHUNK's automation technology. The mention of the specific part number (ST5G1204-PB-A-A) and dimensions (47 mm, 15 mm) provides essential technical details for users implementing the system.</chunk_context>
<chunk>### Page 14
 EGL 90 

Universalgreifer

## Abschlusswiderstand

![img-23.jpeg](img-23.jpeg)
(6) Anschluss modulseitig
(15) Buchse

Die Abschlusswiderstände dienen zur Terminierung des Bus-Strangs direkt am SCHUNK-Modul.

| Bezeichnung | Ident.-Nr. | L2 | D2 | D3 |
| :-- | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] |  |
| Abschlusswiderstand - PROFIBUS |  |  |  |  |
| ST5G1204-PB-A-A | 0349650 | 47 | 15 | M12 |

(1) Am letzten Modul im PROFIBUS-strang muss ein entsprechender Abschlusswiderstand angebracht werden.

### Page 15
 EGL 90 

Universalgreifer

### Page 16
 SCHUNK 

SCHUNK SE \& Co. KG
Spanntechnik
Greiftechnik
Automatisierungstechnik
Bahnhofstr. 106 - 134
D-74348 Lauffen/Neckar
Tel. +49-7133-103-0
Fax +49-7133-103-2399
info@de.schunk.com
schunk.com

Folgen Sie uns | Follow us
(1) 2 (2) $x$ (1)</chunk>