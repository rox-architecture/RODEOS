# Contextualized Document: ROBOCEPTION_rc_randomdot_manual_en_MISTRAL

**Source:** ROBOCEPTION_rc_randomdot_manual_en_MISTRAL.md  
**Processing:** Semantic Chunking + Contextualization  
**Processed by:** Remote LLM via OpenRouter  
**Prompts saved to:** src/contextualEnrichment/prompts/

This document has been processed to create semantic chunks with contextual information for improved search and retrieval.

---

<chunk_context>This is the title and revision section of the rc_randomdot Random Dot Projector's assembly and operating manual, dated November 2024. The document outlines that product specifications and the manual itself may be updated without notice, with the current revision being Rev 1.0 as of November 4, 2024, applicable to Hardware Rev 01. The manual is published by Roboception GmbH, with Effilux listed as the manufacturer.</chunk_context>
<chunk>#### Page 1
 roboception 

Roboception GmbH | November 2024
rc_randomdot Random Dot Projector
ASSEMBLY AND OPERATING MANUAL

### Page 2
 Revisions 

This product may be modified without notice, when necessary, due to product improvements, modifications, or changes in specifications. If such modification is made, the manual will also be revised; see revision information.

DOCUMENTATION REVISION Rev 1.0, Nov 04, 2024
Applicable to rc_randomdot Hardware Rev 01</chunk>

---

<chunk_context>The document is an assembly and operating manual for the rc_randomdot Random Dot Projector, jointly produced by manufacturer Effilux and distributor Roboception GmbH. This section provides contact details for both companies, emphasizing Roboception's role in customer support and distribution. The manual outlines safety, installation, and operational guidelines for the projector, with Effilux handling manufacturing compliance and Roboception managing end-user documentation and support.</chunk_context>
<chunk>## Manufacturer

## Effilux

1, Rue de Terre Neuve
Mini Parc du Verger
Bâtiment E
91940 Les Ulis, France
Web: https://www.effilux.com
Email: contact@effilux.fr
Phone: +33 972381780

## Distributor

## Roboception GmbH

Kaflerstrasse 2
81241 Munich
Germany
CUSTOMER SUPPORT: support@roboception.de | +49 8988950 79-0 (09:00-17:00 CET)

Please read the operating manual in full and keep it with the product.</chunk>

---

<chunk_context>The copyright section emphasizes legal protections for the manual and product under German intellectual property law, prohibiting unauthorized reproduction. It precedes the detailed table of contents, which outlines the manual's structure, covering safety, specifications, installation, and troubleshooting for the rc_randomdot projector. This segment sets the legal framework before diving into technical documentation.</chunk_context>
<chunk>## COPYRIGHT

This manual and the product it describes are protected by copyright. Unless permitted by German intellectual property and related rights legislation, any use and circulation of this content requires the prior consent of the individual owner of the rights. This manual and the product it describes, therefore, may not be reproduced in whole or in part, whether for sale or not, without prior written consent.

Information provided in this document is believed to be accurate and reliable. However, no responsibility is assumed.

Differences may exist between the manual and the product if the product has been modified after the manual's edition date. The information contained in this document is subject to change without notice.

### Page 3
 Contents 

1 Introduction ..... 3
1.1 Overview ..... 4
1.2 Warranty ..... 5
1.3 Applicable standards ..... 6
1.4 Electronical and safety standards ..... 6
1.5 Environmental regulation ..... 7
1.6 Available certificates ..... 8
1.7 Information on disposal ..... 8
2 Safety ..... 9
2.1 General warnings ..... 9
2.2 Intended use ..... 10
3 Hardware specification ..... 11
3.1 Scope of delivery ..... 11
3.2 Technical specification ..... 11
3.3 Mechanical dimensions ..... 12
3.4 Environmental and operating conditions ..... 12
3.5 Power-supply specifications ..... 13
3.6 Wiring ..... 13
3.7 Electrical properties ..... 16
3.8 Optical properties ..... 17
4 Installation ..... 18
4.1 Mounting ..... 18
4.2 Power-up ..... 19
4.3 Operating the projector ..... 19
4.4 Adjusting focus ..... 20
4.5 Adjusting aperture ..... 21
5 Maintenance ..... 22
5.1 Lens cleaning ..... 22
6 Accessories ..... 23
6.1 Connectivity kit ..... 23
6.2 Wiring ..... 23
6.3 Spare parts ..... 24
7 Troubleshooting ..... 25
7.1 LED colors ..... 25
7.2 Hardware issues ..... 25
8 Contact ..... 27
8.1 Support ..... 27
8.2 Address ..... 27
Index ..... 28</chunk>

---

<chunk_context>The document is an assembly and operating manual for the rc_randomdot, a semirandom dot projector designed for use with the rc_visard to enhance scene perception in low-texture environments. This section introduces the manual's structure, safety warnings, and notes, followed by an overview of the projector's purpose and key features, including its compatibility with rc_visard and warranty conditions. The rc_randomdot projects a dot pattern to improve stereo matching, with strict warnings against unauthorized modifications and improper disposal to comply with environmental regulations.</chunk_context>
<chunk>### Page 4
 1 Introduction 

Indications in the manual
To prevent damage to the equipment and ensure the user's safety, this manual indicates each precaution related to safety with Warning. Supplementary information is provided as a Note.

Warning: Warnings in this manual indicate procedures and actions that must be observed to avoid danger of injury to the operator/user, or damage to the equipment. Software-related warnings indicate procedures that must be observed to avoid malfunctions or unexpected behavior of the software.

Note: Notes are used in this manual to indicate supplementary relevant information.

### Page 5
 1.1 Overview 

The dot-matrix projector $r c_{-}$randomdot is specifically tailored to be used with an $r c_{-}$visard. The $r c_{-}$randomdot is utilized when the perception of particularly difficult scenes with little or no natural texture is required. It can be mounted over a scene or directly on any $r c_{-}$visard. By projecting a semirandom dot pattern, it increases the scene density and hence improves the quality of stereo matching when the natural scene texture is low.
![img-0.jpeg](img-0.jpeg)

Fig. 1.1: rc_randomdot White

The terms "projector", "rc_randomdot White", and "rc_randomdot" used throughout the manual all refer to the Effilux rc_randomdot family of semirandom dot projectors with rectangular housing. Installation and control for all projectors are exactly the same, and all use the same mounting base.

Note: This manual uses the metric system and mostly uses the units meter and millimeter. Unless otherwise specified, all dimensions in technical drawings are in millimeters.

### Page 6
 1.2 Warranty 

Any changes or modifications to the hard- and software not expressly approved by Effilux could void the user's warranty and guarantee rights.

Warning: The rc_randomdot utilizes complex hardware technology that may behave in a way not intended by the user. The purchaser must design its application to ensure that any failure of the rc_randomdot does not cause personal injury, property damage, or other losses.

Warning: Do not attempt to take apart, open, service, or modify the rc_randomdot. Doing so could present the risk of electric shock or other hazard. Any evidence of any attempt to open and/or modify the device, including any peeling, puncturing, or removal of any of the labels, will void the Limited Warranty.

Warning: CAUTION: to comply with the European CE requirement, all signal cables used to connect this device must be shielded and the device must be grounded. Operation with incorrect cables may result in interference with other devices or undesired effects of the product.

Note: This product may not be treated as household waste. By ensuring this product is disposed of correctly, you will help to protect the environment. For more detailed information about the recycling of this product, please contact your local authority, your waste disposal service provider, or the product's supplier.</chunk>

---

<chunk_context>The rc_randomdot projector complies with multiple international standards and certifications, including UKCA, TÜV Süd, FCC, and RoHS. It meets IP54 ingress protection and adheres to electromagnetic compatibility (EMC) and safety standards such as EN 55015, EN 61000-6-2, and IEC 62368-1. These approvals ensure the device operates safely in industrial environments without causing or being affected by interference. The broader document outlines technical specifications, installation, and safety guidelines for the projector.</chunk_context>
<chunk>### Page 7
 1.3 Applicable standards 

### 1.3.1 Approvals

The $r c$ randomdot has received the following approvals:
![img-1.jpeg](img-1.jpeg)

UK Conformity Assessed
![img-2.jpeg](img-2.jpeg)

NRTL Safety Certified by TÜV Süd
![img-3.jpeg](img-3.jpeg)

Changes or modifications not expressly approved by the manufacturer could void the user's authority to operate the equipment. This device complies with Part 15 of the FCC rules. Operation is subject to the following two conditions:

1. This device may not cause harmful interference, and
2. this device must accept any interference received, including interference that may cause undesired operation.

IP54 ingress protection according IEC standard 60529

## RoHS

ROHS compliant according to EU directive 2011/65/EU

## 1.4 Electronical and safety standards

The $r c$ randomdot has been tested to be in compliance with the following standards:

### Page 8
- EN 55015:2013 : Electromagnetic compatibility (EMC) Directive (2014/30/EU), Limits and methods of measurement of radio disturbance characteristics of electrical lighting and similar equipment
- CISPR 15:2013 + IS1:2013 + IS2:2013 : Limits and methods of measurement of radio disturbance characteristics of electrical lighting and similar equipment
- EN 61547:2009 : Equipment for general lighting purposes - EMC immunity requirements
- EN 61000-6-2 : Electromagnetic compatibility (EMC): Immunity standard for industrial environments
- EN 61000-6-4 : Electromagnetic compatibility (EMC): Emission standard for industrial environments
- EN/IEC/UL 62368-1:2014 : Audio/Video, Information and Communication Technology Equipment - Safety Requirements
- EN 61010-1 : Safety requirements for electrical equipment for measurement, control, and laboratory use
- CAN/CSA-C22.2 No. 62368-1:2014 Audio/Video, Information and Communication Technology Equipment - Safety Requirements
- EN 62471:2008 / IEC 62471:2008 : Photobiological safety of lamps and lamp systems
- Compliant with FCC 47 CFR Part 15B:2017: Radio Frequency Devices
- Compliant for Canada according to CAN ICES-005(B)/NMB-005(B)</chunk>

---

<chunk_context>The document is an assembly and operating manual for the rc_randomdot random dot projector by Roboception GmbH, detailing technical specifications, safety guidelines, and compliance information. The chunk focuses on environmental regulations, including compliance with the EU RoHS Directive (2011/65/EU) and REACH Regulation (1907/2006/CE), listing restricted hazardous substances and their permissible limits. It also covers disposal procedures for electronic waste (WEEE), including manufacturer return options and data protection responsibilities. This section aligns with the manual’s broader emphasis on regulatory adherence and environmental safety, complementing earlier sections on certifications (e.g., UKCA, TÜV Süd) and later sections on hardware specifications and safety warnings. Key details include the WEEE registration number (DE 33323989) and the absence of batteries in the device.</chunk_context>
<chunk>1.5 Environmental regulation 

### 1.5.1 EU RoHS Directive

As supplier of LED lighting systems, EFFILUX declares that the products manufactured by Effilux are compliant with the EU RoHS 2 Directive 2011/65/EU on the restriction of the use of certain hazardous substances in electrical and electronic equipment:

- Lead $(<0.1 \%)$
- Mercury $(<0.1 \%)$
- Cadmium $(<0.01 \%)$
- Hexavalent Chromium $(<0.1 \%)$
- Polybromobiphényles (PBB) $(<0.1 \%)$
- Polybromodiphényléthers (PBDE) $(<0.1 \%)$

Items that are exempted in the RoHS Directive are excluded from these standards.

### 1.5.2 REACH Regulation

As supplier of LED lighting systems, EFFILUX declares that the products manufactured by Effilux are compliant with REACH Regulation 1907/2006/CE. These products are not classified as hazardous. We hereby certify that these products do not contain any Substance of Very High Concern (SVHC) in amounts $>0.1 \%(\mathrm{w} / \mathrm{w})$.

### Page 9
 1.6 Available certificates 

Copies of the various certificates can be downloaded from https://roboception.com/product/ random-dot-projector.

### 1.7 Information on disposal

## 1. Disposal of Waste Electrical \& Electronic Equipment

This symbol on the product(s) and / or accompanying documents means that used electrical and electronic products should not be mixed with general household waste. For proper treatment, recovery and recycling, please contact your supplier or the manufacturer. Disposing of this product correctly will help save valuable resources and prevent any potential negative effects on human health and the environment, which could otherwise arise from inappropriate waste handling.

## 2. Removal of batteries

If the products contain batteries and accumulators that can be removed from the product without destruction, these must be removed before disposal and disposed of separately as batteries.
The following batteries or accumulators are contained in the rc_randomdot: None

## 3. Options for returning old equipment

Owners of old devices can return them to the manufacturer to ensure proper disposal.
Please contact support (Section 8) about returning the device for disposal.

## 4. Data protection

End users of Electrical \& Electronic Equipment are responsible for deleting personal data on the waste equipment to be disposed of.

## 5. WEEE registration number

Roboception is registered under the registration number DE 33323989 at the stiftung elektroaltgeräte register, Nordostpark 72, 90411 Nuremberg, Germany, as a producer of electrical and/or electronic equipment.

## 6. Collection and recovery quotas

According to the WEEE Directive, EU member states are obliged to collect data on waste electrical and electronic equipment and to transmit this data to the European Commission. Further information can be found on the German Ministry for the Environment website.

## Information on Disposal outside the European Union

This symbol is valid only in the European Union. If you wish to discard this product please contact your local authorities or dealer and ask for the correct method of disposal.</chunk>

---

<chunk_context>The safety section outlines critical warnings and operational guidelines for the rc_randomdot projector, emphasizing proper handling, installation, and compliance with safety standards. It specifies the device's intended use with the rc_visard for enhancing stereo matching in low-texture environments, while explicitly excluding safety-critical applications. Key warnings include avoiding direct beam exposure, proper mounting, and adherence to environmental and electrical specifications (e.g., IP54 rating, 30 m cable limit, EN 62368-1 power supply). The section also highlights the need for risk assessments in robotic applications and compliance with local regulations. This aligns with the manual's broader focus on operational safety, technical specifications, and legal requirements.</chunk_context>
<chunk>### Page 10
 2 Safety 

Warning: The operator must have read and understood all of the instructions in this manual before handling the rc_randomdot product.

Warning: If operating the rc_randomdot with rc_visard product(s), the operator must have read and understood all of the safety, installation, and maintenance instructions given in the rc_visard manual.

Note: The term "operator" refers to anyone responsible for any of the following tasks performed in conjunction with rc_randomdot:

- Installation
- Maintenance
- Inspection
- Calibration
- Programming
- Decommissioning

This manual explains the rc_randomdot's various components and general operations regarding the product's whole life-cycle, from installation through operation to decommissioning.
The drawings and photos in this documentation are representative examples; differences may exist between them and the delivered product.

### 2.1 General warnings

Note: Any use of the rc_randomdot in noncompliance with these warnings is inappropriate and may cause injury or damage as well as void the warranty.

## Warning:

- Do not look directly into the projected beam. Do not look at the beam with an optical instrument.
- Looking at the sun through the lens might cause damage to the eyes. Directing the lens at the sun might start a fire.
- The rc_randomdot is protected according to IP54. High humidity or temperature can damage the device. Do not operate in an environment where combustible or explosive fumes may occur.
- The rc_randomdot needs to be properly mounted before use.

### Page 11
- The supplied mounting bracket is not suitable to mount the rc_randomdot on a robot.
- All cable sets need to be secured to the rc_randomdot and the mount.
- Cables must not be longer than 30 m .
- An appropriate power supply, which conforms to the EN 62368-1 standard must be used to supply power to the rc_randomdot.
- Check polarity and connections.
- The rc_randomdot's housing must be grounded.


 Warning: 

- The rc_randomdot's and any related equipment's safety guidelines must always be satisfied.
- The rc_randomdot does not fall under the purview of the machinery or medical directives.

Risk assessment and final application: The rc_randomdot may be used on a robot together with an rc_visard. Robot, rc_visard, rc_randomdot, and any other equipment used in the final application must be evaluated with a risk assessment. The system integrator's duty is to ensure respect for all local safety measures and regulations. Depending on the application, there may be risks that need additional protection/safety measures.

### 2.2 Intended use

The rc_randomdot is intended to be used in combination with a Roboception rc_visard to increase the scene density and hence improve the quality of stereo matching when the natural scene texture is low. The rc_randomdot together with a Roboception rc_visard are intended for installation on a robot, automated machinery, mobile platform, or stationary equipment. They can also be used for data acquisition in other applications.

Warning: The rc_randomdot is NOT intended for safety critical applications.

The rc_randomdot may be used only within the scope of its technical specification. Any other use of the product is deemed unintended use. Roboception will not be liable for any damages resulting from any improper or unintended use.

Warning: Always comply with local and/or national laws, regulations and directives on automation safety and general machine safety.</chunk>

---

<chunk_context>The rc_randomdot's hardware specifications detail its components, technical parameters, and operational requirements. Key features include a 24V power supply (22-29V range), 62°×48° field of view, and IP54 protection, with strict environmental operating conditions (0°C to 45°C). Wiring and GPIO configurations are specified for integration with the rc_visard, including pin assignments for power and signal transmission. These specifications align with the manual’s broader focus on installation, safety, and industrial application guidelines.</chunk_context>
<chunk>### Page 12
 3 Hardware specification 

Note: The following hardware specifications are provided here as a general reference; differences with the product may exist.

### 3.1 Scope of delivery

Standard delivery for an $r c_{-}$randomdot includes the $r c_{-}$randomdot projector, the mounting bracket and 4 screws, a 30 cm cable to connect the $r c_{-}$randomdot to the $r c_{-}$visard, and a quickstart guide.
The full manual is available in digital form at https://www.roboception.com/documentation.
The following picture shows the important parts of the rc_randomdot which are referenced later in the documentation.
![img-4.jpeg](img-4.jpeg)

Fig. 3.1: Parts description

### 3.2 Technical specification

Table 3.1: Technical specifications for the rc_randomdot White

|  | rc_randomdot |
| :-- | :-- |
| Illumination Mode | Strobe |
| Wavelength | White $(5500 \mathrm{~K})$ |
| Working distance | 500 mm to 3000 mm |
| Field of View | $62^{\circ} \times 48^{\circ}$ (diagonal $75^{\circ}$ ) |
| Lens (C-Mount) | $1^{\prime \prime}, 12 \mathrm{~mm}, \mathrm{f}$ min 1:1.4 |
| Lens Type | VS Technology VS-1214H1 |
| Power supply | 24 V (22 V to 29 V), 44 W (68 W including $r c_{-}$visard $)$ |
| Connectors | M12, 8 Pin, A-coded |
| Size $(\mathrm{W} \times \mathrm{H} \times \mathrm{L})$ | $70 \mathrm{~mm} \times 70 \mathrm{~mm} \times 152 \mathrm{~mm}$ |
| Weight | $\sim 660 \mathrm{~g}$ |

### Page 13
 3.3 Mechanical dimensions 

![img-5.jpeg](img-5.jpeg)

Fig. 3.2: Overall dimensions of the rc_randomdot White

CAD models of the rc_randomdot can be downloaded from https://www.roboception.com/download. The CAD models are provided as-is, with no guarantee of correctness.

### 3.4 Environmental and operating conditions

The rc_randomdot is designed for industrial applications. Always respect the storage, transport, and operating environmental conditions outlined in Table 3.2.

Table 3.2: Environmental conditions

|  | rc_randomdot |
| :-- | :-- |
| Storage/Transport temperature | $-25^{\circ} \mathrm{C}$ to $70^{\circ} \mathrm{C}$ |
| Operating temperature | $0^{\circ} \mathrm{C}$ to $45^{\circ} \mathrm{C}$ |
| Relative humidity (non condensing) | $20 \%$ to $80 \%$ |
| Vibration | 2.5 g |
| Shock | 25 g |
| Protection class | IP54 |
| Others | - Free from corrosive liquids or gases |
|  | - Free from explosive liquids or gases |
|  | - Free from powerful electromagnetic interference |
|  |  |

The rc_randomdot is designed for an operating temperature (surrounding environment) of $0^{\circ} \mathrm{C}$ to 45 ${ }^{\circ} \mathrm{C}$ and relies on convective (passive) cooling. Unobstructed airflow, especially around the cooling fins, needs to be ensured during use. The rc_randomdot should only be mounted on top of the rc_visard

### Page 14
using the provided mechanical mounting interface, and all parts of the housing must remain uncovered. A free space of at least 10 cm extending in all directions from the two devices, and sufficient air exchange with the environment is required to ensure adequate cooling. Cooling fins must be free of dirt and other contamination.

The housing temperature depends on the exposure time, exposure mode, sensor orientation, and surrounding environmental temperatures. When the projector's power LED temperature exceeds $75^{\circ} \mathrm{C}$ (corresponding to a housing temperature of approximately $60^{\circ} \mathrm{C}$ ), the LED at the front will turn red.

 3.5 Power-supply specifications 

The rc_randomdot needs to be supplied by a DC voltage source and will in turn power a connected rc_visard. The rc_randomdot's standard package doesn't include a DC power supply. The power supply contained in the connectivity kit may be used for initial setup. For permanent installation, it is the customer's responsibility to provide suitable DC power. Each rc_randomdot and rc_visard pair must be connected to a separate power supply. Connection to domestic grid power is only allowed through a power supply according EN 62368-1.

Table 3.3: Absolute maximum ratings for power supply

|  | Min | Nominal | Max |
| :-- | :-- | :-- | :-- |
| Supply voltage | 22.0 V | 24 V | 29.0 V |
| Max power consumption |  |  | 40 W |
| Max power consumption during exposure <br> incl. rc_visard |  |  | 65 W |
| Overcurrent protection | Supply must be fuse-protected to a maximum of 2 A |  |  |
| Standards compliance | see Electronical and safety standards (Section 1.4) |  |  |

Warning: Exceeding maximum power rating values may lead to damage to the rc_randomdot, rc_visard, power supply, and connected equipment.

Warning: A separate power supply must power each rc_randomdot and rc_visard pair.

Warning: Connection to domestic grid power is allowed through a power supply certified according to EN 62368 and as EN55011 Class B only.

### 3.6 Wiring

Only a 30 cm cable connecting the $r c \_r a n d o m d o t$ to the $r c \_v i s a r d$ is supplied with the standard package. It is the customer's responsibility to obtain the proper cabling for connecting the $r c \_r a n d o m d o t$ to power. A suggestion of components can be found in Accessories (Section 6) .

Warning: Proper cable management is mandatory. Cabling must always be secured to the $r c \_v i s a r d$ and $r c \_r a n d o m d o t$ base with a strain-relief clamp so that no forces due to cable movements are exerted on the devices' M12 connectors. In robotic applications, enough slack needs to be provided to allow for full range of movement of the $r c \_v i s a r d$ and $r c \_r a n d o m d o t$ without straining the cables. The cables' minimum bend radii need to be observed.

### Page 15
The rc_randomdot provides an industrial 8-pin A-coded M12 plug connector for power and GPIO connectivity and an 8-pin A-coded M12 socket connector for connectivity to the rc_visard. Both connectors are located on the left side of the rc_randomdot as indicated in Fig. 3.1. Type and orientation of the connectors is shown in Fig. 3.3.

Connectors are rotated so that standard $90^{\circ}$ angled connectors will exit horizontally, towards the back of the projector.

The power supply must be connected to the top (plug) M12 connector of the rc_randomdot. Make sure to check the polarity of your power supply as reverse polarity will damage the rc_randomdot. The bottom (socket) M12 connector is connected to the bottom M12 connector of the rc_visard with the supplied 30 cm M12 shielded cable.
![img-6.jpeg](img-6.jpeg)

 Power In <br> M12 8-pin plug <br> A-coded, view towards rc_randomdot 

![img-7.jpeg](img-7.jpeg)

Power to rc_visard
M12 8-pin receptacle
A-coded, view towards rc_randomdot

Fig. 3.3: Pin positions for Power IN/GPIO (top) and rc_visard (bottom) connector

Pin assignments for the Power IN connector are given in Table 3.4.
Table 3.4: Pin assignments for the Power IN connector

| Pin | Assignment | Reference |
| :-- | :-- | :-- |
| 1 | N/C | $/$ |
| 2 | +24 V Power IN | GND |
| 3 | GPIO In 1 Robot | GPIO GND |
| 4 | GPIO GND | GPIO GND |
| 5 | GPIO Vcc | chassis GND |
| 6 | GPIO Out 1 Robot (image exposure) | chassis GND |
| 7 | GND | GND |
| 8 | GPIO Out 2 | chassis GND |

Pin assignments for the rc_visard connector are given in Table 3.5.

### Page 16
Table 3.5: Pin assignments for the rc_visard connector

| Pin | Assignment | Reference |
| :-- | :-- | :-- |
| 1 | GPIO Out 2 (Overtemp): $1=\mathrm{OK}(24 \mathrm{~V}), 0=\mathrm{IOK}(0 \mathrm{~V})$ | chassis GND |
| 2 | +24 V Power OUT | GND |
| 3 | GPIO Out 1 | chassis GND |
| 4 | GND (GPIO GND) | GND |
| 5 | +24 V (GPIO Vcc) | GND |
| 6 | GPIO In 1 (Light Trigger) | GND |
| 7 | GND | GND |
| 8 | GPIO In 2 | GND |

All GPIOs are decoupled by photocoupler. GPIO In 1 needs to be connected to the rc_visard GPIO Out 1 signal, which can be set to provide an exposure sync signal using the rc_visard's IOControl module. A logic high level of the rc_visard's GPIO Out 1 signal triggers the projector light. The projector is ON as long as GPIO In 1 is HIGH.

GPIO Out 2 of the projector provides a 'projector present' signal that is high when an rc_randomdot projector is connected to the $r c \_v i s a r d$ and operating normally. The signal will transition to low during fault (overtemperature) conditions. The status of the $r c \_v i s a r d$ GPIOs is available in every image via the GigE Vision "Chunk Data". For more details, please refer to https://doc.rc-visard.com/latest/en/ gigevision.html\#chunk-data.</chunk>

---

<chunk_context>The section details GPIO pin behavior and electrical properties of the rc_randomdot projector, including signal mirroring between GPIO pins and voltage limits (max 29V). It transitions into projector control specifics, such as LED pulsing behavior (2.2A max current, 25ms minimum off-time) and exposure time constraints (15ms max in ExposureActive mode). This leads into optical properties (50% density dot pattern) and installation guidelines, connecting hardware operation to practical setup requirements like focus/aperture adjustment and mounting. The content bridges technical specifications (Section 3) with installation procedures (Section 4), emphasizing safety and performance optimization.</chunk_context>
<chunk>Note: 

- The state of the rc_randomdot GPIO In 1 is mirrored to GPIO Out 1 Robot
- The state of the rc_randomdot GPIO In 2 is mirrored to GPIO Out 2 Robot
- The state of the rc_randomdot GPIO In 1 Robot is mirrored to GPIO Out 1

Pins of unused GPIOs should be left floating.
GPIO circuitry and specifications are shown in Fig. 3.4. The maximum rated voltage for GPIO In and GPIO Vcc is 29 V .
![img-8.jpeg](img-8.jpeg)

Fig. 3.4: GPIO circuitry and specifications - do not connect signals higher than 29 V

### Page 17
Warning: Do not connect signals with voltages higher than 29 V to the rc_randomdot.

 3.7 Electrical properties 

The power LED driver inside the rc_randomdot is set to automatically pulse the LED according to the state of the GPIO In 1 trigger pin.
For a short trigger pulse ( $<25 \mathrm{~ms}$ ), the projector is driven at maximum power (projector LED maximum current of $2,2 \mathrm{~A}$ ). If the pulse is longer, the driver automatically decreases projector LED current to 0,4 A ( $18 \%$ of max current) to protect the projector LED against damage.
![img-9.jpeg](img-9.jpeg)

Fig. 3.5: Timing of the projector LED with respect to the rc_randomdot GPIO In 1 pin

Fig. 3.5 shows the timing properties of the rc_randomdot projector LED with respect to the rc_randomdot's GPIO In 1. Please note that the rc_randomdot must be turned off for a minimum of 25 ms between light pulses. This limits the maximum allowed exposure time of the connected rc_visard to 15 ms in ExposureActive mode to prevent overheating of the rc_randomdot. It is the user's responsibility to limit the exposure time of the rc_visard accordingly. In ExposureAlternateActive mode, the full 18 ms exposure time of the rc_visard may be used as only every second exposure triggers the rc_randomdot.
For an in depth description of rc_visard projector control settings and operating modes, please refer to the IO and Projector Control section in the full rc_visard documentation at https://doc.rc-visard.com/ latest/en/iocontrol.html .

Warning: In ExposureActive mode, the exposure time of the rc_visard must be limited to a maximum of 15 ms to prevent overheating of the rc_randomdot. It is the user's responsibility to ensure this setting.

### Page 18
Table 3.6: Status LED colors

| Status LED color | rc_randomdot |
| :-- | :-- |
| Red | Overtemperature warning projec- <br> tor LED temperature $>75^{\circ} \mathrm{C}$ |
| Green | Power ON |
| Blue | Trigger Signal active, projector <br> LED ON |

 3.8 Optical properties 

The $r c \_r a n d o m d o t$ projects a rectangular pattern of semirandom dots with $50 \%$ density. Optimal working distance is between 500 mm and 3 m . Focus and the aperture can be adjusted with manual settings of the C -mount lens.
![img-10.jpeg](img-10.jpeg)

Fig. 3.6: Projected pattern of semirandom dots with 50\% density

RandomDot-000 - Spectrum
![img-11.jpeg](img-11.jpeg)

Fig. 3.7: Emission spectrum of the $r c \_r a n d o m d o t$ White

### Page 19
 4 Installation 

Warning: The instructions on Safety (Section 2) related to the rc_randomdot and rc_visard must be read and understood prior to installation.

### 4.1 Mounting

The rc_randomdot offers a mounting-point setup with standard tripod thread at the bottom, and pivot points for the provided mounting bracket on either side.
![img-12.jpeg](img-12.jpeg)

Fig. 4.1: Mounting bracket for connecting the $r c \_$randomdot to the $r c \_v i s a r d$

For troubleshooting purposes, the projector may be mounted using the standardized tripod thread (UNC $1 / 4$ "-20) at the bottom of the housing. For mounting the $r c \_$randomdot on top of an $r c \_v i s a r d$ in static or low dynamic applications (e.g. above robot cells or on mobile platforms), the supplied mounting bracket must be attached to the $r c \_v i s a r d$ with two M4 x 108.8 machine screws, and the projector must be attached to the mounting bracket with two M4 x 108.8 machine screws at the pivot points. All screws must be tightened to 2.4 Nm and only TufLok nylon coated screws may be used. Alternatively screws need to be secured with a medium-strength threadlocking adhesive such as Loctite 243. Maximum thread depth is 6 mm . The supplied mounting bracket is not suitable for dynamic robot applications. It is the customer's responsibility to provide adequate mounting of the $r c \_$randomdot.

### Page 20
Warning: For permanent installations, the rc_randomdot must be mounted with four M4 x 10 8.8 machine screws tightened to 2.4 Nm torque. Screws must be Tuflok coated or secured with threadlocking adhesive. Do not use high-strength bolts.

Warning: The supplied mounting bracket is not suitable for dynamic robot applications. It is the customer's responsibility to provide adequate mounting of the rc_randomdot.

Depending on the working distance, it might be necessary to tilt the projector downwards to cover the complete filed of view of the rc_visard. This can be accomplished by loosening the screws attaching the rc_randomdot to the mounting bracket at the pivot point, and moving the rc_randomdot to the desired angle.
![img-13.jpeg](img-13.jpeg)

Fig. 4.2: Setting the desired tilt angle between $r c \_$randomdot and $r c \_v i s a r d$

 4.2 Power-up 

Note: Always fully connect and tighten all M12 connectors on the both the rc_visard and $r c \_$randomdot before turning on the power supply.

After connecting the system to power, the LEDs on the front of the $r c \_$randomdot and $r c \_v i s a r d$ should immediately illuminate. During the $r c \_v i s a r d$ 's boot process, it's LED will change color and will eventually turn green. This signals that all processes are up and running. The $r c \_r a n d o m d o t$ 's status LED should turn green right away. The $r c \_r a n d o m d o t$ projector will flash a number of times during the boot process.

Warning: Do not look into the lens of the $r c \_r a n d o m d o t$ or into the light beam at any point during startup or operation.

For troubleshooting the $r c \_v i s a r d$ 's boot process and connections, please refer to the $r c \_v i s a r d$ documentation at https://doc.rc-visard.com/latest/en/troubleshooting.html\#led-colors.

### 4.3 Operating the projector

The $r c \_r a n d o m d o t$ projector is controlled via the GPIO Out 1 of the $r c \_v i s a r d$.

### Page 21
For a tutorial on operating the projector, please refer to: https://tutorials.roboception.de/rc_visard_ general/projector.html.

Note: A valid IOControl license is required on the rc_visard. It is included in the standard onboard software package of all rc_visards purchased 07/2020 and thereafter. For upgrading an older rc_visard, please obtain your license at https://roboception.com/product/rc_reason-iocontrol.

State and behavior of the rc_visard's GPIOs can then be controlled via the rc_visard's WebGUI IOControl panel from the Modules tab. Starting with rc_visard firmware 20.10, GPIO Out 1 is set to Low by default, turning the projector off. ExposureActive turns on the rc_randomdot for exactly the exposure time of every image. High will turn the projector on continuously, but reduce power to $18 \%$ to protect the light source.

Typically, the user will select ExposureAlternateActive mode, in which the rc_randomdot is on only for the exposure time of every second image. Images with projected pattern are used for computing depth images. Images without pattern can be used for texture or other image processing modules.
In ExposureAlternateActive mode, the rc_visard's auto exposure algorithm ensures that images with pattern are correctly exposed in order to produce dense disparity images. As identical exposure settings are used for the images without pattern, which are displayed in the WebGUI, those might be underexposed depending on overall illumination conditions. This effect can be minimized by properly adjusting environmental light conditions, projector lens aperture, and exposure time.

 4.4 Adjusting focus 

During production, the focus of the rc_randomdot is set to a distance 1.2 m by default. When the projector is used for a very different working distance, adapting the focus might be necessary. Perfectly focusing the projector is not crucial. A slightly blurred projection pattern will not degrade the depth image.

To inspect the sharpness of the projector pattern, the projector should be turned on permanently by setting the Out1 / Projector mode to High on the Web GUI under Camera $\rightarrow$ IOControl Settings or Configuration $\rightarrow$ IOControl.

The projector focus only needs to be adjusted when the projector pattern is strongly blurred. In this case, remove the rc_randomdot's protective lens cap by unscrewing it. Then loosen the three small fixing Phillips screws on the focus ring as shown in Fig. 4.3. Then, turn the focus ring until the visible projector pattern becomes sharp. After that, lightly tighten the focus ring screws again and replace the protective lens cap to restore the IP54 rating and EMC compatibility of the projector.
![img-14.jpeg](img-14.jpeg)

Fig. 4.3: Focus and aperture ring on the rc_randomdot White

### Page 22
 4.5 Adjusting aperture 

The aperture of the rc_randomdot influences the brightness of the projector pattern. By default, the aperture of the $r c$ _randomdot is fully open, which means the projector has maximum brightness. The aperture should be adjusted so that the brightness difference between images taken with projector and images taken without projector is not too large, but the projector pattern is still visible in the images taken with projector. To find the correct setting, make sure the external light in the working environment is similar to what is expected during productive mode and the camera with the $r c$ _randomdot is mounted at the desired distance from the scene.

Then, on the Web GUI under Camera, set the Exposure mode to Auto and set the Auto Exposure Mode to AdaptiveOut1. Also set the Out1 / Projector mode to ExposureAlternateActive under IOControl Settings, so that every second image is taken with projector pattern. Now, the text line under the live images shows the Out1 reduction value in percent.

The Out1 reduction value describes the reduction of the brightness of the image without projection compared to the image with projection. The value should be between $10 \%$ and $20 \%$. A higher Out1 reduction value means, that the projector is too bright compared to the external lighting, which leads to images without projector patterns being too dark. Thus, external lighting should be increased, e.g. by installing an additional light source, or the brightness of the projector should be reduced by slightly closing the aperture. In analogy, if the Out1 reduction value is too low, the projector is not bright enough compared to the external light, which means that the projector pattern will hardly be visible in the camera images and cannot enhance the depth computation. So the external light should be reduced or the projector brightness must be increased by opening the aperture.

The aperture of the projector can be adjusted by removing the $r c$ _randomdot's protective lens cap by unscrewing it. Then loosen the three small fixing Phillips screws on the aperture ring as shown in Fig. 4.3. Now turn the ring until the Out1 reduction value is in the range between $10 \%$ and $20 \%$.

After that, the darkest object that is possible in the application should be placed in the field of view of the camera. If the dark object is not properly visible in the depth image, then the projector brightness must be increased, despite high Out1 reduction values.

In the end, lightly tighten the aperture ring screws again and replace the protective lens cap to restore the IP54 rating and EMC compatibility of the projector.</chunk>

---

<chunk_context>The maintenance section details user-accessible procedures like lens cleaning and focus/aperture adjustments, emphasizing safety warnings against unauthorized housing access. It transitions into accessories, listing connectivity kits (cables, power supplies) and wiring solutions for the rc_randomdot projector, with specific part numbers and compliance standards (EN 55011/55032 Class B). The document underscores customer responsibility for permanent installations and industrial power supply requirements, noting the lack of user-serviceable spare parts. These sections align with the manual’s broader focus on safe operation, technical specifications, and regulatory compliance (e.g., IP54, EMC). Key details include the 24V/60W power supply and 30m cable limit.</chunk_context>
<chunk>### Page 23
 5 Maintenance 

Warning: The only part removable by the customer is the lens cap, which can be unscrewed. The customer does not need to open the rc_randomdot's housing to perform maintenance. Unauthorized opening of the housing will void the warranty. For all maintenance operations other than adjusting focus and aperture, the product must be switched off.

To handle the optical components, wearing gloves is strongly recommended. The lens cap can be removed by unscrewing the barrel. Then focus and the aperture can be adjusted with manual settings of the C -mount lens.

Warning: The lens cap needs to be in place during normal operation to meet EMC requirements.

### 5.1 Lens cleaning

Glass lenses with antireflective coating are used to reduce glare. Please take special care when cleaning the lenses. To clean them, use a compressed air duster or soft lens-cleaning brush to remove dust or dirt particles. To remove stubborn dirt, wipe 1-2 drops of a non-alcohol-based lens cleaning solution formulated for coated lenses (such as the Uvex Clear family of products) in a gentle circular motion with a cleaning tissue. Always apply the fluid to a tissue rather than the lens itself.

### Page 24
 6 Accessories 

### 6.1 Connectivity kit

Roboception offers an optional connectivity kit to aid customers with setting up the rc_visard and rc_randomdot. The connectivity kit consists of a:

- network cable with straight M12 plug to straight RJ45 connector in either $2 \mathrm{~m}, 5 \mathrm{~m}$, or 10 m length,
- power adapter cable with straight M12 socket to DC barrel connector in 30 cm length,
- $24 \mathrm{~V}, 60 \mathrm{~W}$ desktop power supply.

For permanent installation, the customer is responsible for providing a suitable power supply.
Connecting the $r c \_v i s a r d$ and $r c \_r a n d o m d o t$ to residential or office grid power requires a power supply that meets EN 55011 Class B emission standards and/or EN 55032 Class B emission standards. The power supply contained in the connectivity kit is certified accordingly. However, it does not meet immunity standards for industrial environments under EN 61000-6-2.

### 6.2 Wiring

Only a short cable to connect power and GPIOs between $r c \_v i s a r d$ and $r c \_r a n d o m d o t$ is supplied as standard equipment with the $r c \_r a n d o m d o t$. It can be used for permanently connecting an $r c \_v i s a r d$ to an $r c \_r a n d o m d o t$ mounted on top of it. It is the customer's responsibility to obtain appropriate parts for all other scenarios. The following sections provide an overview of suggested components.

### 6.2.1 Power connections

The $r c \_r a n d o m d o t$ contains an 8-pin A-coded M12 plug connector for power and GPIO connectivity to the robot controller. Various cabling solutions can be obtained from third party vendors. A selection of M12 to open ended cables is provided below. Customers are required to provide power and GPIO connections to the cables according to the pinouts described in Wiring (Section 3.6). Both the rc_visard's and $r c \_r a n d o m d o t$ 's housing must be connected to ground.

## Sensor/Actor cable M12 socket to open end

- Straight M12 socket connector to open end, shielded, 10m length: Phoenix Contact SAC-8P-10,0PUR/M12FS SH, Art.Nr.: 1522891
- Angled M12 socket connector to open end, shielded 10m length: Phoenix Contact SAC-8P-10,0PUR/M12FR SH, Art.Nr.: 1522943


## Sensor/Actor M12 socket for field termination

- Phoenix Contact SACC-M12FS-8CON-PG9-M, Art.Nr.:1513347
- TE Connectivity T4110001081-000 (plastic housing)

### Page 25
 6.2.2 Power supplies 

The $r c \_v i s a r d$ and $r c \_r a n d o m d o t$ are classified as EN-55011 Class B devices and are immune to light industrial and industrial environments. For connecting the sensor to residential grid power, a power supply under EN 55011/55022 Class B has to be used.

It is the customer's responsibility to obtain and install a suitable power supply for permanent use in industrial environments. One example that satisfies both EN 61000-6-2 and EN 55011/55022 Class B is the DIN-Rail mounted PULS MiniLine ML70.100 24V/DC 3 A by PULS GmbH (http://www.pulspower. com). A certified electrician must perform installation.

Only one set of $r c \_v i s a r d$ and $r c \_r a n d o m d o t$ shall be connected to a power supply at any time, and the total length of cables must be less than 30 m .

### 6.3 Spare parts

No user-serviceable spare parts are currently available for $r c \_r a n d o m d o t$ devices.</chunk>

---

<chunk_context>The troubleshooting section details LED color indicators (red, blue, green) for the rc_randomdot projector, covering issues like overtemperature warnings, power faults, and hardware malfunctions. It follows hardware specifications (Section 3) and installation guidelines (Section 4), providing actionable steps for resolving common operational problems. The section concludes with contact information for Roboception GmbH, linking back to the document’s broader purpose as an assembly and operating manual. Key details include temperature thresholds (75°C), voltage ranges (22–29V), and cooling requirements (10cm clearance).</chunk_context>
<chunk>### Page 26
 7 Troubleshooting 

### 7.1 LED colors

During the boot process of the rc_visard, the rc_randomdot will flash several times. The status LED will should turn green almost immediately. During normal operation the following colors of the rc_randomdot can be observed.

Table 7.1: rc_randomdot status LED colors

| LED color | rc_randomdot status |
| :-- | :-- |
| red | Overtemperature Warning: Projector temperature has exceeded $75^{\circ} \mathrm{C}$ |
| blue | Trigger signal active |
| green | rc_randomdot is ready |

### 7.2 Hardware issues

## LED does not illuminate

The rc_randomdot does not start up.

- Ensure that cables are connected and secured properly.
- Ensure that adequate DC voltage ( 22 V to 29 V ) with correct polarity is applied to the power connector at the pins labeled as Power and Ground as described in the device's pin assignment specification (Section 3.4). Connecting the sensor to voltage outside of the specified range, to alternating current, with reversed polarity, or to a supply with voltage spikes will lead to permanent hardware damage.


## LED turns red while the projector appears to function normally

This may indicate a high housing and power LED temperature. The projector might be mounted in a position that obstructs free airflow around the cooling fins.

- Clean cooling fins and housing.
- Ensure a minimum of 10 cm free space in all directions around cooling fins to provide adequate convective cooling.
- Ensure that ambient temperature is within specified range.

The projector may turn off when cooling is insufficient or the ambient temperature exceeds the specified range.

## Reliability issues and/or mechanical damage

This may be an indication of ambient conditions (vibration, shock, resonance, and temperature) being outside of specified range. Please refer to the specification of environmental conditions (Section 3.2).

- Operating the rc_randomdot outside of specified ambient conditions might lead to damage and will void the warranty.

### Page 27
 Electrical shock when touching the projector 

This indicates an electrical fault in sensor, cabling, or power supply or adjacent system.

- Immediately turn off power to the system, disconnect cables, and have a qualified electrician check the setup.
- Ensure that the projector housing is properly grounded; check for large ground loops.

### Page 28
 8 Contact 

### 8.1 Support

For support issues, please see https://www.roboception.com/support or contact support@roboception.de.

### 8.2 Address

Roboception GmbH
Kaflerstrasse 2
81241 Munich
Germany

Web: https://www.roboception.com
Email: info@roboception.de
Phone: +49 8988950 79-0</chunk>

---

<chunk_context>The index provides an alphabetical reference to key terms, concepts, and sections in the rc_randomdot manual, linking them to specific page numbers for quick navigation. It covers technical specifications (e.g., dimensions, GPIO pin assignments), operational modes (e.g., ExposureActive), and maintenance topics (e.g., lens cleaning). This aids users in locating detailed information efficiently within the broader document.</chunk_context>
<chunk>### Page 29
 Index 

## A

aperture, 21

## C

cables, 13, 23
CAD model, 12
components
rc_randomdot, 11
cooling, 12

## D

dimensions
rc_randomdot, 12

## E

electrical, 16
ExposureActive
IOControl, 19
ExposureAlternateActive
IOControl, 19

## F

field of view, 11
focus, 20

## G

GPIO
pin assignments, 14

## H

High
IOControl, 19
housing temperature
LED, 13
humidity, 12

## I

installation, 18
IOControl
ExposureActive, 19
ExposureAlternateActive, 19
High, 19
Low, 19
IP54, 12

## L

LED
colors, 25
housing temperature, 13
lens cleaning, 22
Low
IOControl, 19

## M

maintenance, 22
mounting, 18

## 0

operating conditions, 12
operation, 19
optical, 17

## $P$

pin assignments
GPIO, 14
power, 14
power
pin assignments, 14
power cable, 23
power supply, 13, 24
power-up, 19
projected pattern, 17
protection class, 12

## R

rc_randomdot
components, 11

## S

spare parts, 24
specifications
rc_randomdot, 11
spectrum, 17
status LED, 16

## T

temperature range, 12
tilt, 19
timing, 16

## W

wavelength, 11, 17

### Page 30</chunk>

---

<chunk_context>This is the final page (Page 30) of the rc_randomdot Assembly and Operating Manual, serving as the document's footer with key contact information and resources. It repeats the product name and manufacturer details from Page 1, while adding supplementary links to tutorials, documentation, GitHub repositories, and the Roboception shop. The support contact details mirror those listed in the "Contact" section (Page 27-28), providing a quick reference for users. This section consolidates all essential post-installation resources in one accessible location.</chunk_context>
<chunk>roboception 

## rc_randomdot Random Dot Projector

ASSEMBLY AND OPERATING MANUAL

## Roboception GmbH

Kaflerstrasse 2
81241 Munich
info@roboception.de
Germany
www.roboception.com

Tutorials:
GitHub:
Documentation:

Shop:

http://tutorials.roboception.com
https://github.com/roboception
http://doc.rc-visard.com
http://doc.rc-viscore.com
http://doc.rc-cube.com
http://doc.rc-randomdot.com
https://roboception.com/shop

For customer support, contact
+498988950790
(09:00-17:00 CET) support@roboception.de</chunk>