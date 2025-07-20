# Chunking Prompt

**Source File:** SCHUNK_EZU_MISTRAL  
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
![img-0.jpeg](img-0.jpeg)
<|end_chunk_0|><|start_chunk_1|>
 **Produktdatenblatt**

Zentrischgreifer EZU

![img-1.jpeg](img-1.jpeg)
<|end_chunk_1|><|start_chunk_2|>
### Page 2<|end_chunk_2|><|start_chunk_3|>
 Robust. Flexibel. Intelligent. 

Vielseitig einsetzbarer 3-Finger-Zentrischgreifer ermöglicht das Greifen und Zentrieren exzentrisch positionierter Werkstücke mit konstant hoher Greifkraft.
<|end_chunk_3|><|start_chunk_4|>
## Einsatzgebiet

Flexibles Be- und Entladen von Werkzeugmaschinen mit zylindrischen Werkstücken sowie Handhabung von Wellen und Zahnrädern im Produktions- und Montageprozess von Antriebssträngen in der Automobilfertigung. Durch die abgedichtete Bauweise ist der Greifer besonders geeignet für den Einsatz in rauen Umgebungen mit Verschmutzungen durch Späne oder Kühlschmierstoff.
<|end_chunk_4|><|start_chunk_5|>
## Vorteile - Ihr Nutzen

Flexibles Werkstückhandling Durch den umfangreich einstellbaren, frei programmierbaren Backenhub lassen sich zylindrische Werkstücke unterschiedlicher Größen effizient handhaben
Hohe Fehlertoleranz Der Antriebsstrang sichert auch bei horizontalen Positionierungsfehlern von Werkstück oder Roboter eine zuverlässige Zentrierung des Werkstücks und eine konstant hohe Greifkraft
Gesteigerte Effizienz Zum Greifen ist kein Anfahrweg erforderlich, wodurch die Handhabung vereinfacht und der Gesamtprozess beschleunigt wird
Hohe Robustheit Die abgedichtete Bauweise mit der bewährten Gleitführung macht den Greifer widerstandsfähig gegen raue Einsatzbedingungen
Besonders zuverlässig Dank der integrierten Greifkrafterhaltung mit Verlusterkennung wird das Risiko eines Werkstückverlustes minimiert
Hohe Verfügbarkeit Der integrierte Absolutwertgeber sichert eine dauerhafte Referenzierung, auch bei Not-Aus oder Stromausfall
Einfache Integration Dank vielfältiger Kommunikationsschnittstellen, SPS-Funktionsbausteinen und RoboterPlugins, kompatibel mit führenden Herstellern, wird der Integrationsaufwand deutlich reduziert
![img-2.jpeg](img-2.jpeg)
<|end_chunk_5|><|start_chunk_6|>
### Page 3<|end_chunk_6|><|start_chunk_7|>
 Funktionsbeschreibung 

Der bürstenlose DC-Servomotor treibt über ein Stirnradgetriebe mit Ritzel-Zahnstangen-Prinzip die drei in den gleitgeführten Grundbacken integrierten Zahnstangen an. Durch das Stirnradgetriebe wird die Greifkraft verlässlich erzeugt und bleibt auch bei horizontalen Positionierungsfehlern von Werkstück oder Roboter konstant, was eine zuverlässige Zentrierung des Werkstücks sowie eine hohe Fehlertoleranz sicherstellt. Die Greifkraft wird ohne Mindestanfahrweg erzeugt, was die Handhabung verein-
facht und den Prozess beschleunigt.
Ein integrierter Absolutwertgeber stellt auch nach einem Not-Aus oder Stromausfall die sofortige Einsatzbereitschaft des Greifers sicher. Die Greifkrafterhaltung, welche in Kombination aus Permanentmagnetbremse und einem Dämpfungselement im Antriebsstrang realisiert wird, verringert das Risiko eines Werkstückverlustes, welcher durch die integrierte Werkstückverlusterkennung erkannt wird.
![img-3.jpeg](img-3.jpeg)
(1) Belastbare und widerstandsfähige T-Nuten-Gleitführung für große Fingerlängen, externe Kräfte und Momente. Optional als Staubdicht-Version verfügbar.
(2) Vollintegrierte und abgedichtete Regelungs- und Leistungselektronik
mit Status LED's und M12-Steckverbindern zum Anschluss von Spannungsversorgung und Kommunikation.
(3) Hochauflösender, abtriebsseitiger Absolutwertgeber zur genauen Positionierung der Greiferbacken mit dauerhaft absoluter Positionsrückmeldung.
(4) Abgedichteter Antriebsstrang mit Stirnradgetriebe und Ritzel-Zahnstangenprinzip
ermöglicht eine verlässliche Erzeugung der Greifkraft, ohne Mindestanfahrweg.
(5) Bürstenloser Flachmotor
für begrenzte Platzverhältnisse und hohe Drehmomente dank außen liegendem Rotor.
(6) Elektromagnetische Bremse
mit zusätzlichem Mechanismus zur Greifkraft- und Positionserhaltung bei Stillstand oder Spannungsausfall.
<|end_chunk_7|><|start_chunk_8|>
### Page 4<|end_chunk_8|><|start_chunk_9|>
 Detaillierte Funktionsbeschreibung 
<|end_chunk_9|><|start_chunk_10|>
## Erhöhte Schutzart mit Staubdicht-Version SD

![img-4.jpeg](img-4.jpeg)

Die Staubdicht-Version erhöht den Schutzgrad der Führung und Grundbacken gegen das Eindringen von Staub und Flüssigkeiten. In Kombination mit der abgedichteten Elektronik (IP67) eignet sich die Staubdicht-Version so für den Einsatz in besonders rauen Umgebungsbedingungen, wie zum Beispiel zum Beladen einer Schleifmaschine. Der erreichte Schutz der Führung entspricht der Schutzart IP64 und ist damit absolut staubdicht und gegen Spritzwasser aus allen Richtungen geschützt. Weitere Informationen finden Sie in der Betriebsanleitung.
<|end_chunk_10|><|start_chunk_11|>
## Befestigungsmöglichkeit für Zusatzanbau

![img-5.jpeg](img-5.jpeg)

Im Führungsgehäuse befinden sich zusätzliche Gewinde und Passungen zur Befestigung einer applikationsspezifischen Konstruktion um zusätzliche Funktionen zu realisieren. So kann zum Beispiel ein federndes Andrückelement, zum federgestützten Positionieren des Werkstückes gegen einen Anschlag, montiert werden.
<|end_chunk_11|><|start_chunk_12|>
## Konnektivität

![img-6.jpeg](img-6.jpeg)

Ein breites Angebot an verfügbaren Kommunikationsschnittstellen vereinfacht den Umgang mit der Vielfalt an Steuerungs- und Roboterherstellern und sorgt für Zeitersparnis bei der Integration. Industrial Ethernet (PROFINET, EtherCAT, EtherNet/IP) ermöglicht die direkte Integration ohne zusätzliche Gateways in die Steuerungsumgebung führender SPS Hersteller am Markt. Mit der seriellen Schnittstelle Modbus RTU kann der Greifer ohne externe Kabelführung an den Werkzeugflansch führender Roboterhersteller angebunden werden. IO-Link ist unabhängig und bietet Flexibilität bei der Anbindung an weitere Netzwerke.
<|end_chunk_12|><|start_chunk_13|>
## Greifmodi

![img-7.jpeg](img-7.jpeg)

Es stehen die Greifmodi BasicGrip und StrongGrip zur Verfügung.BasicGrip: Greifgeschwindigkeit wird automatisch zur gewählten Greifkrafteinstellung optimiert, permanentes Nachgreifen ist möglichStrongGrip: maximale Greifkraft wird erzeugt und anschließend durch die Greifkrafterhaltung gesichert, permanentes Nachgreifen ist innerhalb eines einstellbaren Zeitfensters möglich, Pausenzeiten zwischen Greifzyklen müssen berücksichtigt werden
<|end_chunk_13|><|start_chunk_14|>
### Page 5
Software Service - Roboterintegration
![img-8.jpeg](img-8.jpeg)

Für ein nahtloses Zusammenspiel zwischen Greifer und Roboter stehen Softwarebausteine für die Integration in die Robotersteuerung führender Hersteller zur Verfügung. Dadurch ist der Funktionsumfang des Greifers ohne zusätzlichen Programmieraufwand nutzbar und es kann direkt damit begonnen werden die Applikation zu programmieren. Roboterkompatibilität: Universal Robots e-Series über Modbus RTU, FANUC CRX über Modbus RTU, ABB OmniCore C30 über EtherNet/ IP, Yaskawa YRC1000micro über EtherNet/IP, Kassow Robots über Modbus RTU. Software und weitere Kompatibilitätshinweise können unter schunk.com/ downloads-software heruntergeladen werden.

Software Service - SPS Integration
![img-9.jpeg](img-9.jpeg)

Für ein nahtloses Zusammenspiel zwischen Greifer und SPS-Steuerung stehen Funktionsbausteine für die Programmieroberfläche führender Hersteller zur Verfügung. Dadurch ist der Funktionsumfang des Greifers ohne zusätzlichen Programmieraufwand nutzbar und es kann direkt damit begonnen werden die Applikation zu programmieren. SPS-Kompatibilität: Siemens TIA Portal (PROFINET und IO-Link), Beckhoff TwinCAT (EtherCAT und IO-Link), Allen Bradley Studio 5000 Logix Designer (EtherNet/IP und IO-Link), Bosch Rexroth ctrlX (EtherCAT, nur mit Bosch Nexeed Automation).Software und weitere Kompatibilitätshinweise können unter schunk.com/downloads-software heruntergeladen werden.

Inbetriebnahme App im SCHUNK Control Center
![img-10.jpeg](img-10.jpeg)

Die App Mechatronische Greifer vereinfacht die Inbetriebnahme, den Betrieb sowie Diagnose und Service durch einen umfangreichen Funktionskatalog. Nutzer können den Greifer direkt steuern und eine Applikationsvalidierung durchführen ohne Erfordernis einer SPS. Zu den Funktionen gehören Netzwerkkonfiguration, Firmwareupdates, Parameteranpassungen und -sicherungen sowie umfassende Diagnosemöglichkeiten. Die App ist kompatibel mit Windows und kann unter schunk.com/downloads-software heruntergeladen werden.
<|end_chunk_14|><|start_chunk_15|>
### Page 6<|end_chunk_15|><|start_chunk_16|>
 Allgemeine Informationen zur Baureihe 

Gehäusematerial: Aluminiumlegierung, eloxiert
Grundbackenmaterial: Stahl, korrosionsgeschützt
Gewährleistung: 24 Monate oder 5 Mio. Zyklen BasicGrip/ 3 Mio. Zyklen StrongGrip (1 Zyklus besteht aus einem kompletten Greifvorgang: „Greifer öffnen" und „Greifer schließen")
Lieferumfang: Greifer inklusive Sicherheitsinformationen und Beipack mit Zentrierhülsen für Greifermontage und Fingermontage. Produktspezifische Anleitungen und Software können unter schunk.com/downloads-manuals und schunk.com/downloadssoftware heruntergeladen werden.
Greifkraft: ist die arithmetische Summe der an jeder Backe wirkenden Einzelkraft, im Abstand P (siehe Zeichnung)
Wiederholgenauigkeit (Greifen): ist definiert als die Streuung der Ist-Position pro Backe bei 100 aufeinander folgenden Schließbzw. Öffnungsbewegungen auf ein starres Werkstück oder einen Festanschlag unter gleichbleibenden Bedingungen.

Wiederholgenauigkeit (Positionieren, unidirektional): ist definiert als die Streuung der Ist-Position pro Backe bei 100 aufeinander folgenden Bewegungen auf eine Soll-Position aus gleicher Richtung unter gleichbleibenden Bedingungen.
Wiederholgenauigkeit (Positionieren, bidirektional): ist definiert als die Streuung der Ist-Position pro Backe bei 100 aufeinanderfolgenden Bewegungen auf eine Soll-Position aus beiden Richtungen unter gleichbleibenden Bedingungen.
Fingerlänge: wird ab derselben Bezugsfläche wie der Abstand P in Richtung der Hauptachse gemessen.
Schließ- und Öffnungszeiten (Positionieren): Schließ- und Öffnungszeiten sind reine Bewegungszeiten der Finger bei max. Geschwindigkeit, max. Beschleunigung unter Beachtung der max. zulässigen Massen pro Finger und beziehen sich auf 50\% des verfügbaren Hubs pro Backe in der Basisvariante.
Max. Geschwindigkeit (Positionieren) und max. Beschleunigung: ist die an jeder Backe wirkende Geschwindigkeit und Beschleunigung.
![img-11.jpeg](img-11.jpeg)
<|end_chunk_16|><|start_chunk_17|>
## Anwendungsbeispiel

Flexibles, taktzeitoptimiertes Be- und Entladen einer Werkzeugmaschine. Durch den Einsatz von zwei Greifern am Roboter kann die automatisierte Beladung der Werkzeugmaschine taktzeitoptimierend erfolgen und dadurch die Produktivität gesteigert werden. Fertigteil und Rohteil können in einem Beladezyklus transportiert werden. Durch den großen und frei programmierbaren Backenhub des Greifers können unterschiedliche Durchmesser gegriffen werden, ohne dass der Greifer dabei ausgewechselt werden muss.

Doppelgreifer EZU für Roh- und Fertigteilhandling
(2) Werkzeugmaschine mit Kraftspannfutter ROTA THW3
<|end_chunk_17|><|start_chunk_18|>
### Page 7<|end_chunk_18|><|start_chunk_19|>
 SCHUNK bietet mehr ... 

Die folgenden Komponenten machen das Produkt noch produktiver - die passende Ergänzung für höchste Funktionalität, Flexibilität, Zuverlässigkeit und Prozesssicherheit.
![img-12.jpeg](img-12.jpeg)

Q Weitergehende Informationen zu diesen Produkten finden Sie auf den folgenden Produktseiten oder unter schunk.com.
<|end_chunk_19|><|start_chunk_20|>
## Optionen und spezielle Informationen

Greifmodi: Es stehen die Greifmodi BasicGrip und StrongGrip zur Verfügung. Mit BasicGrip ist ein Dauerbetrieb des Motors und damit ein permanentes Nachgreifen des Werkstücks möglich. Die Greifgeschwindigkeit wird automatisch zur Greifkrafteinstellung optimiert. Mit StrongGrip wird die maximale Greifkraft erzeugt und anschließend durch die Greifkrafterhaltung gespeichert. Permanentes Nachgreifen ist innerhalb eines einstellbaren Zeitfensters möglich. Zusätzlich müssen im StrongGrip Modus definierte Pausenzeiten und maximale Umgebungstemperaturen berücksichtigt werden. Weitere Details können der Betriebsanleitung entnommen werden.
Greifkrafterhaltung: Durch eine Kombination aus elektrischer Haltebremse und der Vorspannung eines elastischen Elements kann bei einer Not-Aus-Situation oder einem Spannungsabfall eine Greifkraft von über $80 \%$ der ursprünglich aufgebrachten Greifkraft zuverlässig erhalten werden. Wird die Greifkraft- und Positionserhaltung präventiv aktiviert, so können 100\% der ursprünglich aufgebrachten Greifkraft erhalten werden. Der Nachlaufweg der Greiferfinger beim Entfernen des Werkstücks beträgt wenige Millimeter und ist abhängig von der erzeugten Greifkraft. Optional sind auch Varianten ohne Greifkrafterhaltung verfügbar.
Abdichtung: Der Greifer verfügt standardmäßig über einen erhöhten Schutz gegen das Eindringen von Stäuben oder Flüssigkeiten. Der IP-Schutz der Elektronik ist nur dann gegeben, wenn die Steckverbinder ordnungsgemäß montiert wurden. Das Getriebe des Greifers ist zusätzlich durch eine Abdichtung an den Abtriebsritzeln geschützt.
Schnittstelle der Grundbacken: Bei Verwendung der Zwischenbacke entspricht die Schnittstelle der Grundbacken der des Universalgreifers PZN-plus. Somit kann das umfangreiche Fingerzubehör des PZN-plus unter Berücksichtigung der Störkonturen und der geltenden Einsatzgrenzen für diesen Greifer genutzt werden.
<|end_chunk_20|><|start_chunk_21|>
### Page 8<|end_chunk_21|><|start_chunk_22|>
 EZU 

Zentrischgreifer
<|end_chunk_22|><|start_chunk_23|>
## Bestellbeispiel

![img-13.jpeg](img-13.jpeg)

Greifkrafterhaltung
$M=$ mit Greifkrafterhaltung
$N=$ ohne Greifkrafterhaltung
<|end_chunk_23|><|start_chunk_24|>
## Version

$B=$ Basisversion
$S D=$ Staubdicht-Version
<|end_chunk_24|><|start_chunk_25|>
### Page 9
EZU
Zentrischgreifer
<|end_chunk_25|><|start_chunk_26|>
### Page 10
![img-14.jpeg](img-14.jpeg)

Version mit Greifkrafterhaltung

| Greifkraft |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | $\begin{aligned} & -E Z U 30-30 \% \\ & -E Z U 30-100 \% \end{aligned}$ | $\begin{aligned} & -E Z U 30-150 \% \\ & -E Z U 30-200 \% \end{aligned}$ | $\square$ ResizGrip StrangGrip |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

(1) Die angegebenen Momente und Kräfte sind statische Werte, gelten je Grundbacke und dürfen gleichzeitig auftreten.
<|end_chunk_26|><|start_chunk_27|>
 Technische Daten EZU mit Greifkrafterhaltung 

| Bezeichnung |  | EZU 30-PN-M-B | EZU 30-EI-M-B | EZU 30-EC-M-B | EZU 30-IL-M-B | EZU 30-MB-M-B |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Ident.-Nr. |  | 1581935 | 1581970 | 1581972 | 1581976 | 1581979 |
| Allgemeine Betriebsdaten |  |  |  |  |  |  |
| Hub pro Backe | [mm] | 30 | 30 | 30 | 30 | 30 |
| Min./max. Greifkraft | [N] | 175/700 | 175/700 | 175/700 | 175/700 | 175/700 |
| Min./max. Greifkrafterhaltung | $[\%]$ | 90/100 | 90/100 | 90/100 | 90/100 | 90/100 |
| Max. zulässige Fingerlänge | [mm] | 80 | 80 | 80 | 80 | 80 |
| Max. zulässige Masse pro Finger | [kg] | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 |
| Wiederholgenauigkeit (Greifen) | [mm] | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |
| Wiederholgenauigkeit (Positionieren, unidirektional) | [mm] | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |
| Wiederholgenauigkeit (Positionieren, bidirektional) | [mm] | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 |
| Schließ-/Öffnungszeit (Positionieren, 50\% Hub) | [s] | 0.6/0.6 | 0.6/0.6 | 0.6/0.6 | 0.6/0.6 | 0.6/0.6 |
| Max. Geschwindigkeit (Positionieren) | [mm/s] | 40 | 40 | 40 | 40 | 40 |
| Max. Beschleunigung | [mm/s $\left.{ }^{2}\right]$ | 250 | 250 | 250 | 250 | 250 |
| Eigenmasse | [kg] | 2.3 | 2.3 | 2.3 | 2.3 | 2.3 |
| Min./max. Umgebungstemperatur | ${ }^{\circ} \mathrm{C}$ ] | 5/55 | 5/55 | 5/55 | 5/55 | 5/55 |
| Schutzart IP Elektronik |  | 67 | 67 | 67 | 67 | 67 |
| Schutzart IP Führung/Grundbacken |  | 40 | 40 | 40 | 40 | 40 |
| Reinraumklasse ISO 14644-1:2015 |  | 5 | 5 | 5 | 5 | 5 |
| Elektrische Betriebsdaten |  |  |  |  |  |  |
| Nennspannung | [V] | 24 | 24 | 24 | 24 | 24 |
| Kommunikationsschnittstelle |  | PROFINET | EtherNet/IP | EtherCAT | IO-Link | Modbus RTU |
| Stromaufnahme BasicGrip Nenn./Max. | [A] | 0.28/0.96 | 0.28/0.96 | 0.28/0.96 | 0.28/0.96 | 0.28/0.96 |
| Stromaufnahme StrongGrip Nenn./Max. | [A] | 0.7/1.2 | 0.7/1.2 | 0.7/1.2 | 0.7/1.2 | 0.7/1.2 |
| Stromaufnahme Logik Nenn./Max. | [A] | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 |
| Optionen und deren Eigenschaften |  |  |  |  |  |  |
| Staubdicht-Version |  | 1582002 | 1582004 | 1582020 | 1582029 | 1582033 |
| Schutzart IP Führung/Grundbacken |  | 64 | 64 | 64 | 64 | 64 |
| Hub pro Backe | [mm] | 20 | 20 | 20 | 20 | 20 |
| Min./max. Greifkraft | [N] | 210/700 | 210/700 | 210/700 | 210/700 | 210/700 |
| Eigenmasse | [kg] | 2.35 | 2.35 | 2.35 | 2.35 | 2.35 |
| Reinraumklasse ISO 14644-1:2015 |  | 4 | 4 | 4 | 4 | 4 |
<|end_chunk_27|><|start_chunk_28|>
### Page 11<|end_chunk_28|><|start_chunk_29|>
 Technische Daten EZU ohne Greifkrafterhaltung

|  Bezeichnung |  | EZU 30-PN-N-B | EZU 30-EI-N-B | EZU 30-EC-N-B | EZU 30-IL-N-B | EZU 30-MB-N-B  |
| --- | --- | --- | --- | --- | --- | --- |
|  Ident.-Nr. |  | 1581956 | 1581971 | 1581974 | 1581978 | 1582001  |
|  Allgemeine Betriebsdaten |  |  |  |  |  |   |
|  Hub pro Backe | [mm] | 30 | 30 | 30 | 30 | 30  |
|  Min./max. Greifkraft | [N] | 175/350 | 175/350 | 175/350 | 175/350 | 175/350  |
|  Max. zulässige Fingerlänge | [mm] | 80 | 80 | 80 | 80 | 80  |
|  Max. zulässige Masse pro Finger | [kg] | 0.4 | 0.4 | 0.4 | 0.4 | 0.4  |
|  Wiederholgenauigkeit (Greifen) | [mm] | 0.02 | 0.02 | 0.02 | 0.02 | 0.02  |
|  Wiederholgenauigkeit (Positionieren, unidirektional) | [mm] | 0.05 | 0.05 | 0.05 | 0.05 | 0.05  |
|  Wiederholgenauigkeit (Positionieren, bidirektional) | [mm] | 0.15 | 0.15 | 0.15 | 0.15 | 0.15  |
|  Schließ-/Öffnungszeit (Positionieren, 50\% Hub) | [s] | 0.6/0.6 | 0.6/0.6 | 0.6/0.6 | 0.6/0.6 | 0.6/0.6  |
|  Max. Geschwindigkeit (Positionieren) | [mm/s] | 40 | 40 | 40 | 40 | 40  |
|  Max. Beschleunigung | [mm/s²] | 150 | 150 | 150 | 150 | 150  |
|  Eigenmasse | [kg] | 2.25 | 2.25 | 2.25 | 2.25 | 2.25  |
|  Min./max. Umgebungstemperatur | [ ${ }^{\circ} \mathrm{C}$ ] | 5/55 | 5/55 | 5/55 | 5/55 | 5/55  |
|  Schutzart IP Elektronik |  | 67 | 67 | 67 | 67 | 67  |
|  Schutzart IP Führung/Grundbacken |  | 40 | 40 | 40 | 40 | 40  |
|  Reinraumklasse ISO 14644-1:2015 |  | 5 | 5 | 5 | 5 | 5  |
|  Elektrische Betriebsdaten |  |  |  |  |  |   |
|  Nennspannung | [V] | 24 | 24 | 24 | 24 | 24  |
|  Kommunikationsschnittstelle |  | PROFINET | EtherNet/IP | EtherCAT | IO-Link | Modbus RTU  |
|  Stromaufnahme BasicGrip Nenn./Max. | [A] | 0.14/0.67 | 0.14/0.67 | 0.14/0.67 | 0.14/0.67 | 0.14/0.67  |
|  Stromaufnahme Logik Nenn./Max. | [A] | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2  |
|  Optionen und deren Eigenschaften |  |  |  |  |  |   |
|  Staubdicht-Version |  | 1582003 | 1582007 | 1582025 | 1582031 | 1582037  |
|  Schutzart IP Führung/Grundbacken |  | 64 | 64 | 64 | 64 | 64  |
|  Hub pro Backe | [mm] | 20 | 20 | 20 | 20 | 20  |
|  Min./max. Greifkraft | [N] | 210/350 | 210/350 | 210/350 | 210/350 | 210/350  |
|  Eigenmasse | [kg] | 2.3 | 2.3 | 2.3 | 2.3 | 2.3  |
|  Reinraumklasse ISO 14644-1:2015 |  | 4 | 4 | 4 | 4 | 4  |
<|end_chunk_29|><|start_chunk_30|>
### Page 12<|end_chunk_30|><|start_chunk_31|>
 Hauptansicht 

![img-15.jpeg](img-15.jpeg)

Die Zeichnung zeigt den Greifer in der Ausführung PROFINET, EtherNet/IP oder EtherCAT, mit und ohne Greifkrafterhaltung mit geöffneten Backen. Die Mindestanzahl der Befestigungsschrauben für die Montage der Greiferfinger ist der Betriebsanleitung des Produkts zu entnehmen.
(1) Greiferanschluss
(2) Fingeranschluss

72 Passung für Zentrierhülse
80 Tiefe der Zentrierhülsen-
bohrung im Gegenstück
90 Spannungsversorgung (M12, Stecker, 4 Pin, L-kodiert)
(91) Kommunikation (M12, Buchse, 4 Pin, D-kodiert)
92 Anschraubung mit Passungen für Zusatzanbau (diese Zentrierhülsen sind nicht im Lieferumfang enthalten)
93 Anschluss Funktionserde
<|end_chunk_31|><|start_chunk_32|>
### Page 13<|end_chunk_32|><|start_chunk_33|>
## Version IO-Link und Modbus RTU

![img-16.jpeg](img-16.jpeg)

Spannungsversorgung und Kommunikation (M12, Stecker, A-kodiert, IL: 5 Pin, MB: 4 Pin)

Die Zeichnung zeigt die Maßänderungen der Versionen IO-Link und Modbus RTU im Vergleich zu der in der Hauptansicht dargestellten Grundausführung.

Gewinkelte Steckverbinder Ausführung IO-Link und Modbus RTU
![img-17.jpeg](img-17.jpeg)

Die Zeichnung zeigt die Richtung des Kabelabgangs bei der Verwendung von gewinkelten Steckverbindern. Der Abstand vom Steckverbinder zum Gehäuse des Greifers kann je nach verwendetem Kabelhersteller variieren.

Gewinkelte Steckverbinder Ausführung PROFINET, EtherNet/IP und EtherCAT
![img-18.jpeg](img-18.jpeg)

Die Zeichnung zeigt die Richtung des Kabelabgangs bei der Verwendung von gewinkelten Steckverbindern. Der Abstand vom Steckverbinder zum Gehäuse des Greifers kann je nach verwendetem Kabelhersteller variieren.
<|end_chunk_33|><|start_chunk_34|>
## Staubdicht-Version

![img-19.jpeg](img-19.jpeg)

Anschraubbild siehe Grundversion

Die Option „Staubdicht" erhöht den Schutzgrad gegen eindringende Stoffe. Das Anschraubbild verschiebt sich um die Höhe der Zwischenbacke. Die Fingerlänge ist weiter ab Oberkante des Greifergehäuses zu messen.
<|end_chunk_34|><|start_chunk_35|>
### Page 14
Roboter Adaptionspakete Einzelgreifer
![img-20.jpeg](img-20.jpeg)
(3) Adapter
(4) Kabel Funktionserde

Im Lieferumfang enthalten
(5) Zentrierbund

Roboter Adaptionspakete Für Einzelgreifer enthalten alle notwendigen Komponenten um den Greifer mechanisch an den gewünschten Roboterflansch zu adaptieren. Je nach Flanschbild sind passende Schrauben, Zentrierstifte und der Zentrierbund beigelegt.

| Bezeichnung | Ident.-Nr. | Höhe | Lochkreis DIN ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |  |
| AKO EZU30I GP12 | 1597759 | 11 |  | YASKAWA | GP12 |
| AKO EZU30I GP7,8 | 1597758 | 10.5 |  | YASKAWA | GP7, GP8 |
| AKO EZU30I ISO31.5 | 1597749 | 10.5 | 31.5 | ABB | SWIFTI <br> CRB1100, <br> IRB1100, <br> IRB1200 |
| AKO EZU30I ISO40 | 1597756 | 10.5 | 40 | ABB | IRB1300 |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | ABB | Gofa <br> CRB15000 |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | FANUC | CRX-5IA, CRX-10IA, CRX-20IA, CRX-25IA |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | Kassow <br> Robots |  |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | Universal Robots | UR7e, UR12e, UR16e, UR15 |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | YASKAWA | HC10DTP, HC20DTP |

Roboter Adaptionspakete Einzelgreifer
![img-21.jpeg](img-21.jpeg)
(60) Roboterflansch

Die einteilige Ausführung ermöglicht einen flachen Aufbau des Gesamtsystems. Der Adapter wird aus blankem Aluminium hergestellt. Die aufgelisteten Roboterhersteller mit zugehörigen Modellen sind eine sinnvolle Empfehlung unter Berücksichtigung der Gesamtmasse. SCHUNK empfiehlt dennoch die Nutzlast des Roboters im Detail zu betrachten.

| Bezeichnung | Ident.-Nr. | Höhe | Lochkreis DIN ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |  |
| AKO EZU30I GP12 | 1597759 | 11 |  | YASKAWA | GP12 |
| AKO EZU30I GP7,8 | 1597758 | 10.5 |  | YASKAWA | GP7, GP8 |
| AKO EZU30I ISO31.5 | 1597749 | 10.5 | 31.5 | ABB | SWIFTI <br> CRB1100, <br> IRB1100, <br> IRB1200 |
| AKO EZU30I ISO40 | 1597756 | 10.5 | 40 | ABB | IRB1300 |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | ABB | Gofa <br> CRB15000 |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | FANUC | CRX-5IA, CRX-10IA, CRX-20IA, CRX-25IA |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | Kassow <br> Robots |  |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | Universal Robots | UR7e, UR12e, UR16e, UR15 |
| AKO EZU30I ISO50 | 1597757 | 10.5 | 50 | YASKAWA | HC10DTP, HC20DTP |
<|end_chunk_35|><|start_chunk_36|>
### Page 15
Roboter Adaptionspakete Doppelgreifer
![img-22.jpeg](img-22.jpeg)
![img-23.jpeg](img-23.jpeg)

Roboter Adaptionspakete für Doppelgreifer enthalten alle notwendigen Komponenten um zwei Greifer mechanisch an den gewünschten Roboterflansch zu adaptieren. Je nach Flanschbild sind passende Schrauben, Zentrierstifte und Zentriermaterial beigelegt. Optional kann eine kurze oder lange Abblasdüse ergänzt werden.

| Bezeichnung Ident.-Nr. | Höhe | Lochkreis DIN ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: |
|  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |
| ARO <br> 2xEZU30/ <br> GP12 | 1597809 | 15.8 |  | YASKAWA GP12 |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | FANUC CRX-10iA, CRX-20iA, CRX-25iA |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | Kassow <br> Robots |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | Universal <br> Robots UR12e, UR16e, UR15 |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | YASKAWA HC100TP, HC200TP |
| ARO <br> 2xEZU30/ <br> ISO63 | 1597806 | 14.8 | 63 |  |
| ARO <br> 2xEZU30/ <br> ISO80 | 1597808 | 14.8 | 80 | Universal <br> Robots UR20, UR30 |
| Anbauset <br> Abblasdüse <br> (kurz) | 1524788 |  |  |  |

Roboter Adaptionspakete Doppelgreifer
![img-24.jpeg](img-24.jpeg)

Roboterflansch
Der Adapter wird aus blankem Aluminium hergestellt. Die aufgelisteten Roboterhersteller mit zugehörigen Modellen sind eine sinnvolle Empfehlung unter Berücksichtigung der Gesamtmasse. SCHUNK empfiehlt dennoch die Nutzlast des Roboters im Detail zu betrachten.

| Bezeichnung Ident.-Nr. | Höhe | Lochkreis <br> DIN <br> ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: |
|  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |
| ARO <br> 2xEZU30/ <br> GP12 | 1597809 | 15.8 |  | YASKAWA GP12 |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | FANUC CRX-10iA, CRX-20iA, CRX-25iA |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | Kassow <br> Robots |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | Universal <br> Robots UR12e, UR16e, UR15 |
| ARO <br> 2xEZU30/ <br> ISO50 | 1597804 | 10.8 | 50 | YASKAWA HC100TP, HC200TP |
| ARO <br> 2xEZU30/ <br> ISO63 | 1597806 | 14.8 | 63 |  |
| ARO <br> 2xEZU30/ <br> ISO80 | 1597808 | 14.8 | 80 | Universal <br> Robots | UR20, UR30 |
<|end_chunk_36|><|start_chunk_37|>
### Page 16<|end_chunk_37|><|start_chunk_38|>
 Roboterspezifische Anschlusskabel 

![img-25.jpeg](img-25.jpeg)

Anschlusskabel und Anschlusskabelpakete für den elektrischen Anschluss an spezifische Robotermodelle und Steuerungen. Je nach Hersteller ist eine Direktanbindung am Toolflansch möglich oder eine externe Verkabelung erforderlich. In Kombination mit mechanischen Adaptern und Softwarebausteinen kann dadurch die Inbetriebnahme am Roboter in nur wenigen Schritten erfolgen. Kabel für die externe Kabelführung sind torsionstauglich ausgeführt.

| Bezeichnung | Ident.-Nr. | Hersteller | Baureihe | Modell | Steuerung | Anschluss | Kabellänge [m] | Schnittstelle |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Doppelgreifer |  |  |  |  |  |  |  |  |
| EGIJEGKIEZU CNK-DG-FANUC-CRX | 1532241 | FANUC | CRX | CRX-5iA, CRX-10iA, CRX-20iA, CRX-25iA, CRX-30iA | R-30iB Plus Mini | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-DG-KR-Gen2 | 1620285 | Kassow Robots | KR Series, Edge Edition (Gen2) | KR810, KR1018, KR1205, KR1410, KR1805 |  | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-DG-UR-eSeries | 1532238 | Universal <br> Robots | e-Series, UR-Series | UR3e, UR7e, UR12e, UR16e, UR15, UR20, UR30 | CB5 | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEZU CNK-DG-ABB-OmniCoreC30 | 1529608 | ABB | IRB, CRB |  | OmniCore C30 | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| EGIJEZU CNK-DG-YASKAWA-YRC1000micro | 1529621 | YASKAWA | GP, HC |  | YRC1000MICRO | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| Einzelgreifer |  |  |  |  |  |  |  |  |
| EGIJEGKIEZU CNK-SG-FANUC-CRX | 1532240 | FANUC | CRX | CRX-5iA, CRX-10iA, CRX-20iA, CRX-25iA, CRX-30iA | R-30iB Plus Mini | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-SG-KR-Gen2 | 1620284 | Kassow Robots | KR Series, Edge Edition (Gen2) | KR810, KR1018, KR1205, KR1410, KR1805 |  | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-SG-UR-eSeries | 1532237 | Universal <br> Robots | e-Series, UR-Series | UR3e, UR7e, UR12e, UR16e, UR15, UR20, UR30 | CB5 | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEZU CNK-SG-ABB-OmniCoreC30 | 1529600 | ABB | IRB, CRB |  | OmniCore C30 | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| EGIJEZU CNK-SG-YASKAWA-YRC1000micro | 1529619 | YASKAWA | GP, HC |  | YRC1000MICRO | Steuerung, externe Kabelführung | 5 | EtherNet/IP |

(๑) Es sind die Leistungsdaten des Roboters zu berücksichtigen. SCHUNK empfiehlt zudem die Verwendung einer geeigneten Zugentlastung.
<|end_chunk_38|><|start_chunk_39|>
### Page 17<|end_chunk_39|><|start_chunk_40|>
## Backenschnellwechselsysteme BSWS

![img-26.jpeg](img-26.jpeg)

Für den Greifer bestehen unterschiedliche Backenschnellwechselsysteme. Detaillierte Informationen sind beim entsprechenden Produkt nachzulesen.
<|end_chunk_40|><|start_chunk_41|>
## Zwischenbacke ZBA-EZU 30

![img-27.jpeg](img-27.jpeg)

| 1) Greiferanschluss | 72 Passung für Zentrierhülse  |
| --- | --- |
|  2) Fingeranschluss | 80 Tiefe der Zentrierhülsen-  |
|   | bohrung im Gegenstück  |

Bei Verwendung entspricht die Schnittstelle der Grundbacken der des Universalgreifers PZN-plus. Somit kann das umfangreiche Fingerzubehör des PZN-plus unter Berücksichtigung der Störkonturen und der geltenden Einsatzgrenzen für diesen Greifer genutzt werden.

|  Bezeichnung | Ident.-Nr. | Material | Lieferumfang  |
| --- | --- | --- | --- |
|  Zwischenbacke |  |  |   |
|  ZBA EZU 30 | 1582547 | Stahl | 3  |
|  ZBA EZU 30 SD | 1591235 | Stahl | 3  |

Fingerrohlinge ABR-/SBR-PGZN-plus 64
![img-28.jpeg](img-28.jpeg)

Die Zeichnung zeigt den Fingerrohling zur kundenspezifischen Nachbearbeitung.

|  Bezeichnung | Ident.-Nr. | Material | Lieferumfang  |
| --- | --- | --- | --- |
|  Fingerrohling |  |  |   |
|  ABR-PGZN-plus 64 | 0300010 | Aluminium (3.4365) | 1  |
|  SBR-PGZN-plus 64 | 0300020 | Stahl (1.7131) | 1  |

(1) Bei der Verwendung von Fingerrohlingen kann es bei einzelnen Greiferbaureihen zu einer Begrenzung des Schließhubs kommen. Bitte prüfen Sie dies im Vorfeld detailliert mithilfe der CAD-Daten und passen Sie die Nachbearbeitung der Finger entsprechend an.
<|end_chunk_41|><|start_chunk_42|>
### Page 18<|end_chunk_42|><|start_chunk_43|>
 Anschlusskabel Spannungsversorgung 

![img-29.jpeg](img-29.jpeg)

Die Anschlusskabel dienen dem Anschluss des SCHUNK-Produktes an die Spannungsversorgung.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel Spannungsversorgung - schleppketten- und torsionstauglich M12 Buchse, gerade |  |  |  |  |  |  |  |
| KA GLN12L04-LK-00500-A | 1502019 | 5 | 7.2 | 53.5 | 18 |  | M12 L-kodiert |
| KA GLN12L04-LK-01000-A | 1502023 | 10 | 7.2 | 53.5 | 18 |  | M12 L-kodiert |
| Anschlusskabel Spannungsversorgung - schleppketten- und torsionstauglich M12 Buchse, gewinkelt |  |  |  |  |  |  |  |
| KA WLN12L04-LK-00500-A | 1502028 | 5 | 7.2 | 49 | 18 | 40 | M12 L-kodiert |
| KA WLN12L04-LK-01000-A | 1502032 | 10 | 7.2 | 49 | 18 | 40 | M12 L-kodiert |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.
<|end_chunk_43|><|start_chunk_44|>
### Page 19<|end_chunk_44|><|start_chunk_45|>
 Anschlusskabel Kommunikation PROFINET, EtherNet/IP und EtherCAT 

![img-30.jpeg](img-30.jpeg)

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel EtherCAT Sternverteiler M12 D-kodiert Buchse, gerade auf M8 A-kodiert Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-08A04-ET-00020-A | 1521990 | 0.2 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-12D04-ET-00500-A | 1505114 | 5 | 6.5 | 47.3 | 14.8 |  | M12 |
| KA GGN12D04-12D04-ET-01000-A | 1505119 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gerade - auf RJ45 Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-RJ45-ET-00200-A | 1511256 | 2 | 6.5 | 47.3 | 14.8 |  | M12 |
| KA GGN12D04-RJ45-ET-00500-A | 1354681 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KA GGN12D04-RJ45-ET-01000-A | 1505143 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gewinkelt - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KA WGN12D04-12D04-ET-00500-A | 1354661 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KA WGN12D04-12D04-ET-01000-A | 1505141 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gewinkelt - auf RJ45 Stecker, gerade |  |  |  |  |  |  |  |
| KA WGN12D04-RJ45-ET-00500-A | 1354688 | 5 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| KA WGN12D04-RJ45-ET-01000-A | 1505142 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR GGN12D04-12D04-ET-00500-A | 1505146 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR GGN12D04-12D04-ET-01000-A | 1505147 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR GGN12D04-RJ45-ET-00500-A | 1354677 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR GGN12D04-RJ45-ET-01000-A | 1505160 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gewinkelt - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR WGN12D04-12D04-ET-00500-A | 1354674 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR WGN12D04-12D04-ET-01000-A | 1505148 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gewinkelt - auf RJ45 Stecker, gerade |  |  |  |  |  |  |  |
| KAR WGN12D04-RJ45-ET-00500-A | 1354692 | 5 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| KAR WGN12D04-RJ45-ET-01000-A | 1505149 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das löfache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.
<|end_chunk_45|><|start_chunk_46|>
### Page 20<|end_chunk_46|><|start_chunk_47|>
 Anschlusskabel für Spannungsversorgung und Kommunikation IO-Link 

![img-31.jpeg](img-31.jpeg)

Die Anschlusskabel eignen sich ideal zum Anschluss der jeweiligen Komponenten an die Steuerung. Die Anschlusskabel verfügen auf der einen Seite über eine 5-polige M12-Buchse und auf der anderen Seite über offene Litzen zum individuellen Anschluss. Die Anschlusskabel sind für den Einsatz sowohl in der Schleppkette als auch in Torsionsanwendungen geeignet.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel IO-Link - schleppketten- und torsionstauglich |  |  |  |  |  |  |  |
| KA GLN1205-IOL-00500-A | 1387207 | 5 | 4.8 | 38 | 15 |  | M12 |
| KA GLN1205-IOL-01000-A | 1387209 | 10 | 4.8 | 38 | 15 |  | M12 |
| KA WLN1205-IOL-00500-A | 1387210 | 5 | 4.8 | 39 | 15 | 28 | M12 |
| KA WLN1205-IOL-01000-A | 1387211 | 10 | 4.8 | 39 | 15 | 28 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.
<|end_chunk_47|><|start_chunk_48|>
### Page 21
Kabelverlängerung für Spannungsversorgung und Kommunikation IO-Link
![img-32.jpeg](img-32.jpeg)

Die Kabelverlängerungen eignen sich ideal zum Anschluss der jeweiligen Komponenten an die Steuerung oder als Verlängerungsleitung. Die Kabelverlängerungen verfügen modulseitig über eine 5-polige M12-Buchse in gerader oder gewinkelter Ausführung und auf der anderen Seite über einen 5-poligen M12-Stecker in gerader Ausführung. Die Kabelverlängerungen sind für den Einsatz sowohl in der Schleppkette als auch in Torsionsanwendungen geeignet.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Kabelverlängerung IO-Link - schleppketten- und torsionstauglich |  |  |  |  |  |  |  |
| KV GGM1205-IOL-00200-A | 1387195 | 2 | 4.8 | 41 | 15 |  | M12 |
| KV GGM1205-IOL-00500-A | 1387199 | 5 | 4.8 | 41 | 15 |  | M12 |
| KV WGM1205-IOL-00200-A | 1387202 | 2 | 4.8 | 39 | 15 | 28 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder +/- $180^{\circ} / \mathrm{m}$.
<|end_chunk_48|><|start_chunk_49|>
### Page 22<|end_chunk_49|><|start_chunk_50|>
 Anschlusssteckverbinder Spannungsversorgung 

![img-33.jpeg](img-33.jpeg)

Die Steckverbinder dienen dem Anschluss der SCHUNK Produkte an die Spannungsversorgung. Hierbei kann ein kundenseitiges Kabel verwendet werden. Die Einzellitzen werden mittels Schraubverbindung im Steckverbinder geklemmt.

| Bezeichnung | Ident.-Nr. | D1 (max.) | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] | [mm] | [mm] |  |
| Steckverbinder |  |  |  |  |  |  |
| KBU-M12L-G | 1502044 | 13 | 70 | 25 |  | M12 L-kodiert |
| KBU-M12L-W 4P | 1543957 | 13 | 49 | 25 | 99 | M12 L-kodiert |

(1) Für das Anschlusskabel wird ein Querschnitt je Einzellitze von min. 1,5 mm2 empfohlen. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.
<|end_chunk_50|><|start_chunk_51|>
## Y-Verteiler für IO-Link zur Aufteilung von Logik- und

Leistungsversorgung
![img-34.jpeg](img-34.jpeg)

Der Y-Verteiler ermöglicht die Versorgung der Leistung über eine separierte Spannungsquelle und wird dann empfohlen wenn die Stromaufnahme des Produkts die Stromabgabe des IO-Link Masters übersteigt. Die Logikversorgung und die IO-Link Kommunikation laufen weiterhin über den IO-Link Master. Es können IO-Link Master mit Port Class A oder Port Class B eingesetzt werden.

| Bezeichnung | Ident.-Nr. | Länge |
| :-- | :-- | :-- |
| Y-Verteiler, M12 Buchse, gerade - auf 2xM12 Stecker, gerade A-kodiert |  |  |
| Y-Verteiler M12 5pol. auf 1x M12 3pol. | 1523560 | 0.3 |
<|end_chunk_51|><|start_chunk_52|>
### Page 23<|end_chunk_52|><|start_chunk_53|>
## Schaltnetzteil

![img-35.jpeg](img-35.jpeg)

Die Netzteile mit einer Ausgangsspannung von 24 V und einem Eingangsspannungsbereich von 100V - 240V sind abgestimmt auf die Leistungsversorgung unserer SCHUNK Produkte. Ob zur Montage im Schaltschrank auf DIN-Schiene in der Schutzart IP20 oder direkt im Feld in der Schutzart IP67, die Netzteile liefern Spannung dort, wo sie gebraucht wird. Gerne unterstützen wir Sie bei der weiteren Auswahl.

|  Bezeichnung | Ident.-Nr.  |
| --- | --- |
|  24V Netzteil IP20 |   |
|  BLOCK PC-0124-050-0 | 31001408  |
|  24V Netzteil IP67 |   |
|  TURCK PSU67-12-2480/M | 1524336  |

(c) Bei dem Netzteil IP67 sind konfektionierbare Steckverbinder zum Anschluss an das Netzteil im Lieferumfang enthalten.
<|end_chunk_53|><|start_chunk_54|>
## Switch

![img-36.jpeg](img-36.jpeg)
<|end_chunk_54|><|start_chunk_55|>
## (b) Ethernet 5-Port Switch

Die Switche ermöglichen die einfache Erweiterung eines Hochgeschwindigkeitsnetzwerkes mithilfe kabelgebundener Verbindungen. Mit dem Switch können mehrere SCHUNK-Produkte in ein Netzwerk aufgenommen und so über bspw. eine SPS angesteuert werden.

|  Bezeichnung | Ident.-Nr.  |
| --- | --- |
|  Ethernet Switch |   |
|  D-Link DGS-105 5-Port Ethernet Switch | 1526496  |
<|end_chunk_55|><|start_chunk_56|>
### Page 24
![img-37.jpeg](img-37.jpeg)

Version mit Greifkrafterhaltung

| Greifkraft |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

<|end_chunk_56|><|start_chunk_57|>
### Page 25<|end_chunk_57|><|start_chunk_58|>
 Technische Daten EZU ohne Greifkrafterhaltung

|  Bezeichnung |  | EZU 35-PN-N-B | EZU 35-EI-N-B | EZU 35-EI-N-B | EZU 35-IL-N-B | EZU 35-MB-N-B  |
| --- | --- | --- | --- | --- | --- | --- |
|  Ident.-Nr. |  | 1582077 | 1582079 | 1582091 | 1582093 | 1582096  |
|  Allgemeine Betriebsdaten |  |  |  |  |  |   |
|  Hub pro Backe | [mm] | 35 | 35 | 35 | 35 | 35  |
|  Min./max. Greifkraft | [N] | 390/780 | 390/780 | 390/780 | 390/780 | 390/780  |
|  Max. zulässige Fingerlänge | [mm] | 125 | 125 | 125 | 125 | 125  |
|  Max. zulässige Masse pro Finger | [kg] | 0.8 | 0.8 | 0.8 | 0.8 | 0.8  |
|  Wiederholgenauigkeit (Greifen) | [mm] | 0.02 | 0.02 | 0.02 | 0.02 | 0.02  |
|  Wiederholgenauigkeit (Positionieren, unidirektional) | [mm] | 0.05 | 0.05 | 0.05 | 0.05 | 0.05  |
|  Wiederholgenauigkeit (Positionieren, bidirektional) | [mm] | 0.15 | 0.15 | 0.15 | 0.15 | 0.15  |
|  Schließ-/Öffnungszeit (Positionieren, 50\% Hub) | [s] | 0.6/0.6 | 0.6/0.6 | 0.6/0.6 | 0.6/0.6 | 0.6/0.6  |
|  Max. Geschwindigkeit (Positionieren) | [mm/s] | 40 | 40 | 40 | 40 | 40  |
|  Max. Beschleunigung | [mm/s²] | 250 | 250 | 250 | 250 | 250  |
|  Eigenmasse | [kg] | 4.3 | 4.3 | 4.3 | 4.3 | 4.3  |
|  Min./max. Umgebungstemperatur | [ ${ }^{\circ} \mathrm{C}$ ] | 5/55 | 5/55 | 5/55 | 5/55 | 5/55  |
|  Schutzart IP Elektronik |  | 67 | 67 | 67 | 67 | 67  |
|  Schutzart IP Führung/Grundbacken |  | 40 | 40 | 40 | 40 | 40  |
|  Reinraumklasse ISO 14644-1:2015 |  | 5 | 5 | 5 | 5 | 5  |
|  Elektrische Betriebsdaten |  |  |  |  |  |   |
|  Nennspannung | [V] | 24 | 24 | 24 | 24 | 24  |
|  Kommunikationsschnittstelle |  | PROFINET | EtherNet/IP | EtherCAT | IO-Link | Modbus RTU  |
|  Stromaufnahme BasicGrip Nenn./Max. | [A] | 0.37/1.15 | 0.37/1.15 | 0.37/1.15 | 0.37/1.15 | 0.37/1.15  |
|  Stromaufnahme Logik Nenn./Max. | [A] | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2  |
|  Optionen und deren Eigenschaften |  |  |  |  |  |   |
|  Staubdicht-Version |  | 1582113 | 1582118 | 1582120 | 1582126 | 1582129  |
|  Schutzart IP Führung/Grundbacken |  | 64 | 64 | 64 | 64 | 64  |
|  Hub pro Backe | [mm] | 25 | 25 | 25 | 25 | 25  |
|  Min./max. Greifkraft | [N] | 470/780 | 470/780 | 470/780 | 470/780 | 470/780  |
|  Eigenmasse | [kg] | 4.37 | 4.37 | 4.37 | 4.37 | 4.37  |
|  Reinraumklasse ISO 14644-1:2015 |  | 4 | 4 | 4 | 4 | 4  |
<|end_chunk_58|><|start_chunk_59|>
### Page 26<|end_chunk_59|><|start_chunk_60|>
 Hauptansicht 

![img-38.jpeg](img-38.jpeg)

Die Zeichnung zeigt den Greifer in der Ausführung PROFINET, EtherNet/IP oder EtherCAT, mit und ohne Greifkrafterhaltung mit geöffneten Backen. Die Mindestanzahl der Befestigungsschrauben für die Montage der Greiferfinger ist der Betriebsanleitung des Produkts zu entnehmen.
(1) Greiferanschluss
(2) Fingeranschluss

72 Passung für Zentrierhülse
80 Tiefe der Zentrierhülsen-
bohrung im Gegenstück
90 Spannungsversorgung (M12, Stecker, 4 Pin, L-kodiert)
(91) Kommunikation (M12, Buchse, 4 Pin, D-kodiert)
92 Anschraubung mit Passungen für Zusatzanbau (diese Zentrierhülsen sind nicht im Lieferumfang enthalten)
93 Anschluss Funktionserde
<|end_chunk_60|><|start_chunk_61|>
### Page 27<|end_chunk_61|><|start_chunk_62|>
## Version IO-Link und Modbus RTU

![img-39.jpeg](img-39.jpeg)

90 Spannungsversorgung und Kommunikation (M12, Stecker, A-kodiert, IL: 5 Pin, MB: 4 Pin)

Die Zeichnung zeigt die Maßänderungen der Versionen IO-Link und Modbus RTU im Vergleich zu der in der Hauptansicht dargestellten Grundausführung.

Gewinkelte Steckverbinder Ausführung IO-Link und Modbus RTU
![img-40.jpeg](img-40.jpeg)

Die Zeichnung zeigt die Richtung des Kabelabgangs bei der Verwendung von gewinkelten Steckverbindern. Der Abstand vom Steckverbinder zum Gehäuse des Greifers kann je nach verwendetem Kabelhersteller variieren.

Gewinkelte Steckverbinder Ausführung PROFINET, EtherNet/IP und EtherCAT
![img-41.jpeg](img-41.jpeg)

Die Zeichnung zeigt die Richtung des Kabelabgangs bei der Verwendung von gewinkelten Steckverbindern. Der Abstand vom Steckverbinder zum Gehäuse des Greifers kann je nach verwendetem Kabelhersteller variieren.
<|end_chunk_62|><|start_chunk_63|>
## Staubdicht-Version

![img-42.jpeg](img-42.jpeg)

Anschraubbild siehe Grundversion

Die Option „Staubdicht" erhöht den Schutzgrad gegen eindringende Stoffe. Das Anschraubbild verschiebt sich um die Höhe der Zwischenbacke. Die Fingerlänge ist weiter ab Oberkante des Greifergehäuses zu messen.
<|end_chunk_63|><|start_chunk_64|>
### Page 28
Roboter Adaptionspakete Einzelgreifer
![img-43.jpeg](img-43.jpeg)
(3) Adapter
(4) Kabel Funktionserde

Im Lieferumfang enthalten
(5) Zentrierbund

Roboter Adaptionspakete Für Einzelgreifer enthalten alle notwendigen Komponenten um den Greifer mechanisch an den gewünschten Roboterflansch zu adaptieren. Je nach Flanschbild sind passende Schrauben, Zentrierstifte und der Zentrierbund beigelegt.

| Bezeichnung | Ident.-Nr. | Höhe | Lochkreis <br> DIN <br> ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |  |
| AKO EZU35/ <br> GP12 | 1597788 | 11 |  | YASKAWA | GP12 |
| AKO EZU35/ <br> GP7,8 | 1597783 | 10.5 |  | YASKAWA | GP7, GP8 |
| AKO EZU35/ <br> ISO31.5 | 1597762 | 10.5 | 31.5 | ABB | IRB1200 |
| AKO EZU35/ <br> ISO40 | 1597763 | 10.5 | 40 | ABB | IRB1300 |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | FANUC | CRX-10iA, <br> CRX-20iA, <br> CRX-25iA |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | Kassow <br> Robots |  |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | Universal <br> Robots | UR12e, <br> UR16e, UR15 |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | YASKAWA | HC100TP, <br> HC200TP |

Roboter Adaptionspakete Einzelgreifer
![img-44.jpeg](img-44.jpeg)
(60) Roboterflansch

Die einteilige Ausführung ermöglicht einen flachen Aufbau des Gesamtsystems. Der Adapter wird aus blankem Aluminium hergestellt. Die aufgelisteten Roboterhersteller mit zugehörigen Modellen sind eine sinnvolle Empfehlung unter Berücksichtigung der Gesamtmasse. SCHUNK empfiehlt dennoch die Nutzlast des Roboters im Detail zu betrachten.

| Bezeichnung | Ident.-Nr. | Höhe | Lochkreis <br> DIN <br> ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |  |
| AKO EZU35/ <br> GP12 | 1597788 | 11 |  | YASKAWA | GP12 |
| AKO EZU35/ <br> GP7,8 | 1597783 | 10.5 |  | YASKAWA | GP7, GP8 |
| AKO EZU35/ <br> ISO31.5 | 1597762 | 10.5 | 31.5 | ABB | IRB1200 |
| AKO EZU35/ <br> ISO40 | 1597763 | 10.5 | 40 | ABB | IRB1300 |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | FANUC | CRX-10iA, <br> CRX-20iA, <br> CRX-25iA |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | Kassow <br> Robots |  |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | Universal <br> Robots | UR12e, <br> UR16e, UR15 |
| AKO EZU35/ <br> ISO50 | 1597769 | 10.5 | 50 | YASKAWA | HC100TP, <br> HC200TP |
<|end_chunk_64|><|start_chunk_65|>
### Page 29
Roboter Adaptionspakete Doppelgreifer
![img-45.jpeg](img-45.jpeg)
![img-46.jpeg](img-46.jpeg)

Roboter Adaptionspakete für Doppelgreifer enthalten alle notwendigen Komponenten um zwei Greifer mechanisch an den gewünschten Roboterflansch zu adaptieren. Je nach Flanschbild sind passende Schrauben, Zentrierstifte und Zentriermaterial beigelegt. Optional kann eine kurze oder lange Abblasdüse ergänzt werden.

| Bezeichnung Ident.-Nr. | Höhe | Lochkreis DIN ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: |
|  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |
| AKO <br> 2xEZU35/ <br> ISO50 | 1597810 | 10.8 | 50 | FANUC |
| AKO <br> 2xEZU35/ <br> ISO50 | 1597810 | 10.8 | 50 | Kassow <br> Robots |
| AKO <br> 2xEZU35/ <br> ISO50 | 1597810 | 10.8 | 50 | YASKAWA |
| AKO <br> 2xEZU35/ <br> ISO63 | 1597811 | 14.8 | 63 |  |
| AKO <br> 2xEZU35/ <br> ISO80 | 1597812 | 14.8 | 80 | Universal <br> Robots UR20, UR30 |
| Anbauset <br> Abblasdüse <br> (kurz) | 1524788 |  |  |  |

Roboter Adaptionspakete Doppelgreifer
![img-47.jpeg](img-47.jpeg)

80 Roboterflansch
Der Adapter wird aus blankem Aluminium hergestellt. Die aufgelisteten Roboterhersteller mit zugehörigen Modellen sind eine sinnvolle Empfehlung unter Berücksichtigung der Gesamtmasse. SCHUNK empfiehlt dennoch die Nutzlast des Roboters im Detail zu betrachten.

| Bezeichnung Ident.-Nr. | Höhe | Lochkreis <br> DIN <br> ISO-9409 | Hersteller | Modell |
| :--: | :--: | :--: | :--: | :--: |
|  | [mm] | [mm] |  |  |
| Adapter |  |  |  |  |
| AKO <br> 2xEZU35/ <br> ISO50 | 1597810 | 10.8 | 50 | FANUC | CRX-20iA, <br> CRX-25iA |
| AKO <br> 2xEZU35/ <br> ISO50 | 1597810 | 10.8 | 50 | Kassow <br> Robots |  |
| AKO <br> 2xEZU35/ <br> ISO50 | 1597810 | 10.8 | 50 | YASKAWA | HC20DTP |
| AKO <br> 2xEZU35/ <br> ISO63 | 1597811 | 14.8 | 63 |  |  |
| AKO <br> 2xEZU35/ <br> ISO80 | 1597812 | 14.8 | 80 | Universal <br> Robots | UR20, UR30 |
<|end_chunk_65|><|start_chunk_66|>
### Page 30<|end_chunk_66|><|start_chunk_67|>
 Roboterspezifische Anschlusskabel 

![img-48.jpeg](img-48.jpeg)

Anschlusskabel und Anschlusskabelpakete für den elektrischen Anschluss an spezifische Robotermodelle und Steuerungen. Je nach Hersteller ist eine Direktanbindung am Toolflansch möglich oder eine externe Verkabelung erforderlich. In Kombination mit mechanischen Adaptern und Softwarebausteinen kann dadurch die Inbetriebnahme am Roboter in nur wenigen Schritten erfolgen. Kabel für die externe Kabelführung sind torsionstauglich ausgeführt.

| Bezeichnung | Ident.-Nr. | Hersteller | Baureihe | Modell | Steuerung | Anschluss | Kabellänge [m] | Schnittstelle |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Doppelgreifer |  |  |  |  |  |  |  |  |
| EGIJEGKIEZU CNK-DG-FANUC-CRX | 1532241 | FANUC | CRX | CRX-5iA, CRX-10iA, CRX-20iA, CRX-25iA, CRX-30iA | R-30iB Plus Mini | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-DG-KR-Gen2 | 1620285 | Kassow Robots | KR Series, Edge Edition (Gen2) | KR810, KR1018, KR1205, KR1410, KR1805 |  | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-DG-UR-eSeries | 1532238 | Universal <br> Robots | e-Series, UR-Series | UR3e, UR7e, UR12e, UR16e, UR15, UR20, UR30 | CB5 | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEZU CNK-DG-ABB-OmniCoreC30 | 1529608 | ABB | IRB, CRB |  | OmniCore C30 | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| EGIJEZU CNK-DG-YASKAWA-YRC1000micro | 1529621 | YASKAWA | GP, HC |  | YRC1000MICRO | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| Einzelgreifer |  |  |  |  |  |  |  |  |
| EGIJEGKIEZU CNK-SG-FANUC-CRX | 1532240 | FANUC | CRX | CRX-5iA, CRX-10iA, CRX-20iA, CRX-25iA, CRX-30iA | R-30iB Plus Mini | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-SG-KR-Gen2 | 1620284 | Kassow Robots | KR Series, Edge Edition (Gen2) | KR810, KR1018, KR1205, KR1410, KR1805 |  | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-SG-UR-eSeries | 1532237 | Universal <br> Robots | e-Series, UR-Series | UR3e, UR7e, UR12e, UR16e, UR15, UR20, UR30 | CB5 | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEZU CNK-SG-ABB-OmniCoreC30 | 1529600 | ABB | IRB, CRB |  | OmniCore C30 | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| EGIJEZU CNK-SG-YASKAWA-YRC1000micro | 1529619 | YASKAWA | GP, HC |  | YRC1000MICRO | Steuerung, externe Kabelführung | 5 | EtherNet/IP |

(๑) Es sind die Leistungsdaten des Roboters zu berücksichtigen. SCHUNK empfiehlt zudem die Verwendung einer geeigneten Zugentlastung.
<|end_chunk_67|><|start_chunk_68|>
### Page 31<|end_chunk_68|><|start_chunk_69|>
## Backenschnellwechselsysteme BSWS

![img-49.jpeg](img-49.jpeg)

Für den Greifer bestehen unterschiedliche Backenschnellwechselsysteme. Detaillierte Informationen sind beim entsprechenden Produkt nachzulesen.
<|end_chunk_69|><|start_chunk_70|>
## Zwischenbacke ZBA-EZU 35

![img-50.jpeg](img-50.jpeg)

| 1 Greiferanschluss | 72 Passung für Zentrierhülse  |
| --- | --- |
|  2 Fingeranschluss | 80 Tiefe der Zentrierhülsen-  |
|   | bohrung im Gegenstück  |

Bei Verwendung entspricht die Schnittstelle der Grundbacken der des Universalgreifers PZN-plus. Somit kann das umfangreiche Fingerzubehör des PZN-plus unter Berücksichtigung der Störkonturen und der geltenden Einsatzgrenzen für diesen Greifer genutzt werden.

|  Bezeichnung | Ident.-Nr. | Material | Lieferumfang  |
| --- | --- | --- | --- |
|  Zwischenbacke |  |  |   |
|  ZBA EZU 35 | 1582549 | Stahl | 3  |
|  ZBA EZU 35 SD | 1591236 | Stahl | 3  |

Fingerrohlinge ABR-/SBR-PGZN-plus 100
![img-51.jpeg](img-51.jpeg)

Die Zeichnung zeigt den Fingerrohling zur kundenspezifischen Nachbearbeitung.

|  Bezeichnung | Ident.-Nr. | Material | Lieferumfang  |
| --- | --- | --- | --- |
|  Fingerrohling |  |  |   |
|  ABR-PGZN-plus 100 | 0300012 | Aluminium (3.4365) | 1  |
|  SBR-PGZN-plus 100 | 0300022 | Stahl (1.7131) | 1  |

(1) Bei der Verwendung von Fingerrohlingen kann es bei einzelnen Greiferbaureihen zu einer Begrenzung des Schließhubs kommen. Bitte prüfen Sie dies im Vorfeld detailliert mithilfe der CAD-Daten und passen Sie die Nachbearbeitung der Finger entsprechend an.
<|end_chunk_70|><|start_chunk_71|>
### Page 32<|end_chunk_71|><|start_chunk_72|>
 Anschlusskabel Spannungsversorgung 

![img-52.jpeg](img-52.jpeg)

Die Anschlusskabel dienen dem Anschluss des SCHUNK-Produktes an die Spannungsversorgung.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel Spannungsversorgung - schleppketten- und torsionstauglich M12 Buchse, gerade |  |  |  |  |  |  |  |
| KA GLN12L04-LK-00500-A | 1502019 | 5 | 7.2 | 53.5 | 18 |  | M12 L-kodiert |
| KA GLN12L04-LK-01000-A | 1502023 | 10 | 7.2 | 53.5 | 18 |  | M12 L-kodiert |
| Anschlusskabel Spannungsversorgung - schleppketten- und torsionstauglich M12 Buchse, gewinkelt |  |  |  |  |  |  |  |
| KA WLN12L04-LK-00500-A | 1502028 | 5 | 7.2 | 49 | 18 | 40 | M12 L-kodiert |
| KA WLN12L04-LK-01000-A | 1502032 | 10 | 7.2 | 49 | 18 | 40 | M12 L-kodiert |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.
<|end_chunk_72|><|start_chunk_73|>
### Page 33
Anschlusskabel Kommunikation PROFINET, EtherNet/IP und EtherCAT
![img-53.jpeg](img-53.jpeg)

Die Kommunikationskabel sind für die mechatronischen Produkte von SCHUNK passend konfektioniert und können für die Kommunikationsschnittstelle PROFINET, EtherNET/IP und EtherCAT verwendet werden. Sie verfügen modulseitig immer über einen M12-Steckverbinder (D-kodiert, Stecker). Die Steckverbinder sind modulseitig gerade (KA G...) oder gewinkelt (KA W...) ausgeführt. Auf der zweiten Seite verfügen die Kabel entweder über einen geraden M12-Steckverbinder (D-kodiert, Stecker) oder einen R/45-Steckverbinder.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel EtherCAT Sternverteiler M12 D-kodiert Buchse, gerade auf M8 A-kodiert Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-08A04-ET-00020-A | 1521990 | 0.2 | 6.5 | 47.3 | 14.8 |  | M12 |
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

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das löfache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.
<|end_chunk_73|><|start_chunk_74|>
### Page 34<|end_chunk_74|><|start_chunk_75|>
 Anschlusskabel für Spannungsversorgung und Kommunikation IO-Link 

![img-54.jpeg](img-54.jpeg)

Die Anschlusskabel eignen sich ideal zum Anschluss der jeweiligen Komponenten an die Steuerung. Die Anschlusskabel verfügen auf der einen Seite über eine 5-polige M12-Buchse und auf der anderen Seite über offene Litzen zum individuellen Anschluss. Die Anschlusskabel sind für den Einsatz sowohl in der Schleppkette als auch in Torsionsanwendungen geeignet.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel IO-Link - schleppketten- und torsionstauglich |  |  |  |  |  |  |  |
| KA GLN1205-IOL-00500-A | 1387207 | 5 | 4.8 | 38 | 15 |  | M12 |
| KA GLN1205-IOL-01000-A | 1387209 | 10 | 4.8 | 38 | 15 |  | M12 |
| KA WLN1205-IOL-00500-A | 1387210 | 5 | 4.8 | 39 | 15 | 28 | M12 |
| KA WLN1205-IOL-01000-A | 1387211 | 10 | 4.8 | 39 | 15 | 28 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.
<|end_chunk_75|><|start_chunk_76|>
### Page 35
Kabelverlängerung für Spannungsversorgung und Kommunikation IO-Link
![img-55.jpeg](img-55.jpeg)

Die Kabelverlängerungen eignen sich ideal zum Anschluss der jeweiligen Komponenten an die Steuerung oder als Verlängerungsleitung. Die Kabelverlängerungen verfügen modulseitig über eine 5-polige M12-Buchse in gerader oder gewinkelter Ausführung und auf der anderen Seite über einen 5-poligen M12-Stecker in gerader Ausführung. Die Kabelverlängerungen sind für den Einsatz sowohl in der Schleppkette als auch in Torsionsanwendungen geeignet.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Kabelverlängerung IO-Link - schleppketten- und torsionstauglich |  |  |  |  |  |  |  |
| KV GGM1205-IOL-00200-A | 1387195 | 2 | 4.8 | 41 | 15 |  | M12 |
| KV GGM1205-IOL-00500-A | 1387199 | 5 | 4.8 | 41 | 15 |  | M12 |
| KV WGM1205-IOL-00200-A | 1387202 | 2 | 4.8 | 39 | 15 | 28 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder +/- $180^{\circ} / \mathrm{m}$.
<|end_chunk_76|><|start_chunk_77|>
### Page 36<|end_chunk_77|><|start_chunk_78|>
 Anschlusssteckverbinder Spannungsversorgung 

![img-56.jpeg](img-56.jpeg)

Die Steckverbinder dienen dem Anschluss der SCHUNK Produkte an die Spannungsversorgung. Hierbei kann ein kundenseitiges Kabel verwendet werden. Die Einzellitzen werden mittels Schraubverbindung im Steckverbinder geklemmt.

| Bezeichnung | Ident.-Nr. | D1 (max.) | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] | [mm] | [mm] |  |
| Steckverbinder |  |  |  |  |  |  |
| KBU-M12L-G | 1502044 | 13 | 70 | 25 |  | M12 L-kodiert |
| KBU-M12L-W AP | 1543957 | 13 | 49 | 25 | 99 | M12 L-kodiert |

(1) Für das Anschlusskabel wird ein Querschnitt je Einzellitze von min. 1,5 mm2 empfohlen. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.
<|end_chunk_78|><|start_chunk_79|>
## Y-Verteiler für IO-Link zur Aufteilung von Logik- und

Leistungsversorgung
![img-57.jpeg](img-57.jpeg)

Der Y-Verteiler ermöglicht die Versorgung der Leistung über eine separierte Spannungsquelle und wird dann empfohlen wenn die Stromaufnahme des Produkts die Stromabgabe des IO-Link Masters übersteigt. Die Logikversorgung und die IO-Link Kommunikation laufen weiterhin über den IO-Link Master. Es können IO-Link Master mit Port Class A oder Port Class B eingesetzt werden.

| Bezeichnung | Ident.-Nr. | Länge |
| :-- | :-- | :-- |
| Y-Verteiler, M12 Buchse, gerade - auf 2xM12 Stecker, gerade A-kodiert |  |  |
| Y-Verteiler M12 Spol. auf 1x M12 3pol. | 1523560 | 0.3 |
<|end_chunk_79|><|start_chunk_80|>
### Page 37<|end_chunk_80|><|start_chunk_81|>
## Schaltnetzteil

![img-58.jpeg](img-58.jpeg)

Die Netzteile mit einer Ausgangsspannung von $24 V$ und einem Eingangsspannungsbereich von 100V - 240V sind abgestimmt auf die Leistungsversorgung unserer SCHUNK Produkte. Ob zur Montage im Schaltschrank auf DIN-Schiene in der Schutzart IP20 oder direkt im Feld in der Schutzart IP67, die Netzteile liefern Spannung dort, wo sie gebraucht wird. Gerne unterstützen wir Sie bei der weiteren Auswahl.

|  Bezeichnung | Ident.-Nr.  |
| --- | --- |
|  24V Netzteil IP20 |   |
|  BLOCK PC-0124-050-0 | 31001408  |
|  24V Netzteil IP67 |   |
|  TURCK PSU67-12-2480/M | 1524336  |

(c) Bei dem Netzteil IP67 sind konfektionierbare Steckverbinder zum Anschluss an das Netzteil im Lieferumfang enthalten.
<|end_chunk_81|><|start_chunk_82|>
## Switch

![img-59.jpeg](img-59.jpeg)
<|end_chunk_82|><|start_chunk_83|>
## (b) Ethernet 5-Port Switch

Die Switche ermöglichen die einfache Erweiterung eines Hochgeschwindigkeitsnetzwerkes mithilfe kabelgebundener Verbindungen. Mit dem Switch können mehrere SCHUNK-Produkte in ein Netzwerk aufgenommen und so über bspw. eine SPS angesteuert werden.

|  Bezeichnung | Ident.-Nr.  |
| --- | --- |
|  Ethernet Switch |   |
|  D-Link DGS-105 5-Port Ethernet Switch | 1526496  |
<|end_chunk_83|><|start_chunk_84|>
### Page 38
![img-60.jpeg](img-60.jpeg)

Version mit Greifkrafterhaltung

| Greifkraft |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  |  |  |  |  |
| 4000 | - $E Z U 40-50 \%$ | - EZU 40-500\% | Resistirip |  |
|  | - $E Z U 40-500 \%$ | - EZU 40 - 200\% | Strengthip |  |
|  |  |  |  |  |
| Version ohne Greifkrafterhaltung |  |  |  |  |
| Greifkraft |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Dimensionen und max. Belastungen

| $\mathrm{Mx} \mathrm{~max} .65 \mathrm{Nm}$ |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- |
| My max. 105 Nm |  |  |  |  |

( Die angegebenen Momente und Kräfte sind statische Werte, gelten je Grundbacke und dürfen gleichzeitig auftreten.
<|end_chunk_84|><|start_chunk_85|>
 Technische Daten EZU mit Greifkrafterhaltung 

| Bezeichnung |  | EZU 40-PN-M-B | EZU 40-EI-M-B | EZU 40-EI-M-B | EZU 40-IL-M-B | EZU 40-MB-M-B |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Ident.-Nr. |  | 1582134 | 1582137 | 1582152 | 1582154 | 1582156 |
| Allgemeine Betriebsdaten |  |  |  |  |  |  |
| Hub pro Backe | [mm] | 40 | 40 | 40 | 40 | 40 |
| Min./max. Greifkraft | [N] | 900/3600 | 900/3600 | 900/3600 | 900/3600 | 900/3600 |
| Min./max. Greifkrafterhaltung | $[\%]$ | 80/100 | 80/100 | 80/100 | 80/100 | 80/100 |
| Max. zulässige Fingerlänge | [mm] | 160 | 160 | 160 | 160 | 160 |
| Max. zulässige Masse pro Finger | [kg] | 1.4 | 1.4 | 1.4 | 1.4 | 1.4 |
| Wiederholgenauigkeit (Greifen) | [mm] | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |
| Wiederholgenauigkeit (Positionieren, unidirektional) | [mm] | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |
| Wiederholgenauigkeit (Positionieren, bidirektional) | [mm] | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 |
| Schließ-/Öffnungszeit (Positionieren, 50\% Hub) | [s] | $1 / 1$ | $1 / 1$ | $1 / 1$ | $1 / 1$ | $1 / 1$ |
| Max. Geschwindigkeit (Positionieren) | [mm/s] | 25 | 25 | 25 | 25 | 25 |
| Max. Beschleunigung | [mm/s] | 150 | 150 | 150 | 150 | 150 |
| Eigenmasse | [kg] | 7.43 | 7.43 | 7.43 | 7.43 | 7.43 |
| Min./max. Umgebungstemperatur | ${ }^{\circ} \mathrm{C}$ ] | $5 / 55$ | $5 / 55$ | $5 / 55$ | $5 / 55$ | $5 / 55$ |
| Schutzart IP Elektronik |  | 67 | 67 | 67 | 67 | 67 |
| Schutzart IP Führung/Grundbacken |  | 40 | 40 | 40 | 40 | 40 |
| Reinraumklasse ISO 14644-1:2015 |  | 5 | 5 | 5 | 5 | 5 |
| Elektrische Betriebsdaten |  |  |  |  |  |  |
| Nennspannung | [V] | 24 | 24 | 24 | 24 | 24 |
| Kommunikationsschnittstelle |  | PROFINET | EtherNet/IP | EtherCAT | IO-Link | Modbus RTU |
| Stromaufnahme BasicGrip Nenn./Max. | [A] | 0.82/1.99 | 0.82/1.99 | 0.82/1.99 | 0.82/1.99 | 0.82/1.99 |
| Stromaufnahme StrongGrip Nenn./Max. | [A] | 2.75/5.29 | 2.75/5.29 | 2.75/5.29 | 2.75/5.29 | 2.75/5.29 |
| Stromaufnahme Logik Nenn./Max. | [A] | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 |
| Optionen und deren Eigenschaften |  |  |  |  |  |  |
| Staubdicht-Version |  | 1582164 | 1582167 | 1582218 | 1582222 | 1582226 |
| Schutzart IP Führung/Grundbacken |  | 64 | 64 | 64 | 64 | 64 |
| Hub pro Backe | [mm] | 30 | 30 | 30 | 30 | 30 |
| Min./max. Greifkraft | [N] | 1080/3600 | 1080/3600 | 1080/3600 | 1080/3600 | 1080/3600 |
| Eigenmasse | [kg] | 7.55 | 7.55 | 7.55 | 7.55 | 7.55 |
| Reinraumklasse ISO 14644-1:2015 |  | 4 | 4 | 4 | 4 | 4 |
<|end_chunk_85|><|start_chunk_86|>
### Page 39<|end_chunk_86|><|start_chunk_87|>
 Technische Daten EZU ohne Greifkrafterhaltung

|  Bezeichnung |  | EZU 40-PN-N-B | EZU 40-EI-N-B | EZU 40-EC-N-B | EZU 40-IL-N-B | EZU 40-MB-N-B  |
| --- | --- | --- | --- | --- | --- | --- |
|  Ident.-Nr. |  | 1582136 | 1582139 | 1582153 | 1582155 | 1582158  |
|  Allgemeine Betriebsdaten |  |  |  |  |  |   |
|  Hub pro Backe | [mm] | 40 | 40 | 40 | 40 | 40  |
|  Min./max. Greifkraft | [N] | 900/1800 | 900/1800 | 900/1800 | 900/1800 | 900/1800  |
|  Max. zulässige Fingerlänge | [mm] | 160 | 160 | 160 | 160 | 160  |
|  Max. zulässige Masse pro Finger | [kg] | 1.4 | 1.4 | 1.4 | 1.4 | 1.4  |
|  Wiederholgenauigkeit (Greifen) | [mm] | 0.02 | 0.02 | 0.02 | 0.02 | 0.02  |
|  Wiederholgenauigkeit (Positionieren, unidirektional) | [mm] | 0.05 | 0.05 | 0.05 | 0.05 | 0.05  |
|  Wiederholgenauigkeit (Positionieren, bidirektional) | [mm] | 0.15 | 0.15 | 0.15 | 0.15 | 0.15  |
|  Schließ-/Öffnungszeit (Positionieren, 50\% Hub) | [s] | $1 / 1$ | $1 / 1$ | $1 / 1$ | $1 / 1$ | $1 / 1$  |
|  Max. Geschwindigkeit (Positionieren) | [mm/s] | 25 | 25 | 25 | 25 | 25  |
|  Max. Beschleunigung | [mm/s²] | 150 | 150 | 150 | 150 | 150  |
|  Eigenmasse | [kg] | 7.29 | 7.29 | 7.29 | 7.29 | 7.29  |
|  Min./max. Umgebungstemperatur | [ ${ }^{\circ} \mathrm{C}$ ] | 5/55 | 5/55 | 5/55 | 5/55 | 5/55  |
|  Schutzart IP Elektronik |  | 67 | 67 | 67 | 67 | 67  |
|  Schutzart IP Führung/Grundbacken |  | 40 | 40 | 40 | 40 | 40  |
|  Reinraumklasse ISO 14644-1:2015 |  | 5 | 5 | 5 | 5 | 5  |
|  Elektrische Betriebsdaten |  |  |  |  |  |   |
|  Nennspannung | [V] | 24 | 24 | 24 | 24 | 24  |
|  Kommunikationsschnittstelle |  | PROFINET | EtherNet/IP | EtherCAT | IO-Link | Modbus RTU  |
|  Stromaufnahme BasicGrip Nenn./Max. | [A] | 0.36/1.52 | 0.36/1.52 | 0.36/1.52 | 0.36/1.52 | 0.36/1.52  |
|  Stromaufnahme Logik Nenn./Max. | [A] | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2 | 0.16/0.2  |
|  Optionen und deren Eigenschaften |  |  |  |  |  |   |
|  Staubdicht-Version |  | 1582166 | 1582216 | 1582219 | 1582223 | 1582228  |
|  Schutzart IP Führung/Grundbacken |  | 64 | 64 | 64 | 64 | 64  |
|  Hub pro Backe | [mm] | 30 | 30 | 30 | 30 | 30  |
|  Min./max. Greifkraft | [N] | 1080/1800 | 1080/1800 | 1080/1800 | 1080/1800 | 1080/1800  |
|  Eigenmasse | [kg] | 7.41 | 7.41 | 7.41 | 7.41 | 7.41  |
|  Reinraumklasse ISO 14644-1:2015 |  | 4 | 4 | 4 | 4 | 4  |
<|end_chunk_87|><|start_chunk_88|>
### Page 40<|end_chunk_88|><|start_chunk_89|>
 Hauptansicht 

![img-61.jpeg](img-61.jpeg)

Die Zeichnung zeigt den Greifer in der Ausführung PROFINET, EtherNet/IP oder EtherCAT, mit und ohne Greifkrafterhaltung mit geöffneten Backen. Die Mindestanzahl der Befestigungsschrauben für die Montage der Greiferfinger ist der Betriebsanleitung des Produkts zu entnehmen.
(1) Greiferanschluss
(2) Fingeranschluss

72 Passung für Zentrierhülse
80 Tiefe der Zentrierhülsen-
bohrung im Gegenstück
90 Spannungsversorgung (M12, Stecker, 4 Pin, L-kodiert)
(91) Kommunikation (M12, Buchse, 4 Pin, D-kodiert)
92 Anschraubung mit Passungen für Zusatzanbau (diese Zentrierhülsen sind nicht im Lieferumfang enthalten)
93 Anschluss Funktionserde
<|end_chunk_89|><|start_chunk_90|>
### Page 41<|end_chunk_90|><|start_chunk_91|>
## Version IO-Link und Modbus RTU

![img-62.jpeg](img-62.jpeg)

90 Spannungsversorgung und Kommunikation (M12, Stecker, A-kodiert, IL: 5 Pin, MB: 4 Pin)

Die Zeichnung zeigt die Maßänderungen der Versionen IO-Link und Modbus RTU im Vergleich zu der in der Hauptansicht dargestellten Grundausführung.

Gewinkelte Steckverbinder Ausführung IO-Link und Modbus RTU
![img-63.jpeg](img-63.jpeg)

Die Zeichnung zeigt die Richtung des Kabelabgangs bei der Verwendung von gewinkelten Steckverbindern. Der Abstand vom Steckverbinder zum Gehäuse des Greifers kann je nach verwendetem Kabelhersteller variieren.

Gewinkelte Steckverbinder Ausführung PROFINET, EtherNet/IP und EtherCAT
![img-64.jpeg](img-64.jpeg)

Die Zeichnung zeigt die Richtung des Kabelabgangs bei der Verwendung von gewinkelten Steckverbindern. Der Abstand vom Steckverbinder zum Gehäuse des Greifers kann je nach verwendetem Kabelhersteller variieren.
<|end_chunk_91|><|start_chunk_92|>
## Staubdicht-Version

![img-65.jpeg](img-65.jpeg)

Anschraubbild siehe Grundversion

Die Option „Staubdicht" erhöht den Schutzgrad gegen eindringende Stoffe. Das Anschraubbild verschiebt sich um die Höhe der Zwischenbacke. Die Fingerlänge ist weiter ab Oberkante des Greifergehäuses zu messen.
<|end_chunk_92|><|start_chunk_93|>
### Page 42<|end_chunk_93|><|start_chunk_94|>
 **Roboter Adaptionspakete Einzelgreifer**

![img-66.jpeg](img-66.jpeg)

|  3 | Adapter |  | 91 | Kabel Funktionserde  |
| --- | --- | --- | --- | --- |
|  56 | Im Lieferumfang enthalten |  | 92 | Zentrierbund  |
|  93 | Roboterflansch |  |  |   |

Roboter Adaptionspakete für Einzelgreifer enthalten alle notwendigen Komponenten um den Greifer mechanisch an den gewünschten Roboterflansch zu adaptieren. Je nach Flanschbild sind passende Schrauben, Zentrierstifte und der Zentrierbund beigelegt.

|  Bezeichnung | Ident.-Nr. | Höhe | Lochkreis
DIN
ISO-9409 | Hersteller | Modell  |
| --- | --- | --- | --- | --- | --- |
|   |  | [mm] | [mm] |  |   |
|  Adapter |  |  |  |  |   |
|  AKO EZU40i
ISO50 | 1597800 | 12.9 | 50 | Kassow
Robots |   |
|  AKO EZU40i
ISO50 | 1597800 | 12.9 | 50 | Universal
Robots | UR12e,
UR16e, UR15  |
|  AKO EZU40i
ISO50 | 1597800 | 12.9 | 50 | YASKAWA | HC100TP,
HC200TP  |
|  AKO EZU40i
ISO63 | 1597801 | 12.9 | 63 |  |   |
|  AKO EZU40i
ISO80 | 1597803 | 12.9 | 80 | Universal
Robots | UR20, UR30  |

![img-67.jpeg](img-67.jpeg)

|  Bezeichnung | Ident.-Nr. | Höhe | Lochkreis
DIN
ISO-9409 | Hersteller | Modell  |
| --- | --- | --- | --- | --- | --- |
|   |  | [mm] | [mm] |  |   |
|  Adapter |  |  |  |  |   |
|  AKO EZU40i
ISO50 | 1597800 | 12.9 | 50 | Kassow
Robots |   |
|  AKO EZU40i
ISO50 | 1597800 | 12.9 | 50 | Universal
Robots | UR12e,
UR16e, UR15  |
|  AKO EZU40i
ISO50 | 1597800 | 12.9 | 50 | YASKAWA | HC100TP,
HC200TP  |
|  AKO EZU40i
ISO63 | 1597801 | 12.9 | 63 |  |   |
|  AKO EZU40i
ISO80 | 1597803 | 12.9 | 80 | Universal
Robots | UR20, UR30  |
<|end_chunk_94|><|start_chunk_95|>
### Page 43
Roboter Adaptionspakete Doppelgreifer
![img-68.jpeg](img-68.jpeg)
(3) Adapter
(5) Im Lieferumfang enthalten

60 Roboterflansch
61 Kabel Funktionserde
62 Zentrierbund Greifer
(9) Winkeladapter
64 Adapter Roboter
65 Kabelhalter (im Lieferumfang des Kabelpakets enthalten)
66 Anbauset Abblasdüse

Roboter Adaptionspakete für Doppelgreifer enthalten alle notwendigen Komponenten um zwei Greifer mechanisch an den gewünschten Roboterflansch zu adaptieren. Je nach Flanschbild sind passende Schrauben, Zentrierstifte und Zentriermaterial beigelegt. Optional kann eine kurze oder lange Abblasdüse ergänzt werden.

| Bezeichnung | Ident.-Nr. | Höhe | Lochkreis DIN ISO-9409 |
| :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] |
| Adapter |  |  |  |
| AK0 2xEZU40IIS063 | 1597813 | 14.8 | 63 |
| AK0 2xEZU40IIS080 | 1597832 | 14.8 | 80 |
| Anbauset Abblasdüse (lang) | 1524789 |  |  |

Roboter Adaptionspakete Doppelgreifer
![img-69.jpeg](img-69.jpeg)
(10) Roboterflansch

Der Adapter wird aus blankem Aluminium hergestellt. Die aufgelisteten Roboterhersteller mit zugehörigen Modellen sind eine sinnvolle Empfehlung unter Berücksichtigung der Gesamtmasse. SCHUNK empfiehlt dennoch die Nutzlast des Roboters im Detail zu betrachten.

| Bezeichnung | Ident.-Nr. | Höhe | Lochkreis DIN ISO-9409 |
| :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] |
| Adapter |  |  |  |
| AK0 2xEZU40IIS063 | 1597813 | 14.8 | 63 |
| AK0 2xEZU40IIS080 | 1597832 | 14.8 | 80 |
<|end_chunk_95|><|start_chunk_96|>
### Page 44<|end_chunk_96|><|start_chunk_97|>
 Roboterspezifische Anschlusskabel 

![img-70.jpeg](img-70.jpeg)

Anschlusskabel und Anschlusskabelpakete für den elektrischen Anschluss an spezifische Robotermodelle und Steuerungen. Je nach Hersteller ist eine Direktanbindung am Toolflansch möglich oder eine externe Verkabelung erforderlich. In Kombination mit mechanischen Adaptern und Softwarebausteinen kann dadurch die Inbetriebnahme am Roboter in nur wenigen Schritten erfolgen. Kabel für die externe Kabelführung sind torsionstauglich ausgeführt.

| Bezeichnung | Ident.-Nr. | Hersteller | Baureihe | Modell | Steuerung | Anschluss | Kabellänge | Schnittstelle |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Doppelgreifer |  |  |  |  |  |  |  |  |
| EGIJEGKIEZU CNK-DG-FANUC-CRX | 1532241 | FANUC | CRX | CRX-5iA, CRX-10iA, CRX-20iA, CRX-25iA, CRX-30iA | R-30iB Plus Mini | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-DG-KR-Gen2 | 1620285 | Kassow Robots | KR Series, Edge Edition (Gen2) | KR810, KR1018, KR1205, KR1410, KR1805 |  | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-DG-UR-eSeries | 1532238 | Universal <br> Robots | e-Series, UR-Series | UR3e, UR7e, UR12e, UR16e, UR15, UR20, UR30 | CB5 | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEZU CNK-DG-ABB-OmniCoreC30 | 1529608 | ABB | IRB, CRB |  | OmniCore C30 | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| EGIJEZU CNK-DG-YASKAWA-YRC1000micro | 1529621 | YASKAWA | GP, HC |  | YRC1000MICRO | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| Einzelgreifer |  |  |  |  |  |  |  |  |
| EGIJEGKIEZU CNK-SG-FANUC-CRX | 1532240 | FANUC | CRX | CRX-5iA, CRX-10iA, CRX-20iA, CRX-25iA, CRX-30iA | R-30iB Plus Mini | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-SG-KR-Gen2 | 1620284 | Kassow Robots | KR Series, Edge Edition (Gen2) | KR810, KR1018, KR1205, KR1410, KR1805 |  | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEGKIEZU CNK-SG-UR-eSeries | 1532237 | Universal <br> Robots | e-Series, UR-Series | UR3e, UR7e, UR12e, UR16e, UR15, UR20, UR30 | CB5 | Tool (male), interne Durchführung |  | Modbus RTU |
| EGIJEZU CNK-SG-ABB-OmniCoreC30 | 1529600 | ABB | IRB, CRB |  | OmniCore C30 | Steuerung, externe Kabelführung | 5 | EtherNet/IP |
| EGIJEZU CNK-SG-YASKAWA-YRC1000micro | 1529619 | YASKAWA | GP, HC |  | YRC1000MICRO | Steuerung, externe Kabelführung | 5 | EtherNet/IP |

(๑) Es sind die Leistungsdaten des Roboters zu berücksichtigen. SCHUNK empfiehlt zudem die Verwendung einer geeigneten Zugentlastung.
<|end_chunk_97|><|start_chunk_98|>
### Page 45<|end_chunk_98|><|start_chunk_99|>
## Backenschnellwechselsysteme BSWS

![img-71.jpeg](img-71.jpeg)

Für den Greifer bestehen unterschiedliche Backenschnellwechselsysteme. Detaillierte Informationen sind beim entsprechenden Produkt nachzulesen.
<|end_chunk_99|><|start_chunk_100|>
## Zwischenbacke ZBA-EZU 40

![img-72.jpeg](img-72.jpeg)

| 1 Greiferanschluss | 72 Passung für Zentrierhülse  |
| --- | --- |
|  2 Fingeranschluss | 80 Tiefe der Zentrierhülsen-  |
|   | bohrung im Gegenstück  |

Bei Verwendung entspricht die Schnittstelle der Grundbacken der des Universalgreifers PZN-plus. Somit kann das umfangreiche Fingerzubehör des PZN-plus unter Berücksichtigung der Störkonturen und der geltenden Einsatzgrenzen für diesen Greifer genutzt werden.

|  Bezeichnung | Ident.-Nr. | Material | Lieferumfang  |
| --- | --- | --- | --- |
|  Zwischenbacke |  |  |   |
|  ZBA EZU 40 | 1582571 | Stahl | 3  |
|  ZBA EZU 40 SD | 1591237 | Stahl | 3  |

Fingerrohlinge ABR-JSBR-PGZN-plus 125
![img-73.jpeg](img-73.jpeg)

Die Zeichnung zeigt den Fingerrohling zur kundenspezifischen Nachbearbeitung.

|  Bezeichnung | Ident.-Nr. | Material | Lieferumfang  |
| --- | --- | --- | --- |
|  Fingerrohling |  |  |   |
|  ABR-PGZN-plus 125 | 0300013 | Aluminium (3.4365) | 1  |
|  SBR-PGZN-plus 125 | 0300023 | Stahl (1.7131) | 1  |

(1) Bei der Verwendung von Fingerrohlingen kann es bei einzelnen Greiferbaureihen zu einer Begrenzung des Schließhubs kommen. Bitte prüfen Sie dies im Vorfeld detailliert mithilfe der CAD-Daten und passen Sie die Nachbearbeitung der Finger entsprechend an.
<|end_chunk_100|><|start_chunk_101|>
### Page 46<|end_chunk_101|><|start_chunk_102|>
 Anschlusskabel Spannungsversorgung 

![img-74.jpeg](img-74.jpeg)

Die Anschlusskabel dienen dem Anschluss des SCHUNK-Produktes an die Spannungsversorgung.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel Spannungsversorgung - schleppketten- und torsionstauglich M12 Buchse, gerade |  |  |  |  |  |  |  |
| KA GLN12L04-LK-00500-A | 1502019 | 5 | 7.2 | 53.5 | 18 |  | M12 L-kodiert |
| KA GLN12L04-LK-01000-A | 1502023 | 10 | 7.2 | 53.5 | 18 |  | M12 L-kodiert |
| Anschlusskabel Spannungsversorgung - schleppketten- und torsionstauglich M12 Buchse, gewinkelt |  |  |  |  |  |  |  |
| KA WLN12L04-LK-00500-A | 1502028 | 5 | 7.2 | 49 | 18 | 40 | M12 L-kodiert |
| KA WLN12L04-LK-01000-A | 1502032 | 10 | 7.2 | 49 | 18 | 40 | M12 L-kodiert |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.
<|end_chunk_102|><|start_chunk_103|>
### Page 47<|end_chunk_103|><|start_chunk_104|>
 Anschlusskabel Kommunikation PROFINET, EtherNet/IP und EtherCAT 

![img-75.jpeg](img-75.jpeg)

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel EtherCAT Sternverteiler M12 D-kodiert Buchse, gerade auf M8 A-kodiert Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-08A04-ET-00020-A | 1521990 | 0.2 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-12D04-ET-00500-A | 1505114 | 5 | 6.5 | 47.3 | 14.8 |  | M12 |
| KA GGN12D04-12D04-ET-01000-A | 1505119 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gerade - auf RJ45 Stecker, gerade |  |  |  |  |  |  |  |
| KA GGN12D04-RJ45-ET-00200-A | 1511256 | 2 | 6.5 | 47.3 | 14.8 |  | M12 |
| KA GGN12D04-RJ45-ET-00500-A | 1354681 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KA GGN12D04-RJ45-ET-01000-A | 1505143 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gewinkelt - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KA WGN12D04-12D04-ET-00500-A | 1354661 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KA WGN12D04-12D04-ET-01000-A | 1505141 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel schleppkettentauglich M12 Stecker, gewinkelt - auf RJ45 Stecker, gerade |  |  |  |  |  |  |  |
| KA WGN12D04-RJ45-ET-00500-A | 1354688 | 5 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| KA WGN12D04-RJ45-ET-01000-A | 1505142 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR GGN12D04-12D04-ET-00500-A | 1505146 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR GGN12D04-12D04-ET-01000-A | 1505147 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gerade - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR GGN12D04-12D04-ET-00500-A | 1354677 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR GGN12D04-12D04-ET-01000-A | 1505160 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gewinkelt - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR WGN12D04-RJ45-ET-00500-A | 1354674 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR GGN12D04-RJ45-ET-01000-A | 1505160 | 10 | 6.5 | 47.3 | 14.8 |  | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gewinkelt - auf M12 Stecker, gerade |  |  |  |  |  |  |  |
| KAR WGN12D04-12D04-ET-00500-A | 1354676 | 5 | 6.5 | 47.8 | 14.8 |  | M12 |
| KAR WGN12D04-12D04-ET-01000-A | 1505148 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| Kommunikationskabel torsionstauglich M12 Stecker, gewinkelt - auf RJ45 Stecker, gerade |  |  |  |  |  |  |  |
| KAR WGN12D04-RJ45-ET-00500-A | 1354692 | 5 | 6.5 | 36.3 | 14.8 | 30 | M12 |
| KAR WGN12D04-RJ45-ET-01000-A | 1505149 | 10 | 6.5 | 36.3 | 14.8 | 30 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das löfache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.
<|end_chunk_104|><|start_chunk_105|>
### Page 48<|end_chunk_105|><|start_chunk_106|>
 Anschlusskabel für Spannungsversorgung und Kommunikation IO-Link 

![img-76.jpeg](img-76.jpeg)

Die Anschlusskabel eignen sich ideal zum Anschluss der jeweiligen Komponenten an die Steuerung. Die Anschlusskabel verfügen auf der einen Seite über eine 5-polige M12-Buchse und auf der anderen Seite über offene Litzen zum individuellen Anschluss. Die Anschlusskabel sind für den Einsatz sowohl in der Schleppkette als auch in Torsionsanwendungen geeignet.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Anschlusskabel IO-Link - schleppketten- und torsionstauglich |  |  |  |  |  |  |  |
| KA GLN1205-IOL-00500-A | 1387207 | 5 | 4.8 | 38 | 15 |  | M12 |
| KA GLN1205-IOL-01000-A | 1387209 | 10 | 4.8 | 38 | 15 |  | M12 |
| KA WLN1205-IOL-00500-A | 1387210 | 5 | 4.8 | 39 | 15 | 28 | M12 |
| KA WLN1205-IOL-01000-A | 1387211 | 10 | 4.8 | 39 | 15 | 28 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder $+/-180^{\circ} / \mathrm{m}$.
<|end_chunk_106|><|start_chunk_107|>
### Page 49
Kabelverlängerung für Spannungsversorgung und Kommunikation IO-Link
![img-77.jpeg](img-77.jpeg)

Die Kabelverlängerungen eignen sich ideal zum Anschluss der jeweiligen Komponenten an die Steuerung oder als Verlängerungsleitung. Die Kabelverlängerungen verfügen modulseitig über eine 5-polige M12-Buchse in gerader oder gewinkelter Ausführung und auf der anderen Seite über einen 5-poligen M12-Stecker in gerader Ausführung. Die Kabelverlängerungen sind für den Einsatz sowohl in der Schleppkette als auch in Torsionsanwendungen geeignet.

| Bezeichnung | Ident.-Nr. | L1 | D1 | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [m] | [mm] | [mm] | [mm] | [mm] |  |
| Kabelverlängerung IO-Link - schleppketten- und torsionstauglich |  |  |  |  |  |  |  |
| KV GGM1205-IOL-00200-A | 1387195 | 2 | 4.8 | 41 | 15 |  | M12 |
| KV GGM1205-IOL-00500-A | 1387199 | 5 | 4.8 | 41 | 15 |  | M12 |
| KV WGM1205-IOL-00200-A | 1387202 | 2 | 4.8 | 39 | 15 | 28 | M12 |

(1) Bitte beachten Sie den min. Biegeradius bei schleppkettentauglichen Kabeln oder den max. Torsionswinkel bei torsionstauglichen Kabeln. Diese betragen im Allgemeinen das 10fache des Kabeldurchmessers oder +/- $180^{\circ} / \mathrm{m}$.
<|end_chunk_107|><|start_chunk_108|>
### Page 50<|end_chunk_108|><|start_chunk_109|>
 Anschlusssteckverbinder Spannungsversorgung 

![img-78.jpeg](img-78.jpeg)

Die Steckverbinder dienen dem Anschluss der SCHUNK Produkte an die Spannungsversorgung. Hierbei kann ein kundenseitiges Kabel verwendet werden. Die Einzellitzen werden mittels Schraubverbindung im Steckverbinder geklemmt.

| Bezeichnung | Ident.-Nr. | D1 (max.) | L2 | D2 | L3 | D3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | [mm] | [mm] | [mm] | [mm] |  |
| Steckverbinder |  |  |  |  |  |  |
| KBU-M12L-G | 1502044 | 13 | 70 | 25 |  | M12 L-kodiert |
| KBU-M12L-W 4P | 1543957 | 13 | 49 | 25 | 99 | M12 L-kodiert |

(1) Für das Anschlusskabel wird ein Querschnitt je Einzellitze von min. 1,5 mm2 empfohlen. Informationen zu max. Leitungslänge und dem min. Aderquerschnitt finden Sie in der jeweiligen Produktdokumentation.
<|end_chunk_109|><|start_chunk_110|>
## Y-Verteiler für IO-Link zur Aufteilung von Logik- und

Leistungsversorgung
![img-79.jpeg](img-79.jpeg)

Der Y-Verteiler ermöglicht die Versorgung der Leistung über eine separierte Spannungsquelle und wird dann empfohlen wenn die Stromaufnahme des Produkts die Stromabgabe des IO-Link Masters übersteigt. Die Logikversorgung und die IO-Link Kommunikation laufen weiterhin über den IO-Link Master. Es können IO-Link Master mit Port Class A oder Port Class B eingesetzt werden.

| Bezeichnung | Ident.-Nr. | Länge |
| :-- | :-- | :-- |
| Y-Verteiler, M12 Buchse, gerade - auf 2xM12 Stecker, gerade A-kodiert |  |  |
| Y-Verteiler M12 5pol. auf 1x M12 3pol. | 1523560 | 0.3 |
<|end_chunk_110|><|start_chunk_111|>
### Page 51<|end_chunk_111|><|start_chunk_112|>
## Schaltnetzteil

![img-80.jpeg](img-80.jpeg)

Die Netzteile mit einer Ausgangsspannung von 24 V und einem Eingangsspannungsbereich von 100V - 240V sind abgestimmt auf die Leistungsversorgung unserer SCHUNK Produkte. Ob zur Montage im Schaltschrank auf DIN-Schiene in der Schutzart IP20 oder direkt im Feld in der Schutzart IP67, die Netzteile liefern Spannung dort, wo sie gebraucht wird. Gerne unterstützen wir Sie bei der weiteren Auswahl.

|  Bezeichnung | Ident.-Nr.  |
| --- | --- |
|  24V Netzteil IP20 |   |
|  BLOCK PC-0124-050-0 | 31001408  |
|  24V Netzteil IP67 |   |
|  TURCK PSU67-12-2480/M | 1524336  |

(c) Bei dem Netzteil IP67 sind konfektionierbare Steckverbinder zum Anschluss an das Netzteil im Lieferumfang enthalten.
<|end_chunk_112|><|start_chunk_113|>
## Switch

![img-81.jpeg](img-81.jpeg)
<|end_chunk_113|><|start_chunk_114|>
## (b) Ethernet 5-Port Switch

Die Switche ermöglichen die einfache Erweiterung eines Hochgeschwindigkeitsnetzwerkes mithilfe kabelgebundener Verbindungen. Mit dem Switch können mehrere SCHUNK-Produkte in ein Netzwerk aufgenommen und so über bspw. eine SPS angesteuert werden.

|  Bezeichnung | Ident.-Nr.  |
| --- | --- |
|  Ethernet Switch |   |
|  D-Link DGS-105 5-Port Ethernet Switch | 1526496  |
<|end_chunk_114|><|start_chunk_115|>
### Page 52<|end_chunk_115|><|start_chunk_116|>
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
(1) 2 (2) $x$ (1)<|end_chunk_116|>
</document>

Respond only with the IDs of the chunks where you believe a split should occur. 
YOU MUST RESPOND WITH AT LEAST ONE SPLIT.
