# Chunking Prompt

**Source File:** ROBOCEPTION_rc_viscore_manual_en_MISTRAL  
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
 roboception 

Roboception GmbH | May 2024
rc_viscore 3D Stereo Sensor
ASSEMBLY AND OPERATING MANUAL
<|end_chunk_1|><|start_chunk_2|>
### Page 2<|end_chunk_2|><|start_chunk_3|>
 Revisions 

This product may be modified without notice, when necessary, due to product improvements, modifications, or changes in specifications. If such modification is made, the manual will also be revised; see revision information.

DOCUMENTATION REVISION Rev 1.1, May 17, 2024
<|end_chunk_3|><|start_chunk_4|>
## Manufacturer
<|end_chunk_4|><|start_chunk_5|>
## Roboception GmbH

Kaflerstrasse 2
81241 Munich
Germany
CUSTOMER SUPPORT: support@roboception.de | +49 8988950 79-0 (09:00-17:00 CET)
<|end_chunk_5|><|start_chunk_6|>
## Please read the operating manual in full and keep it with the product.
<|end_chunk_6|><|start_chunk_7|>
## COPYRIGHT

This manual and the product it describes are protected by copyright. Unless permitted by German intellectual property and related rights legislation, any use and circulation of this content requires the prior consent of the individual owner of the rights. This manual and the product it describes, therefore, may not be reproduced in whole or in part, whether for sale or not, without prior written consent.

Information provided in this document is believed to be accurate and reliable. However, no responsibility is assumed.

Differences may exist between the manual and the product if the product has been modified after the manual's edition date. The information contained in this document is subject to change without notice.
<|end_chunk_7|><|start_chunk_8|>
### Page 3<|end_chunk_8|><|start_chunk_9|>
 Contents 

1 Introduction ..... 4
1.1 Overview ..... 5
1.2 Warranty ..... 6
1.3 Applicable standards ..... 7
1.4 Electronical and safety standards ..... 7
1.5 Environmental regulation ..... 8
1.6 Available certificates ..... 8
1.7 Information on disposal ..... 8
2 Safety ..... 10
2.1 General warnings ..... 10
2.2 Intended use ..... 11
3 Hardware specification ..... 12
3.1 Scope of delivery ..... 12
3.2 Technical specification ..... 13
3.3 Environmental and operating conditions ..... 15
3.4 Power-supply specifications ..... 16
3.5 Wiring ..... 16
3.6 Coordinate frames ..... 18
4 Installation ..... 19
4.1 Mounting ..... 19
4.2 Power-up ..... 20
4.3 Connecting ..... 20
4.4 Adjust camera focus ..... 21
4.5 Adjust projector focus ..... 23
4.6 Adjust projector aperture ..... 23
4.7 Calibration ..... 24
5 Maintenance ..... 25
5.1 Lens cleaning ..... 25
5.2 Change of Working Range ..... 25
6 Accessories ..... 26
6.1 Power connections ..... 26
6.2 Power supplies ..... 26
6.3 Spare parts ..... 26
6.4 SGM®Producer and rc_cube ..... 26
7 Troubleshooting ..... 28
7.1 Hardware issues ..... 28
7.2 Sparse depth images ..... 28
7.3 Dark camera images ..... 29
8 Contact ..... 30
8.1 Support ..... 30
<|end_chunk_9|><|start_chunk_10|>
### Page 4
8.2 Address ..... 30
Index ..... 31
<|end_chunk_10|><|start_chunk_11|>
### Page 5<|end_chunk_11|><|start_chunk_12|>
 1 Introduction 
<|end_chunk_12|><|start_chunk_13|>
## Indications in the manual

To prevent damage to the equipment and ensure the user's safety, this manual indicates each precaution related to safety with Warning. Supplementary information is provided as a Note.

Warning: Warnings in this manual indicate procedures and actions that must be observed to avoid danger of injury to the operator/user, or damage to the equipment. Software-related warnings indicate procedures that must be observed to avoid malfunctions or unexpected behavior of the software.

Note: Notes are used in this manual to indicate supplementary relevant information.
<|end_chunk_13|><|start_chunk_14|>
### Page 6<|end_chunk_14|><|start_chunk_15|>
 1.1 Overview

The *rc_viscore* stereo camera is a high-resolution IP54-protected 3D stereo camera with an integrated *rc_randomdot* projector. The *rc_viscore* stereo camera provides 12MP camera images and – in combination with an *rc_cube* or the SGM® producer – depth, confidence, and error images. The integrated *rc_randomdot* projector projects a random dot pattern and allows for dense depth images even in weakly textured scenes and the high resolution permits the detection of small parts with high accuracy.

In combination with the *rc_cube*, the *rc_viscore* stereo camera provides the data for object detection and grasp computation applications, e.g., in industrial automation and logistics applications.

Supplementary information is provided in:

- *rc_cube*: https://doc.rc-cube.com
- *rc_randomdot* projector: https://doc.rc-randomdot.com
- SGM® producer: https://roboception.com/product/sgmproducer

![img-0.jpeg](img-0.jpeg)

Fig. 1.1: The Roboception *rc_viscore* stereo camera

The terms "stereo camera", "camera" and "*rc_viscore* stereo camera" used throughout the manual all refer to the Roboception *rc_viscore* stereo camera stereo camera.
<|end_chunk_15|><|start_chunk_16|>
### Page 7<|end_chunk_16|><|start_chunk_17|>
 1.2 Warranty 

Any changes or modifications to the hard- and software not expressly approved by Roboception could void the user's warranty and guarantee rights.

Warning: The $r c_{\text {_ }}$viscore stereo camera utilizes complex hardware technology that may behave in a way not intended by the user. The purchaser must design its application to ensure that any failure of the $r c_{\text {_ }}$ viscore stereo camera does not cause personal injury, property damage, or other losses.

Warning: Do not attempt to take apart, open, service, or modify the $r c_{\text {_ }}$ viscore stereo camera. Doing so could present the risk of electric shock or other hazard. Any evidence of any attempt to open and/or modify the device, including any peeling, puncturing, or removal of any of the labels, will void the Limited Warranty.

Warning: CAUTION: to comply with the European CE requirement, all signal cables used to connect this device must be shielded and the device must be grounded. Operation with incorrect cables may result in interference with other devices or undesired effects of the product.

Note: This product may not be treated as household waste. By ensuring this product is disposed of correctly, you will help to protect the environment. For more detailed information about the recycling of this product, please contact your local authority, your waste disposal service provider, or the product's supplier.
<|end_chunk_17|><|start_chunk_18|>
### Page 8<|end_chunk_18|><|start_chunk_19|>
 1.3 Applicable standards 
<|end_chunk_19|><|start_chunk_20|>
### 1.3.1 Approvals

The $r c_{\text {_ }}$viscore stereo camera has received the following approvals:
![img-1.jpeg](img-1.jpeg)

EC Declaration of Conformity

IP54 ingress protection according IEC standard 60529

ROHS compliant according to EU directive 2011/65/EU

WEEE compliant according to EU directive 2012/19/EC
<|end_chunk_20|><|start_chunk_21|>
### 1.4 Electronical and safety standards

The $r c_{\text {_viscore }}$ stereo camera has been designed to be in compliance with 2014/30/EU and 2011/65/EU. The $r c_{\text {_ }}$viscore stereo camera consists of the $r c_{\text {_ }}$ randomdot projector and two industrial vision cameras.

The $r c_{\text {_ }}$ randomdot projector has been tested based on the following harmonized standards:

- EN 61000-6-4:2007 + A1:2011 : Interference Emission
- EN 61000-6-2:2005 : Interference Immunity
- EN 62471:2008 / IEC 62471:2008 : Photobiological safety of lamps and lamp systems

The industrial cameras have been tested based on the following harmonized standards:

- EN 61000-6-4:2007 + A1:2011 : Interference Emission
- EN 61000-6-2:2005 : Interference Immunity

The $r c_{\text {_ }}$viscore stereo camera is intended for use in the US only in industrial plants and is, therefore, exempt from specific technical standards and other requirements of CFR Title 47, Part 15:

47 CFR § 15.103 - Exempted devices
The following devices are subject only to the general conditions of operation in $\S \S 15.5$ and 15.29 and are exempt from the specific technical standards and other requirements contained in this part. The operator of the exempted device shall be required to stop operating the device upon a finding by the Commission or its representative that the device is causing harmful interference. Operation shall not resume until the condition causing the harmful interference has been corrected. Although not mandatory, it is strongly recommended that the manufacturer of an exempted device endeavor to have the device meet the specific technical standards in this part. (b) A digital device used exclusively as an electronic control or power system utilized by a public utility
<|end_chunk_21|><|start_chunk_22|>
### Page 9
or in an industrial plant. The term public utility includes equipment only to the extent that it is in a dedicated building or large room owned or leased by the utility and does not extend to equipment installed in a subscriber's facility.

The rc_viscore stereo camera is intended for use in Canada only in industrial plants/factories and, therefore, does not fall under the scope of ICES-003:
1.5.1 General exemptions

ICES-003 does not apply to the following types of equipment:
c. ITE or digital apparatus used exclusively as an electronic control or power system either by a public utility, in a dedicated building/facility owned or leased by the utility and which is not the subscriber facility, or in an industrial plant/factory.
<|end_chunk_22|><|start_chunk_23|>
 1.5 Environmental regulation 
<|end_chunk_23|><|start_chunk_24|>
### 1.5.1 EU RoHS Directive

All components of the rc_viscore stereo camera, including the rc_randomdot projector, the industrial cameras, cabling, and structure comply with the provisions in EU RoHS 2 Directive 2011/65/EU on the restriction of the use of certain hazardous substances in electrical and electronic equipment. Items that are exempted in the RoHS Directive are excluded from these standards.
<|end_chunk_24|><|start_chunk_25|>
### 1.5.2 REACH Regulation

All components of the rc_viscore stereo camera, including the rc_randomdot projector, the industrial cameras, cabling, and structure comply with REACH Regulation 1907/2006/CE. These products are not classified as hazardous. We hereby certify that these products do not contain any Substance of Very High Concern (SVHC) in amounts $>0.1 \%(\mathrm{w} / \mathrm{w})$.
<|end_chunk_25|><|start_chunk_26|>
### 1.6 Available certificates

Copies of the various certificates can be downloaded from https://roboception.com/support/.
<|end_chunk_26|><|start_chunk_27|>
### 1.7 Information on disposal
<|end_chunk_27|><|start_chunk_28|>
## 1. Disposal of Waste Electrical \& Electronic Equipment

This symbol on the product(s) and / or accompanying documents means that used electrical and electronic products should not be mixed with general household waste. For proper treatment, recovery and recycling, please contact your supplier or the manufacturer. Disposing of this product correctly will help save valuable resources and prevent any potential negative effects on human health and the environment, which could otherwise arise from inappropriate waste handling.
<|end_chunk_28|><|start_chunk_29|>
## 2. Removal of batteries

If the products contain batteries and accumulators that can be removed from the product without destruction, these must be removed before disposal and disposed of separately as batteries.

The following batteries or accumulators are contained in the rc_viscore stereo camera: None
<|end_chunk_29|><|start_chunk_30|>
### Page 10<|end_chunk_30|><|start_chunk_31|>
 3. Options for returning old equipment 

Owners of old devices can return them to the manufacturer to ensure proper disposal.
Please contact support (Section 8) about returning the device for disposal.
<|end_chunk_31|><|start_chunk_32|>
## 4. Data protection

End users of Electrical \& Electronic Equipment are responsible for deleting personal data on the waste equipment to be disposed of.
<|end_chunk_32|><|start_chunk_33|>
## 5. WEEE registration number

Roboception is registered under the registration number DE 33323989 at the stiftung elektroaltgeräte register, Nordostpark 72, 90411 Nuremberg, Germany, as a producer of electrical and/or electronic equipment.
<|end_chunk_33|><|start_chunk_34|>
## 6. Collection and recovery quotas

According to the WEEE Directive, EU member states are obliged to collect data on waste electrical and electronic equipment and to transmit this data to the European Commission. Further information can be found on the German Ministry for the Environment website.
<|end_chunk_34|><|start_chunk_35|>
## Information on Disposal outside the European Union

This symbol is valid only in the European Union. If you wish to discard this product please contact your local authorities or dealer and ask for the correct method of disposal.
<|end_chunk_35|><|start_chunk_36|>
### Page 11<|end_chunk_36|><|start_chunk_37|>
 2 Safety 

Warning: The operator must have read and understood all of the instructions in this manual before handling the $r c_{\text {_ }}$viscore stereo camera product.

Warning: If operating the $r_{c}$ viscore stereo camera with the $r_{c}$ cube product, the operator must have read and understood all of the safety, installation, and maintenance instructions given in the $r_{c}$ cube manual.

Note: The term "operator" refers to anyone responsible for any of the following tasks performed in conjunction with the $r_{c}$ viscore stereo camera:

- Installation
- Maintenance
- Inspection
- Calibration
- Programming
- Decommissioning

This manual explains the $r_{c}$ viscore stereo camera's various components and general operations regarding the product's whole life-cycle, from installation through operation to decommissioning.

The drawings and photos in this documentation are representative examples; differences may exist between them and the delivered product.
<|end_chunk_37|><|start_chunk_38|>
### 2.1 General warnings

Note: Any use of the $r_{c}$ viscore stereo camera in noncompliance with these warnings is inappropriate and may cause injury or damage as well as void the warranty.
<|end_chunk_38|><|start_chunk_39|>
## Warning:

- The $r_{c}$ viscore stereo camera is protected according to IP54. High humidity or temperature can damage the device. Do not operate in an environment where combustible or explosive fumes may occur.
- The $r_{c}$ viscore stereo camera needs to be properly mounted before use.
- All cable sets need to be secured to the $r_{c}$ viscore stereo camera and the mount.
- Cables must not be longer than 30 m . The 8 -Pin power supply cable must not be longer than 15 m .
<|end_chunk_39|><|start_chunk_40|>
### Page 12
- Power to the rc_viscore stereo camera must be supplied through an appropriate, separate DC power source.
- An appropriate power supply, which conforms to the EN 62368-1 standard must be used to supply power to the rc_viscore stereo camera.
- Check polarity and connections.
- The rc_viscore stereo camera's housing must be grounded.

<|end_chunk_40|><|start_chunk_41|>
 Warning: 

- The $r c_{\text {_ }}$ viscore stereo camera's and any related equipment's safety guidelines must always be satisfied.
- The $r c_{\text {_ }}$ viscore stereo camera does not fall under the purview of the machinery or medical directives.

Risk assessment and final application: The $r c_{\text {_ }}$ viscore stereo camera may be used together with an $r c_{\text {_ }}$ cube with a robot. Robot, $r c_{\text {_ }}$ viscore stereo camera, $r c_{\text {_ }}$ cube, and any other equipment used in the final application must be evaluated with a risk assessment. The system integrator's duty is to ensure respect for all local safety measures and regulations. Depending on the application, there may be risks that need additional protection/safety measures.
<|end_chunk_41|><|start_chunk_42|>
### 2.2 Intended use

The $r c_{\text {_ }}$ viscore stereo camera is intended to be used in combination with a Roboception $r c_{\text {_ }}$ cube or the SGM®Producer. The $r c_{\text {_ }}$ viscore stereo camera together with a Roboception $r c_{\text {_ }}$ cube are intended for installation with automated machinery, a mobile platform, or stationary equipment. They can also be used for data acquisition in other applications.

Warning: The $r c_{\text {_ }}$ viscore stereo camera is NOT intended for safety critical applications.

Warning: The $r c_{\text {_ }}$ viscore stereo camera is NOT to be used in dynamic environments or mounted to a robot end-effector.

The $r c_{\text {_ }}$ viscore stereo camera may be used only within the scope of its technical specification. Any other use of the product is deemed unintended use. Roboception will not be liable for any damages resulting from any improper or unintended use.

Warning: Always comply with local and/or national laws, regulations and directives on automation safety and general machine safety.
<|end_chunk_42|><|start_chunk_43|>
### Page 13<|end_chunk_43|><|start_chunk_44|>
 3 Hardware specification 

Note: The following hardware specifications are provided here as a general reference; differences with the product may exist.
<|end_chunk_44|><|start_chunk_45|>
### 3.1 Scope of delivery

Standard delivery for the rc_viscore stereo camera includes

- rc_viscore stereo camera,
- Calibration grid large (A3),
- $2 \times 10 \mathrm{~m}$ gigabit Ethernet network cables,
- 10 m power cable with M12 connector and one open end,
- Quickstart guide.

The full manual is online available in digital form at https://doc.rc-viscore.com.
Note: The following items are not included in the delivery unless otherwise specified:

- Couplings, adapters, mounts,
- Power supply unit and fuses.

Please refer to Accessories (Section 6) for suggested cables.
The following picture shows the important parts of the rc_viscore stereo camera which are referenced later in the documentation.
![img-2.jpeg](img-2.jpeg)

Fig. 3.1: Parts description
<|end_chunk_45|><|start_chunk_46|>
### Page 14<|end_chunk_46|><|start_chunk_47|>
 3.2 Technical specification 

The technical specification of the $r c_{\text {_ }}$viscore stereo camera is shown in Table 3.1. The given depth image frame rate can be reached on an $r c_{\text {_ }}$ cube or with the SGM®producer on a computer with an Nvidia RTX2070 GPU. Higher frame rates (up to 9 Hz ) are possible with faster graphics cards.

Table 3.1: Technical specifications of the rc_viscore stereo camera

|  | $r c_{\text {_ }}$ viscore stereo camera |
| :-- | :-- |
| Image resolution | $4112 \times 3008$ pixels monochrome |
| Framerate | 9 Hz |
| Focal length | 16 mm |
| Field of view | Horizontal: $47.5^{\circ}$, Vertical: $35.7^{\circ}$ |
| Workspace | $670 \mathrm{~mm} \times 640 \mathrm{~mm} @ 1.0 \mathrm{~m}$ distance <br> $1550 \mathrm{~mm} \times 1280 \mathrm{~mm} @ 2.0 \mathrm{~m}$ distance <br> $2430 \mathrm{~mm} \times 1920 \mathrm{~mm} @ 3.0 \mathrm{~m}$ distance <br> $3310 \mathrm{~mm} \times 2560 \mathrm{~mm} @ 4.0 \mathrm{~m}$ distance |
| Depth image | $4112 \times 3008$ pixel (Full) @ 2.8 Hz (Nvidia RTX2070) <br> $2056 \times 1504$ pixel (High) @ 4.6 Hz (Nvidia RTX2070) <br> $1028 \times 752$ pixel (Medium) @ 9 Hz (Nvidia RTX2070) <br> $686 \times 502$ pixel (Low) @ 9 Hz (Nvidia RTX2070) |
| Cooling | Passive |
| Baseline | 210 mm |
| Size $(\mathrm{W} \times \mathrm{H} \times \mathrm{L})$ | $262 \mathrm{~mm} \times 204 \mathrm{~mm} \times 82 \mathrm{~mm}$ |
| Mass | 1.64 kg |

The depth image range of the $r c_{\text {_ }}$ viscore stereo camera depends on the depth image quality, the specified maximum depth range and the available GPU memory. Depth ranges at closer distance are much smaller than depth ranges at far distances. The $r c_{\text {_ }}$ cube uses 3.4 Gbytes of GPU memory for stereo matching. Table 3.2 shows examples of resulting depth ranges with 3.4 Gbytes of GPU memory. Larger depth ranges are possible by using the SGM®producer with a graphics card that offers more GPU memory.
<|end_chunk_47|><|start_chunk_48|>
### Page 15
Table 3.2: Examples of possible depth ranges of the rc_viscore stereo camera with 3.4 Gbytes of GPU memory as in case of the rc_cube

|  | rc_viscore stereo camera |
| :-- | :-- |
| Full depth quality |  |
|  | 0.89 m to 1.00 m |
|  | 1.60 m to 2.00 m |
|  | 2.18 m to 3.00 m |
|  | 2.65 m to 4.00 m |
| High depth quality |  |
|  | 0.52 m to 1.00 m |
|  | 0.66 m to 2.00 m |
|  | 0.75 m to 3.00 m |
|  | 0.80 m to 4.00 m |
|  | 1.00 m to infinity |
| Medium and low depth quality | 0.52 m to infinity |

The resolution and accuracy at different distances is given in Table 3.3 for the recommended high depth quality. In full depth quality, the resolution and accuracy will be better by a factor of 2 . Similarly, in medium quality, the resolution and accuracy will be about 2 times worse than shown in the table.

Table 3.3: Resolution and accuracy of the $r c_{\text {_ }}$ viscore stereo camera in millimeters with high quality stereo matching and random dot projection on non-reflective and non-transparent objects.

|  | distance | rc_viscore stereo camera |
| :--: | :--: | :--: |
| Lateral resolution | 1.0 m | 0.4 mm |
|  | 2.0 m | 0.9 mm |
|  | 3.0 m | 1.3 mm |
|  | 4.0 m | 1.7 mm |
| Depth resolution | 1.0 m | 0.1 mm |
|  | 2.0 m | 0.5 mm |
|  | 3.0 m | 1.2 mm |
|  | 4.0 m | 2.0 mm |
| Average depth accuracy | 1.0 m | 0.5 mm |
|  | 2.0 m | 2.0 mm |
|  | 3.0 m | 4.6 mm |
|  | 4.0 m | 8.2 mm |
<|end_chunk_48|><|start_chunk_49|>
### Page 16
![img-3.jpeg](img-3.jpeg)

Fig. 3.2: Overall dimensions of the rc_viscore stereo camera in millimeters

CAD models of the $r c_{\text {_ }}$ viscore stereo camera can be downloaded from https://www.roboception.com/ download. The CAD models are provided as-is, with no guarantee of correctness.
<|end_chunk_49|><|start_chunk_50|>
 3.3 Environmental and operating conditions 

The $r c_{\text {_ }}$viscore stereo camera is designed for industrial applications. Always respect the storage, transport, and operating environmental conditions outlined in Table 3.4.

Table 3.4: Environmental conditions

|  | rc_viscore stereo camera |
| :-- | :-- |
| Storage/Transport temperature | $-20^{\circ} \mathrm{C}$ to $60^{\circ} \mathrm{C}$ |
| Operating temperature | $0^{\circ} \mathrm{C}$ to $45^{\circ} \mathrm{C}$ (passive cooling) |
| Relative humidity (non <br> condensing) | $20 \%$ to $80 \%$ |
| Protection class | IP54 |
| Others | - Free from corrosive liquids or gases <br> - Free from explosive liquids or gases <br> - Free from powerful electromagnetic interference |
|  |  |

The $r c_{\text {_ }}$viscore stereo camera is designed for an operating temperature (surrounding environment) of $0^{\circ} \mathrm{C}$ to $45^{\circ} \mathrm{C}$ and relies on convective (passive) cooling. Unobstructed airflow, especially around the cooling fins, needs to be ensured during use. The $r c_{\text {_ }}$viscore stereo camera should only be mounted using the provided mechanical mounting interface, and all parts of the housing must remain uncovered. A free space of at least 10 cm extending in all directions from the housing, and sufficient air exchange with the environment is required to ensure adequate cooling. Cooling fins must be free of dirt and other contamination.
<|end_chunk_50|><|start_chunk_51|>
### Page 17<|end_chunk_51|><|start_chunk_52|>
 3.4 Power-supply specifications 

The $r c_{\text {_ }}$viscore stereo camera needs to be supplied by a DC voltage source. The camera's standard package does not include a DC power supply. Each $r c_{\text {_ }}$viscore stereo camera must be connected to a separate power supply. Connection to domestic grid power is only allowed through a power supply certified as EN55011 Class B.

Table 3.5: Absolute maximum ratings for power supply

|  | Min | Nominal | Max |
| :-- | :-- | :-- | :-- |
| Supply voltage | 22.0 V | 24 V | 26.0 V |
| Max power consumption |  |  | 48 W |
| Overcurrent protection | Supply must be fuse-protected to a maximum of 2 A |  |  |
| EMC compliance | see Electronical and safety standards (Section 1.4) |  |  |

Warning: Exceeding maximum power rating values may lead to damage of the $r c_{\text {_ }}$viscore stereo camera, power supply, and connected equipment.

Warning: A separate power supply must power each $r c_{\text {_ }}$viscore stereo camera.

Warning: Connection to domestic grid power is allowed through a power supply certified as EN55011 Class B only.
<|end_chunk_52|><|start_chunk_53|>
### 3.5 Wiring

The $r c_{\text {_ }}$viscore stereo camera is delivered with a sync cable already connected between projector and cameras. It is the customer's responsibility to connect the two provided M12 X-coded network cables to the left and right camera, as well as the power cable with an angled M12 connector to the projector (see Fig. 3.3). The network cables must be clipped into the cable guide for strain relief. All cables must be secured to the mounting bracket.
![img-4.jpeg](img-4.jpeg)

Fig. 3.3: Locations of the electrical connections for the $r c_{\text {_ }}$viscore stereo camera

Warning: Due to the voltage drop, the maximum power cable length is limited to 15 m . The supply voltage should be set to the specified 24 V and must not be set above 26 V due to the highly variable current draw of the $r c_{\text {_ }}$viscore stereo camera.
<|end_chunk_53|><|start_chunk_54|>
### Page 18
Warning: Proper cable management is mandatory. Cabling must always be secured to the rc_viscore stereo camera mount with a strain-relief clamp so that no forces due to cable movements are exerted on the rc_viscore stereo camera's M12 connectors. Enough slack needs to be provided to allow for full range of movement of the camera without straining the cable. The cable's minimum bend radius (i.e. $R_{\text {min }}=15 d$ ) needs to be observed.

Pin assignments for the power connector are given in Table 3.6.
Table 3.6: Pin assignments for the power connector

| Pin | Cable Color | Designation | Details |
| :-- | :-- | :-- | :-- |
| 1 | White | nc |  |
| 2 | Brown | Power +24 V | $2 \mathrm{~A} @ 24 \mathrm{~V}$ |
| 3 | Green | GPIO In 1 | $12-24 \mathrm{~V}, 15 \mathrm{~mA}$ max. |
| 4 | Yellow | GPIO GND |  |
| 5 | Grey | GPIO Vcc | $5-24 \mathrm{~V}, 50 \mathrm{~mA}$ max. |
| 6 | Pink | GPIO Out 1 | Projector exposure signal |
| 7 | Blue | Power GND |  |
| 8 | Red | GPIO Out 2 |  |

Note: Please note that in hardware revisions prior to 1.1 the pins number 3 and 4 were not connected.

GPIOs are decoupled by photocouplers. GPIO Out 1 by default provides an exposure sync signal with a logic high level for the duration of the image exposure. Pins of unused GPIOs should be left floating. GPIO circuitry and specifications are shown in Fig. 3.4.
![img-5.jpeg](img-5.jpeg)

Fig. 3.4: GPIO circuitry and specifications
<|end_chunk_54|><|start_chunk_55|>
### Page 19<|end_chunk_55|><|start_chunk_56|>
 3.6 Coordinate frames 

The $r c_{\text {_ }}$viscore stereo camera's coordinate-frame origin is defined as the exit pupil of the left camera lens. This frame is called camera coordinate frame. It is shown in Fig. 3.5.
![img-6.jpeg](img-6.jpeg)

Fig. 3.5: Camera coordinate frame location and orientation

Note: The correct offset between the camera frame and a robot coordinate frame can be calibrated through hand-eye calibration. See https://doc.rc-cube.com/latest/en/handeye_calibration.html.
<|end_chunk_56|><|start_chunk_57|>
### Page 20<|end_chunk_57|><|start_chunk_58|>
 4 Installation 

Warning: The instructions on Safety (Section 2) related to the rc_viscore stereo camera must be read and understood prior to installation.
<|end_chunk_58|><|start_chunk_59|>
### 4.1 Mounting

The $r c_{\text {_ }}$ viscore stereo camera is intended to be mounted on a wall or ceiling above the target area. It is not intended to be used in dynamic applications mounted to a robot wrist. It is the customer's responsibility to provide an adequate mounting bracket.

For mounting, the $r c_{\text {_ }}$ viscore stereo camera provides an M4 and M5 thread pattern on its top and bottom sides (see Fig. 4.1). A medium-strength thread-locker or Tuflok ${ }^{\circledR}$ screws must be used to protect against vibrations. M5 screws must be tightened to 4.0 Nm , M4 screws must be tightened to 3.3 Nm .

Warning: The $r c_{\text {_ }}$ viscore stereo camera cannot be mounted on the end-effector of a robot.
![img-7.jpeg](img-7.jpeg)

Fig. 4.1: Mounting of the $r c_{\text {_viscore }}$ stereo camera

Only the surface containing the thread pattern must be in contact with the mounting bracket, all other surfaces must remain free. At least 10 cm clearance must be provided behind the $r c_{\text {_ }}$ viscore stereo camera to facilitate adequate air flow for cooling.
<|end_chunk_59|><|start_chunk_60|>
### Page 21<|end_chunk_60|><|start_chunk_61|>
 4.2 Power-up 

Note: Always fully connect and tighten all M12 connectors on the rc_viscore stereo camera before turning on the power supply.

After connecting the system to power, the LED on the front of the $r c_{\text {_ }}$ viscore stereo camera should immediately illuminate.

Warning: Do not look into the projector lens in the center of the $r c_{\text {_ }}$ viscore stereo camera or into the light beam at any point during startup or operation.
<|end_chunk_61|><|start_chunk_62|>
### 4.3 Connecting

The $r c_{\text {_ }}$viscore stereo camera can be used together with an $r c_{\text {_ }}$ cube or as a stand-alone high-resolution RGBD camera with the SGM®producer. The following sections describe connecting the $r c_{\text {_ }}$ viscore stereo camera in both scenarios.
<|end_chunk_62|><|start_chunk_63|>
### 4.3.1 Connecting to the rc_cube

The $r c_{\text {_ }}$ cube I (Industrial Edge Computer) offers four network ports that are labelled sensors 0-3. The two network cables of the $r c_{\text {_ }}$ viscore stereo camera must be connected directly to two of those ports. It does not matter which ones. Two stereo cameras can be connected and used at the same time.

The $r c_{\text {_ }}$ cube S (Edge Computer) offers one 2.5 gigabit sensor port. A switch must be used for connecting an $r c_{\text {_ }}$ viscore stereo camera. The switch must support 2.5 gigabit for the connection to the $r c_{\text {_ }}$ cube and 1 gigabit speed for the connection to the $r c_{\text {_ }}$ viscore stereo camera. The switch is not in the scope of the delivery of the $r c_{\text {_ }}$ cube S . Roboception can recommend a suitable switch upon request.

By default, the $r c_{\text {_ }}$ cube is configured to support one $r c_{\text {_ }}$ visard as sensor. For supporting one $r c_{\text {_ }}$ viscore stereo camera, the type of the camera pipeline must be changed in the Web GUI of the $r c_{\text {_ }}$ cube under System $\rightarrow$ Camera Pipelines (see https://doc.rc-cube.com/latest/en/pipelines.html). Clicking on Configure Camera Pipelines opens a dialog that permits to change the type of pipeline to rc_viscore. A reboot is necessary after changing the pipeline configuration.

For connecting two stereo cameras at the same time, it is additionally necessary to configure a second pipeline, as explained above, and to specify which pipeline should use which $r c_{\text {_ }}$ viscore stereo camera by setting a filter expression. This is done by clicking on Configure Camera Connection on the Camera Pipelines page, or select the corresponding pipeline in the menu, e.g. under System $\rightarrow$ Camera Pipelines $\rightarrow$ Pipeline .... Clicking Choose Camera opens a dialog to edit the device filter (see also https://doc. rc-cube.com/latest/en/pipelines.html\#configuration-of-connected-cameras).

It may take up to one minute until the $r c_{\text {_ }}$ viscore stereo camera is connected. For each successfully connected sensor, the connection speed and frame rate is shown in the Dashboard of the Web GUI.
<|end_chunk_63|><|start_chunk_64|>
### 4.3.2 Connecting to the SGM®Producer

For using the $r c_{\text {_ }}$ viscore stereo camera as high-resolution RGBD camera, Roboception offers the SGM®Producer, which is a GenICam compatible transport layer (see https://roboception.com/product/ sgmproducer).

The producer can be used with Halcon, with the rc_genicam_api for C++ programmers, with the rc_genicam_driver for ROS and ROS2, as well as with any other GenICam compatible application. It can be downloaded free of charge from https://www.roboception.com/download and installed on Windows and Ubuntu computers with an Nvidia graphics card.
<|end_chunk_64|><|start_chunk_65|>
### Page 22
It is strongly recommended to connect both network cables directly to 1 gigabit Ethernet ports of the computer. When using a network switch, the network link between the switch and the computer should have a bandwidth of more than 2 gigabit, e.g. 2.5, 5 or 10 gigabit. Otherwise, the full frame rate cannot be reached.

In the default network configuration and according to the GigE Vision® standard, the rc_viscore stereo camera will try to obtain its configuration from a DHCP server and fall back to the Link-Local selfconfiguration protocol, if no DHCP server can be found. For direct connection without a DHCP server, the Ethernet ports of the computer should be configured for Link-Local network. It is also possible to manually configure IP addresses of the left and right camera.

Options for changing the network settings and IP configuration are:

- any configuration tool compatible with GigE Vision® 2.0, or Roboception's command-line tool gc_config. Typically, these tools scan for all available GigE Vision® devices on the network. All $r c_{\text {_ }}$ viscore stereo camera devices can be uniquely identified by their serial number, which is printed on the device.
- temporarily changing the network configuration via Roboception's rcdiscover-gui tool. The individual cameras can be seen in the list after unchecking the Only Roboception devices check box.

Note: The command-line tool gc_config is part of Roboception's open-source convenience layer rc_genicam_api, which can be downloaded free of charge for Windows and Linux from https://www. roboception.com/download.

For adjusting the focus, checking and calibrating the $r c_{\text {_ }}$ viscore stereo camera, as explained in the next sections, the SGM®Producer package contains a calibration program, called rc_calib, and a viewer program, called rc_viewer.
<|end_chunk_65|><|start_chunk_66|>
 4.4 Adjust camera focus 

It is highly recommended to check the focus of the $r c_{\text {_ }}$ viscore stereo camera for the actual working range. By default, Roboception focuses the $r c_{\text {_ }}$ viscore stereo camera to a distance of 1.6 m (unless otherwise specified by the customer), which results in a working range of approximately 1.4-2.0 m. If a different working range is used in the application, the focus must be adapted. Please note that the focus range is limited due to the high resolution of the camera. At close distance, the focus range is much smaller than at higher distances. Therefore, the minimum distance for focusing should be chosen as far away as useful for the application.

If focus adjustment is needed, the lens caps of the left and right cameras must be removed as shown in Fig. 4.2.
<|end_chunk_66|><|start_chunk_67|>
### Page 23
![img-8.jpeg](img-8.jpeg)

Fig. 4.2: Removing of lens caps for re-focusing and changing aperture

The focus ring and the aperture ring (iris ring) are locked by 3 screws for each ring as shown in Fig. 4.3. All three screws must be loosened for moving a ring.
![img-9.jpeg](img-9.jpeg)

Fig. 4.3: Locations of screws for focus ring and aperture ring (iris ring)

The rc_cube offers a focus helper as part of camera calibration on the Web GUI under Pipeline ... $\rightarrow$ Configuration $\rightarrow$ Camera Calibration. In the first step, the size of the calibration grid has to be specified. Clicking on Next opens the focus helper. See also https://doc.rc-cube.com/latest/en/camera_calibration. html.

In the SGM®Producer, a focus helper can be found in the calibration program rc_calib after selecting the $r c_{\text {_ }}$ viscore stereo camera with File $\rightarrow$ Connect sensor ..., and specifying the grid size.

The bars on the right side of the focus helper image report the blur of the calibration grid, thus a minimum is desirable. See also https://doc.rc-cube.com/latest/en/camera_calibration.html\#adjust-focus.

For setting the focus correctly, the calibration grid should be placed in the middle of the working range.
<|end_chunk_67|><|start_chunk_68|>
### Page 24
Then, the focus ring of each camera should be turned until the bar in the corresponding image becomes minimal. A value near the lowest dividing line is desirable. After focusing in this way, the grid should be placed at the minimum and maximum working distance. If the blur is unsatisfactory at the minimum and maximum working distance (e.g. near the second dividing line or higher), the aperture of the camera can be closed a bit by turning the iris ring, i.e. a higher aperture number should be chosen to expand the focus range of the cameras. Please be aware that this also increases exposure time and potentially gain, which increases noise in the image. The optimal tradeoff is application dependent. The default aperture number of the cameras is 4 .

Warning: The same aperture setting must be used for the left and right camera to avoid degraded image processing performance. Please validate that the left and right images appear with the same brightness.

After adjusting focus and aperture, all screws must be lightly tightened and the lens caps must be reattached.

Warning: It is mandatory to always check calibration after changing the focus or aperture of the rc_viscore stereo camera (see Calibration, Section 4.7) .

Please contact support (Section 8) in case of questions regarding working distance and focusing of the $r c_{\text {_viscore }}$ stereo camera.
<|end_chunk_68|><|start_chunk_69|>
 4.5 Adjust projector focus 

During production, the focus of the projector is adjusted to match the focus distance of the cameras, which is 1.6 m by default (unless otherwise specified by the customer). Perfectly focusing the projector is not crucial. A slightly blurred projection pattern will not degrade the depth image.

To inspect the sharpness of the projector pattern, the projector should be turned on permanently by setting the Out1 / Projector mode to High on the rc_cube Web GUI under Pipeline ... $\rightarrow$ Camera $\rightarrow$ IOControl Settings or Pipeline $\ldots \rightarrow$ Configuration $\rightarrow$ IOControl.

The projector focus only needs to be adjusted when the projector pattern is strongly blurred. In this case, loosen the three small fixing Phillips screws on the focus ring of the projector lens as shown in Fig. 4.3. Then, turn the focus ring until the visible projector pattern becomes sharp. After that, lightly tighten the focus ring screws again.
<|end_chunk_69|><|start_chunk_70|>
### 4.6 Adjust projector aperture

The aperture of the projector influences the brightness of the projector pattern. By default, the aperture of the projector is fully open, which means the projector has maximum brightness. The aperture should be adjusted so that the brightness difference between images taken with projector and images taken without projector is not too large, but the projector pattern is still visible in the images taken with projector. To find the correct setting, make sure the external light in the working environment is similar to what is expected during productive mode and the $r c_{\text {_ }}$ viscore stereo camera is mounted at the desired distance from the scene.

Then, on the $r c_{\text {_ }}$ cube Web GUI under Pipeline $\ldots \rightarrow$ Camera, set the Exposure mode to Auto and set the Auto Exposure Mode to AdaptiveOut1. Also set the Out1 / Projector mode to ExposureAlternateActive under IOControl Settings, so that every second image is taken with projector pattern. Now, the text line under the live images shows the Out1 reduction value in percent.

The Out1 reduction value describes the reduction of the brightness of the image without projection compared to the image with projection. The value should be between $10 \%$ and $20 \%$. A higher Out1
<|end_chunk_70|><|start_chunk_71|>
### Page 25
reduction value means, that the projector is too bright compared to the external lighting, which leads to images without projector patterns being too dark. Thus, external lighting should be increased, e.g. by installing an additional light source, or the brightness of the projector should be reduced by slightly closing the aperture. In analogy, if the Out1 reduction value is too low, the projector is not bright enough compared to the external light, which means that the projector pattern will hardly be visible in the camera images and cannot enhance the depth computation. So the external light should be reduced or the projector brightness must be increased by opening the aperture.

The aperture of the projector can be adjusted by loosening the three small fixing Phillips screws on the iris ring of the projector lens as shown in Fig. 4.3. Then, turn the iris ring until the Out1 reduction value is in the range between $10 \%$ and $20 \%$.

After that, the darkest object that is possible in the application should be placed in the field of view of the camera. If the dark object is not properly visible in the depth image, then the projector brightness must be increased, despite high Out1 reduction values.

In the end, lightly tighten the iris ring screws again.
Please contact support (Section 8) in case of questions regarding adjusting the projector of the rc_viscore stereo camera.
<|end_chunk_71|><|start_chunk_72|>
 4.7 Calibration 

After checking and potentially adjusting the focus of the cameras, the next step is to check the camera calibration. This step should never be skipped and - as opposed to all $r c_{\text {_ }}$ visard products - is mandatory. Please note that the working range of the $r c_{\text {_ }}$ viscore stereo camera is pre-defined and the calibration should be checked for the minimum and maximum working distance. Please contact support (Section 8) in case of questions regarding working distance and calibration of the $r c_{\text {_viscore }}$ stereo camera.

The $r c_{\text {_ }}$ cube manual explains checking calibration and re-calibrating in detail (see https://doc.rc-cube. com/latest/en/camera_calibration.html\#verify-calibration). The procedure that is described there can be applied in the same way to the SGM®Producer, by using the $r c_{\text {_ }}$ calib program that is provided with the producer.

Warning: It is mandatory to always check calibration after mounting the $r c_{\text {_ }}$ viscore stereo camera, changing the focus or aperture.

Recalibration is only necessary if the reported calibration error is above 0.3 pixels. After recalibration, also a new hand-eye calibration is required.

Note: Roboception will deliver the $r c_{\text {_ }}$ viscore stereo camera with pre-adjusted focus to make sure it works in the desired depth range. Please contact support (Section 8) and provide your specification to enable us to set up the $r c_{\text {_ }}$ viscore stereo camera accordingly. An onsite calibration check is still required to make sure that no problem occurred during shipping or mounting.
<|end_chunk_72|><|start_chunk_73|>
### Page 26<|end_chunk_73|><|start_chunk_74|>
 5 Maintenance 

Warning: The only parts removable by the customer are the lens caps, which can be unscrewed. The customer does not need to open the rc_viscore stereo camera's housing to perform maintenance. Unauthorized opening of the housing will void the warranty. For all maintenance operations other than adjusting focus and aperture, the product must be switched off.

To handle the optical components, wearing gloves is strongly recommended. The lens cap can be removed by unscrewing the barrel. Then focus and the aperture can be adjusted with manual settings of the C -mount lens.

Warning: The lens cap needs to be in place during normal operation to meet EMC requirements.
<|end_chunk_74|><|start_chunk_75|>
### 5.1 Lens cleaning

Glass lenses with antireflective coating are used to reduce glare. Please take special care when cleaning the lenses. To clean them, use a compressed air duster or soft lens-cleaning brush to remove dust or dirt particles. To remove stubborn dirt, wipe 1-2 drops of a non-alcohol-based lens cleaning solution formulated for coated lenses (such as the Uvex Clear family of products) in a gentle circular motion with a cleaning tissue. Always apply the fluid to a tissue rather than the lens itself.

Warning: In case the lens covers are removed, a calibration check is required.
<|end_chunk_75|><|start_chunk_76|>
### 5.2 Change of Working Range

In case a change of working range is desired, an adjustment of the focus (see Adjust camera focus, Section 4.4) as well as the depth range is required. Please note the limitations in the measurement range in Table 3.2.
<|end_chunk_76|><|start_chunk_77|>
### Page 27<|end_chunk_77|><|start_chunk_78|>
 6 Accessories 
<|end_chunk_78|><|start_chunk_79|>
### 6.1 Power connections

The $r c_{\text {_ }}$viscore stereo camera contains an 8-pin A-coded M12 plug connector for power and GPIO connectivity to the robot controller. Various cabling solutions can be obtained from third party vendors, however, the M12 connector on the $r c_{\text {_ }}$viscore stereo camera side must be angled. One possibility for an angled M12 to open ended cable is provided below. Customers are required to provide power and GPIO connections to the cables according to the pinouts described in Wiring (Section 3.5). The $r c_{\text {_ }}$viscore stereo camera's housing must be connected to ground.
<|end_chunk_79|><|start_chunk_80|>
## Sensor/Actor cable M12 socket to open end for power and GPIO connection

- Angled M12 socket connector to open end, shielded 10m length: Phoenix Contact SAC-8P-10,0PUR/M12FR SH, Art.Nr.: 1522943

<|end_chunk_80|><|start_chunk_81|>
## Network cable M12 X-coded to RJ45

- Straight M12 X-coded to RJ45 CAT6A cable, 10m length, 2 required per $r c_{\text {_ }}$viscore stereo camera: Phoenix Contact NBC-M12MSX/10,0-94F/R4AC, Art.Nr.: 1407474

<|end_chunk_81|><|start_chunk_82|>
### 6.2 Power supplies

The $r c_{\text {_ }}$viscore stereo camera is classified as EN-55011 Class B device and is immune to light industrial and industrial environments. For connecting the camera to residential grid power, a power supply under EN 55011/55022 Class B has to be used.

It is the customer's responsibility to obtain and install a suitable power supply for permanent use in industrial environments. One example that satisfies both EN 61000-6-2 and EN 55011/55022 Class B is the DIN-Rail mounted PULS MiniLine ML70.100 24V/DC 3 A by PULS GmbH (http://www.pulspower.com). A certified electrician must perform installation.

Only one $r c_{\text {_ }}$viscore stereo camera shall be connected to a power supply at any time, and the total length of cables must be less than 15 m .
<|end_chunk_82|><|start_chunk_83|>
### 6.3 Spare parts

Roboception can provide calibration grids, power cables and network cables as spare parts for $r c_{\text {_ }}$viscore stereo camera upon request.
<|end_chunk_83|><|start_chunk_84|>
### 6.4 SGM®Producer and rc_cube

The $r c_{\text {_ }}$viscore stereo camera provides 12MP camera images and - in combination with an $r c_{\text {_ }}$ cube or the SGM®Producer - depth, confidence and error images. The integrated $r c_{\text {_ }}$ randomdot projector allows for dense depth images even in weakly textured scenes and the high resolution permits the detection of
<|end_chunk_84|><|start_chunk_85|>
### Page 28
small parts with high accuracy. The SGM®Producer can be downloaded from http://www.roboception. com/download .

In combination with the rc_cube, the rc_viscore stereo camera provides the data for object detection and grasp computation applications, e.g. in industrial automation and logistics applications.
<|end_chunk_85|><|start_chunk_86|>
### Page 29<|end_chunk_86|><|start_chunk_87|>
 7 Troubleshooting 
<|end_chunk_87|><|start_chunk_88|>
### 7.1 Hardware issues
<|end_chunk_88|><|start_chunk_89|>
## LED does not illuminate

The $r c_{\text {_ }}$viscore stereo camera does not start up.

- Ensure that cables are connected and secured properly.
- Ensure that adequate DC voltage ( 24 V ) with correct polarity is applied to the power connector at the pins labeled as Power and Ground as described in the device's pin assignment specification (Section 3.6). Connecting the camera to voltage outside of the specified range, to alternating current, with reversed polarity, or to a supply with voltage spikes will lead to permanent hardware damage.

<|end_chunk_89|><|start_chunk_90|>
## Reliability issues and/or mechanical damage

This may be an indication of ambient conditions (vibration, shock, resonance, and temperature) being outside of specified range. Please refer to the specification of environmental conditions (Section 3.4).

- Operating the $r c_{\text {_ }}$viscore stereo camera outside of specified ambient conditions might lead to damage and will void the warranty.

<|end_chunk_90|><|start_chunk_91|>
## Electrical shock when touching the projector

This indicates an electrical fault in camera, cabling, or power supply or adjacent system.

- Immediately turn off power to the system, disconnect cables, and have a qualified electrician check the setup.
- Ensure that the projector housing is properly grounded; check for large ground loops.

<|end_chunk_91|><|start_chunk_92|>
### 7.2 Sparse depth images

The depth images of the $r c_{\text {_ }}$ viscore stereo camera, which can be seen on the depth image page in the $r c_{\text {_ }}$ cube's Web GUI or by using the SGM®Producer, may have missing values, which are shown in black. Missing values near object borders are normal. If major parts of the depth image are invalid, then this may be due to the following reasons:

- The scene may be out of the current working range of the $r c_{\text {_ }}$ viscore stereo camera. Depending on the depth quality, reducing the parameter Maximum Distance also reduces the possible minimum distance. In the Web GUI of the $r c_{\text {_ }}$ cube, the used depth range is given on the depth image page below the images. Sliders on the depth image page permit to change the depth range. See also Table 3.2 for examples of possible depth ranges.
- Depth values may be missing on objects without texture. In this case, the internal projector should be used for projecting an artificial texture. For single shot depth images, the Single+Out1 mode should be selected on the depth image page of the $r c_{\text {_ }}$ cube's Web GUI . For continuously computing depth images, the projector should be turned on for every second image by setting Out1 / Projector to ExposureAlternateActive in Pipeline $\ldots \rightarrow$ Configuration $\rightarrow$ IOControl .
<|end_chunk_92|><|start_chunk_93|>
### Page 30
- The internal projector may be too dark to be visible in the scene. Adjust the external lighting or the aperture of the projector as described in Adjust projector aperture (Section 4.6).
- The pattern of the internal projector may be too blurred to support depth computation. Adjust the focus of the projector as described in Adjust projector focus (Section 4.5).
- The camera focus may be inadequate for the working range. Please check the camera focus using a calibration grid as described in Adjust camera focus (Section 4.4).
- The calibration of the rc_viscore stereo camera may be inaccurate. Please check the calibration as described in Calibration (Section 4.7).

<|end_chunk_93|><|start_chunk_94|>
 7.3 Dark camera images 

The camera images of the $r c_{\text {_ }}$ viscore stereo camera, which can be seen on the camera page in the $r_{c}$ cube's Web GUI under Pipeline $\ldots \rightarrow$ Camera or by using the SGM®Producer, may be too dark. This can have the following reasons:

- The internal projector may be too bright. Increase the external lighting or reduce the projector brightness by adapting the aperture of the projector as described in Adjust projector aperture (Section 4.6).
<|end_chunk_94|><|start_chunk_95|>
### Page 31<|end_chunk_95|><|start_chunk_96|>
 8 Contact 
<|end_chunk_96|><|start_chunk_97|>
### 8.1 Support

For support issues, please see https://www.roboception.com/support or contact support@roboception.de.
<|end_chunk_97|><|start_chunk_98|>
### 8.2 Address

Roboception GmbH
Kaflerstrasse 2
81241 Munich
Germany

Web: https://www.roboception.com
Email: info@roboception.de
Phone: +49 8988950 79-0
<|end_chunk_98|><|start_chunk_99|>
### Page 32<|end_chunk_99|><|start_chunk_100|>
 Index 
<|end_chunk_100|><|start_chunk_101|>
## A

aperture, 21
<|end_chunk_101|><|start_chunk_102|>
## C

cables, 16
CAD model, 15
calibration, 24
connecting
rc_cube, 20
SGM Producer, 20
cooling, 15
coordinate frames, 18
<|end_chunk_102|><|start_chunk_103|>
## D

dimensions, 14
disposal, 8
<|end_chunk_103|><|start_chunk_104|>
## F

focus adjustment, 21
frame rate, 13
<|end_chunk_104|><|start_chunk_105|>
## H

humidity, 15
<|end_chunk_105|><|start_chunk_106|>
## I

installation, 19
IP54, 15
<|end_chunk_106|><|start_chunk_107|>
## L

lens cleaning, 25
<|end_chunk_107|><|start_chunk_108|>
## M

maintenance, 25
mounting, 19
<|end_chunk_108|><|start_chunk_109|>
## 0

operating conditions, 15
<|end_chunk_109|><|start_chunk_110|>
## $P$

pin assignments, 17
power cable, 26
power supply, 16, 26
power-up, 20
projector, 23
projector aperture, 23
projector brightness, 23
projector focus, 23
protection class, 15
<|end_chunk_110|><|start_chunk_111|>
## R

rc_cube
connecting, 20
resolution, 13
<|end_chunk_111|><|start_chunk_112|>
## S

safety, 10
SGM Producer
connecting, 20
spare parts, 26
specifications, 13
standards, 7
<|end_chunk_112|><|start_chunk_113|>
## T

temperature range, 15
troubleshooting, 28
<|end_chunk_113|><|start_chunk_114|>
## W

working range, 13, 21, 25
<|end_chunk_114|><|start_chunk_115|>
### Page 33<|end_chunk_115|><|start_chunk_116|>
 roboception 
<|end_chunk_116|><|start_chunk_117|>
## rc_viscore 3D Stereo Sensor

ASSEMBLY AND OPERATING MANUAL
<|end_chunk_117|><|start_chunk_118|>
## Roboception GmbH

Kaflerstrasse 2
81241 Munich
Germany
info@roboception.de
www.roboception.com

Tutorials:
GitHub:
Documentation:

Shop:

https://tutorials.roboception.com
https://github.com/roboception
https://doc.rc-visard.com
https://doc.rc-viscore.com
https://doc.rc-cube.com
https://doc.rc-randomdot.com
https://roboception.com/shop

For customer support, contact
+49 8988950790
(09:00-17:00 CET) support@roboception.de<|end_chunk_118|>
</document>

Respond only with the IDs of the chunks where you believe a split should occur. 
YOU MUST RESPOND WITH AT LEAST ONE SPLIT.
