# RODEOS Semantic Model - Strukturdokumentation

<!-- TOC -->

- [RODEOS Semantic Model - Strukturdokumentation](#rodeos-semantic-model---strukturdokumentation)
    - [Überblick](#%C3%BCberblick)
    - [Grundkonzept: Union Type](#grundkonzept-union-type)
    - [Hierarchische Struktur](#hierarchische-struktur)
        - [Ebene: dcat:Resource Basis](#ebene-dcatresource-basis)
            - [Pflichtfelder mandatory](#pflichtfelder-mandatory)
        - [Ebene: Asset-Typen](#ebene-asset-typen)
    - [A. rodeos:Dataset](#a-rodeosdataset)
        - [Pflichtfelder](#pflichtfelder)
        - [Optionale Felder](#optionale-felder)
    - [B. rodeos:Component](#b-rodeoscomponent)
        - [Pflichtfeld](#pflichtfeld)
        - [B.1 rodeos:hardwareComponent](#b1-rodeoshardwarecomponent)
            - [B.1.1 rodeos:roboter](#b11-rodeosroboter)
                - [rodeos:mobileRobot](#rodeosmobilerobot)
                - [rodeos:stationaryRobot](#rodeosstationaryrobot)
            - [B.1.2 rodeos:tooling](#b12-rodeostooling)
            - [B.1.3 rodeos:controller](#b13-rodeoscontroller)
            - [B.1.4 rodeos:sensor](#b14-rodeossensor)
        - [B.2 rodeos:softwareComponent](#b2-rodeossoftwarecomponent)
    - [C. rodeos:Service](#c-rodeosservice)
        - [Pflichtfelder](#pflichtfelder)
        - [Optionale Felder](#optionale-felder)
    - [Datentypen](#datentypen)
    - [Feldkategorien](#feldkategorien)
        - [Mandatory Pflichtfelder](#mandatory-pflichtfelder)
        - [Optional Optionale Felder](#optional-optionale-felder)
        - [DefaultValues](#defaultvalues)
    - [Hierarchie-Navigation](#hierarchie-navigation)
    - [Verwendungszweck](#verwendungszweck)
    - [Erweiterbarkeit](#erweiterbarkeit)

<!-- /TOC -->

## Überblick

Das RODEOS Semantic Model (`semantic_model.json`) definiert eine hierarchische Struktur zur semantischen Beschreibung von Robotik-Assets. Das Modell basiert auf dem W3C DCAT-3 Standard und erweitert diesen um robotik-spezifische Klassen und Eigenschaften.

## Grundkonzept: Union Type

Das Modell implementiert einen **Union Type** - ein Asset kann genau einer der drei Hauptkategorien angehören:
- `rodeos:Dataset` - Datensätze und Datenprodukte
- `rodeos:Component` - Hardware- oder Software-Komponenten
- `rodeos:Service` - Dienste und Services

Die Auswahl erfolgt über das Pflichtfeld `rodeos:coreType` im Basis-Resource.

## Hierarchische Struktur

### Ebene: dcat:Resource (Basis)

Die Wurzel jedes Assets ist eine `dcat:Resource` mit folgenden Feldern:

#### Pflichtfelder (mandatory)
| Feldname | Datentyp | Beschreibung |
|----------|----------|--------------|
| `dcterms:title` | `xsd:text` | Titel des Assets |
| `dcterms:type` | `skos:concept` | Typ-Klassifikation |
| `dcterms:publisher` | `xsd:text` | Herausgeber/Veröffentlicher |
| `dcterms:license` | `xsd:anyUri` | Lizenz-URI |
| `dcterms:identifier` | `xsd:text` | Eindeutiger Identifikator |
| `dcterms:description` | `xsd:text` | Beschreibung des Assets |
| `dcat:version` | `xsd:text` | Versionsnummer |
| `dcat:keyword` | `List[xsd:text]` | Schlüsselwörter (Liste) |
| `dcat:contactPoint` | `xsd:anyUri` | Kontakt-URI |
| `rodeos:coreType` | `enum[Dataset, Component, Service]` | Asset-Hauptkategorie |

### Ebene: Asset-Typen

Nach Auswahl des `rodeos:coreType` verzweigt sich die Struktur:

## A. rodeos:Dataset

Beschreibt Datensätze, Sensordaten, Logs und Datenprodukte.

### Pflichtfelder
| Feldname | Datentyp | Beschreibung |
|----------|----------|--------------|
| `dprod:informationSensitivityClassification` | `skos:concept` | Sensitivitätsklassifizierung |
| `dprod:type` | `skos:concept` | Datenprodukt-Typ |
| `rodeos:dataFormat` | `xsd:text` | Format der Daten |
| `rodeos:isDataproduct` | `xsd:boolean` | Ist es ein Datenprodukt? |
| `dcat:byteSize` | `xsd:integer` | Größe in Bytes |

### Optionale Felder
| Feldname | Datentyp | Beschreibung |
|----------|----------|--------------|
| `rodeos:dataTypeSchema` | `xsd:anyUri` | Schema-URI |
| `dcat:checksum` | `xsd:hexBinary` | Prüfsumme |
| `dcat:endpointDescription` | `xsd:text` | Endpunkt-Beschreibung |
| `dcat:endpointURL` | `xsd:anyUri` | Endpunkt-URL |
| `dcat:protocol` | `xsd:text` | Übertragungsprotokoll |
| `dprod:dataProductOwner` | `xsd:text` | Datenprodukt-Eigentümer |

## B. rodeos:Component

Komponenten unterteilen sich in Hardware und Software:

### Pflichtfeld
| Feldname | Datentyp | Beschreibung |
|----------|----------|--------------|
| `rodeos:componentType` | `enum[hardwareComponent, softwareComponent]` | Komponententyp |

### B.1 rodeos:hardwareComponent

Hardware-Komponenten haben vier Hauptkategorien:

#### B.1.1 rodeos:roboter
Robotersysteme mit zwei Haupttypen:

##### rodeos:mobileRobot
Mobile Roboter unterteilen sich in:

**rodeos:agv (Automated Guided Vehicle)**
- Optionale Felder:
  - `rodeos:guidanceSystem` (xsd:text) - Führungssystem
  - `rodeos:loadCapacity` (xsd:decimal) - Ladekapazität

**rodeos:amr (Autonomous Mobile Robot)**
- Optionale Felder:
  - `rodeos:navigationSystem` (xsd:text) - Navigationssystem
  - `rodeos:autonomyLevel` (xsd:integer) - Autonomiegrad

##### rodeos:stationaryRobot
Stationäre Roboter mit zwei Kinematik-Typen:

**rodeos:parallelRobot**
Parallelkinematiken:
- `rodeos:hexapod` - Hexapod-Roboter
  - `rodeos:legCount` (xsd:integer) - Anzahl der Beine
  - `rodeos:actuatorType` (xsd:text) - Aktuator-Typ

- `rodeos:delta` - Delta-Roboter
  - `rodeos:armLength` (xsd:decimal) - Armlänge
  - `rodeos:baseDiameter` (xsd:decimal) - Basis-Durchmesser

**rodeos:serielRobot**
Serielle Kinematiken mit fünf Typen:
- `rodeos:cylindrical` - Zylindrische Roboter
- `rodeos:articulated` - Gelenkarmroboter
- `rodeos:scara` - SCARA-Roboter
- `rodeos:cartesian` - Kartesische Roboter
- `rodeos:polarSpherical` - Polar/Sphärische Roboter

#### B.1.2 rodeos:tooling
Werkzeuge und Endeffektoren:

| Typ | Beschreibung | Spezifische Felder |
|-----|--------------|-------------------|
| `rodeos:welding` | Schweißwerkzeuge | weldingType, powerRating |
| `rodeos:gripping` | Greifer | gripForce, gripType |
| `rodeos:cuttingSeparationTool` | Schneid-/Trennwerkzeuge | cuttingSpeed, toolDiameter |
| `rodeos:screwingAssemblyTool` | Schraub-/Montagewerkzeuge | torqueRange, screwSize |
| `rodeos:grindingPolishingFinishingTool` | Schleif-/Polierwerkzeuge | gritSize, rotationSpeed |
| `rodeos:dispensingAdditiveTool` | Dosier-/Additivwerkzeuge | flowRate, materialType |
| `rodeos:measuringInspectionTool` | Mess-/Inspektionswerkzeuge | measurementAccuracy, measurementRange |
| `rodeos:specialTool` | Spezialwerkzeuge | customFunction, specialRequirements |

#### B.1.3 rodeos:controller
Steuerungssysteme:

| Typ | Beschreibung | Spezifische Felder |
|-----|--------------|-------------------|
| `rodeos:robotController` | Robotersteuerung | controlCycles, supportedProtocols |
| `rodeos:plc` | SPS-Steuerung | ioPoints, programmingLanguage |
| `rodeos:ipc` | Industrie-PC | operatingSystem, interfaceTypes |

#### B.1.4 rodeos:sensor
Sensorsysteme:

| Typ | Beschreibung | Spezifische Felder |
|-----|--------------|-------------------|
| `rodeos:visionSensor` | Bildverarbeitungssensoren | resolution, frameRate |
| `rodeos:lidarsensor` | LIDAR-Sensoren | scanRange, angularResolution |
| `rodeos:forceTorqueSensor` | Kraft-/Drehmomentsensoren | forceRange, torqueRange |
| `rodeos:tactileProximitySensor` | Taktile/Näherungssensoren | detectionRange, sensitivity |
| `rodeos:inertialSensor` | Inertialsensoren | accelerometerRange, gyroscopeRange |
| `rodeos:encoder` | Encoder/Drehgeber | pulsesPerRevolution, interfaceType |

### B.2 rodeos:softwareComponent

Software-Komponenten mit sechs Hauptkategorien:

| Typ | Beschreibung | Enum-Werte für Subtyp |
|-----|--------------|------------------------|
| `rodeos:robotOperationSoftware` | Roboterbetriebssoftware | ROS1, ROS2, Orcos, vendorSpecificMiddleware |
| `rodeos:motionControlSoftware` | Bewegungssteuerung | trajectoryPlanning, inverseKinematicSolvers, servoDriverControl |
| `rodeos:perceptionVisionSoftware` | Wahrnehmung/Vision | 2d3dVisionLibraries, objectDetection, slam |
| `rodeos:simulationDigitalTwinSoftware` | Simulation/Digital Twin | physicsEngine, cadKinematics, digitalTwinConnectors |
| `rodeos:aiAnalyticsSoftware` | KI/Analytik | mlModel, dataAnalticsPipeline, reinforcementLearning |
| `rodeos:integrationOrchestration` | Integration/Orchestrierung | workflowOrchestration, dataIntegrationMiddleware, mesErpConnector |

Alle Software-Komponenten haben:
- Pflichtfeld: `aasSubmodel` (xsd:anyUri) - Verweis auf AAS-Submodell
- Verschiedene optionale Felder je nach Typ

## C. rodeos:Service

Beschreibt Dienste und Services.

### Pflichtfelder
| Feldname | Datentyp | Beschreibung |
|----------|----------|--------------|
| `rodeos:usedModels` | `List[xsd:anyUri]` | Verwendete Modelle |
| `rodeos:serviceTypeMain` | `skos:concept` | Haupt-Servicetyp |
| `rodeos:serviceType` | `skos:concept` | Spezifischer Servicetyp |
| `dcat:endpointURL` | `xsd:anyUri` | Service-Endpunkt |

### Optionale Felder
| Feldname | Datentyp | Beschreibung |
|----------|----------|--------------|
| `rodeos:input` | `schema:quantitativeValue` | Eingabeparameter |
| `rodeos:output` | `schema:quantitativeValue` | Ausgabeparameter |
| `dcat:endpointDescription` | `xsd:text` | Endpunkt-Beschreibung |
| `dcat:landingPage` | `xsd:anyUri` | Landing Page |

## Datentypen

Das Modell verwendet folgende Datentypen:

| Datentyp | Beschreibung | Beispiel | Validierung |
|----------|--------------|----------|-------------|
| `xsd:text` | Freitext | "Beliebiger Text" | Keine |
| `xsd:integer` | Ganzzahl | 42 | Nur Ziffern |
| `xsd:decimal` | Dezimalzahl | 3.14 | Ziffern mit optionalem Punkt |
| `xsd:boolean` | Wahrheitswert | true/false | Boolean |
| `xsd:anyUri` | URI/URL | "https://example.com" | URI-Format |
| `xsd:hexBinary` | Hexadezimal | "A1B2C3" | Hex-Zeichen [0-9A-F] |
| `skos:concept` | SKOS-Konzept | "Konzept-ID" | Freitext |
| `schema:quantitativeValue` | Quantitativer Wert | "100 kg" | Freitext |
| `List[...]` | Liste von Werten | ["Wert1", "Wert2"] | Komma-getrennt |
| `enum[...]` | Aufzählung | Einer der definierten Werte | Dropdown-Auswahl |

## Feldkategorien

### Mandatory (Pflichtfelder)
- Müssen ausgefüllt werden
- Definieren die Mindestanforderungen für ein gültiges Asset
- Werden in der UI mit einem Stern (*) gekennzeichnet

### Optional (Optionale Felder)
- Können ausgefüllt werden, sind aber nicht zwingend
- Erweitern die Beschreibung um zusätzliche Details
- Werden in der UI in aufklappbaren Bereichen angezeigt

### DefaultValues
- Vordefinierte Standardwerte für bestimmte Felder
- Hauptsächlich bei Software-Komponenten für AAS-Submodell-Verweise

## Hierarchie-Navigation

Die Struktur folgt einem Entscheidungsbaum:

1. **Start**: dcat:Resource (Basis-Metadaten)
2. **Erste Verzweigung**: Auswahl des coreType (Dataset/Component/Service)
3. **Weitere Verzweigungen**: Je nach gewähltem Pfad
   - Component → Hardware/Software
   - Hardware → Robot/Tooling/Controller/Sensor
   - Robot → Mobile/Stationary
   - Mobile → AGV/AMR
   - Stationary → Parallel/Serial
   - usw.

Jede Ebene kann eigene Pflicht- und optionale Felder haben, die sich zu den Feldern der übergeordneten Ebenen addieren.

## Verwendungszweck

Dieses hierarchische Modell ermöglicht:
- **Standardisierte Beschreibung** von Robotik-Assets
- **Interoperabilität** zwischen verschiedenen Systemen
- **Semantische Suche** und Filterung
- **Automatische Validierung** von Asset-Beschreibungen
- **Konsistente Dokumentation** über verschiedene Robotik-Domänen

## Erweiterbarkeit

Das Modell ist erweiterbar durch:
- Hinzufügen neuer Instanzen auf jeder Ebene
- Ergänzung von optionalen Feldern
- Definition neuer Enum-Werte
- Einbindung zusätzlicher AAS-Submodelle

Die JSON-Struktur ermöglicht eine einfache Erweiterung ohne Breaking Changes für bestehende Implementierungen.