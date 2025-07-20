# Chunking Prompt

**Source File:** ROBOCEPTION_rc_visard_manual_en_MISTRAL  
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

Roboception GmbH | April 2025
rc_visard 3D Stereo Sensor
ASSEMBLY AND OPERATING MANUAL
<|end_chunk_1|><|start_chunk_2|>
### Page 2<|end_chunk_2|><|start_chunk_3|>
 Revisions 

This product may be modified without notice, when necessary, due to product improvements, modifications, or changes in specifications. If such modification is made, the manual will also be revised; see revision information.

DOCUMENTATION REVISION 25.04.2 Apr 30, 2025
Applicable to rc_visard firmware 25.04.x
<|end_chunk_3|><|start_chunk_4|>
## MANUFACTURER
<|end_chunk_4|><|start_chunk_5|>
## Roboception GmbH

Kaflerstrasse 2
81241 Munich
Germany
CUSTOMER SUPPORT: support@roboception.de | +49 8988950 79-0 (09:00-17:00 CET)

Please read the operating manual in full and keep it with the product.
<|end_chunk_5|><|start_chunk_6|>
## COPYRIGHT

This manual and the product it describes are protected by copyright. Unless permitted by German intellectual property and related rights legislation, any use and circulation of this content requires the prior consent of Roboception or the individual owner of the rights. This manual and the product it describes therefore, may not be reproduced in whole or in part, whether for sale or not, without prior written consent from Roboception.

Information provided in this document is believed to be accurate and reliable. However, Roboception assumes no responsibility for its use.

Differences may exist between the manual and the product if the product has been modified after the manual's edition date. The information contained in this document is subject to change without notice.
<|end_chunk_6|><|start_chunk_7|>
### Page 3<|end_chunk_7|><|start_chunk_8|>
 Contents 

1 Introduction ..... 6
1.1 Overview ..... 6
1.2 Warranty ..... 8
1.3 Applicable standards ..... 9
1.3.1 Interfaces ..... 9
1.3.2 Approvals ..... 9
1.3.3 Standards ..... 9
1.4 Information on disposal ..... 10
1.5 Glossary ..... 12
2 Safety ..... 14
2.1 General warnings ..... 14
2.2 Intended use ..... 15
3 Hardware specification ..... 16
3.1 Scope of delivery ..... 16
3.2 Technical specification ..... 17
3.3 Environmental and operating conditions ..... 20
3.4 Power-supply specifications ..... 20
3.5 Wiring ..... 21
3.6 Mechanical interface ..... 23
3.7 Coordinate frames ..... 24
4 Installation ..... 26
4.1 Software license ..... 26
4.2 Power up ..... 26
4.3 Discovery of rc_visard devices ..... 26
4.3.1 Resetting configuration ..... 27
4.4 Network configuration ..... 28
4.4.1 Host name ..... 29
4.4.2 Automatic configuration (factory default) ..... 29
4.4.3 Manual configuration ..... 30
5 Measurement principles ..... 31
5.1 Stereo vision ..... 31
5.2 General information on 3D data ..... 32
5.2.1 Computing disparity images ..... 32
5.2.2 Computing depth images and point clouds ..... 33
5.2.3 Confidence and error images ..... 33
5.3 Sensor dynamics ..... 34
6 Software modules ..... 36
6.1 Camera module ..... 36
6.1.1 Rectification ..... 36
6.1.2 Viewing and downloading images ..... 37
6.1.3 Parameters, status values and services ..... 37
<|end_chunk_8|><|start_chunk_9|>
### Page 4
6.2 Stereo matching module ..... 45
6.2.1 Parameters ..... 45
6.2.2 Status values ..... 52
6.2.3 Services ..... 52
6.3 Navigation modules ..... 54
6.3.1 Sensor dynamics ..... 54
6.3.2 Visual odometry ..... 62
6.3.3 Stereo INS ..... 66
6.3.4 SLAM ..... 67
6.4 Detection \& Measure modules ..... 74
6.4.1 Measure ..... 74
6.4.2 LoadCarrier ..... 79
6.4.3 TagDetect ..... 92
6.4.4 ItemPick ..... 105
6.4.5 BoxPick ..... 123
6.4.6 SilhouetteMatch ..... 150
6.5 Configuration modules ..... 187
6.5.1 Hand-eye calibration ..... 187
6.5.2 CollisionCheck ..... 209
6.5.3 Camera calibration ..... 217
6.5.4 IO and Projector Control ..... 225
6.6 Database modules ..... 228
6.6.1 LoadCarrierDB ..... 229
6.6.2 RoiDB ..... 237
6.6.3 GripperDB ..... 243
7 Interfaces ..... 254
7.1 Web GUI ..... 254
7.1.1 Accessing the Web GUI ..... 254
7.1.2 Exploring the Web GUI ..... 255
7.1.3 Web GUI access control ..... 255
7.1.4 Downloading camera images ..... 256
7.1.5 Downloading depth images and point clouds ..... 256
7.2 GigE Vision 2.0/GenICam image interface ..... 257
7.2.1 GigE Vision ports ..... 257
7.2.2 Important GenICam parameters ..... 257
7.2.3 Important standard GenICam features ..... 258
7.2.4 Custom GenICam features of the rc_visard ..... 262
7.2.5 Chunk data ..... 265
7.2.6 Provided image streams ..... 265
7.2.7 Image stream conversions ..... 266
7.3 REST-API interface ..... 267
7.3.1 General API structure ..... 267
7.3.2 Migration from API version 1 ..... 269
7.3.3 Available resources and requests ..... 269
7.3.4 Data type definitions ..... 302
7.3.5 Swagger UI ..... 315
7.4 The rc_dynamics interface ..... 319
7.4.1 Starting/stopping dynamic-state estimation ..... 319
7.4.2 Configuring data streams ..... 319
7.4.3 Data-stream protocol ..... 320
7.4.4 rc_dynamics_api ..... 322
7.5 KUKA Ethernet KRL Interface ..... 322
7.5.1 Ethernet connection configuration ..... 323
7.5.2 Generic XML structure ..... 323
7.5.3 Services ..... 324
7.5.4 Parameters ..... 328
7.5.5 Migration to firmware version 22.01 ..... 330
<|end_chunk_9|><|start_chunk_10|>
### Page 5
7.5.6 Example applications ..... 330
7.5.7 Troubleshooting ..... 330
7.6 gRPC image stream interface ..... 330
7.6.1 gRPC service definition ..... 331
7.6.2 Image stream conversions ..... 333
7.6.3 Example client ..... 333
7.7 OPC UA interface ..... 333
7.8 Time synchronization ..... 333
7.8.1 NTP ..... 334
7.8.2 PTP ..... 334
7.8.3 Setting time manually ..... 334
8 Maintenance ..... 335
8.1 Lens cleaning ..... 335
8.2 Camera calibration ..... 335
8.3 Creating and restoring backups of settings ..... 335
8.4 Updating the firmware ..... 336
8.5 Restoring the previous firmware version ..... 337
8.6 Rebooting the $r c$ visard ..... 337
8.7 Updating the software license ..... 338
8.8 Downloading log files ..... 338
9 Accessories ..... 339
9.1 Connectivity kit ..... 339
9.2 Wiring ..... 339
9.2.1 Ethernet connections ..... 339
9.2.2 Power connections ..... 340
9.2.3 Power supplies ..... 340
9.3 Spare parts ..... 340
10 Troubleshooting ..... 341
10.1 LED colors ..... 341
10.2 Hardware issues ..... 341
10.3 Connectivity issues ..... 342
10.4 Camera-image issues ..... 342
10.5 Depth/Disparity, error, and confidence image issues ..... 343
10.6 Dynamics issues ..... 344
10.7 GigE Vision/GenICam issues ..... 345
11 Contact ..... 346
11.1 Support ..... 346
11.2 Downloads ..... 346
11.3 Address ..... 346
12 Appendix ..... 347
12.1 Pose formats ..... 347
12.1.1 Rotation matrix and translation vector ..... 348
12.1.2 ABB pose format ..... 348
12.1.3 FANUC XYZ-WPR format ..... 348
12.1.4 Franka Emika Pose Format ..... 349
12.1.5 Fruitcore HORST pose format ..... 351
12.1.6 Kawasaki XYZ-OAT format ..... 351
12.1.7 KUKA XYZ-ABC format ..... 352
12.1.8 Mitsubishi XYZ-ABC format ..... 352
12.1.9 Universal Robots pose format ..... 353
12.1.10 Yaskawa Pose Format ..... 354
HTTP Routing Table ..... 356
<|end_chunk_10|><|start_chunk_11|>
### Page 6
Index

Roboception GmbH
5
Rev: 25.04.2
Manual: rc_visard
Status: Apr 30, 2025
<|end_chunk_11|><|start_chunk_12|>
### Page 7<|end_chunk_12|><|start_chunk_13|>
 1 Introduction 

Indications in the manual
To prevent damage to the equipment and ensure the user's safety, this manual indicates each precaution related to safety with Warning. Supplementary information is provided as a Note.

Warning: Warnings in this manual indicate procedures and actions that must be observed to avoid danger of injury to the operator/user, or damage to the equipment. Software-related warnings indicate procedures that must be observed to avoid malfunctions or unexpected behavior of the software.

Note: Notes are used in this manual to indicate supplementary relevant information.
<|end_chunk_13|><|start_chunk_14|>
### 1.1 Overview

The 3D sensor rc_visard is an IP54-protected, self-registering stereo-camera with on-board computing capabilities.

The $r c \_v i s a r d$ provides real-time camera images and depth images, which can be used to compute 3D point clouds. Additionally, it provides confidence and error images as quality measures for each image acquisition. It offers an intuitive web UI (user interface) and a standardized GenICam interface, making it compatible with all major image processing libraries.
With optionally available software modules the $r c \_v i s a r d$ provides out-of-the-box solutions for object detection and robotic pick-and-place applications.
The $r c \_v i s a r d$ also provides self-localization based on image and inertial data. A mobile navigation solution can be established with the optional on-board SLAM module.
The $r c \_v i s a r d$ is offered with two different stereo baselines: The $r c \_v i s a r d 65$ is optimally suited for mounting on robotic manipulators, whereas the $r c \_v i s a r d 160$ can be employed as a navigation or as externally-fixed sensor.

The $r c \_v i s a r d$ 's intuitive calibration, configuration, and use enable 3D vision for everyone.
<|end_chunk_14|><|start_chunk_15|>
### Page 8
![img-0.jpeg](img-0.jpeg)

Fig. 1.1: rc_visard 65 and $r c \_v i s a r d 160$

The terms "sensor," "rc_visard 65," and "rc_visard 160" used throughout the manual all refer to the Roboception $r c \_v i s a r d$ family of self-registering cameras. Installation and control for all sensors are exactly the same, and all use the same mounting base.

Note: Unless specified, the information provided in this manual applies to both the $r c \_v i s a r d 65$ and $r c \_v i s a r d 160$ versions of the Roboception $r c \_v i s a r d$ sensor.

Note: This manual uses the metric system and mostly uses the units meter and millimeter. Unless otherwise specified, all dimensions in technical drawings are in millimeters.
<|end_chunk_15|><|start_chunk_16|>
### Page 9<|end_chunk_16|><|start_chunk_17|>
 1.2 Warranty 

Any changes or modifications to the hard- and software not expressly approved by Roboception could void the user's warranty and guarantee rights.

Warning: The rc_visard utilizes complex hardware and software technology that may behave in a way not intended by the user. The purchaser must design its application to ensure that any failure or the $r c \_v i s a r d$ does not cause personal injury, property damage, or other losses.

Warning: Do not attempt to take apart, open, service, or modify the $r c \_v i s a r d$. Doing so could present the risk of electric shock or other hazard. Any evidence of any attempt to open and/or modify the device, including any peeling, puncturing, or removal of any of the labels, will void the Limited Warranty.

Warning: CAUTION: to comply with the European CE requirement, all cables used to connect this device must be shielded and grounded. Operation with incorrect cables may result in interference with other devices or undesired effects of the product.

Note: This product may not be treated as household waste. By ensuring this product is disposed of correctly, you will help to protect the environment. For more detailed information about the recycling of this product, please contact your local authority, your household waste disposal service provider, or the product's supplier.
<|end_chunk_17|><|start_chunk_18|>
### Page 10<|end_chunk_18|><|start_chunk_19|>
 1.3 Applicable standards 
<|end_chunk_19|><|start_chunk_20|>
### 1.3.1 Interfaces

The $r c \_v i s a r d$ supports the following interface standards:
<|end_chunk_20|><|start_chunk_21|>
## GEN<i>CAM

The Generic Interface for Cameras standard is the basis for plug \& play handling of cameras and devices.
<|end_chunk_21|><|start_chunk_22|>
## GIG

GigE Vision® is an interface standard for transmitting high-speed video and related control data over Ethernet networks.
<|end_chunk_22|><|start_chunk_23|>
### 1.3.2 Approvals

The $r c \_v i s a r d$ has received the following approvals:
![img-1.jpeg](img-1.jpeg)

EC Declaration of Conformity

NRTL certification by TÜV Süd

Changes or modifications not expressly approved by the manufacturer could void the user's authority to operate the equipment. This device complies with Part 15 of the FCC rules. Operation is subject to the following two conditions:

1. This device may not cause harmful interference, and
2. this device must accept any interference received, including interference that may cause undesired operation.
<|end_chunk_23|><|start_chunk_24|>
### 1.3.3 Standards

The $r c \_v i s a r d$ has been tested to be in compliance with the following standards:

- AS/NZS CISPR32 : 2015 Information technology equipment, Radio disturbance characteristics, Limits and methods of measurement
- CISPR 32 : 2015 Electromagnetic compatibility of multimedia equipment - Emission requirements
- GB 9254 : 2008 This standard is out of the accreditation scope. Information technology equipment, Radio disturbance characteristics, Limits and methods of measurement
<|end_chunk_24|><|start_chunk_25|>
### Page 11
- EN 55032 : 2015 Electromagnetic compatibility of multimedia equipment - Emission requirements
- EN 55024 : 2010 +A1:2015 Information technology equipment, Immunity characteristics, Limits and methods of measurement
- CISPR 24 : 2015 +A1:2015 International special committee on radio interference, Information technology equipment-Immunity characteristics-Limits and methods of measurement
- EN 61000-6-2 : 2005 Electromagnetic compatibility (EMC) Part 6-2:Generic standards - Immunity for industrial environments
- EN 61000-6-3 : 2007+A1:2011 Electromagnetic compatibility (EMC) - Part 6-3: Generic standards - Emission standard for residential, commercial and light-industrial environments
- Registered FCC ID: 2AVMTRCV17
- Certified for Canada according to CAN ICES-3(B)/NMB-3(B)

<|end_chunk_25|><|start_chunk_26|>
 1.4 Information on disposal 

![img-2.jpeg](img-2.jpeg)
<|end_chunk_26|><|start_chunk_27|>
## 1. Disposal of Waste Electrical \& Electronic Equipment

This symbol on the product(s) and / or accompanying documents means that used electrical and electronic products should not be mixed with general household waste. For proper treatment, recovery and recycling, please contact your supplier or the manufacturer. Disposing of this product correctly will help save valuable resources and prevent any potential negative effects on human health and the environment, which could otherwise arise from inappropriate waste handling.
<|end_chunk_27|><|start_chunk_28|>
## 2. Removal of batteries

If the products contain batteries and accumulators that can be removed from the product without destruction, these must be removed before disposal and disposed of separately as batteries.
The following batteries or accumulators are contained in the rc_visard: None
<|end_chunk_28|><|start_chunk_29|>
## 3. Options for returning old equipment

Owners of old devices can return them to the manufacturer to ensure proper disposal.
Please contact support (Section 11) about returning the device for disposal.
<|end_chunk_29|><|start_chunk_30|>
## 4. Data protection

End users of Electrical \& Electronic Equipment are responsible for deleting personal data on the waste equipment to be disposed of.
<|end_chunk_30|><|start_chunk_31|>
## 5. WEEE registration number
<|end_chunk_31|><|start_chunk_32|>
### Page 12
Roboception is registered under the registration number DE 33323989 at the stiftung elektroaltgeräte register, Nordostpark 72, 90411 Nuremberg, Germany, as a producer of electrical and/or electronic equipment.
<|end_chunk_32|><|start_chunk_33|>
 6. Collection and recovery quotas 

According to the WEEE Directive, EU member states are obliged to collect data on waste electrical and electronic equipment and to transmit this data to the European Commission. Further information can be found on the German Ministry for the Environment website.
<|end_chunk_33|><|start_chunk_34|>
## Information on Disposal outside the European Union

This symbol is valid only in the European Union. If you wish to discard this product please contact your local authorities or dealer and ask for the correct method of disposal.
<|end_chunk_34|><|start_chunk_35|>
### Page 13<|end_chunk_35|><|start_chunk_36|>
 1.5 Glossary 

DHCP The Dynamic Host Configuration Protocol (DHCP) is used to automatically assign an IP address to a network device. Some DHCP servers only accept known devices. In this case, an administrator needs to configure the DHCP server with the fixed MAC address of a device.
<|end_chunk_36|><|start_chunk_37|>
## DNS

mDNS The Domain Name Server (DNS) manages the host names and IP addresses of all network devices. It is responsible for resolving the host name into the IP address for communication with a device. A DNS can be configured to get this information automatically when a device appears on a network or manually by an administrator. In contrast, multicast DNS (mDNS) works without a central server by querying all devices on a local network each time a host name needs to be resolved. mDNS is available by default on Linux and Mac operating systems and is used when '.local' is appended to a host name.
DOF The Degrees Of Freedom (DOF) are the number of independent parameters for translation and rotation. In 3D space, 6DOF (i.e. three for translation and three rotation) are sufficient to describe an arbitrary position and orientation.

GenICam GenICam is a generic standard interface for cameras. It serves as a unified interface around other standards such as GigE Vision, Camera Link, USB, etc. See http://genicam.org for more information.

GigE Gigabit Ethernet (GigE) is a networking technology for transmitting data at one gigabit per second.
GigE Vision GigE Vision® is a standard for configuring cameras and transmitting images over a GigE network link. See http://gigevision.com for more information.

IMU An Inertial Measurement Unit (IMU) consists of three accelerometers and three gyroscopes that measure the linear accelerations and the turn rates in all three dimensions.

INS An Inertial Navigation System (INS) is a 3D measurement system which uses inertial measurements (accelerations and turn rates) to compute position and orientation information. We refer to our combination of stereo vision and inertial navigation as stereo INS.

IP
IP address The Internet Protocol (IP) is a standard for sending data between devices in a computer network. Every device requires an IP address, which must be unique in the network. The IP address can be configured by $D H C P$, Link-Local, or manually.
Link-Local Link-Local is a technology where network devices associate themselves with an IP address from the 169.254.0.0/16 IP range and check if it is unique in the local network. Link-Local can be used if $D H C P$ is unavailable and manual IP configuration is not or cannot be done. Link-Local is especially useful for connecting a network device directly to a host computer. By default, Windows 10 reverts automatically to Link-Local if DHCP is unavailable. Under Linux, Link-Local must be enabled manually in the network manager.

MAC address The Media Access Control (MAC) address is a unique, persistent address for networking devices. It is also known as the hardware address of a device. In contrast to the IP address, the MAC address is (normally) permanently given to a device and does not change.

NTP The Network Time Protocol (NTP) is a TCP/IP protocol for synchronizing time over a network. Basically a client requests the current time from a server, and uses it to set its own clock.

PTP The Precision Time Protocol (PTP, also known as IEEE1588) is a protocol which enables more precise and robust clock synchronization than with NTP.

SDK A Software Development Kit (SDK) is a collection of software development tools or a collection of software components.

SGM SGM stands for Semi-Global Matching and is a state-of-the-art stereo matching algorithm which offers brief run times and a great accuracy, especially at object borders, fine structures, and in weakly textured areas.
<|end_chunk_37|><|start_chunk_38|>
### Page 14
SLAM SLAM stands for Simultaneous Localization and Mapping and describes the process of creating a map of an unknown environment and simultaneously updating the sensor pose within the map.
TCP The Tool Center Point (TCP) is the position of the tool at the end effector of a robot. The position and orientation of the TCP determines the position and orientation of the tool in 3D space.
UDP The User Datagram Protocol (UDP) is the minimal message-oriented transport layer of the Internet Protocol (IP) family. It uses a simple connectionless transmission model with a minimum of protocol mechanism such as integrity verification (via checksum). The rc_visard uses UDP for publishing its estimated dynamical states (Section 6.3.1.2) via the rc_dynamics interface (Section 7.4). To receive this data, applications may use datagram sockets to bind to the endpoint of the data transmission consisting of a combination of an IP address and a service port number such as 192.168.0.100:49500, which is typically referred to as a destination of an rc_dynamics data stream in this documentation.
<|end_chunk_38|><|start_chunk_39|>
 URI 

URL A Uniform Resource Identifier (URI) is a string of characters identifying resources of the rc_visard's REST-API. An example of such a URI is /nodes/rc_camera/parameters/fps, which points to the fps run-time parameter of the stereo camera module.
A Uniform Resource Locator (URL) additionally specifies the full network location and protocol, i.e., an exemplary URL to locate the above resource would be https://<ip>/api/v1/nodes/ rc_camera/parameters/fps where <ip> refers to the rc_visard's IP address.
XYZ+quaternion Format to represent a pose. See Rotation matrix and translation vector (Section 12.1.1) for its definition.

XYZABC Format to represent a pose. See KUKA XYZ-ABC format (Section 12.1.7) for its definition.
<|end_chunk_39|><|start_chunk_40|>
### Page 15<|end_chunk_40|><|start_chunk_41|>
 2 Safety 

Warning: The operator must have read and understood all of the instructions in this manual before handling the $r c \_v i s a r d$ product.

Note: The term "operator" refers to anyone responsible for any of the following tasks performed in conjunction with $r c \_v i s a r d$ :

- Installation
- Maintenance
- Inspection
- Calibration
- Programming
- Decommissioning

This manual explains the rc_visard's various components and general operations regarding the product's whole life-cycle, from installation through operation to decommissioning.

The drawings and photos in this documentation are representative examples; differences may exist between them and the delivered product.
<|end_chunk_41|><|start_chunk_42|>
### 2.1 General warnings

Note: Any use of the $r c \_v i s a r d$ in noncompliance with these warnings is inappropriate and may cause injury or damage as well as void the warranty.
<|end_chunk_42|><|start_chunk_43|>
## Warning:

- The $r c \_v i s a r d$ needs to be properly mounted before use.
- All cable sets need to be secured to the $r c \_v i s a r d$ and the mount.
- Cords must be at most 30 m long.
- An appropriate DC power source must supply power to the $r c \_v i s a r d$.
- Each $r c \_v i s a r d$ must be connected to a separate power supply.
- The $r c \_v i s a r d$ 's housing must be grounded.
- The $r c \_v i s a r d$ 's and any related equipment's safety guidelines must always be satisfied.
- The $r c \_v i s a r d$ does not fall under the purview of the machinery, low voltage, or medical directives.
<|end_chunk_43|><|start_chunk_44|>
### Page 16<|end_chunk_44|><|start_chunk_45|>
 Risk assessment and final application: 

The $r c \_v i s a r d$ may be used on a robot. Robot, $r c \_v i s a r d$, and any other equipment used in the final application must be evaluated with a risk assessment. The system integrator's duty is to ensure respect for all local safety measures and regulations. Depending on the application, there may be risks that need additional protection/safety measures.
<|end_chunk_45|><|start_chunk_46|>
### 2.2 Intended use

The $r c \_v i s a r d$ is intended for data acquisition (e.g., images, egomotion and disparity images) in stationary and mobile robotic applications. The $r c \_v i s a r d$ is intended for installation on a robot, automated machinery, mobile platform, or stationary equipment. It can also be used for data acquisition in other applications.

Warning: The rc_visard is NOT intended for safety critical applications.

The GigE Vision® industry standard used by the $r c \_v i s a r d$ does not support authentication and encryption. All data from and to the device is transmitted without authentication and encryption and could be monitored or manipulated by a third party. It is the operator's responsibility to connect the $r c \_v i s a r d$ only to a secured internal network.

Warning: The $r c \_v i s a r d$ must be connected to secured internal networks.

The $r c \_v i s a r d$ may be used only within the scope of its technical specification. Any other use of the product is deemed unintended use. Roboception will not be liable for any damages resulting from any improper or unintended use.

Warning: Always comply with local and/or national laws, regulations and directives on automation safety and general machine safety.
<|end_chunk_46|><|start_chunk_47|>
### Page 17<|end_chunk_47|><|start_chunk_48|>
 3 Hardware specification 

Note: The following hardware specifications are provided here as a general reference; differences with the product may exist.
<|end_chunk_48|><|start_chunk_49|>
### 3.1 Scope of delivery

Standard delivery for an rc_visard includes the rc_visard sensor and a quickstart guide only. The full manual is available in digital form and is always installed on the sensor, accessible through the Web GUI (Section 7.1), and available at https://roboception.com/resources/knowledge-base/.

Note: The following items are not included in the delivery unless otherwise specified:

- Couplings, adapters, mounts
- Power supply unit, cabling, and fuses
- Network cabling

Please refer to Accessories (Section 9) for suggested third-party cable vendors.
A connectivity kit can be purchased for the rc_visard. It contains an M12 to RJ45 network cable, 24 V power supply, and a DC plug to M12 power adapter. Please refer to Accessories (Section 9) for details.

Note: The connectivity kit is intended only for initial setup, not for permanent installation in industrial environment.

The following picture shows the important parts of the rc_visard which are referenced later in the documentation.
![img-3.jpeg](img-3.jpeg)

Fig. 3.1: Parts description
<|end_chunk_49|><|start_chunk_50|>
### Page 18<|end_chunk_50|><|start_chunk_51|>
 3.2 Technical specification 

The common technical specifications for the rc_visard variants are given in Table 3.1. The rc_visard 160 is available with two different types of lenses: 4 mm and 6 mm focal length. The rc_visard 65 is only available with 4 mm lenses.

Table 3.1: Common technical specifications for both rc_visard baselines

|  | rc_visard 65 / rc_visard 160 |
| :-- | :-- |
| Image resolution | $1280 \times 960$ pixel, color or monochrome |
| Field of view | 4 mm lens: Horizontal: $61^{\circ}$, Vertical: $48^{\circ}$ <br> 6 mm lens: Horizontal: $43^{\circ}$, Vertical: $33^{\circ}$ |
| IR Cutoff | 650 nm |
| Depth image | $1280 \times 960$ pixel (Full) @ 1 Hz (with StereoPlus <br> license) |
|  | $640 \times 480$ pixel (High) @ 3 Hz <br> $320 \times 240$ pixel (Medium) @ 15 Hz <br> $214 \times 160$ pixel (Low) @ 25 Hz |
| Egomotion | 200 Hz , low latency |
| Computing unit | Nvidia Tegra K1 |
| Power supply | 18 V to 30 V |
| Cooling | Passive |

The $r c \_v i s a r d 65$ and $r c \_v i s a r d 160$ differ in their baselines, which affects depth range and resolution as well as the sensors' size and weight.

Table 3.2: Differing technical specifications for the $r c \_v i s a r d$ variants

|  | $r c \_v i s a r d 65$ | $r c \_v i s a r d 160$ |
| :-- | :-- | :-- |
| Baseline | 65 mm | 160 mm |
| Depth range | 0.2 m to infinity | 0.5 m to infinity |
| Size $(\mathrm{W} \times \mathrm{H} \times \mathrm{L})$ | $135 \mathrm{~mm} \times 75 \mathrm{~mm} \times 96$ <br> mm | $230 \mathrm{~mm} \times 75 \mathrm{~mm} \times 84$ <br> mm |
| Mass | 0.68 kg | 0.84 kg |

The combination of baselines and lens types leads to different resolutions and accuracies.
<|end_chunk_51|><|start_chunk_52|>
### Page 19
Table 3.3: Resolution and accuracy of the rc_visard variants in millimeters with full resolution stereo matching and random dot projection on non-reflective and non-transparent objects.

|  | distance (mm) | rc_visard 65-4 | rc_visard 160-4 | rc_visard 160-6 |
| :--: | :--: | :--: | :--: | :--: |
| lateral resolution $(\mathrm{mm})$ | 200 | 0.2 |  |  |
|  | 500 | 0.5 | 0.5 | 0.3 |
|  | 1000 | 0.9 | 0.9 | 0.6 |
|  | 2000 | 1.9 | 1.9 | 1.3 |
|  | 3000 | 2.8 | 2.8 | 1.9 |
| depth resolution $(\mathrm{mm})$ | 200 | 0.04 |  |  |
|  | 500 | 0.2 | 0.1 | 0.06 |
|  | 1000 | 0.9 | 0.4 | 0.3 |
|  | 2000 | 3.6 | 1.5 | 1.0 |
|  | 3000 | 8.0 | 3.3 | 2.2 |
| Average depth accuracy (mm) | 200 | 0.2 |  |  |
|  | 500 | 0.9 | 0.4 | 0.3 |
|  | 1000 | 3.6 | 1.5 | 1.0 |
|  | 2000 | 14.2 | 5.8 | 3.9 |
|  | 3000 | 32.1 | 13.0 | 8.8 |

The $r c$ visard can be equipped with on-board software modules for additional features. These software modules can be ordered from the Roboception and require a license update.
<|end_chunk_52|><|start_chunk_53|>
### Page 20
![img-4.jpeg](img-4.jpeg)

Fig. 3.2: Overall dimensions of the $r c \_v i s a r d 65$
![img-5.jpeg](img-5.jpeg)

Fig. 3.3: Overall dimensions of the $r c \_v i s a r d 160$
<|end_chunk_53|><|start_chunk_54|>
### Page 21
CAD models of the $r c \_$visard can be downloaded from http://www.roboception.com/download. The CAD models are provided as-is, with no guarantee of correctness. When a material property of aluminum is assigned (density of $2.76 \frac{\mathrm{~g}}{\mathrm{~g} / \mathrm{m}^{3}}$ ), the mass properties of the CAD model are within $5 \%$ of the actual product with respect to weight and center of mass, and within $10 \%$ with respect to moment of inertia.
<|end_chunk_54|><|start_chunk_55|>
 3.3 Environmental and operating conditions 

The $r c \_v i s a r d$ is designed for industrial applications. Always respect the storage, transport, and operating environmental conditions outlined in Table 3.4.

Table 3.4: Environmental conditions

|  | $r c \_v i s a r d$ |
| :-- | :-- |
| Storage/Transport temperature | $-25^{\circ} \mathrm{C}$ to $70^{\circ} \mathrm{C}$ |
| Operating temperature | $0^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$ |
| Relative humidity (non condensing) | $20 \%$ to $80 \%$ |
| Vibration | 5 g |
| Shock | 50 g |
| Protection class | IP54 |
| Others | - Free from corrosive liquids or gases |
|  | - Free from explosive liquids or gases |
|  | - Free from powerful electromagnetic interference |

The $r c \_v i s a r d$ is designed for an operating temperature (surrounding environment) of $0^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$ and relies on convective (passive) cooling. Unobstructed airflow, especially around the cooling fins, needs to be ensured during use. The $r c \_v i s a r d$ should only be mounted using the provided mechanical mounting interface, and all parts of the housing must remain uncovered. A free space of at least 10 cm extending in all directions from the housing, and sufficient air exchange with the environment is required to ensure adequate cooling. Cooling fins must be free of dirt and other contamination.
The housing temperature depends on the processing load, sensor orientation, and surrounding environmental temperatures. When the sensor's exposed housing surfaces exceed $60^{\circ} \mathrm{C}$, the LED at the front will turn from green to red.

Warning: For hand-guided applications, a heat-insulated handle should be attached to the sensor to reduce the risk of burn injuries due to skin exposure to surface temperatures exceeding $60^{\circ} \mathrm{C}$.
<|end_chunk_55|><|start_chunk_56|>
### 3.4 Power-supply specifications

The $r c \_v i s a r d$ needs to be supplied by a DC voltage source. The $r c \_v i s a r d$ 's standard package doesn't include a DC power supply. The power supply contained in the connectivity kit may be used for initial setup. For permanent installation, it is the customer's responsibility to provide suitable DC power. Each $r c \_v i s a r d$ must be connected to a separate power supply. Connection to domestic grid power is only allowed through a power supply certified as EN55011 Class B.

Table 3.5: Absolute maximum ratings for power supply

|  | Min | Nominal | Max |
| :-- | :-- | :-- | :-- |
| Supply voltage | 18.0 V | 24 V | 30.0 V |
| Max power consumption |  |  | 25 W |
| Overcurrent protection | Supply must be fuse-protected to a maximum of 2 A |  |  |
| EMC compliance | see Standards (Section 1.3.3) |  |  |
<|end_chunk_56|><|start_chunk_57|>
### Page 22
Warning: Exceeding maximum power rating values may lead to damage of the rc_visard, power supply, and connected equipment.

Warning: A separate power supply must power each $r c \_v i s a r d$.

Warning: Connection to domestic grid power is allowed through a power supply certified as EN55011 Class B only.
<|end_chunk_57|><|start_chunk_58|>
 3.5 Wiring 

Cables are not provided with the $r c \_v i s a r d$ standard package. It is the customer's responsibility to obtain the proper cabling. Accessories (Section 9) provides an overview of suggested components.

Warning: Proper cable management is mandatory. Cabling must always be secured to the $r c \_v i s a r d$ mount with a strain-relief clamp so that no forces due to cable movements are exerted on the $r c \_v i s a r d$ 's M12 connectors. Enough slack needs to be provided to allow for full range of movement of the $r c \_v i s a r d$ without straining the cable. The cable's minimum bend radius needs to be observed.

The $r c \_v i s a r d$ provides an industrial 8-pin A-coded M12 socket connector for Ethernet connectivity and an 8-pin A-coded M12 plug connector for power and GPIO connectivity. Both connectors are located at the back. Their locations (distance from center lines) are identical for both baseline variants. The location of both connectors on the $r c \_v i s a r d$ is shown in Fig. 3.4.
![img-6.jpeg](img-6.jpeg)

Fig. 3.4: Locations of the electrical connections for the $r c \_v i s a r d$, with Ethernet on top and power on the bottom

Connectors are rotated so that standard $90^{\circ}$ angled connectors will exit horizontally, away from the camera (away from the cooling fins).
<|end_chunk_58|><|start_chunk_59|>
### Page 23
![img-7.jpeg](img-7.jpeg)

Fig. 3.5: Pin positions for power and Ethernet connector

Pin assignments for the Ethernet connector are given in Fig. 3.6.
![img-8.jpeg](img-8.jpeg)

Fig. 3.6: Pin assignments for M12 to Ethernet cabling

Pin assignments for the power connector are given in Table 3.6.
Table 3.6: Pin assignments for the power connector

| Pin | Assignment |
| :-- | :-- |
| 1 | GPIO In 2 |
| 2 | Power |
| 3 | GPIO In 1 |
| 4 | GPIO Gnd |
| 5 | GPIO Vcc |
| 6 | GPIO Out 1 (image expo- <br> sure) |
| 7 | Gnd |
| 8 | GPIO Out 2 |

GPIOs are decoupled by photocoupler. GPIO Out 1 by default provides an exposure sync signal with a logic high level for the duration of the image exposure. All GPIOs can be controlled via the IOControl module (IO and Projector Control, Section 6.5.4). Pins of unsused GPIOs should be left floating.

Warning: It is especially important that during the boot phase GPIO In 1 is left floating or remains low. The $r c \_v i s a r d$ will not boot if the pin is high during boot time.
<|end_chunk_59|><|start_chunk_60|>
### Page 24
GPIO circuitry and specifications are shown in Fig. 3.7. The maximum rated voltage for GPIO In and GPIO Vcc is 30 V .
![img-9.jpeg](img-9.jpeg)

Fig. 3.7: GPIO circuitry and specifications - do not connect signals higher than 30 V

Warning: Do not connect signals with voltages higher than 30 V to the rc_visard.
<|end_chunk_60|><|start_chunk_61|>
 3.6 Mechanical interface 

The $r c \_v i s a r d 65$ and $r c \_v i s a r d 160$ offer identical mounting-point setups at the bottom.
<|end_chunk_61|><|start_chunk_62|>
### Page 25
![img-10.jpeg](img-10.jpeg)

Fig. 3.8: Mounting-point for connecting the $r c \_v i s a r d$ to robots or other mountings

For troubleshooting and static applications, the sensor may be mounted using the standardized tripod thread (UNC 1/4"-20) indicated at the coordinate-frame origin. For dynamic applications such as mounting on a robotic arm, the sensor must be mounted with three M4 (metric standard) 8.8 machine screws tightened to 2.5 Nm and secured with a medium-strength threadlocking adhesive such as Loctite 243. Maximum thread depth is 6 mm . The two 4 mm diameter holes may be used for positioning pins (ISO 23384 m 6 ) to ensure precise repositioning of the sensor.

Warning: For dynamic applications, the $r c \_v i s a r d$ must be mounted with three M4 8.8 machine screws tightened to 2.5 Nm torque and secured with threadlocking adhesive. Do not use highstrength bolts. The engaged thread depth must be at least 5 mm .
<|end_chunk_62|><|start_chunk_63|>
 3.7 Coordinate frames 

The $r c \_v i s a r d$ 's coordinate-frame origin is defined as the exit pupil of the left camera lens. This frame is called sensor coordinate frame or camera coordinate frame. An approximate location for the $r c \_v i s a r d$ is shown in the next image.

The mounting-point frame for the $r c \_v i s a r d$ is defined to be at the bottom, centered in the tripod thread, with orientation identical to that of the sensor's coordinate frame.
Fig. 3.9 and Fig. 3.10 show approximate offsets.
<|end_chunk_63|><|start_chunk_64|>
### Page 26
![img-11.jpeg](img-11.jpeg)

Fig. 3.9: Approximate location of sensor/camera coordinate frame (inside left lens) and mounting-point frame (at tripod thread) for the $r c \_v i s a r d 65$
![img-12.jpeg](img-12.jpeg)

Fig. 3.10: Approximate locations of sensor/camera coordinate frame (inside left lens) and mountingpoint frame (at tripod thread) for the $r c \_v i s a r d 160$

Note: The correct offset between the sensor/camera frame and a robot coordinate frame can be calibrated through the hand-eye-calibration procedure (Section 6.5.1).
<|end_chunk_64|><|start_chunk_65|>
### Page 27<|end_chunk_65|><|start_chunk_66|>
 4 Installation 

Warning: The instructions on Safety (Section 2) related to the rc_visard must be read and understood prior to installation.

The $r c \_v i s a r d$ offers a Gigabit Ethernet interface for connecting the device to a computer network. All communications to and from the device are performed via this interface. The $r c \_v i s a r d$ has an on-board computing resource that requires booting time after powering up the device.
<|end_chunk_66|><|start_chunk_67|>
### 4.1 Software license

Every $r c \_v i s a r d$ device ships with a pre-installed license file for licensing and protection of the installed software packages. The license is bound to that specific $r c \_v i s a r d$ device and cannot be used or transferred to other devices.

The functionality of the $r c \_v i s a r d$ can be enhanced anytime by upgrading the license (Section 8.7), e.g., for optionally available software modules.

Note: The $r c \_v i s a r d$ requires to be rebooted whenever the installed licenses have changed.

Note: The license status can be retrieved via the $r c \_v i s a r d$ 's various interfaces such as the System $\rightarrow$ Firmware \& License page of the Web GUI (Section 7.1).
<|end_chunk_67|><|start_chunk_68|>
### 4.2 Power up

Note: Always fully connect and tighten the M12 power connector on the rc_visard before turning on the power supply.

After connecting the $r c \_v i s a r d$ to the power, the LED on the front of the device should immediately illuminate. During the device's boot process, the LED will change color and will eventually turn green. This signals that all processes are up and running.

If the network is not plugged in or the network is not properly configured, then the LED will flash red every 5 seconds. In this case, the device's network configuration should be verified. See LED colors (Section 10.1) for more information on the LED color codes.
<|end_chunk_68|><|start_chunk_69|>
### 4.3 Discovery of $r c \_v i s a r d$ devices

Roboception $r c \_v i s a r d$ devices that are powered up and connected to the local network or directly to a computer can be found using the standard GigE Vision® discovery mechanism.
<|end_chunk_69|><|start_chunk_70|>
### Page 28
Roboception offers the open-source tool rcdiscover-gui, which can be downloaded free of charge from https://github.com/roboception/rcdiscover/releases for Windows and Linux. The tool's Windows version consists of a single executable for Windows 7, 10 and 11, which can be executed without installation. For Linux an installation package is available for Ubuntu.
At startup, all available GigE Vision® devices - including rc_visard devices - are listed with their names, serial numbers, current IP addresses, and unique MAC addresses. The discovery tool finds all devices reachable by global broadcasts. Misconfigured devices that are located in different subnets than the application host may also be listed. A tickmark in the discovery tool indicates whether devices are actually reachable via a web browser.
![img-13.jpeg](img-13.jpeg)

Fig. 4.1: Label on the $r c \_v i s a r d$ indicating model, serial number and MAC address
![img-14.jpeg](img-14.jpeg)

Fig. 4.2: rcdiscover-gui tool for finding connected GigE Vision® devices

After successful discovery, a double click on the device row opens the Web GUI (Section 7.1) of the device in the operating system's default web browser. Google Chrome or Mozilla Firefox are recommended as web browser.
<|end_chunk_70|><|start_chunk_71|>
 4.3.1 Resetting configuration 

A misconfigured device can be reset by using the Reset $r c \_v i s a r d$ button in the discovery tool. The reset mechanism is only available for two minutes after device startup. Thus, the $r c \_v i s a r d$ may require rebooting before being able to reset the device.
<|end_chunk_71|><|start_chunk_72|>
### Page 29
![img-15.jpeg](img-15.jpeg)

Fig. 4.3: Reset dialog of the rcdiscover-gui tool

If the discovery tool still successfully detects the the misconfigured rc_visard, then the latter can be selected from the rc-visard drop-down menu. Otherwise, the rc_visard's MAC address, which is printed on the device label, can be entered manually into the designated fields.

One of four options can be chosen after entering the MAC address:

- Reset Parameters: Reset all rc_visard parameters, such as frame rate, that are configurable via Web GUI (Section 7.1).
- Reset Network: Reset network settings and user-defined name.
- Reset All: Reset the rc_visard parameters as well as network settings and user-defined name.
- Switch Partitions: Allows a rollback to be performed as described in Restoring the previous firmware version (Section 8.5).

A white status LED followed by a device reboot indicates a successful reset. If no reaction is noticeable, the two minutes time slot may have elapsed, requiring another reboot.

Note: The reset mechanism is only available for the first two minutes after startup.
<|end_chunk_72|><|start_chunk_73|>
 4.4 Network configuration 

The rc_visard requires an Internet Protocol (IP) address for communication with other network devices. The IP address must be unique in the local network, and can be set either manually via a user-configurable persistent IP address, or automatically via DHCP. If none of these IP configuration methods apply, the rc_visard falls back to a Link-Local IP address.
Following the GigE Vision ${ }^{\circledR}$ standard, the priority of IP configuration methods on the rc_visard is

1. Persistent IP (if enabled)
2. DHCP (if enabled)
3. Link-Local
<|end_chunk_73|><|start_chunk_74|>
### Page 30
![img-16.jpeg](img-16.jpeg)

Fig. 4.4: rc_visard's IP configuration method selection flowchart

Options for changing the $r c \_v i s a r d$ 's network settings and IP configuration are:

- the System $\rightarrow$ Network page of the $r c \_v i s a r d$ 's Web GUI - if it is reachable in the local network already, see Web GUI (Section 7.1)
- any configuration tool compatible with GigE Vision® 2.0, or Roboception's command-line tool gc_config. Typically, these tools scan for all available GigE Vision® devices on the network. All $r c \_v i s a r d$ devices can be uniquely identified by their serial number and MAC address, which are both printed on the device.
- temporarily changing or completely resetting the $r c \_v i s a r d$ 's network configuration via Roboception's rcdiscover-gui tool, see Discovery of rc_visard devices (Section 4.3)

Note: The command-line tool gc_config is part of Roboception's open-source convenience layer rc_genicam_api, which can be downloaded free of charge for Windows and Linux from http://www. roboception.com/download.
<|end_chunk_74|><|start_chunk_75|>
 4.4.1 Host name 

The $r c \_v i s a r d$ 's host name is based on its serial number, which is printed on the device, and is defined as rc-visard-<serial number>.
<|end_chunk_75|><|start_chunk_76|>
### 4.4.2 Automatic configuration (factory default)

The Dynamic Host Configuration Protocol (DHCP) is preferred for setting an IP address. If DHCP is active on the $r c \_v i s a r d$, which is the factory default, the device tries to contact a DHCP server at startup and every time the network cable is being plugged in. If a DHCP server is available on the network, the IP address is automatically configured.
In some networks, the DHCP server is configured so that it only accepts known devices. In this case, the Media Access Control address (MAC address), which is printed on the device label, needs to be configured in the DHCP server. At the same time, the $r c \_v i s a r d$ 's host name can also be set in the Domain
<|end_chunk_76|><|start_chunk_77|>
### Page 31
Name Server (DNS). Both MAC address and host name should be sent to the network administrator for configuration.

If the rc_visard cannot contact a DHCP server within about 15 seconds after startup, or after plugging in the network cable, it assigns itself a unique IP address. This process is called Link-Local. This option is especially useful for connecting the $r c \_$visard directly to a computer. The computer must be configured for Link-Local as well. Link-Local might already be configured as a standard fallback option, as it is under Windows 10. Other operating systems such as Linux require Link-Local to be explicitly configured in their network managers.
<|end_chunk_77|><|start_chunk_78|>
 4.4.3 Manual configuration 

Specifying a persistent, i.e. static IP address manually might be useful in some cases. This address is stored on the rc_visard to be used on device startup or network reconnection. Please make sure the selected IP address, subnet mask and gateway will not cause any conflicts on the network.

Warning: The IP address must be unique within the local network and within the local network's range of valid addresses. Furthermore, the subnet mask must match the local network; otherwise, the $r c \_$visard may become inaccessible. This can be avoided by using automatic configuration as explained in Automatic configuration (factory default) (Section 4.4.2).

If this IP address cannot be assigned, e.g. because it is already used by another device in the network, IP configuration will fall back to automatic configuration via DHCP (if enabled) or a Link-Local address.
<|end_chunk_78|><|start_chunk_79|>
### Page 32<|end_chunk_79|><|start_chunk_80|>
 5 Measurement principles 

The rc_visard is a self-registering 3D camera. It provides rectified camera, disparity, confidence, and error images, which enable the viewed scene's depth values along with their uncertainties to be computed. Furthermore, the motion of visual features in the images is combined with acceleration and turn-rate measurements at a high rate, which enables the sensor to provide real-time estimates of its current pose, velocity, and acceleration.

In the following, the underlying measurement principles are explained in more detail.
<|end_chunk_80|><|start_chunk_81|>
### 5.1 Stereo vision

In stereo vision, 3D information about a scene can be extracted by comparing two images taken from different viewpoints. The main idea behind using a camera pair for measuring depth is the fact that object points appear at different positions in the two camera images depending on their distance from the camera pair. Very distant object points appear at approximately the same position in both images, whereas very close object points occupy different positions in the left and right camera image. The object points' displacement in the two images is called disparity. The larger the disparity, the closer the object is to the camera. The principle is illustrated in Fig. 5.1.
![img-17.jpeg](img-17.jpeg)

Fig. 5.1: Sketch of the stereo-vision principle: The more distant object (black) exhibits a smaller disparity $d_{2}$ than that of the close object (gray), $d_{1}$.

Stereo vision is a form of passive sensing, meaning that it emits neither light nor other signals to measure distances, but uses only light that the environment emits or reflects. Thus, the Roboception products utilizing this sensing principle can work indoors and outdoors and multiple devices can work together without interferences.

To compute the 3D information, the stereo matching algorithm must be able to find corresponding object points in the left and right camera images. For this, the algorithm requires texture, meaning changes in
<|end_chunk_81|><|start_chunk_82|>
### Page 33
image intensity values due to patterns or the objects' surface structure, in the images. Stereo matching is not possible for completely untextured regions, such as a flat white wall without any visible surface structure. The stereo matching method used by the rc_visard is SGM (Semi-Global Matching), which provides the best trade-off between runtime and accuracy, even for fine structures.
The following software modules are required to compute 3D information:

- Camera module: This module is responsible for capturing synchronized image pairs and transforming them into images approaching those taken by an ideal camera (rectification).
- Stereo matching module: This module computes disparities for the rectified stereo image pair using SGM (Section 6.2).
For stereo matching, the position and orientation of the left and right cameras relative to each other has to be known with very high accuracy. This is achieved by calibration. The rc_visard's cameras are pre-calibrated during production. However, if the rc_visard has been decalibrated, during transport for example, then the user has to recalibrate the stereo camera:
- Camera calibration: This module enables the user to recalibrate the rc_visard's stereo camera (Section 6.5.3).

<|end_chunk_82|><|start_chunk_83|>
 5.2 General information on 3D data 

The following sections describe how disparity images are computed from stereo image pairs and how disparity, error and confidence images can be used to compute depth data and depth errors.
<|end_chunk_83|><|start_chunk_84|>
### 5.2.1 Computing disparity images

After rectification, an object point is guaranteed to be projected onto the same pixel row in both left and right image. That point's pixel column in the right image is always lower than or equal to the same point's pixel column in the left image. The term disparity signifies the difference between the pixel columns in the right and left images and expresses the depth or distance of the object point from the camera. The disparity image stores the disparity values of all pixels in the left camera image.
The larger the disparity, the closer the object point. A disparity of 0 means that the projections of the object point are in the same image column and the object point is at infinite distance. Often, there are pixels for which disparity cannot be determined. This is the case for occlusions that appear on the left sides of objects, because these areas are not seen from the right camera. Furthermore, disparity cannot be determined for textureless areas. Pixels for which the disparity cannot be determined are marked as invalid with the special disparity value of 0 . To distinguish between invalid disparity measurements and disparity measurements of 0 for objects that are infinitely far away, the disparity value for the latter is set to the smallest possible disparity value above 0 .
To compute disparity values, the stereo matching algorithm has to find corresponding object points in the left and right camera images. These are points that represent the same object point in the scene. For stereo matching, the rc_visard uses SGM (Semi-Global Matching), which offers quick run times and great accuracy, especially at object borders, fine structures, and in weakly textured areas.
A key requirement for any stereo matching method is the presence of texture in the image, i.e., imageintensity changes due to patterns or surface structure within the scene. In completely untextured regions such as a flat white wall without any structure, disparity values can either not be computed or the results are erroneous or have low confidence (see Confidence and error images, Section 5.2.3). The texture in the scene should not be an artificial, repetitive pattern, since those structures may lead to ambiguities and hence to wrong disparity measurements.
When working with poorly textured objects or in untextured environments, a static artificial texture can be projected onto the scene using an external pattern projector. This pattern should be random-like and not contain repetitive structures. The rc_visard provides the IOControl module (see IO and Projector Control, Section 6.5.4) as optional software module which can control a pattern projector connected to the sensor.
<|end_chunk_84|><|start_chunk_85|>
### Page 34<|end_chunk_85|><|start_chunk_86|>
 5.2.2 Computing depth images and point clouds 

The following equations show how to compute an object point's actual 3D coordinates $P_{x}, P_{y}, P_{z}$ in the camera coordinate frame from the disparity image's pixel coordinates $p_{x}, p_{y}$ and the disparity value $d$ in pixels:

$$
\begin{aligned}
& P_{x}=\frac{p_{x} \cdot t}{d} \\
& P_{y}=\frac{p_{y} \cdot t}{d} \\
& P_{z}=\frac{f \cdot t}{d}
\end{aligned}
$$

where $f$ is the focal length after rectification in pixels and $t$ is the stereo baseline in meters, which was determined during calibration. These values are also transferred over the GenICam interface (see Custom GenICam features of the rc_visard, Section 7.2.4).

Note: The $r c \_v i s a r d$ 's camera coordinate frame is defined as shown in Coordinate frames (Section 3.7).

Note: The $r c \_v i s a r d$ reports a focal length factor via its various interfaces. It relates to the image width for supporting different image resolutions. The focal length $f$ in pixels can be easily obtained by multiplying the focal length factor by the image width in pixels.

Please note that equations (5.1) assume that the coordinate frame is centered in the principal point that is typically in the center of the image, and $p_{x}, p_{y}$ refer to the middle of the pixel, i.e. by adding 0.5 to the integer pixel coordinates. The following figure shows the definition of the image coordinate frame.
![img-18.jpeg](img-18.jpeg)

Fig. 5.2: The image coordinate frame's origin is defined to be at the image center $-w$ is the image width and $h$ is the image height.

The same equations, but with the corresponding GenICam parameters are given in Image stream conversions (Section 7.2.7).

The set of all object points computed from the disparity image gives the point cloud, which can be used for 3D modeling applications. The disparity image is converted into a depth image by replacing the disparity value in each pixel with the value of $P_{z}$.

Note: Roboception provides software and examples for receiving disparity images from the $r c \_v i s a r d$ via GigE Vision and computing depth images and point clouds. See http://www.roboception.com/ download.
<|end_chunk_86|><|start_chunk_87|>
### 5.2.3 Confidence and error images

For each disparity image, additionally an error image and a confidence image are provided, which give uncertainty measures for each disparity value. These images have the same resolution and the same
<|end_chunk_87|><|start_chunk_88|>
### Page 35
frame rate as the disparity image. The error image contains the disparity error $d_{\text {eps }}$ in pixels corresponding to the disparity value at the same image coordinates in the disparity image. The confidence image contains the corresponding confidence value $c$ between 0 and 1 . The confidence is defined as the probability of the true disparity value being within the interval of three times the error around the measured disparity $d$, i.e., $\left[d-3 d_{\text {eps }}, d+3 d_{\text {eps }}\right]$. Thus, the disparity image with error and confidence values can be used in applications requiring probabilistic inference. The confidence and error values corresponding to an invalid disparity measurement will be 0.
The disparity error $d_{\text {eps }}$ (in pixels) can be converted to a depth error $z_{\text {eps }}$ (in meters) using the focal length $f$ (in pixels), the baseline $t$ (in meters), and the disparity value $d$ (in pixels) of the same pixel in the disparity image:

$$
z_{e p s}=\frac{d_{e p s} \cdot f \cdot t}{d^{2}}
$$

Combining equations (5.1) and (5.2) allows the depth error to be related to the depth:

$$
z_{e p s}=\frac{d_{e p s} \cdot P_{z}^{2}}{f \cdot t}
$$

With the focal lengths and baselines of the different camera models and the typical combined calibration and stereo matching error $d_{\text {eps }}$ of 0.25 pixels, the depth accuracy can be visualized as shown below.
![img-19.jpeg](img-19.jpeg)
<|end_chunk_88|><|start_chunk_89|>
 5.3 Sensor dynamics 

In addition to providing 3D information about the scene, the rc_visard can also estimate its egomotion or dynamic state in real time. This comprises its current pose, i.e., its position and orientation relative to a reference coordinate system or reference frame, as well as its velocity and acceleration. Measurements from stereo visual odometry (SVO) and the integrated Inertial Measurement Unit (IMU) are fused to compute this information. This combination is called a Visual Inertial Navigation System (VINS).
Visual odometry observes the motion of characteristic points in the camera images to estimate the camera motion. Object points are projected on different pixels in the camera image depending on the camera's viewing position. Each point's 3D coordinates can also be computed using stereo matching between the point positions in the left and right camera images. Thus, for two different viewing positions A and B, two sets of corresponding 3D points are computed. Assuming a static environment, the motion that transforms one set of points into the other is the camera's motion. The principle is illustrated for a simplified 2D case in Fig. 5.3.
<|end_chunk_89|><|start_chunk_90|>
### Page 36
![img-20.jpeg](img-20.jpeg)

Fig. 5.3: Simplified sketch of the stereo visual odometry principle for 2D motions: Camera motion is computed from the observed motion of characteristic image points.

Since visual odometry relies on image-data quality, motion estimates deteriorate when the images are blurred or are poorly illuminated. Furthermore, visual odometry's frame rate is too low for control applications. That's why the $r c \_$visard has an integrated Inertial Measurement Unit (IMU), which measures the accelerations and angular velocities that occur when the $r c \_$visard moves. It also measures acceleration due to gravity, which gives global orientation in the vertical direction. Further, IMU measurements have a high rate of 200 Hz . The $r c \_$visard's linear velocity, position, and orientation can be computed by integrating the IMU measurements. However, the integration results suffer from increasing drift over time. The $r c \_$visard thus fuses accurate, but low-frequency and sometimes volatile visual odometry measurements with reliable high-rate IMU measurements to provide an accurate, robust, high-frequency estimate of the $r c \_$visard's current position, orientation, velocity, and acceleration, which can be used in a control loop.

In addition to the stereo camera module and the calibration module, pose-estimate computations require the following $r c \_$visard software modules:

- Sensor dynamics: This module handles starting, stopping, and streaming of the estimates for the individual modules (Section 6.3.1).
- Visual odometry: This module computes a motion estimate from the camera images (Section 6.3.2).
- Stereo INS: This module fuses the motion estimates from visual odometry with the measurements from the integrated IMU to provide real-time pose estimates at a high frequency (Section 6.3.3).
- SLAM: This module is optionally available for the $r c \_$visard and creates an internal map of the environment, which is used to correct pose errors (Section 6.3.4).
<|end_chunk_90|><|start_chunk_91|>
### Page 37<|end_chunk_91|><|start_chunk_92|>
 6 Software modules 

The rc_visard comes with several on-board software modules, each of which corresponds to a certain functionality and can be interfaced via its respective node in the REST-API interface (Section 7.3).
The $r c \_v i s a r d$ 's software modules can be divided into

- Camera module (Section 6.1) acquires images and performs planar rectification for using the camera as a measurement device. Images are provided both for further internal processing by other modules and for external use as GenICam image streams.
- Stereo matching module (Section 6.2) which provides 3D depth information such as disparity, error, and confidence images, and is also accessible via the rc_visard's GigE Vision/GenICam interface,
- Navigation modules (Section 6.3) which provide estimates of $r c \_v i s a r d$ 's current pose, velocity, and acceleration,
- Detection \& Measure modules (Section 6.4) which provide a variety of detection functionalities, such as grasp point computation and object detection,
- Configuration modules (Section 6.5) which enable the user to perform calibrations and configure the $r c \_v i s a r d$ for specific applications.
- Database modules (Section 6.6) which enable the user to configure global data available to all other modules, such as load carriers, regions of interest and grippers.

<|end_chunk_92|><|start_chunk_93|>
### 6.1 Camera module

The camera module is a base module which is available on every $r c \_v i s a r d$ and is responsible for image acquisition and rectification. It provides various parameters, e.g. to control exposure and frame rate.
<|end_chunk_93|><|start_chunk_94|>
### 6.1.1 Rectification

To simplify image processing, the camera module rectifies all camera images based on the camera calibration. This means that lens distortion is removed and the principal point is located exactly in the middle of the image.
The model of a rectified camera is described with just one value, which is the focal length. The $r c \_v i s a r d$ reports a focal length factor via its various interfaces. It relates to the image width for supporting different image resolutions. The focal length $f$ in pixels can be easily obtained by multiplying the focal length factor by the image width in pixels.
In case of a stereo camera, rectification also aligns images such that an object point is always projected onto the same image row in both images. The cameras' optical axes become exactly parallel.
<|end_chunk_94|><|start_chunk_95|>
### Page 38<|end_chunk_95|><|start_chunk_96|>
 6.1.2 Viewing and downloading images 

The rc_visard provides the time-stamped, rectified images over the GenICam interface (see Provided image streams, Section 7.2.6). Live streams of the images are provided with reduced quality in the Web GUI (Section 7.1).

The Web GUI also provides the possibility to download a snapshot of the current scene as a .tar.gz file as described in Downloading camera images (Section 7.1.4).
<|end_chunk_96|><|start_chunk_97|>
### 6.1.3 Parameters, status values and services
<|end_chunk_97|><|start_chunk_98|>
### 6.1.3.1 Parameters

The camera module is called rc camera and is represented by the Camera page in the desired pipeline in the Web GUI (Section 7.1). The user can change the camera parameters there, or directly via the REST-API (REST-API interface, Section 7.3) or GigE Vision (GigE Vision 2.0/GenICam image interface, Section 7.2).
<|end_chunk_98|><|start_chunk_99|>
## Parameter overview

This module offers the following run-time parameters:
<|end_chunk_99|><|start_chunk_100|>
### Page 39
Table 6.1: The rc_camera module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :--: | :--: | :--: | :--: | :--: | :--: |
| exp_auto | bool | false | true | true | Switching between auto and manual exposure (deprecated, please use exp_control instead) |
| exp_auto_average_max | float64 | 0.0 | 1.0 | 0.75 | Maximum average intensity in Auto exposure mode |
| exp_auto_average_min | float64 | 0.0 | 1.0 | 0.25 | Minimum average intensity in Auto exposure mode |
| exp_auto_mode | string | - | - | Normal | Auto-exposure mode: [Normal, Out1High, AdaptiveOut1] |
| exp_control | string | - | - | Auto | Exposure control mode: [Manual, Auto, HDR] |
| exp_height | int32 | 0 | 959 | 0 | Height of auto exposure region. 0 for whole image. |
| exp_max | float64 | $6.6 \mathrm{e}-05$ | 0.018 | 0.018 | Maximum exposure time in seconds in Auto exposure mode |
| exp_offset_x | int32 | 0 | 1279 | 0 | First column of auto exposure region |
| exp_offset_y | int32 | 0 | 959 | 0 | First row of auto exposure region |
| exp_value | float64 | $6.6 \mathrm{e}-05$ | 0.018 | 0.005 | Exposure time in seconds in Manual exposure mode |
| exp_width | int32 | 0 | 1279 | 0 | Width of auto exposure region. 0 for whole image. |
| fps | float64 | 1.0 | 25.0 | 25.0 | Frames per second in Hertz |
| gain_value | float64 | 0.0 | 18.0 | 0.0 | Gain value in decibel if not in Auto exposure mode |
| gamma | float64 | 0.1 | 10.0 | 1.0 | Gamma factor |
| wb_auto | bool | false | true | true | Switching white balance on and off (only for color camera) |
| wb_ratio_blue | float64 | 0.125 | 8.0 | 2.4 | Blue to green balance ratio if wb_auto is false (only for color camera) |
| wb_ratio_red | float64 | 0.125 | 8.0 | 1.2 | Red to green balance ratio if wb_auto is false (only for color camera) |
<|end_chunk_100|><|start_chunk_101|>
 Description of run-time parameters 

Each run-time parameter is represented by a row on the Web GUI's Camera page. The name in the Web GUI is given in brackets behind the parameter name and the parameters are listed in the order they appear in the Web GUI.
<|end_chunk_101|><|start_chunk_102|>
### Page 40
![img-21.jpeg](img-21.jpeg)

Fig. 6.1: The Web GUI's Camera page
fps (FPS (Hz))
This value is the cameras' frame rate (fps, frames per second), which determines the upper frequency at which depth images can be computed. This is also the frequency at which the $r c \_v i s a r d$ delivers images via GigE Vision. Reducing this frequency also reduces the network bandwidth required to transmit the images.
<|end_chunk_102|><|start_chunk_103|>
### Page 41
Via the REST-API, this parameter can be set as follows.
<|end_chunk_103|><|start_chunk_104|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?fps=<value>
<|end_chunk_104|><|start_chunk_105|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?fps=<value>
The camera always runs with 25 Hz to ensure proper working of internal modules such as visual odometry that need a constant frame rate. The user frame rate setting is implemented by excluding frames for stereo matching and transmission via GigE Vision to reduce bandwidth as shown in figure fig-fps.

| Internal acquisition | 圆 | 圆 | 圆 | 圆 | 圆 | 圆 | 圆 | 圆 | 圆 | 圆 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |

Fig. 6.2: Images are internally always captured with 25 Hz . The fps parameter determines how many of them are sent as camera images via GigE Vision.
gamma (Gamma)
The gamma value determines the mapping of perceived light to the brightness of a pixel. A gamma value of 1 corresponds to a linear relationship. Lower gamma values let dark image parts appear brighter. A value around 0.5 corresponds to human vision.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_105|><|start_chunk_106|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?gamma=<value>
<|end_chunk_106|><|start_chunk_107|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?gamma=<value>
exp_control (Exposure Auto, HDR or Manual)

The exposure control mode can be set to Auto, HDR or Manual. This replaces the deprecated exp_auto parameter.

Auto: This is the default mode in which the exposure time and gain factor is chosen automatically to correctly expose the image. The last automatically determined exposure and gain values are set into exp_value and gain_value when switching auto-exposure off.
HDR: The HDR mode computes high-dynamic-range images by combining images with different exposure times to avoid under-exposed and over-exposed areas. This decreases the frame rate and is only suitable for static scenes.

Manual: In the manual exposure mode the exposure time and gain are kept fixed independent of the resulting image brightness.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_107|><|start_chunk_108|>
## API version 2
<|end_chunk_108|><|start_chunk_109|>
### Page 42
PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?exp_control= ...<value>
<|end_chunk_109|><|start_chunk_110|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_camera/parameters?exp_control=<value>
<|end_chunk_110|><|start_chunk_111|>
## exp_auto_mode (Auto Exposure Mode)

The auto exposure mode can be set to Normal, Out1High or AdaptiveOut1. These modes are relevant when the rc_visard is used with an external light source or projector connected to the camera's GPIO Out1, which can be controlled by the IOControl module (IO and Projector Control, Section 6.5.4).
Normal: All images are considered for exposure control, except if the IOControl mode for GPIO Out1 is ExposureAlternateActive: then only images where GPIO Out1 is HIGH will be considered, since these images may be brighter in case GPIO Out1 is used to trigger an external light source.
Out1High: This exposure mode adapts the exposure time using only images with GPIO Out1 HIGH. Images where GPIO Out1 is LOW are not considered at all, which means, that the exposure time does not change when only images with Out1 LOW are acquired. This mode is recommended for using the acquisition_mode SingleFrameOut1 in the stereo matching module as described in Stereo Matching Parameters (Section 6.2.1) and having an external projector connected to GPIO Out1, when changes in the brightness of the scene should only be considered when Out1 is HIGH. This is the case, for example, when a bright part of the robot moves through the field of view of the camera just before a detection is triggered, which should not affect the exposure time.
AdaptiveOut1: This exposure mode uses all camera images and tracks the exposure difference between images with GPIO Out1 LOW and HIGH. While the IOControl mode for GPIO Out1 is LOW, the images are under-exposed by this exposure difference to avoid over-exposure for when GPIO Out1 triggers an external projector. The resulting exposure difference is given as Out1 Reduction below the live images. This mode is recommended for using the acquisition_mode SingleFrameOut1 in the stereo matching module as described in Stereo Matching Parameters (Section 6.2.1) and having an external projector connected to GPIO Out1, when changes in the brightness of the scene should be considered at all times. This is the case, for example, in applications where the external lighting changes.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_111|><|start_chunk_112|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?exp_auto_mode= ...<value>
<|end_chunk_112|><|start_chunk_113|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?exp_auto_mode=<value>
<|end_chunk_113|><|start_chunk_114|>
## exp_max (Max Exposure)

This value is the maximal exposure time in auto-exposure mode in seconds. The actual exposure time is adjusted automatically so that the images are exposed correctly. If the maximum exposure time is reached, but the images are still underexposed, the rc_visard stepwise increases the gain to increase the images' brightness. Limiting the exposure time is useful for avoiding or reducing motion blur during fast movements. However, higher gain introduces noise into the image. The best trade-off depends on the application.
<|end_chunk_114|><|start_chunk_115|>
### Page 43
Via the REST-API, this parameter can be set as follows.
<|end_chunk_115|><|start_chunk_116|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?exp_max= $\ldots<$ value $>$
<|end_chunk_116|><|start_chunk_117|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?exp_max=<value>
exp_auto_average_max (Max Brightness) and exp_auto_average_min (Min Brightness)

The auto-exposure tries to set the exposure time and gain factor such that the average intensity (i.e. brightness) in the image or exposure region is between a maximum and a minimum. The maximum brightness will be used if there is no saturation, e.g. no overexposure due to bright surfaces or reflections. In case of saturation, the exposure time and gain factor are reduced, but only down to the minimum brightness.

The maximum brightness has precedence over the minimum brightness parameter. If the minimum brightness is larger than the maximum brightness, the auto-exposure always tries to make the average intensity equal to the maximum brightness.

The current brightness is always shown in the status bar below the images.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_117|><|start_chunk_118|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?<exp_auto_...average_max |exp_auto_average_min>=<value>
<|end_chunk_118|><|start_chunk_119|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?<exp_auto_average_max|exp_auto_...average_min>=<value>
exp_offset_x, exp_offset_y, exp_width, exp_height (Exposure Region)

These values define a rectangular region in the left rectified image for limiting the area used for computing the auto exposure. The exposure time and gain factor of both images are chosen to optimally expose the defined region. This can lead to over- or underexposure of image parts outside the defined region. If either the width or height is 0 , then the whole left and right images are considered by the auto exposure function. This is the default.

The region is visualized in the Web GUI by a rectangle in the left rectified image. It can be defined using the sliders or by selecting it in the image after pressing the button Select Region in Image.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_119|><|start_chunk_120|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?<exp_offset_...x|exp_offset_y|exp_width|exp_height>=<value>
<|end_chunk_120|><|start_chunk_121|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?<exp_offset_x|exp_offset_y|exp_...width|exp_height>=<value>
<|end_chunk_121|><|start_chunk_122|>
### Page 44<|end_chunk_122|><|start_chunk_123|>
 exp_value (Exposure) 

This value is the exposure time in manual exposure mode in seconds. This exposure time is kept constant even if the images are underexposed.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_123|><|start_chunk_124|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?exp_value= $\ldots<$ value $>$
<|end_chunk_124|><|start_chunk_125|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?exp_value=<value>
gain_value (Gain (dB))

This value is the gain factor in decibel that can be set in manual exposure mode. Higher gain factors reduce the required exposure time but introduce noise.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_125|><|start_chunk_126|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?gain_value= $\ldots<$ value $>$
<|end_chunk_126|><|start_chunk_127|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?gain_value=<value>
<|end_chunk_127|><|start_chunk_128|>
## wb_auto (White Balance Auto or Manual)

This value can be set to true for automatic white balancing or false for manually setting the ratio between the colors using wb_ratio_red and wb_ratio_blue. The last automatically determined ratios are set into wb_ratio_red and wb_ratio_blue when switching automatic white balancing off. White balancing is without function for monochrome cameras and will not be displayed in the Web GUI in this case.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_128|><|start_chunk_129|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?wb_auto= $\ldots<$ value $>$
<|end_chunk_129|><|start_chunk_130|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/parameters?wb_auto=<value>
wb_ratio_blue and wb_ratio_red (Blue / Green and Red / Green)

These values are used to set blue to green and red to green ratios for manual white balance. White balancing is without function for monochrome cameras and will not be displayed in the Web GUI in this case.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_130|><|start_chunk_131|>
## API version 2
<|end_chunk_131|><|start_chunk_132|>
### Page 45
PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/parameters?<wb_ratio_blue|wb_ratio_ red $=<$ value $>$
<|end_chunk_132|><|start_chunk_133|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_camera/parameters?<wb_ratio_blue|wb_ratio_red>=<value>
These parameters are also available over the GenICam interface with slightly different names and partly with different units or data types (see GigE Vision 2.0/GenICam image interface, Section 7.2).
<|end_chunk_133|><|start_chunk_134|>
### 6.1.3.2 Status values

This module reports the following status values:
Table 6.2: The rc camera module's status values

| Name | Description |
| :--: | :--: |
| baseline | Stereo baseline $t$ in meters |
| brightness | Current brightness of the image as value between 0 and 1 |
| color | 0 for monochrome cameras, 1 for color cameras |
| device_trigger_sources | Gives the available trigger sources |
| exp | Current exposure time in seconds. This value is shown below the image preview in the Web GUI as Exposure (ms). |
| focal | Focal length factor normalized to an image width of 1 |
| fps | Current frame rate of the camera images in Hertz. This value is shown in the Web GUI below the image preview as FPS (Hz). |
| gain | Current gain factor in decibel. This value is shown in the Web GUI below the image preview as Gain (dB). |
| gamma | Current gamma value. |
| height | Height of the camera image in pixels. This value is shown in the Web GUI below the image preview as the second part of Resolution (px). |
| last_timestamp_grabbed | Timestamp of the last image acquired in case the camera is in trigger mode |
| out1_reduction | Fraction of reduction ( $0.0-1.0)$ of brightness for images with GPIO Out1=LOW in exp_auto_mode=AdaptiveOut1 or exp_auto_mode=Out1High. This value is shown in the Web GUI below the image preview as Out1 Reduction (\%). |
| params_override_active | 1 if parameters are temporarily overwritten by a calibration process |
| selfcalib_counter | How often a correction has been performed by the self-calibration |
| selfcalib_offset | Current offset determined by the self-calibration |
| temp_left | Temperature of the left camera sensor in degrees Celsius |
| temp_right | Temperature of the right camera sensor in degrees Celsius |
| test | 0 for live images and 1 for test images |
| time | Processing time for image grabbing in seconds |
| width | Width of the camera image in pixels. This value is shown in the Web GUI below the image preview as the first part of Resolution (px). |
<|end_chunk_134|><|start_chunk_135|>
### 6.1.3.3 Services

The camera module offers the following services.
reset_defaults
Restores and applies the default values for this module's parameters ("factory reset").
<|end_chunk_135|><|start_chunk_136|>
## Details
<|end_chunk_136|><|start_chunk_137|>
### Page 46
This service can be called as follows.
<|end_chunk_137|><|start_chunk_138|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_camera/services/reset_defaults
<|end_chunk_138|><|start_chunk_139|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_camera/services/reset_defaults
<|end_chunk_139|><|start_chunk_140|>
## Request

This service has no arguments.
<|end_chunk_140|><|start_chunk_141|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_141|><|start_chunk_142|>
### 6.2 Stereo matching module

The stereo matching module is a base module which is available on every $r c \_v i s a r d$ and uses the rectified stereo-image pair to compute disparity, error, and confidence images.
To compute full resolution disparity, error and confidence images, an additional StereoPlus license (Section 8.7) is required. This license is included in every rc_visard purchased after 31.01.2019.
<|end_chunk_142|><|start_chunk_143|>
### 6.2.1 Parameters

The stereo matching module is called rc_stereomatching in the REST-API and it is represented by the Depth Image page in the Web GUI (Section 7.1). The user can change the stereo matching parameters there, or use the REST-API (REST-API interface, Section 7.3) or GigE Vision (GigE Vision 2.0/GenICam image interface, Section 7.2).
<|end_chunk_143|><|start_chunk_144|>
### 6.2.1.1 Parameter overview

This module offers the following run-time parameters:
<|end_chunk_144|><|start_chunk_145|>
### Page 47
Table 6.3: The rc_stereomatching module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :--: | :--: | :--: | :--: | :--: | :--: |
| acquisition_mode | string | - | - | Continuous | Acquisition mode: [Continuous, SingleFrame, SingleFrameOut!] |
| double_shot | bool | false | true | false | Combination of disparity images from two subsequent stereo image pairs |
| exposure_adapt_timeout | float64 | 0.0 | 2.0 | 0.0 | Maximum time in seconds to wait after triggering in SingleFrame modes until auto exposure has finished adjustments |
| fill | int32 | 0 | 4 | 3 | Disparity tolerance for hole filling in pixels |
| maxdepth | float64 | 0.1 | 100.0 | 100.0 | Maximum depth in meters |
| maxdeptherr | float64 | 0.01 | 100.0 | 100.0 | Maximum depth error in meters |
| minconf | float64 | 0.5 | 1.0 | 0.5 | Minimum confidence |
| mindepth | float64 | 0.1 | 100.0 | 0.1 | Minimum depth in meters |
| quality | string | - | - | High | Quality: [Low, Medium, High, Full]. Full requires 'stereo_plus' license. |
| seg | int32 | 0 | 4000 | 200 | Minimum size of valid disparity segments in pixels |
| smooth | bool | false | true | true | Smoothing of disparity image (requires 'stereo_plus' license) |
| static_scene | bool | false | true | false | Accumulation of images in static scenes to reduce noise |
<|end_chunk_145|><|start_chunk_146|>
 6.2.1.2 Description of run-time parameters 

Each run-time parameter is represented by a row on the Web GUI's Depth Image page. The name in the Web GUI is given in brackets behind the parameter name and the parameters are listed in the order they appear in the Web GUI:
<|end_chunk_146|><|start_chunk_147|>
### Page 48
![img-22.jpeg](img-22.jpeg)

Fig. 6.3: The Web GUI's Depth Image page
acquisition_mode (Acquisition Mode)

The acquisition mode can be set to Continuous, SingleFrame (Single) or SingleFrameOut1 (Single + Out1). The first one is the default, which performs stereo matching continuously according to the user defined frame rate and the available computation resources. The two other modes perform stereo matching upon each click of the Acquire button. The Single + Out1 mode additionally controls an external projector that is connected to GPIO Out1 (IO and Projector Control, Section 6.5.4). In this mode, out1 mode of the IOControl module is automatically set to ExposureAlternateActive upon each trigger call and reset to Low after receiving images for stereo matching.
<|end_chunk_147|><|start_chunk_148|>
### Page 49
Note: The Single + Out1 mode can only change the out1_mode if the IOControl license is available on the rc_visard.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_148|><|start_chunk_149|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
acquisition_mode=<value>
<|end_chunk_149|><|start_chunk_150|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?acquisition_mode=<value>
<|end_chunk_150|><|start_chunk_151|>
## exposure_adapt_timeout (Exposure Adaptation Timeout)

The exposure adaptation timeout gives the maximum time in seconds that the system will wait after triggering an image acquisition until auto exposure has found the optimal exposure time. This timeout is only used in SingleFrame (Single) or SingleFrameOut1 (Single + Out1) acquisition mode with auto exposure active. This value should be increased in applications with changing lighting conditions, when images are under- oder overexposed and the resulting disparity images are too sparse. In these cases multiple images are acquired until the auto-exposure mode has adjusted or the timeout is reached, and only then the actual image acquisition is triggered.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_151|><|start_chunk_152|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...exposure_adapt_timeout=<value>
<|end_chunk_152|><|start_chunk_153|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?exposure_adapt_timeout= ...<value>
<|end_chunk_153|><|start_chunk_154|>
## quality (Quality)

Disparity images can be computed in different resolutions: Full (full image resolution), High (half of the full image resolution), Medium (quarter of the full image resolution) and Low (sixth of the full image resolution). Full resolution matching (Full) is only possible with a valid StereoPlus license. The lower the resolution, the higher the frame rate of the disparity image. Please note that the frame rate of the disparity, confidence, and error images will always be less than or equal to the camera frame rate. In case the projector is in ExposureAlternateActive mode, the frame rate of the images can be at most half of the camera frame rate.

A 25 Hz frame rate can be achieved only at the lowest resolution.
If full resolution is selected, the depth range is internally limited due to limited onboard memory resources. It is recommended to adjust mindepth and maxdepth to the depth range that is required by the application.
<|end_chunk_154|><|start_chunk_155|>
### Page 50
Table 6.4: Depth image resolutions depending on the chosen quality

| Quality | Full | High | Medium | Low |
| :-- | :--: | :--: | :--: | :--: |
| Resolution (pixel) | $1280 \times 960$ | $640 \times 480$ | $320 \times 240$ | $214 \times 160$ |

Via the REST-API, this parameter can be set as follows.
<|end_chunk_155|><|start_chunk_156|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...quality=<value>
<|end_chunk_156|><|start_chunk_157|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?quality=<value>
double_shot (Double-Shot)

Enabling this option will lead to denser disparity images, but will increase processing time.
For scenes recorded with a projector in Single + Out1 acquisition mode, or in continuous acquisition mode with the projector in ExposureAlternateActive mode, holes caused by reflections of the projector are filled with depth information computed from the images without projector pattern. In this case, the double_shot parameter must only be enabled if the scene does not change during the acquisition of the images.

For all other scenes, holes are filled with depth information computed from a downscaled version of the same image.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_157|><|start_chunk_158|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...double_shot=<value>
<|end_chunk_158|><|start_chunk_159|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?double_shot=<value>
static_scene (Static)

This option averages 8 consecutive camera images before matching. This reduces noise, which improves the stereo matching result. However, the latency increases significantly. The timestamp of the first image is taken as timestamp of the disparity image. This option only affects matching in full or high quality. It must only be enabled if the scene does not change during the acquisition of the 8 images.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_159|><|start_chunk_160|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...static_scene=<value>
<|end_chunk_160|><|start_chunk_161|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?static_scene=<value>
<|end_chunk_161|><|start_chunk_162|>
### Page 51<|end_chunk_162|><|start_chunk_163|>
 mindepth (Minimum Distance) 

The minimum distance is the smallest distance from the camera at which measurements should be possible. Larger values implicitly reduce the disparity range, which also reduces the computation time. The minimum distance is given in meters.

Depending on the capabilities of the sensor, the actual minimum distance can be higher than the user setting. The actual minimum distance will be reported in the status values.

In quality mode Full, the actual minimum distance can also be higher than the user-defined minimum distance due to memory limitations. In this case, lowering the maximum distance helps to reduce the actual minimum distance.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_163|><|start_chunk_164|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...mindepth=<value>
<|end_chunk_164|><|start_chunk_165|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?mindepth=<value>
<|end_chunk_165|><|start_chunk_166|>
## maxdepth (Maximum Distance)

The maximum distance is the largest distance from the camera at which measurements should be possible. Pixels with larger distance values are set to invalid in the disparity image. Setting this value to its maximum permits values up to infinity. The maximum distance is given in meters.

In quality mode Full, the actual minimum distance can be higher than the user-defined minimum distance due to memory limitations. In this case, lowering the maximum distance helps to reduce the actual minimum distance.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_166|><|start_chunk_167|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...maxdepth=<value>
<|end_chunk_167|><|start_chunk_168|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?maxdepth=<value>
<|end_chunk_168|><|start_chunk_169|>
## smooth (Smoothing)

This option activates advanced smoothing of disparity values. It is only available with a valid StereoPlus license.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_169|><|start_chunk_170|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...smooth=<value>
<|end_chunk_170|><|start_chunk_171|>
## API version 1 (deprecated)
<|end_chunk_171|><|start_chunk_172|>
### Page 52<|end_chunk_172|><|start_chunk_173|>
 fill (Fill-in) 

This option is used to fill holes in the disparity image by interpolation. The fill-in value is the maximum allowed disparity step on the border of the hole. Larger fill-in values can decrease the number of holes, but the interpolated values can have larger errors. At most $5 \%$ of pixels are interpolated. Interpolation of small holes is preferred over interpolation of larger holes. The confidence for the interpolated pixels is set to a low value of 0.5 . A fill-in value of 0 switches hole filling off.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_173|><|start_chunk_174|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters? $\ldots$ fill $=$ <value>
<|end_chunk_174|><|start_chunk_175|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?fill=<value>
<|end_chunk_175|><|start_chunk_176|>
## seg (Segmentation)

The segmentation parameter is used to set the minimum number of pixels that a connected disparity region in the disparity image must fill. Isolated regions that are smaller are set to invalid in the disparity image. The value is related to the high quality disparity image with half resolution and does not have to be scaled when a different quality is chosen. Segmentation is useful for removing erroneous disparities. However, larger values may also remove real objects.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_176|><|start_chunk_177|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?seg= $\ldots<$ value $>$
<|end_chunk_177|><|start_chunk_178|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?seg=<value>
<|end_chunk_178|><|start_chunk_179|>
## minconf (Minimum Confidence)

The minimum confidence can be set to filter potentially false disparity measurements. All pixels with less confidence than the chosen value are set to invalid in the disparity image.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_179|><|start_chunk_180|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters? ...minconf=<value>
<|end_chunk_180|><|start_chunk_181|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?minconf=<value>
<|end_chunk_181|><|start_chunk_182|>
### Page 53<|end_chunk_182|><|start_chunk_183|>
 maxdeptherr (Maximum Depth Error) 

The maximum depth error is used to filter measurements that are too inaccurate. All pixels with a larger depth error than the chosen value are set to invalid in the disparity image. The maximum depth error is given in meters. The depth error generally grows quadratically with an object's distance from the camera (see Confidence and error images, Section 5.2.3).

Via the REST-API, this parameter can be set as follows.
<|end_chunk_183|><|start_chunk_184|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters/parameters?
...maxdeptherr=<value>
<|end_chunk_184|><|start_chunk_185|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereomatching/parameters?maxdeptherr=<value>
The same parameters are also available over the GenICam interface with slightly different names and partly with different data types (see GigE Vision 2.0/GenICam image interface, Section 7.2).
<|end_chunk_185|><|start_chunk_186|>
### 6.2.2 Status values

This module reports the following status values:
Table 6.5: The rc_stereomatching module's status values

| Name | Description |
| :-- | :-- |
| fps | Actual frame rate of the disparity, error, and confidence images. This value <br> is shown in the Web GUI below the image preview as FPS (Hz). |
| latency | Time in seconds between image acquisition and publishing of disparity <br> image. This value is shown in the Web GUI below the image preview as <br> Latency (s). |
| width | Current width of the disparity, error, and confidence images in pixels. This <br> value is shown in the Web GUI below the image preview as the first <br> number of Resolution (px). |
| height | Current height of the disparity, error, and confidence images in pixels. This <br> value is shown in the Web GUI below the image preview as the second <br> number of Resolution (px). |
| mindepth | Actual minimum working distance in meters. This value is shown in the <br> Web GUI below the image preview as Minimum Distance (m). |
| maxdepth | Actual maximum working distance in meters. This value is shown in the <br> Web GUI below the image preview as Maximum Distance (m). |
| time_matching | Time in seconds for performing stereo matching using SGM on the GPU <br> Time in seconds for postprocessing the matching result on the CPU |
| time_postprocessing | Indicates whether the depth range is reduced due to computation <br> resources |
| reduced_depth_range |  |
<|end_chunk_186|><|start_chunk_187|>
### 6.2.3 Services

The stereo matching module offers the following services.
<|end_chunk_187|><|start_chunk_188|>
### 6.2.3.1 acquisition_trigger

Signals the module to perform stereo matching of the next available images, if the parameter acquisition_mode is set to SingleFrame or SingleFrameOut1.
<|end_chunk_188|><|start_chunk_189|>
## Details
<|end_chunk_189|><|start_chunk_190|>
### Page 54
An error is returned if the acquisition...mode is set to Continuous.
This service can be called as follows.
<|end_chunk_190|><|start_chunk_191|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc...stereomatching/services/acquisition...
...trigger
<|end_chunk_191|><|start_chunk_192|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc...stereomatching/services/acquisition...trigger
<|end_chunk_192|><|start_chunk_193|>
## Request

This service has no arguments.
<|end_chunk_193|><|start_chunk_194|>
## Response

Possible return codes are shown below.
Table 6.6: Possible return codes of the acquisition...trigger service call.

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -8 | Triggering is only possible in SingleFrame acquisition mode |
| 101 | Trigger is ignored, because there is a trigger call pending |
| 102 | Trigger is ignored, because there are no subscribers |

The definition for the response with corresponding datatypes is:

```
{
    "name": "acquisition...trigger",
    "response": {
        "return...code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_194|><|start_chunk_195|>
### 6.2.3.2 reset_defaults

Restores and applies the default values for this module's parameters ("factory reset").
<|end_chunk_195|><|start_chunk_196|>
## Details

This service can be called as follows.
<|end_chunk_196|><|start_chunk_197|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc...stereomatching/services/reset...defaults
<|end_chunk_197|><|start_chunk_198|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc...stereomatching/services/reset...defaults
<|end_chunk_198|><|start_chunk_199|>
## Request

This service has no arguments.
<|end_chunk_199|><|start_chunk_200|>
## Response

The definition for the response with corresponding datatypes is:
<|end_chunk_200|><|start_chunk_201|>
### Page 55
```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_201|><|start_chunk_202|>
 6.3 Navigation modules 

The $r c \_$visard's navigation modules contain:

- Sensor dynamics (rc_dynamics, Section 6.3.1) provides estimates of $r c \_$visard's dynamic state such as its pose, velocity, and acceleration. These states are transmitted as continuous data streams via the $r c \_$dynamics interface. For this purpose, the dynamics module manages and fuses data from the following individual subcomponents:
- Visual odometry (rc_stereovisodo, Section 6.3.2) estimates the motion of the $r c \_$visard device based on the motion of characteristic visual features in the left camera images.
- Stereo INS (rc_stereo_ins, Section 6.3.3) combines visual odometry measurements with readings from the on-board Inertial Measurement Unit (IMU) to provide accurate and high-frequency state estimates in real time.
- SLAM (rc_slam, Section 6.3.4) performs simultaneous localization and mapping for correcting accumulated poses. The rc_visard's covered trajectory is offered via the REST-API interface (Section 7.3).

<|end_chunk_202|><|start_chunk_203|>
### 6.3.1 Sensor dynamics

The dynamics module is a base module which is available on every $r c \_$visard and provides estimates of the sensor state. These include pose, linear velocity, linear acceleration, and rotational rates. The module handles starting and stopping, and streaming of the estimates for individual subcomponents:

- Visual odometry (rc_stereovisodo) estimates the camera's motion from the motion of characteristic image points in the left camera images (Section 6.3.2).
- Stereo INS (rc_stereo_ins) combines visual odometry measurements with readings from an inertial measurement unit (IMU) to provide accurate, high-frequency state estimates in real time (Section 6.3.3).
- SLAM (rc_slam) performs simultaneous localization and mapping (SLAM) for correcting accumulated poses (Section 6.3.4).

Note: Using Stereo matching module (Section 6.2) in parallel to the dynamics module may lead to decreased localization accuracy. See Visual odometry (Section 6.3.2) for how to avoid this.
<|end_chunk_203|><|start_chunk_204|>
### 6.3.1.1 Coordinate frames for state estimation

The world coordinate frame for state estimation is defined as follows: The coordinate frame's z-axis points upward and is aligned with the gravity vector. The $x$-axis is orthogonal to the $z$-axis and points in the $r c \_$visard's viewing direction at the time when the pose estimation starts. The world frame's origin is located at the origin of the $r c \_$visard's IMU coordinate frame at the instant when state estimation is switched on.
<|end_chunk_204|><|start_chunk_205|>
### Page 56
If pose estimation is switched on when the $r c \_v i s a r d$ 's viewing direction parallels the gravity vector (with a tolerance range of 10 degrees), then the world coordinate frame's $y$-axis is aligned either with the IMU's positive or negative $x$-axis. In this orientation, the initial alignment of the world coordinate frame is no longer continuous. Thus, special care has to be taken when pose estimation has to be started at such an orientation.
![img-23.jpeg](img-23.jpeg)

Fig. 6.4: Coordinate frames for state estimation. The IMU coordinate frame is inside the $r c \_v i s a r d$ 's housing. The camera coordinate frame (Section 3.7) is in the focal point of the left camera.

The transformation between the IMU coordinate frame and the camera/sensor frame is also estimated and provided in the real-time dynamics stream over the rc_dynamics interface (see Interfaces, Section 7).

Warning: The stereo INS module self-calibrates the IMU during its initialization. It is therefore required that the $r c \_v i s a r d$ is not moving and sufficient texture is visible during startup of the stereo INS module.
<|end_chunk_205|><|start_chunk_206|>
 6.3.1.2 Available state estimates 

The $r c \_v i s a r d$ provides seven different kinds of timestamped state-estimate data streams via the rc_dynamics interface (see The rc_dynamics interface, Section 7.4):

| Name | Fre- <br> quency | Source | Description |
| :-- | :-- | :-- | :-- |
| pose | 25 Hz | best effort | Pose of camera frame, slightly delayed but most accurate |
| pose_ins | 25 Hz | Stereo <br> INS | Pose of camera frame, slightly delayed but most accurate |
| pose_rt | 200 Hz | best effort | Pose of camera frame |
| pose_rt_ins | 200 Hz | Stereo <br> INS | Pose of camera frame |
| dynamics | 200 Hz | best effort | Pose, velocity and acceleration in IMU frame |
| dynam- <br> ics_ins | 200 Hz | Stereo <br> INS | Pose, velocity and acceleration in IMU frame |
| imu | 200 Hz | Stereo <br> INS | Raw IMU data |
<|end_chunk_206|><|start_chunk_207|>
### Page 57
Best effort here means that if SLAM is running, then it contains the loop-closure corrected estimates and is equivalent to the stream from Stereo INS when SLAM is not running.

Camera-pose streams (pose and pose_ins)

The camera-pose streams called pose and pose_ins are provided at 25 Hz with timestamps that correspond to image timestamps. The former stream is the best-effort estimate, combining SLAM and Stereo INS if the SLAM module is running. If SLAM is not running, then both data streams are equivalent. Pose values are given in world coordinates, and also refer to the rc_visard's camera frame origin (see Coordinate frames for state estimation, Section 6.3.1.1). They are the most accurate estimates, taking all available $r c \_$visard information into consideration. They can be used in modeling applications, where camera images, depth images, or point clouds have to be aligned highly accurately with each other. To ensure the greatest possible accuracy, these pose values are delayed until a corresponding visual odometry measurement is available.

Real-time camera-pose streams (pose_rt and pose_rt_ins)

Two real-time pose streams called pose_rt and pose_rt_ins are provided at the IMU rate of 200 Hz . The former stream is the best-effort estimate, combining SLAM and Stereo INS when the SLAM module is running. If SLAM is not running, then both data streams are equivalent. They consist of the pose estimates of the $r c \_$visard's camera frame origin (see Coordinate frames for state estimation, Section 6.3.1.1) in world coordinates. The values given in these streams correspond to the values in the realtime dynamics streams, but give the pose of the sensor/camera coordinate frame instead of that of the IMU coordinate frame.

Real-time dynamics streams (dynamics and dynamics_ins)

Two real-time dynamics streams called dynamics and dynamics_ins are provided at the IMU rate of 200 Hz . The former stream is the best-effort estimate, combining SLAM and Stereo INS when the SLAM module is running. If SLAM is not running, then both data streams are equivalent. The estimates can be used for real-time control of a robot. Since the values are provided in real time and visual odometry computation requires some processing time, the latest visual odometry estimate may not be included. Therefore, these estimates are in general slightly less accurate than those in the non-real-time camerapose streams (see above), but are the best estimates available at this instant. The provided dynamics streams contain the $r c \_$visard's

- translation $\mathbf{p}=(x, y, z)^{T}$ in $m$,
- rotation $\mathbf{q}=\left(q_{x}, q_{y}, q_{z}, q_{w}\right)$ as unit quaternion,
- linear velocities $\mathbf{v}=\left(v_{x}, v_{y}, v_{z}\right)^{T}$ in $\frac{m}{s}$,
- angular velocities $\omega=\left(\omega_{x}, \omega_{y}, \omega_{z}\right)^{T}$ in $\frac{r o d}{s}$,
- gravity-compensated linear accelerations $\mathbf{a}=\left(a_{x}, a_{y}, a_{z}\right)^{T}$ in $\frac{m}{s^{2}}$, and
- transformation from camera to IMU coordinate frame as pose with frame name and parent frame name.

For each module, the stream also provides the name of the coordinate frame in which the values are given. Translation, rotation, and linear velocities are given in the world frame; angular velocities and accelerations are given in the IMU frame (see Coordinate frames for state estimation, Section 6.3.1.1). All values refer to the IMU frame's origin. That means, for example, that linear velocity is the velocity of the IMU frame's origin in the world frame.

Lastly, the stream contains a possible_jump flag, which is set to true whenever the optional SLAM module (see SLAM, Section 6.3.4) corrects the state estimation after finding a loop closure. The state estimate can jump in this case, which should be considered when the values are used in a control loop. If SLAM is not running, the jump flag can be ignored and will stay false.
<|end_chunk_207|><|start_chunk_208|>
### Page 58
IMU data stream (imu)

The IMU data stream called imu is provided at the IMU rate of 200 Hz . It consists of the acceleration in $\mathrm{x}, \mathrm{y}, \mathrm{z}$ directions plus the angular velocities around these three axis. The values are calibrated but not bias- and gravity-compensated, and are given in the IMU frame. The transformation between IMU and sensor frame is provided in the real-time dynamics stream.
<|end_chunk_208|><|start_chunk_209|>
 6.3.1.3 Status values 

This module reports the following status values:
Table 6.7: The rc_dynamics module's status values

| Name | Description |
| :-- | :-- |
| state | The current state of the rc_dynamics node |
<|end_chunk_209|><|start_chunk_210|>
### 6.3.1.4 Services

The sensor dynamics module offers the following services for starting dynamics/motion estimation. All services return a numerical code of the entered state. The meaning of the returned state codes and names are given in Table 6.8.

Table 6.8: Possible states of the sensor dynamics module

| State name | Description |
| :-- | :-- |
| IDLE | The module is ready, but idle |
| WAITING_FOR_INS | Waiting for stereo INS to start up |
| WAITING_FOR_INS_AND_SLAM | Waiting for stereo INS and SLAM to start up |
| RUNNING | The stereo INS module is running (SLAM is not running) |
| WAITING_FOR_SLAM | Waiting for SLAM to start up (stereo INS is running) |
| RUNNING_WITH_SLAM | Both stereo INS and SLAM are running |
| STOPPING | Transitional state when going to (or through IDLE) |
| FATAL | A fatal error has occurred (either in stereo INS or SLAM) |

The following diagram shows the main states and transitions. Intermediate states and the fatal error state are omitted for conceptual clarity.
![img-24.jpeg](img-24.jpeg)

Fig. 6.5: Simplified state and transition diagram

These services shall respond quickly. Therefore, for services that cause a state transition the value of the returned current_state in general is the first new (intermediate) state that was transitioned to, not the final state. E.g., for the start command the returned current_state will be WAITING_FOR_INS,
<|end_chunk_210|><|start_chunk_211|>
### Page 59
not state RUNNING. If the transition does not take place within 0.1 seconds, the current state is returned. See Table 6.8 for the meaning of the returned state codes.

Note: The state FATAL can only be left by calling stop, which performs a transition to the state IDLE. The services restart and restart_slam internally use stop and will also work as expected. start and start_slam only work if the state is IDLE, and do nothing if the state is FATAL.

Note: The dynamics modules can also be started and stopped on the Dynamics page of the Web GUI.
start

Starts the stereo INS module.
<|end_chunk_211|><|start_chunk_212|>
 Details 

Transitions from state IDLE through WAITING_FOR_INS to RUNNING.
This service can be called as follows.
<|end_chunk_212|><|start_chunk_213|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_dynamics/services/start
<|end_chunk_213|><|start_chunk_214|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_dynamics/services/start
<|end_chunk_214|><|start_chunk_215|>
## Request

This service has no arguments.
<|end_chunk_215|><|start_chunk_216|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "start",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

start_slam

Starts the SLAM and - if not yet started - the stereo INS module.
<|end_chunk_216|><|start_chunk_217|>
## Details

From state IDLE: Transitions through WAITING FOR INS AND SLAM and WAITING FOR SLAM to RUNNING WITH SLAM. From state RUNNING: Transitions through WAITING FOR SLAM to RUNNING_WITH_SLAM.

This service can be called as follows.
<|end_chunk_217|><|start_chunk_218|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_dynamics/services/start_slam
<|end_chunk_218|><|start_chunk_219|>
## API version 1 (deprecated)
<|end_chunk_219|><|start_chunk_220|>
### Page 60
PUT http://<host>/api/v1/nodes/rc_dynamics/services/start_slam
<|end_chunk_220|><|start_chunk_221|>
 Request 

This service has no arguments.
<|end_chunk_221|><|start_chunk_222|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "start_slam",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
stop
```

Stops the stereo INS and - if running - the SLAM modules.
<|end_chunk_222|><|start_chunk_223|>
## Details

The trajectory estimate of the SLAM module will still be available. Transitions from state RUNNING or RUNNING_WITH_SLAM through STOPPING to IDLE.

This service can be called as follows.
<|end_chunk_223|><|start_chunk_224|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_dynamics/services/stop
<|end_chunk_224|><|start_chunk_225|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_dynamics/services/stop
<|end_chunk_225|><|start_chunk_226|>
## Request

This service has no arguments.
<|end_chunk_226|><|start_chunk_227|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "stop",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
stop_slam
```

Stops the SLAM module. Stereo INS will continue to run.
<|end_chunk_227|><|start_chunk_228|>
## Details

The trajectory estimate of the SLAM module will still be available. Transitions from state RUNNING_WITH_SLAM to RUNNING.

This service can be called as follows.
<|end_chunk_228|><|start_chunk_229|>
### Page 61<|end_chunk_229|><|start_chunk_230|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_dynamics/services/stop_slam
<|end_chunk_230|><|start_chunk_231|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_dynamics/services/stop_slam
<|end_chunk_231|><|start_chunk_232|>
## Request

This service has no arguments.
<|end_chunk_232|><|start_chunk_233|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "stop_slam",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

restart

Restarts to stereo INS. Equivalent to successive stop and start.
<|end_chunk_233|><|start_chunk_234|>
## Details

From state RUNNING or RUNNING..WITH...SLAM: Transitions through states STOPPING, IDLE and WAITING...FOR...INS to RUNNING.

This service can be called as follows.
<|end_chunk_234|><|start_chunk_235|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_dynamics/services/restart
<|end_chunk_235|><|start_chunk_236|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_dynamics/services/restart
<|end_chunk_236|><|start_chunk_237|>
## Request

This service has no arguments.
<|end_chunk_237|><|start_chunk_238|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "restart",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

restart_slam

Restarts to SLAM mode. Equivalent to successive stop and start_slam.
<|end_chunk_238|><|start_chunk_239|>
### Page 62<|end_chunk_239|><|start_chunk_240|>
 Details 

From state RUNNING or RUNNING_WITH_SLAM: Transitions through states STOPPING, IDLE, WAITING_FOR_INS_AND_SLAM, WAITING_FOR_SLAM to RUNNING_WITH_SLAM.

This service can be called as follows.
<|end_chunk_240|><|start_chunk_241|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_dynamics/services/restart_slam
<|end_chunk_241|><|start_chunk_242|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_dynamics/services/restart_slam
<|end_chunk_242|><|start_chunk_243|>
## Request

This service has no arguments.
<|end_chunk_243|><|start_chunk_244|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "restart_slam",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

get_cam2imu_transform
returns the transformation from camera to IMU coordinate frame.
<|end_chunk_244|><|start_chunk_245|>
## Details

This is equivalent to the cam2imu_transform in the Dynamics message (Section 7.4.3).
This service can be called as follows.
<|end_chunk_245|><|start_chunk_246|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_dynamics/services/get_cam2imu_transform
<|end_chunk_246|><|start_chunk_247|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_dynamics/services/get_cam2imu_transform
<|end_chunk_247|><|start_chunk_248|>
## Request

This service has no arguments.
<|end_chunk_248|><|start_chunk_249|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_cam2imu_transform",
    "response": {
        "name": "string",
        "parent": "string",
        "pose": {
            "pose": {
            "orientation": {
```
<|end_chunk_249|><|start_chunk_250|>
### Page 63
![img-25.jpeg](img-25.jpeg)
<|end_chunk_250|><|start_chunk_251|>
 6.3.2 Visual odometry 

The visual odometry module is a base module which is available on every rc_visard.
Visual odometry is part of the sensor dynamics module. It is used to estimate the camera's motion from the motion of characteristic image points (so-called image features) in left camera images. Image features are computed from image corners, which are image regions with high intensity gradients. Image features are used to look for matches between subsequent images to find correspondences. Their 3D coordinates are computed by stereo matching (independent from the disparity image). The camera's motion is computed from a set of corresponding 3D points between two images. To increase the robustness of visual odometry, correspondences are not only computed to the previous camera image but to a certain number of previous images, which are called keyframes. The best result is then chosen.
The visual-odometry frame rate is independent of the user setting in the stereo camera module. It is internally limited to 12 Hz but can be lower, depending on the number of features and keyframes. To ensure good pose-estimation quality, the frame rate should not drop significantly under 10 Hz .

Note: Using Stereo matching module in parallel to the dynamics module may lead to a decreased frame rate of the visual odometry. In this case, we recommend to decrease the frame rate of the Camera module (effectively decreasing the frame rate of the depth image computation), to lower the computational load of stereo matching.

The visual odometry module's measurements are not directly accessible on the rc_visard. Instead, they are internally fused with measurements from the integrated inertial measurement unit to increase robustness and frequency and reduce latency. The result of the sensor data fusion is provided in the form of different streams (see Stereo INS, Section 6.3.3).
<|end_chunk_251|><|start_chunk_252|>
### 6.3.2.1 Parameters

The visual odometry software module is called rc_stereovisodo and it is represented by the Dynamics page in the Web GUI (Section 7.1). The user can change the visual odometry parameters there, or use the REST-API (REST-API interface, Section 7.3).
<|end_chunk_252|><|start_chunk_253|>
### Page 64<|end_chunk_253|><|start_chunk_254|>
 Parameter overview 

This module offers the following run-time parameters:
Table 6.9: The rc_stereovisodo module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :-- | :--: | :--: | :--: | :--: | :-- |
| disprange | int32 | 32 | 512 | 256 | Disparity range in pixels |
| ncorner | int32 | 50 | 4000 | 500 | Number of corners |
| nfeature | int32 | 50 | 4000 | 300 | Number of features |
| nkey | int32 | 1 | 4 | 4 | Number of keyframes |
<|end_chunk_254|><|start_chunk_255|>
## Description of run-time parameters

Run-time parameters influence the number of features used to compute visual odometry. More features increase the visual odometry's robustness at the expense of more run time, which can reduce the frame rate. Although the resulting state estimate will always have a high frequency due to fusion with IMU measurements, high visual-odometry frame rates are nevertheless desirable, since these measurements are much more accurate than IMU measurements alone. A visual-odometry rate of at least 10 Hz should thus be aimed for. The visual-odometry frame rate is provided as a status parameter and is shown below the camera image on the Web GUI's Dynamics page.
![img-26.jpeg](img-26.jpeg)

Fig. 6.6: The Web GUI's Dynamics page

The camera image shown on this page depicts image features as small green dots. The bold green dots are the features in the current image for which correspondences could be found in a previous keyframe. Green lines depict the motion of these features relative to the previous keyframe. This visualization should help to find a good set of parameters for visual odometry. The number of correspondences is
<|end_chunk_255|><|start_chunk_256|>
### Page 65
reported as a status parameter and is shown below the camera image on the Web GUI's Dynamics page. For robust visual-odometry measurements, the parameters should be adjusted so that the resulting number of correspondences in the target environment is around at least 50 when the sensor is moving. The correspondence count will be larger when the rc_visard is static, and the number will change when the $r c \_v i s a r d$ moves through the environment. Short failures of the visual odometry are tolerated due to the fusion with IMU measurements. Longer failures should be avoided because they lead to large pose uncertainties and can lead to errors in the state estimation.

Each run-time parameter is represented by a row on the Web GUI's Dynamics page. The name of the row is given in brackets behind the parameter name, and the parameters are listed in the order they appear in the Web GUI:
<|end_chunk_256|><|start_chunk_257|>
 disprange (Disparity Range) 

The disparity range gives the maximum disparity value for each image feature related to the resolution of the high-quality disparity image (half image resolution). The disparity range determines the minimum working distance of the visual odometry. When the disparity range is narrow, only more distant features are considered in the visual-odometry estimation. When choosing a broader disparity range, close features can also be used. Broader disparity ranges increase processing time, which can reduce the visual odometry's frame rate.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_257|><|start_chunk_258|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereovisodo/parameters?disprange=<value>
<|end_chunk_258|><|start_chunk_259|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereovisodo/parameters?disprange=<value>
nkey (Number of Keyframes)

More keyframes can increase the robustness and accuracy of the visual odometry, but they also increase processing time and can decrease the visual-odometry frame rate.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_259|><|start_chunk_260|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereovisodo/parameters?nkey=<value>
<|end_chunk_260|><|start_chunk_261|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereovisodo/parameters?nkey=<value>
<|end_chunk_261|><|start_chunk_262|>
## ncorner (Number of Corners)

This value gives the approximate number of corners that will be detected in the left image. Larger numbers make visual odometry more robust and accurate but can lead to lower frame rates of the visual odometry.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_262|><|start_chunk_263|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereovisodo/parameters?ncorner=<value>
<|end_chunk_263|><|start_chunk_264|>
## API version 1 (deprecated)
<|end_chunk_264|><|start_chunk_265|>
### Page 66
PUT http://<host>/api/v1/nodes/rc_stereovisodo/parameters?ncorner=<value>
<|end_chunk_265|><|start_chunk_266|>
 nfeature (Number of Features) 

This value is the maximum number of features that will be derived from the corners. It is useful to detect more corners and select the best subset as features. Larger numbers make visual odometry more robust and accurate but can lead to lower visual-odometry frame rates. Fewer features might be computed, depending on the scene and movement. The actual number of features is reported below the camera image on the Web GUI's Dynamics page.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_266|><|start_chunk_267|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereovisodo/parameters?nfeature=<value>
<|end_chunk_267|><|start_chunk_268|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereovisodo/parameters?nfeature=<value>

Note: Increasing the number of keyframes, corners, or features will also increase robustness but will require more computation time and may reduce the frame rate, depending on other modules active on the rc_visard. The visual-odometry frame rate should be at least 10 Hz .
<|end_chunk_268|><|start_chunk_269|>
### 6.3.2.2 Status values

This module reports the following status values:

Table 6.10: The rc_stereovisodo module's status values

| Name | Description |
| :-- | :-- |
| corner | Number of detected corners. This value is shown as Corners below the image <br> preview in the Web GUI. |
| correspondences | Number of correspondences. This value is shown as Correspondences below <br> the image preview in the Web GUI. |
| feature | Number of features. This value is shown as Features below the image preview <br> in the Web GUI. |
| fps | Frame rate of the visual odometry in Hertz. This value is shown below the <br> image preview as Visual Odometry FPS (Hz) in the Web GUI. |
| time_frame | Processing time in seconds to compute corners and features for each frame <br> Processing time in seconds to compute the motion |
| time_vo |  |
<|end_chunk_269|><|start_chunk_270|>
### 6.3.2.3 Services

This module offers no start or stop services itself, because the dynamics module (Section 6.3.1) starts and stops it.

The visual odometry module offers the following services for persisting and restoring parameter settings.
reset_defaults

Restores and applies the default values for this module's parameters ("factory reset").
<|end_chunk_270|><|start_chunk_271|>
## Details
<|end_chunk_271|><|start_chunk_272|>
### Page 67
This service can be called as follows.
<|end_chunk_272|><|start_chunk_273|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereovisodo/services/reset_defaults
<|end_chunk_273|><|start_chunk_274|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_stereovisodo/services/reset_defaults
<|end_chunk_274|><|start_chunk_275|>
## Request

This service has no arguments.
<|end_chunk_275|><|start_chunk_276|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_276|><|start_chunk_277|>
### 6.3.3 Stereo INS

The stereo-vision-aided Inertial Navigation System (INS) module is a base module which is available on every $r c \_$visard and is part of the sensor dynamics module. It combines visual-odometry measurements with inertial measurement unit (IMU) data and provides robust, low latency, real-time state estimates at a high rate. The IMU consists of three accelerometers and three gyroscopes, which measure accelerations and turn rates in all three dimensions. By fusing IMU and visual-odometry measurements, the state estimate has the same frequency as the IMU $(200 \mathrm{~Hz})$ and is very robust even under challenging lighting conditions and for fast motions.

Note: To achieve high-quality pose estimates, it must be ensured that sufficient texture is visible during runtime of the stereo INS module. In case no texture is visible for a longer period of time, the stereo INS module will stop instead of providing highly erroneous data.
<|end_chunk_277|><|start_chunk_278|>
### 6.3.3.1 Self-Calibration

During startup of the stereo INS module, it will self-calibrate the IMU using the visual-odometry measurements. For the self-calibration to succeed, it is required that

- the $r c \_v i s a r d$ is not moving and
- sufficient texture is visible
during startup of the stereo INS module. Failure to meet these requirements will most likely result in a constant drift of the pose estimates.

<|end_chunk_278|><|start_chunk_279|>
### 6.3.3.2 Parameters

The stereo INS module's node name is rc_stereo_ins.
This module has no run-time parameters.
<|end_chunk_279|><|start_chunk_280|>
### Page 68<|end_chunk_280|><|start_chunk_281|>
 6.3.3.3 Status values 

This module reports the following status values:

Table 6.11: The rc_stereo_ins module's status values

| Name | Description |
| :-- | :-- |
| freq | Frequency of the stereo INS process in Hertz |
| state | String representing the internal state |
<|end_chunk_281|><|start_chunk_282|>
### 6.3.4 SLAM

The SLAM module is an optional on-board module of the rc_visard and requires a separate SLAM license (Section 8.7) to be purchased. If a SLAM license is stored on the rc_visard, then the SLAM module is shown as Available on the Web GUI's License section of the System page.
The SLAM module is part of the sensor dynamics module. It provides additional accuracy for the pose estimate of the stereo INS. When the rc_visard moves through the world, the pose estimate slowly accumulates errors over time. The SLAM module can correct these pose errors by recognizing previously visited places.
The acronym SLAM stands for Simultaneous Localization and Mapping. The SLAM module creates a map consisting of the image features as used in the visual odometry module. The map is later used to correct accumulated pose errors. This is most apparent in applications where, e.g., a robot returns to a previously visited place after covering a large distance (this is called a loop closure). In this case, the robot can re-detect image features that are already stored in its map and can use this information to correct the drift in the pose estimate that accumulated since the last visit.
When closing a loop, not only the current pose, but also the past pose estimates (the trajectory of the rc_visard), are corrected. Continuous trajectory correction leads to a more accurate map. On the other hand, the accuracy of the full trajectory is important when it is used to build an integrated world model, e.g., by projecting the 3D point clouds obtained (see Computing depth images and point clouds, Section 5.2.2) into a common coordinate frame. The full trajectory can be requested from the SLAM module for this purpose.
<|end_chunk_282|><|start_chunk_283|>
### 6.3.4.1 Usage

The SLAM module can be activated at any time, either via the rc_dynamics interface (see the documentation of the respective Services, Section 6.3.1.4) or from the Dynamics page of the Web GUI (Section 7.1).

The pose estimate of the SLAM module will be initialized with the current estimate of the stereo INS and thus the origin will be where the stereo INS was started.
Since the SLAM module builds on the motion estimates of the stereo INS module, the latter will automatically be started up if it is not yet running when SLAM is started.
When the SLAM module is running, the corrected pose estimates will be available via the datastreams pose, pose_rt, and dynamics of the rc_dynamics module.
The full trajectory is available through the service get_trajectory, see Services (Section 6.3.4.5) below for details.

To store the feature map on the rc_visard, the SLAM module provides the service save_map, which can be used only during runtime (state "RUNNING") or after stopping (state "HALTED").
A stored map can be loaded before startup using the service load_map, which is only applicable in state "IDLE" (use the reset service to go back to "IDLE" when SLAM is in state "HALTED"). Note that mistaken localization at (visually) similar places may happen more easily when initially localizing in a loaded map than when localizing during continuous operation. Choosing a starting point with a unique visual appearance avoids this problem. The SLAM module will therefore assume that the rc_visard is
<|end_chunk_283|><|start_chunk_284|>
### Page 69
started in the rough vicinity (a few meters) of the origin of the map. The origin of the map is where the Stereo-INS module was started when the map was recorded.
<|end_chunk_284|><|start_chunk_285|>
 6.3.4.2 Memory limitations 

In contrast to the other software modules running on the rc_visard, the SLAM module needs to accumulate data over time, e.g., motion measurements and image features. Further, the optimization of the trajectory requires substantial amounts of memory, particularly when closing large loops. Therefore the memory requirements of the SLAM module increase over time.

Given the memory limitations of the hardware, the SLAM module needs to reduce its own memory footprint when running continuously. When the available memory runs low, the SLAM module will fix parts of the trajectory, i.e. no further optimization will be done on these parts. A minimum of 10 minutes of the trajectory will be kept unfixed at all times.

When the available memory runs low despite the above measures, two options are available. The first option is that the SLAM module automatically goes to the HALTED state, where it stops processing, but the trajectory (up to the stopping time) is still available. This is the default behavior.

The second option is to keep running until the memory is exhausted. In that case, the SLAM module will be restarted. If the autorecovery parameter is set to true, the SLAM module will recover its previous position and resume mapping. Otherwise it will go to FATAL state, requiring to be restarted via the rc_dynamics interface (see Services, Section 6.3.1.4).

The operation time until the memory limit is reached is strongly dependent on the trajectory of the sensor.

Warning: Because of the memory limitations, it is not recommended to run SLAM at the same time as Stereo matching module in full resolution, because the memory available to SLAM will be greatly reduced. In the worst case, a long running SLAM process may even be forcefully reset, when full-resolution stereo matching is turned on.
<|end_chunk_285|><|start_chunk_286|>
### 6.3.4.3 Parameters

The SLAM module is called rc_slam in the REST-API. The user can change the SLAM parameters using the REST-API interface (Section 7.3).
<|end_chunk_286|><|start_chunk_287|>
## Parameter overview

This module offers the following run-time parameters:
Table 6.12: The rc_slam module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :-- | :--: | :--: | :--: | :--: | :-- |
| autorecovery | bool | false | true | true | In case of fatal errors recover cor- <br> rected position and restart mapping |
| halt_on_low_memory | bool | false | true | true | When the memory runs low, go to <br> halted state |
<|end_chunk_287|><|start_chunk_288|>
### 6.3.4.4 Status values

This module reports the following status values:
<|end_chunk_288|><|start_chunk_289|>
### Page 70
Table 6.13: The rc_slam module's status values

| Name | Description |
| :-- | :-- |
| map_frames | Number of frames that constitute the map |
| state | The current state of the rc_slam node |
| trajectory_poses | Number of poses in the estimated trajectory |

The reported state can take one of the following values.
Table 6.14: Possible states of the rc_slam module

| State name | Description |
| :-- | :-- |
| IDLE | The module is ready, but idle. No trajectory data is available. |
| WAITING_FOR_DATA | The module was started but is waiting for data from stereo INS or VO. |
| RUNNING | The module is running. |
| HALTED | The module is stopped. The trajectory data is still available. No new <br> information is processed. |
| RESETTING | The module is being stopped and the internal data is being cleared. |
| RESTARTING | The module is being restarted. |
| FATAL | A fatal error has occurred. |
<|end_chunk_289|><|start_chunk_290|>
 6.3.4.5 Services 

Note: Activation and deactivation of the SLAM module is done via the service interface of rc_dynamics (see Services, Section 6.3.1.4).

Each service response (except for the reset service) contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information.

The SLAM module offers the following services.
get_trajectory
returns the trajectory.
<|end_chunk_290|><|start_chunk_291|>
## Details

This service can be called as follows.
<|end_chunk_291|><|start_chunk_292|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_slam/services/get_trajectory
<|end_chunk_292|><|start_chunk_293|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_slam/services/get_trajectory
<|end_chunk_293|><|start_chunk_294|>
## Request

The service arguments allow to select a subsection of the trajectory by defining a start_time and an end_time. Both are optional, i.e., they could be left empty or filled with zero values, which results in the subsection to include the trajectory from the very beginning, or to the very end, respectively, or both. If not empty or zero, they can be defined either as absolute timestamps or to be relative to the trajectory (start_time_relative and end_time_relative flags). If defined to be relative, the values' signs indicate to which point in time they relate to: Positive values define an offset to the start time of the trajectory; negative values are
<|end_chunk_294|><|start_chunk_295|>
### Page 71
interpreted as an offset from the end time of the trajectory. The below diagram illustrates three examples for the relative parameterization.
![img-27.jpeg](img-27.jpeg)

Fig. 6.7: Examples for combinations of relative start and end times for the get_trajectory service. All combinations shown select the same subset of the trajectory.

Note: A relative start_time of zero will select everything from the start of the trajectory, whereas a relative end_time of zero will select everything to the end of the trajectory. Absolute zero values effectively do the same, so one can set all values zero to get the full trajectory.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "end_time": {
            "nsec": "int32",
            "sec": "int32"
        },
        "end_time_relative": "bool",
        "start_time": {
            "nsec": "int32",
            "sec": "int32"
        },
        "start_time_relative": "bool"
    }
}
```

<|end_chunk_295|><|start_chunk_296|>
 Response 

The field producer indicates where the trajectory data comes from and is always slam.
The field return_code holds possible warnings or error codes and messages. The following table contains a list of possible return_code values:
<|end_chunk_296|><|start_chunk_297|>
### Page 72
| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided (e.g., an invalid time range) |
| 101 | Trajectory is empty, because there is no data in the given time range |
| 102 | Trajectory is empty, because there is no data at all (e.g., when SLAM is IDLE) |

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_trajectory",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        },
        "trajectory": {
            "name": "string",
            "parent": "string",
            "poses": [
                {
                    "pose": {
                        "orientation": {
                        "w": "float64",
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
                    },
                        "position": {
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
                    }
                    },
                        "timestamp": {
                        "nsec": "int32",
                        "sec": "int32"
                    }
                    }
            ],
            "producer": "string",
            "timestamp": {
                        "nsec": "int32",
                        "sec": "int32"
            }
        }
    }
}
save_map
```

stores the current state as a map to persistent memory. The map consists of a set of fixed map frames. It does not contain the full trajectory that has been covered.
<|end_chunk_297|><|start_chunk_298|>
 Details 

This service can be called as follows.
<|end_chunk_298|><|start_chunk_299|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_slam/services/save_map
<|end_chunk_299|><|start_chunk_300|>
### Page 73<|end_chunk_300|><|start_chunk_301|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_slam/services/save_map
Note: Only abstract feature positions and descriptions are stored in the map. No actual footage of the cameras is stored with the map, nor is it possible to reconstruct images or image parts from the stored information.

Warning: The map is lost on software updates or rollbacks
<|end_chunk_301|><|start_chunk_302|>
## Request

This service has no arguments.
<|end_chunk_302|><|start_chunk_303|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "save_map",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

load_map
loads a previously saved map.
<|end_chunk_303|><|start_chunk_304|>
## Details

This is only applicable when the SLAM module is IDLE. It is not possible to load a map into a running system. A loaded map can be cleared with the reset service call.

This service can be called as follows.
<|end_chunk_304|><|start_chunk_305|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_slam/services/load_map
<|end_chunk_305|><|start_chunk_306|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_slam/services/load_map
<|end_chunk_306|><|start_chunk_307|>
## Request

This service has no arguments.
<|end_chunk_307|><|start_chunk_308|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "load_map",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
```

(continues on next page)
<|end_chunk_308|><|start_chunk_309|>
### Page 74
remove_map
removes the stored map from the persistent memory.
<|end_chunk_309|><|start_chunk_310|>
 Details 

This service can be called as follows.
<|end_chunk_310|><|start_chunk_311|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_slam/services/remove_map
<|end_chunk_311|><|start_chunk_312|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_slam/services/remove_map
<|end_chunk_312|><|start_chunk_313|>
## Request

This service has no arguments.
<|end_chunk_313|><|start_chunk_314|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "remove_map",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

reset
clears the internal state of the SLAM module.
<|end_chunk_314|><|start_chunk_315|>
## Details

This service is to be used after stopping the SLAM module using the rc_dynamics interface (see the respective Services, Section 6.3.1.4). The SLAM module maintains the estimate of the full trajectory even when stopped. This service clears this estimate and frees the respective memory. The returned status is RESETTING.

This service can be called as follows.
<|end_chunk_315|><|start_chunk_316|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_slam/services/reset
<|end_chunk_316|><|start_chunk_317|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_slam/services/reset
<|end_chunk_317|><|start_chunk_318|>
### Page 75<|end_chunk_318|><|start_chunk_319|>
 Request 

This service has no arguments.
<|end_chunk_319|><|start_chunk_320|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

<|end_chunk_320|><|start_chunk_321|>
### 6.4 Detection \& Measure modules

The $r c \_v i s a r d$ offers software modules for different detection and measuring applications:

- Measure (rc_measure, Section 6.4.1) provides measure functionalities, such as depth measurements.
- LoadCarrier (rc_load_carrier, Section 6.4.2) allows detecting load carriers and their filling levels.
- TagDetect (rc_april_tag_detect and rc_qr_code_detect, Section 6.4.3) allows the detection of AprilTags and QR codes, as well as the estimation of their poses.
- ItemPick (rc_itempick, Section 6.4.4) provides an out-of-the-box perception solution for robotic pick-and-place applications of unknown objects.
- BoxPick (rc_boxpick, Section 6.4.5) provides an out-of-the-box perception solution for robotic pick-and-place applications of boxes or textured boxes.
- SilhouetteMatch (rc_silhouettematch, Section 6.4.6) provides an object detection solution for objects placed on a plane or stacked planar objects.

These modules are optional and can be activated by purchasing a separate license (Section 8.7).
<|end_chunk_321|><|start_chunk_322|>
### 6.4.1 Measure
<|end_chunk_322|><|start_chunk_323|>
### 6.4.1.1 Introduction

The Measure module allows measuring of depth values in a specific region of interest.
The Measure module is an on-board module of the $r c \_v i s a r d$.
<|end_chunk_323|><|start_chunk_324|>
### 6.4.1.2 Measuring Depth

The Measure module provides functionality to measure depth values in the current scene in a 2D region of interest. Optionally, the region of interest can be subdivided into up to 100 cells, for which separate depth measurements are returned in addition to the overall depth measurements of the whole region.
A depth measurement consist of the average depth mean. $z$, the minimum depth min. $z$ and the maximum depth max. $z$, each containing 3D coordinates. The coordinates of the min. $z$ and max. $z$ measurements correspond to the point in the cell or overall region with the minimum and maximum distance from the camera, respectively. The $x$ and $y$ coordinates of the mean. $z$ measurements define a point in the center of the cell or the overall region and the $z$ coordinate is determined by the average of all depth value measurements (distances from the camera) in this region. Additionally, a coverage value is returned for each cell and the overall region, which is a number between 0 and 1 that reflects the fraction of valid
<|end_chunk_324|><|start_chunk_325|>
### Page 76
depth values inside the respective region. A coverage value of 0 means that the cell is invalid and no depth value could be computed.

When the external pose_frame is used for the depth measurements, all 3D coordinates are computed as described above, but then transformed to the external frame. That means, the depth is always measured along the line of sight of the camera, independently of the chosen pose frame.
<|end_chunk_325|><|start_chunk_326|>
 6.4.1.3 Interaction with other modules 

Internally, the Measure module depends on, and interacts with other on-board modules as listed below.
Note: All changes and configuration updates to these modules will affect the performance of the Measure module.
<|end_chunk_326|><|start_chunk_327|>
## Depth Images

The Measure module internally makes use of the following data:

- Disparity images from the Stereo matching module (rc_stereomatching, Section 6.2)

<|end_chunk_327|><|start_chunk_328|>
## Hand-eye calibration

In case the camera has been calibrated to a robot, the Measure module can automatically provide points in the robot coordinate frame. For the Measure node's Services (Section 6.4.1.6), the frame of the output points can be controlled with the pose_frame argument.

Two different pose_frame values can be chosen:

1. Camera frame (camera). All points provided by the module are in the camera frame, and no prior knowledge about the pose of the camera in the environment is required. It is the user's responsibility to update the configured points if the camera frame moves (e.g. with a robot-mounted camera).
2. External frame (external). All points provided by the module are in the external frame, configured by the user during the hand-eye calibration process. The module relies on the on-board Hand-eye calibration module (Section 6.5.1) to retrieve the sensor mounting (static or robot mounted) and the hand-eye transformation. If the mounting is static, no further information is needed. If the sensor is robot-mounted, the robot. pose is required to transform poses to and from the external frame.

Note: If no hand-eye calibration is available, all pose_frame values should be set to camera.

All pose_frame values that are not camera or external are rejected.
<|end_chunk_328|><|start_chunk_329|>
### 6.4.1.4 Parameters

The Measure module is called rc_measure in the REST-API and is represented in the Web GUI (Section 7.1) under Modules $\rightarrow$ Measure.
<|end_chunk_329|><|start_chunk_330|>
## Parameter overview

This module has no run-time parameters.
<|end_chunk_330|><|start_chunk_331|>
### Page 77<|end_chunk_331|><|start_chunk_332|>
 6.4.1.5 Status values 

The Measure module reports the following status values:

Table 6.15: The rc_measure module's status values

| Name | Description |
| :-- | :-- |
| data_acquisition_time | Time in seconds required to acquire depth image |
| last_timestamp_processed | The timestamp of the last processed depth image |
| processing_time | Processing time of the last measurement in seconds |
<|end_chunk_332|><|start_chunk_333|>
### 6.4.1.6 Services

The user can explore and call the Measure module's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1) on the Measure page under Modules.

The Measure module offers the following services.
measure_depth

Computes the mean, minimum and maximum depth in a given region of interest, which can optionally be subdivided into cells.
<|end_chunk_333|><|start_chunk_334|>
## Details

This service can be called as follows.
<|end_chunk_334|><|start_chunk_335|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_measure/services/measure_depth
<|end_chunk_335|><|start_chunk_336|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_measure/services/measure_depth
<|end_chunk_336|><|start_chunk_337|>
## Request

Required arguments:
pose_frame: see Hand-eye calibration (Section 6.4.1.3).
Optional arguments:
region_of_interest_2d_id is the ID of the 2D region of interest (see RoiDB, Section 6.6.2) that will be used for the depth measurements.
region_of_interest_2d is an alternative on-the-fly definition of the region of interest for the depth measurements. This region of interest will be ignored if a region_of_interest_2d_id is given. The region of interest is always defined on the camera image with full resolution, where offset_x and offset_y are the pixel coordinates of the upper left corner of the rectangular region of interest, and width and height are the width and height of it in pixels. Default is a region of interest covering the whole image.
cell_count is the number of cells in $x$ and $y$ direction into which the region of interest is divided. If not given, a cell count of 0,0 is assumed and only the overall values will be computed. The total cell count is computed as product of the $x$ and $y$ values must not exceed 100.
data_acquisition_mode: if set to CAPTURE_NEW (default), a new image dataset will be used for the measurement. If set to USE_LAST, the previous dataset will be used for the measurement.
<|end_chunk_337|><|start_chunk_338|>
### Page 78
Potentially required arguments:
robot...pose: see Hand-eye calibration (Section 6.4.1.3).
The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "cell_count": {
            "x": "uint32",
            "y": "uint32"
        },
        "data_acquisition_mode": "string",
        "pose_frame": "string",
        "region_of_interest_2d": {
            "height": "uint32",
            "offset_x": "uint32",
            "offset_y": "uint32",
            "width": "uint32"
        },
        "region_of_interest_2d_id": "string",
        "robot_pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        }
    }
}
```

<|end_chunk_338|><|start_chunk_339|>
 Response 

cells contains the depth measurements of all requested cells. The cells are always ordered from left to right and top to bottom in image coordinates.
overal1 contains the depth measurements of the full region of interest.
coverage contains the valid pixel ratio as described in Measuring Depth (Section 6.4.1.2).
mean...z, min...z and max...z contains the measurement coordinates as described in Measuring Depth (Section 6.4.1.2).
region...of...interest... 2 d returns the definition of the requested region of interest for the depth measurement.
pose...frame contains the pose frame of the depth measurement coordinates.
The definition for the response with corresponding datatypes is:

```
{
    "name": "measure_depth",
    "response": {
        "cell_count": {
            "x": "uint32",
            "y": "uint32"
        },
        "cells": [
            {
```
<|end_chunk_339|><|start_chunk_340|>
### Page 79
![img-28.jpeg](img-28.jpeg)
<|end_chunk_340|><|start_chunk_341|>
 6.4.1.7 Return codes 

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all
<|end_chunk_341|><|start_chunk_342|>
### Page 80
messages are appended in the return_code message.
The following table contains a list of common codes:
Table 6.16: Return codes of the Measure module's services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
<|end_chunk_342|><|start_chunk_343|>
 6.4.2 LoadCarrier 
<|end_chunk_343|><|start_chunk_344|>
### 6.4.2.1 Introduction

The LoadCarrier module allows the detection of load carriers, which is usually the first step when objects or grasp points inside a bin should be found. The models of the load carriers to be detected have to be defined in the LoadCarrierDB (Section 6.6.1) module.

The LoadCarrier module is an optional on-board module of the $r c \_v i s a r d$ and is licensed with any of the modules ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5) or SilhouetteMatch (Section 6.4.6). Otherwise it requires a separate LoadCarrier license (Section 8.7) to be purchased.
<|end_chunk_344|><|start_chunk_345|>
### 6.4.2.2 Detection of load carriers

The load carrier detection algorithm detects load carriers that match a specific load carrier model, which must be defined in the LoadCarrierDB (Section 6.6.1) module. The load carrier model is referenced by its ID, which is passed to the load carrier detection. The detection of a load carrier is based on the detection of its rectangular rim. For this, it uses lines detected in the left camera image and the depth values of the load carrier rim. Thus, the rim should form a contrast to the background and the disparity image must be dense on the rim.

If multiple load carriers of the specified load carrier ID are visible in the scene, all of them will be detected and returned by the load carrier detection.

By default, when assume_gravity_aligned is true and gravity measurements are available, the algorithm searches for load carriers whose rim planes are perpendicular to the measured gravity vector. To detect tilted load carriers, assume_gravity_aligned must be set to false or the load carrier's approximate orientation must be specified as pose and the pose_type should be set to ORIENTATION_PRIOR.

Load carriers can be detected at a distance of up to 3 meters from the camera.
When a 3D region of interest (see RoiDB, Section 6.6.2) is used to limit the volume in which load carriers should be detected, only the load carriers' rims must be fully included in the region of interest.

The detection algorithm returns the poses of the load carriers' origins (see Load carrier definition, Section 6.6.1.2) in the desired pose frame.

The detection functionality also determines if the detected load carriers are overfilled, which means, that objects protrude from the plane defined by the load carrier's outer part of the rim.
<|end_chunk_345|><|start_chunk_346|>
### Page 81
![img-29.jpeg](img-29.jpeg)

Fig. 6.8: Load carrier models and reference frames
<|end_chunk_346|><|start_chunk_347|>
 6.4.2.3 Detection of filling level 

The LoadCarrier module offers the detect_filling_level service to compute the filling level of all detected load carriers.

The load carriers are subdivided into a configurable number of cells in a 2D grid. The maximum number of cells is $10 \times 10$. For each cell, the following values are reported:

- level_in_percent: minimum, maximum and mean cell filling level in percent from the load carrier floor. These values can be larger than $100 \%$ if the cell is overfilled.
- level_free_in_meters: minimum, maximum and mean cell free level in meters from the load carrier rim. These values can be negative if the cell is overfilled.
- cell_size: dimensions of the 2D cell in meters.
- cell_position: position of the cell center in meters (either in camera or external frame, see Hand-eye calibration, Section 6.4.2.4). The z-coordinate is on the level of the load carrier rim.
- coverage: represents the proportion of valid pixels in this cell. It varies between 0 and 1 with steps of 0.1. A low coverage indicates that the cell contains several missing data (i.e. only a few points were actually measured in this cell).

These values are also calculated for the whole load carrier itself. If no cell subdivision is specified, only the overall filling level is computed.
![img-30.jpeg](img-30.jpeg)

Fig. 6.9: Visualizations of the load carrier filling level: overall filling level without grid (left), $4 \times 3$ grid (center), $8 \times 8$ grid (right). The load carrier content is shown in a green gradient from white (on the load carrier floor) to dark green. The overfilled regions are visualized in red. Numbers indicate cell IDs.
<|end_chunk_347|><|start_chunk_348|>
### Page 82<|end_chunk_348|><|start_chunk_349|>
 6.4.2.4 Interaction with other modules 

Internally, the LoadCarrier module depends on, and interacts with other on-board modules as listed below.

Note: All changes and configuration updates to these modules will affect the performance of the LoadCarrier module.
<|end_chunk_349|><|start_chunk_350|>
## Camera and depth data

The LoadCarrier module makes internally use of the following data:

- Rectified images from the Camera module (rc_camera, Section 6.1);
- Disparity, error, and confidence images from the Stereo matching module (rc_stereomatching, Section 6.2)

All processed images are guaranteed to be captured after the module trigger time.
<|end_chunk_350|><|start_chunk_351|>
## IO and Projector Control

In case the rc_visard is used in conjunction with an external random dot projector and the IO and Projector Control module (rc_iocontrol, Section 6.5.4), it is recommended to connect the projector to GPIO Out 1 and set the stereo-camera module's acquisition mode to SingleFrameOut1 (see Stereo matching parameters, Section 6.2.1), so that on each image acquisition trigger an image with and without projector pattern is acquired.

Alternatively, the output mode for the GPIO output in use should be set to ExposureAlternateActive (see Description of run-time parameters, Section 6.5.4.1).

In either case, the Auto Exposure Mode exp_auto_mode should be set to AdaptiveOut1 to optimize the exposure of both images.

No additional changes are required to use the LoadCarrier module in combination with a random dot projector.
<|end_chunk_351|><|start_chunk_352|>
## Hand-eye calibration

In case the camera has been calibrated to a robot, the LoadCarrier module can automatically provide poses in the robot coordinate frame. For the LoadCarrier node's Services (Section 6.4.2.7), the frame of the output poses can be controlled with the pose_frame argument.

Two different pose_frame values can be chosen:

1. Camera frame (camera). All poses provided by the module are in the camera frame, and no prior knowledge about the pose of the camera in the environment is required. This means that the configured load carriers move with the camera. It is the user's responsibility to update the configured poses if the camera frame moves (e.g. with a robot-mounted camera).
2. External frame (external). All poses provided by the module are in the external frame, configured by the user during the hand-eye calibration process. The module relies on the on-board Hand-eye calibration module (Section 6.5.1) to retrieve the sensor mounting (static or robot mounted) and the hand-eye transformation. If the mounting is static, no further information is needed. If the sensor is robot-mounted, the robot_pose is required to transform poses to and from the external frame.

Note: If no hand-eye calibration is available, all pose_frame values should be set to camera.

All pose_frame values that are not camera or external are rejected.
<|end_chunk_352|><|start_chunk_353|>
### Page 83<|end_chunk_353|><|start_chunk_354|>
 6.4.2.5 Parameters 

The LoadCarrier module is called rc_load_carrier in the REST-API and is represented in the Web GUI (Section 7.1) under Modules $\rightarrow$ LoadCarrier. The user can explore and configure the LoadCarrier module's run-time parameters, e.g. for development and testing, using the Web GUI or the REST-API interface (Section 7.3).
<|end_chunk_354|><|start_chunk_355|>
## Parameter overview

This module offers the following run-time parameters:
Table 6.17: The rc_load_carrier module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :-- | :--: | :--: | :--: | :--: | :-- |
| assume_gravity_aligned | bool | false | true | true | When true, only gravity-aligned load <br> carriers are detected, if gravity mea- <br> surement is available. |
| crop_distance | float64 | 0.0 | 0.05 | 0.005 | Safety margin in meters by which <br> the load carrier inner dimensions <br> are reduced to define the region of <br> interest for detection |
| min_plausibility | float64 | 0.0 | 0.99 | 0.8 | Indicates how much of the plane <br> surrounding the load carrier rim <br> must be free to count as valid de- <br> tection |
| model_tolerance | float64 | 0.003 | 0.025 | 0.008 | Indicates how much the estimated <br> load carrier dimensions are allowed <br> to differ from the load carrier model <br> dimensions in meters |
<|end_chunk_355|><|start_chunk_356|>
## Description of run-time parameters

Each run-time parameter is represented by a row on the LoadCarrier Settings section of the Web GUI's LoadCarrier page under Modules. The name in the Web GUI is given in brackets behind the parameter name and the parameters are listed in the order they appear in the Web GUI. The parameters are prefixed with load_carrier_ when they are used outside the rc_load_carrier module from another detection module using the REST-API interface (Section 7.3).
assume_gravity_aligned (Assume Gravity Aligned)

If this parameter is set to true, then only load carriers without tilt will be detected. This can speed up the detection. If this parameter is set to false, tilted load carriers will also be detected.

This parameter is ignored for load carriers with an orientation prior.
model_tolerance (Model Tolerance)
indicates how much the estimated load carrier dimensions are allowed to differ from the load carrier model dimensions in meters.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_356|><|start_chunk_357|>
## API version 2
<|end_chunk_357|><|start_chunk_358|>
### Page 84
PUT http://<host>/api/v2/pipelines/0/nodes/rc_load_carrier/parameters?model_tolerance= ...<value>
<|end_chunk_358|><|start_chunk_359|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_load_carrier/parameters?model_tolerance=<value>
crop_distance (Crop Distance)
sets the safety margin in meters by which the load carrier's inner dimensions are reduced to define the region of interest for detection (ref. Fig. 6.41).

Via the REST-API, this parameter can be set as follows.
<|end_chunk_359|><|start_chunk_360|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_load_carrier/parameters?crop_distance= ...<value>
<|end_chunk_360|><|start_chunk_361|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_load_carrier/parameters?crop_distance=<value>
min_plausibility (Minimum Plausibility):
The minimum plausibility defines how much of the plane around the load carrier rim must at least be free to count as valid detection. Increase the minimal plausibility to reject false positive detections and decrease the value in case a clearly visible load carrier cannot be detected.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_361|><|start_chunk_362|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_load_carrier/parameters?min_plausibility= ...<value>
<|end_chunk_362|><|start_chunk_363|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_load_carrier/parameters?min_plausibility=<value>
<|end_chunk_363|><|start_chunk_364|>
### 6.4.2.6 Status values

The LoadCarrier module reports the following status values:
Table 6.18: The rc_load_carrier module's status values

| Name | Description |
| :-- | :-- |
| data_acquisition_time | Time in seconds required to acquire image pair |
| last_timestamp_processed | The timestamp of the last processed image pair |
| load_carrier_detection_time | Processing time of the last detection in seconds |
<|end_chunk_364|><|start_chunk_365|>
### 6.4.2.7 Services

The user can explore and call the LoadCarrier module's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1) on the LoadCarrier page under Modules.
<|end_chunk_365|><|start_chunk_366|>
### Page 85
The LoadCarrier module offers the following services.
detect_load_carriers

Triggers a load carrier detection as described in Detection of load carriers (Section 6.4.2.2).
<|end_chunk_366|><|start_chunk_367|>
 Details 

This service can be called as follows.
<|end_chunk_367|><|start_chunk_368|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_load_carrier/services/detect_load_ carriers
<|end_chunk_368|><|start_chunk_369|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_load_carrier/services/detect_load_carriers
<|end_chunk_369|><|start_chunk_370|>
## Request

Required arguments:
pose_frame: see Hand-eye calibration (Section 6.4.2.4).
load_carrier_ids: IDs of the load carriers which should be detected. Currently only one ID can be specified.

Potentially required arguments:
robot_pose: see Hand-eye calibration (Section 6.4.2.4).
Optional arguments:
region_of_interest_id: ID of the 3D region of interest where to search for the load carriers.
region_of_interest_2d_id: ID of the 2D region of interest where to search for the load carriers.

Note: Only one type of region of interest can be set.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
    "load_carrier_ids": [
        "string"
    },
    "pose_frame": "string",
    "region_of_interest_2d_id": "string",
    "region_of_interest_id": "string",
    "robot_pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
```
<|end_chunk_370|><|start_chunk_371|>
### Page 86<|end_chunk_371|><|start_chunk_372|>
 Response 

load_carriers: list of detected load carriers.
timestamp: timestamp of the image set the detection ran on.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "detect_load_carriers",
    "response": {
        "load_carriers": [
            {
            "height_open_side": "float64",
            "id": "string",
            "inner_dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "outer_dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "overfilled": "bool",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    }
            },
            "pose_frame": "string",
            "rim_ledge": {
                    "x": "float64",
                    "y": "float64"
            },
            "rim_step_height": "float64",
            "rim_thickness": {
                    "x": "float64",
                    "y": "float64"
            },
            "type": "string"
        }
    ],
    "return_code": {
        "message": "string",
        "value": "int16"
    },
```
<|end_chunk_372|><|start_chunk_373|>
### Page 87<|end_chunk_373|><|start_chunk_374|>
 (continued from previous page) 

```
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    }
    }
}
```

detect_filling_level

Triggers a load carrier filling level detection as described in Detection of filling level (Section 6.4.2.3).
<|end_chunk_374|><|start_chunk_375|>
## Details

This service can be called as follows.
<|end_chunk_375|><|start_chunk_376|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_load_carrier/services/detect_filling_ - level
<|end_chunk_376|><|start_chunk_377|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_load_carrier/services/detect_filling_level
<|end_chunk_377|><|start_chunk_378|>
## Request

Required arguments:
pose_frame: see Hand-eye calibration (Section 6.4.2.4).
load_carrier_ids: IDs of the load carriers which should be detected. Currently only one ID can be specified.

Potentially required arguments:
robot_pose: see Hand-eye calibration (Section 6.4.2.4).
Optional arguments:
filling_level_cell_count: Number of cells in the filling level grid.
region_of_interest_id: ID of the 3D region of interest where to search for the load carriers.
region_of_interest_2d_id: ID of the 2D region of interest where to search for the load carriers.

Note: Only one type of region of interest can be set.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "filling_level_cell_count": {
            "x": "uint32",
            "y": "uint32"
        },
        "load_carrier_ids": [
            "string"
        ],
        "pose_frame": "string",
```
<|end_chunk_378|><|start_chunk_379|>
### Page 88
(continued from previous page)

```
    "region_of_interest_2d_id": "string",
    "region_of_interest_id": "string",
    "robot_pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
        }
    }
}
```

<|end_chunk_379|><|start_chunk_380|>
 Response 

load_carriers: list of detected load carriers and their filling levels.
timestamp: timestamp of the image set the detection ran on.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "detect_filling_level",
    "response": {
        "load_carriers": [
            {
            "cells_filling_levels": [
                {
                    "cell_position": {
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
                    },
                    "cell_size": {
                        "x": "float64",
                        "y": "float64"
                    },
                    "coverage": "float64",
                    "level_free_in_meters": {
                        "max": "float64",
                        "mean": "float64",
                        "min": "float64"
                    },
                    "level_in_percent": {
                        "max": "float64",
                        "mean": "float64",
                        "min": "float64"
                    }
                    }
                    ],
                    "filling_level_cell_count": {
                        "x": "uint32",
                        "y": "uint32"
                    },
                    "height_open_side": "float64",
```
<|end_chunk_380|><|start_chunk_381|>
### Page 89
(continued from previous page)
![img-31.jpeg](img-31.jpeg)
<|end_chunk_381|><|start_chunk_382|>
### Page 90
(continued from previous page)

```
        "message": "string",
        "value": "int16"
    },
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    }
    }
}
```

reset_defaults

Restores and applies the default values for this module's parameters ("factory reset").
<|end_chunk_382|><|start_chunk_383|>
 Details 

This service can be called as follows.
<|end_chunk_383|><|start_chunk_384|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_load_carrier/services/reset_defaults
<|end_chunk_384|><|start_chunk_385|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_load_carrier/services/reset_defaults
<|end_chunk_385|><|start_chunk_386|>
## Request

This service has no arguments.
<|end_chunk_386|><|start_chunk_387|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

set_load_carrier (deprecated)

Persistently stores a load carrier on the $r c \_v i s a r d$.
<|end_chunk_387|><|start_chunk_388|>
## API version 2

This service is not available in API version 2. Use set_load_carrier (Section 6.6.1.5) in rc_load_carrier_db instead.
<|end_chunk_388|><|start_chunk_389|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/set_load_carrier
The definitions of the request and response are the same as described in set_load_carrier (Section 6.6.1.5) in rc_load_carrier_db.
<|end_chunk_389|><|start_chunk_390|>
### Page 91
get_load_carriers (deprecated)
Returns the configured load carriers with the requested load_carrier_ids.
<|end_chunk_390|><|start_chunk_391|>
 API version 2 

This service is not available in API version 2. Use get_load_carriers (Section 6.6.1.5) in rc_load_carrier_db instead.
<|end_chunk_391|><|start_chunk_392|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/get_load_carriers
The definitions of the request and response are the same as described in get_load_carriers (Section 6.6.1.5) in rc_load_carrier_db.
delete_load_carriers (deprecated)
Deletes the configured load carriers with the requested load_carrier_ids.
<|end_chunk_392|><|start_chunk_393|>
## API version 2

This service is not available in API version 2. Use delete_load_carriers (Section 6.6.1.5) in rc_load_carrier_db instead.
<|end_chunk_393|><|start_chunk_394|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/delete_load_carriers
The definitions of the request and response are the same as described in delete_load_carriers (Section 6.6.1.5) in rc_load_carrier_db.
set_region_of_interest (deprecated)
Persistently stores a 3D region of interest on the rc_visard.
<|end_chunk_394|><|start_chunk_395|>
## API version 2

This service is not available in API version 2. Use set_region_of_interest (Section 6.6.2.4) in rc_roi_db instead.
<|end_chunk_395|><|start_chunk_396|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/set_region_of_interest
The definitions of the request and response are the same as described in set_region_of_interest (Section 6.6.2.4) in rc_roi_db.
get_regions_of_interest (deprecated)
Returns the configured 3D regions of interest with the requested region_of_interest_ids.
<|end_chunk_396|><|start_chunk_397|>
## API version 2

This service is not available in API version 2. Use get_regions_of_interest (Section 6.6.2.4) in rc_roi_db instead.
<|end_chunk_397|><|start_chunk_398|>
### Page 92<|end_chunk_398|><|start_chunk_399|>
 API version 1 (deprecated) 

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/get_regions_of_interest
The definitions of the request and response are the same as described in get_regions_of_interest (Section 6.6.2.4) in rc_roi_db.
delete_regions_of_interest (deprecated)

Deletes the configured 3D regions of interest with the requested region_of_interest_ids.
<|end_chunk_399|><|start_chunk_400|>
## API version 2

This service is not available in API version 2. Use delete_regions_of_interest (Section 6.6.2.4) in rc_roi_db instead.
<|end_chunk_400|><|start_chunk_401|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/delete_regions_of_interest
The definitions of the request and response are the same as described in delete_regions_of_interest (Section 6.6.2.4) in rc_roi_db.
set_region_of_interest_2d (deprecated)

Persistently stores a 2D region of interest on the $r c \_v i s a r d$.
<|end_chunk_401|><|start_chunk_402|>
## API version 2

This service is not available in API version 2. Use set_region_of_interest_2d (Section 6.6.2.4) in rc_roi_db instead.
<|end_chunk_402|><|start_chunk_403|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/set_region_of_interest_2d
The definitions of the request and response are the same as described in set_region_of_interest_2d (Section 6.6.2.4) in rc_roi_db.
get_regions_of_interest_2d (deprecated)

Returns the configured 2D regions of interest with the requested region_of_interest_2d_ids.
<|end_chunk_403|><|start_chunk_404|>
## API version 2

This service is not available in API version 2. Use get_regions_of_interest_2d (Section 6.6.2.4) in rc_roi_db instead.
<|end_chunk_404|><|start_chunk_405|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/get_region_of_interest_2d
The definitions of the request and response are the same as described in get_regions_of_interest_2d (Section 6.6.2.4) in rc_roi_db.
<|end_chunk_405|><|start_chunk_406|>
### Page 93
delete_regions_of_interest_2d (deprecated)
Deletes the configured 2D regions of interest with the requested region_of_interest_2d_ids.
<|end_chunk_406|><|start_chunk_407|>
 API version 2 

This service is not available in API version 2. Use delete_regions_of_interest_2d (Section 6.6.2.4) in rc_roi_db instead.
<|end_chunk_407|><|start_chunk_408|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_load_carrier/services/delete_regions_of_interest_2d
The definitions of the request and response are the same as described in delete_regions_of_interest_2d (Section 6.6.2.4) in rc_roi_db.
<|end_chunk_408|><|start_chunk_409|>
### 6.4.2.8 Return codes

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.
The following table contains a list of common codes:
Table 6.19: Return codes of the LoadCarrier module's services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -4 | Data acquisition took longer than allowed |
| -10 | New element could not be added as the maximum storage capacity of load carriers has <br> been exceeded |
| -11 | Sensor not connected, not supported or not ready |
| -302 | More than one load carrier provided to the detect_load_carriers or <br> detect_filling_level services, but only one is supported |
| 3 | The detection timeout during load carrier detection has been reached. Consider reducing <br> the model tolerance. |
| 10 | The maximum storage capacity of load carriers has been reached |
| 11 | An existent persistent model was overwritten by the call to set_load_carrier |
| 100 | The requested load carriers were not detected in the scene |
| 102 | The detected load carrier has no points inside |
| 300 | A valid robot pose was provided as argument but it is not required |
<|end_chunk_409|><|start_chunk_410|>
### 6.4.3 TagDetect
<|end_chunk_410|><|start_chunk_411|>
### 6.4.3.1 Introduction

The TagDetect modules are optional on-board modules of the $r c \_v i s a r d$ and require separate licenses (Section 8.7) to be purchased. The licenses are included in every $r c \_v i s a r d$ purchased after 01.07.2020.
The TagDetect modules run on board the $r c \_v i s a r d$ and allow the detection of 2D matrix codes and tags. Currently, there are TagDetect modules for $Q R$ codes and AprilTags. The modules, furthermore, compute the position and orientation of each tag in the 3D camera coordinate system, making it simple to manipulate a tag with a robot or to localize the camera with respect to a tag.
<|end_chunk_411|><|start_chunk_412|>
### Page 94
Tag detection is made up of three steps:

1. Tag reading on the 2D image pair (see Tag reading, Section 6.4.3.2).
2. Estimation of the pose of each tag (see Pose estimation, Section 6.4.3.3).
3. Re-identification of previously seen tags (see Tag re-identification, Section 6.4.3.4).

In the following, the two supported tag types are described, followed by a comparison.
<|end_chunk_412|><|start_chunk_413|>
 QR code 

![img-32.jpeg](img-32.jpeg)

Fig. 6.10: Sample QR code

QR codes are two-dimensional matrix codes that contain arbitrary user-defined data. There is wide support for decoding of QR codes on commodity hardware such as smartphones. Also, many online and offline tools are available for the generation of such codes.

The "pixels" of a QR code are called modules. Appearance and resolution of QR codes change with the amount of data they contain. While the special patterns in the three corners are always 7 modules wide, the number of modules between them increases the more data is stored. The lowest-resolution QR code is of size $21 \times 21$ modules and can contain up to 152 bits.

Even though many QR code generation tools support generation of specially designed QR codes (e.g., containing a logo, having round corners, or having dots as modules), a reliable detection of these tags by the rc_visard's TagDetect module is not guaranteed. The same holds for QR codes which contain characters that are not part of regular ASCII.
<|end_chunk_413|><|start_chunk_414|>
### Page 95<|end_chunk_414|><|start_chunk_415|>
 AprilTag 

![img-33.jpeg](img-33.jpeg)

Fig. 6.11: A 16 h 5 tag (left), a 36 h 11 tag (center) and a 41 h 12 tag (right). AprilTags consist of a mandatory white (a) and black (b) border and a variable amount of data bits (c).

AprilTags are similar to QR codes. However, they are specifically designed for robust identification at large distances. As for QR codes, we will call the tag pixels modules. Fig. 6.11 shows how AprilTags are structured. They have a mandatory white and black border, each one module wide. The tag families $16 \mathrm{~h} 5,25 \mathrm{~h} 9,36 \mathrm{~h} 10$ and 36 h 11 are surrounded by this border and carry a variable amount of data modules in the center. For tag family 41 h 12 , the black and white border is shifted towards the inside and the data modules are in the center and also at the border of the tags. Other than QR codes, AprilTags do not contain any user-defined information but are identified by a predefined family and ID. The tags in Fig. 6.11 for example are of family 16h5, 36h11 and 41 h 12 have id 0,11 and 0 , respectively. All supported families are shown in Table 6.20.

Table 6.20: AprilTag families

| Family | Number of tag IDs | Recommended |
| :-- | :-- | :-- |
| 16 h 5 | 30 | - |
| 25 h 9 | 35 | 0 |
| 36 h 10 | 2320 | 0 |
| 36 h 11 | 587 | + |
| 41 h 12 | 2115 | + |

For each family, the number before the " $h$ " states the number of data modules contained in the tag: While a 16 h 5 tag contains $16(4 \times 4)$ data modules ((c) in Fig. 6.11), a 36 h 11 tag contains $36(6 \times 6)$ modules and a 41 h 12 tag contains 41 ( $3 \times 3$ inner $+4 \times 8$ outer) modules. The number behind the " $h$ " refers to the Hamming distance between two tags of the same family. The higher, the more robust is the detection, but the fewer individual tag IDs are available for the same number of data modules (see Table 6.20).

The advantage of fewer modules (as for 16 h 5 compared to 36 h 11 ) is the lower resolution of the tag. Hence, each tag module is larger and the tag therefore can be detected from a larger distance. This, however, comes at a price: Firstly, fewer data modules lead to fewer individual tag IDs. Secondly, and more importantly, detection robustness is significantly reduced due to a higher false positive rate; i.e, tags are mixed up or nonexistent tags are detected in random image texture or noise. The 41 h 12 family has its border shifted towards the inside, which gives it more data modules at a lower number of total modules compared to the 36 h 11 family.
For these reasons we recommend using the 41 h 12 and 36 h 11 families and highly discourage the use of the 16 h 5 family. The latter family should only be used if a large detection distance really is necessary for an application. However, the maximum detection distance increases only by approximately $25 \%$ when using a 16 h 5 tag instead of a 36 h 11 tag.
<|end_chunk_415|><|start_chunk_416|>
### Page 96
Pre-generated AprilTags can be downloaded at the AprilTag project website (https://april.eecs.umich. edu/software/apriltag.html). There, each family consists of multiple PNGs containing single tags. Each pixel in the PNGs corresponds to one AprilTag module. When printing the tags of the families 36h11, 36h10, 25 h 9 and 16 h 5 special care must be taken to also include the white border around the tag that is contained in the PNG (see (a) in Fig. 6.11). Moreover, all tags should be scaled to the desired printing size without any interpolation, so that the sharp edges are preserved.
<|end_chunk_416|><|start_chunk_417|>
 Comparison 

Both QR codes and AprilTags have their up and down sides. While QR codes allow arbitrary userdefined data to be stored, AprilTags have a pre-defined and limited set of tags. On the other hand, AprilTags have a lower resolution and can therefore be detected at larger distances. Moreover, the continuous white to black border in AprilTags allow for more precise pose estimation.

Note: If user-defined data is not required, AprilTags should be preferred over QR codes.
<|end_chunk_417|><|start_chunk_418|>
### 6.4.3.2 Tag reading

The first step in the tag detection pipeline is reading the tags on the 2D image pair. This step takes most of the processing time and its precision is crucial for the precision of the resulting tag pose. To control the speed of this step, the quality parameter can be set by the user. It results in a downscaling of the image pair before reading the tags. High yields the largest maximum detection distance and highest precision, but also the highest processing time. Low results in the smallest maximum detection distance and lowest precision, but processing requires less than half of the time. Medium lies in between. Please note that this quality parameter has no relation to the quality parameter of Stereo matching module (Section 6.2).
![img-34.jpeg](img-34.jpeg)

Fig. 6.12: Visualization of module size $s$, size of a tag in modules $r$, and size of a tag in meters $t$ for AprilTags (left and center) and QR codes (right)

The maximum detection distance $z$ at quality High can be approximated by using the following formulae,

$$
\begin{aligned}
z & =\frac{f s}{p} \\
s & =\frac{t}{r}
\end{aligned}
$$

where $f$ is the focal length (Section 6.1.1) in pixels and $s$ is the size of a module in meters. $s$ can easily be calculated by the latter formula, where $t$ is the size of the tag in meters and $r$ is the width of the code in modules (for AprilTags without the white border). Fig. 6.12 visualizes these variables. $p$ denotes the number of image pixels per module required for detection. It is different for QR codes and AprilTags.
<|end_chunk_418|><|start_chunk_419|>
### Page 97
Moreover, it varies with the tag's angle to the camera and illumination. Approximate values for robust detection are:

- AprilTag: $p=5$ pixels/module
- QR code: $p=6$ pixels/module

The following tables give sample maximum distances for different situations, assuming a focal length of 1075 pixels and the parameter quality to be set to High.

Table 6.21: Maximum detection distance examples for AprilTags with a width of $t=4 \mathrm{~cm}$

| AprilTag family | Tag width | Maximum distance |
| :-- | :-- | :-- |
| 36 h 11 (recommended) | 8 modules | 1.1 m |
| 16 h 5 | 6 modules | 1.4 m |
| 41 h 12 (recommended) | 5 modules | 1.7 m |

Table 6.22: Maximum detection distance examples for QR codes with a width of $t=8 \mathrm{~cm}$

| Tag width | Maximum distance |
| :-- | :-- |
| 29 modules | 0.49 m |
| 21 modules | 0.70 m |
<|end_chunk_419|><|start_chunk_420|>
 6.4.3.3 Pose estimation 

For each detected tag, the pose of this tag in the camera coordinate frame is estimated. A requirement for pose estimation is that a tag is fully visible in the left and right camera image. The coordinate frame of the tag is aligned as shown below.
![img-35.jpeg](img-35.jpeg)

Fig. 6.13: Coordinate frames of AprilTags (left and center) and QR codes (right)

The z-axis is pointing "into" the tag. Please note that for AprilTags, although having the white border included in their definition, the coordinate system's origin is placed exactly at the transition from the white to the black border. Since AprilTags do not have an obvious orientation, the origin is defined as the upper left corner in the orientation they are pre-generated in.

During pose estimation, the tag's size is also estimated, while assuming the tag to be square. For QR codes, the size covers the full tag. For AprilTags, the size covers only the part inside the border defined by the transition from the black to the white border modules, hence ignoring the outermost white border for the tag families 16h5, 25h9, 36h10 and 36h11.

The user can also specify the approximate size $( \pm 10 \%)$ of tags. All tags not matching this size constraint are automatically filtered out. This information is further used to resolve ambiguities in pose estimation
<|end_chunk_420|><|start_chunk_421|>
### Page 98
that may arise if multiple tags with the same ID are visible in the left and right image and these tags are aligned in parallel to the image rows.

Note: For best pose estimation results one should make sure to accurately print the tag and to attach it to a rigid and as planar as possible surface. Any distortion of the tag or bump in the surface will degrade the estimated pose.

Note: It is highly recommended to set the approximate size of a tag. Otherwise, if multiple tags with the same ID are visible in the left or right image, pose estimation may compute a wrong pose if these tags have the same orientation and are approximately aligned in parallel to the image rows. However, even if the approximate size is not given, the TagDetect modules try to detect such situations and filter out affected tags.

Below tables give approximate precisions of the estimated poses of AprilTags. We distinguish between lateral precision (i.e., in x and y direction) and precision in z direction. It is assumed that quality is set to High, that the camera's viewing direction is parallel to the tag's normal and that the images are well exposed and do not suffer from motion blur. The size of a tag does not have a significant effect on the lateral or z precision; however, in general, larger tags improve precision. With respect to precision of the orientation especially around the $x$ and $y$ axes, larger tags clearly outperform smaller ones.

Table 6.23: Approximate position precision for AprilTag detections with High quality in an ideal scenario for different base lines

| Distance | rc_visard 65 - lateral | rc_visard 65 - z | rc_visard 160 - lateral | rc_visard 160 - z |
| :-- | :-- | :-- | :-- | :-- |
| 0.5 m | 0.05 mm | 0.5 mm | 0.05 mm | 0.3 mm |
| 1.0 m | 0.15 mm | 1.8 mm | 0.15 mm | 1.4 mm |
| 2.0 m | 1.5 mm | 14.5 mm | 0.5 mm | 3.7 mm |

Table 6.24: Approximate orientation precision for AprilTag detections with High quality in an ideal scenario for different tag sizes

| Distance | $60 \times 60 \mathrm{~mm}$ | $120 \times 120 \mathrm{~mm}$ |
| :-- | :-- | :-- |
| 0.5 m | $0.2^{\circ}$ | - |
| 1.0 m | $0.8^{\circ}$ | $0.3^{\circ}$ |
| 2.0 m | $2.0^{\circ}$ | $0.8^{\circ}$ |
| 3.0 m | - | $1.8^{\circ}$ |
<|end_chunk_421|><|start_chunk_422|>
 6.4.3.4 Tag re-identification 

Each tag has an ID; for AprilTags it is the family plus tag ID, for QR codes it is the contained data. However, these IDs are not unique, since the same tag may appear multiple times in a scene.
For distinction of these tags, the TagDetect modules also assign each detected tag a unique identifier. To help the user identifying an identical tag over multiple detections, tag detection tries to re-identify tags; if successful, a tag is assigned the same unique identifier again.
Tag re-identification compares the positions of the corners of the tags in a static coordinate frame to find identical tags. Tags are assumed identical if they did not or only slightly move in that static coordinate frame. For that static coordinate frame to be available, dynamic-state estimation (Section 6.3.1) must be switched on. If it is not, the sensor is assumed to be static; tag re-identification will then not work across sensor movements.

By setting the max_corner_distance threshold, the user can specify how much a tag is allowed move in the static coordinate frame between two detections to be considered identical. This parameter defines the maximum distance between the corners of two tags, which is shown in Fig. 6.14. The Euclidean distances of all four corresponding tag corners are computed in 3D. If none of these distances exceeds the threshold, the tags are considered identical.
<|end_chunk_422|><|start_chunk_423|>
### Page 99
![img-36.jpeg](img-36.jpeg)

Fig. 6.14: Simplified visualization of tag re-identification. Euclidean distances between associated tag corners in 3D are compared (red arrows).

After a number of tag detection runs, previously detected tag instances will be discarded if they are not detected in the meantime. This can be configured by the parameter forget_after_n_detections.
<|end_chunk_423|><|start_chunk_424|>
 6.4.3.5 Hand-eye calibration 

In case the camera has been calibrated to a robot, the TagDetect module can automatically provide poses in the robot coordinate frame. For the TagDetect node's Services (Section 6.4.3.8), the frame of the output poses can be controlled with the pose_frame argument.
Two different pose_frame values can be chosen:

1. Camera frame (camera). All poses provided by the module are in the camera frame.
2. External frame (external). All poses provided by the module are in the external frame, configured by the user during the hand-eye calibration process. The module relies on the on-board Hand-eye calibration module (Section 6.5.1) to retrieve the sensor mounting (static or robot mounted) and the hand-eye transformation. If the sensor mounting is static, no further information is needed. If the sensor is robot-mounted, the robot pose is required to transform poses to and from the external frame.

All pose_frame values that are not camera or external are rejected.
<|end_chunk_424|><|start_chunk_425|>
### 6.4.3.6 Parameters

There are two separate modules available for tag detection, one for detecting AprilTags and one for QR codes, named rc_april_tag_detect and rc_qr_code_detect, respectively. Apart from the module names they share the same interface definition.
In addition to the REST-API interface (Section 7.3), the TagDetect modules provide pages on the Web GUI under Modules $\rightarrow$ AprilTag and Modules $\rightarrow$ QR Code, on which they can be tried out and configured manually.

In the following, the parameters are listed based on the example of rc_qr_code_detect. They are the same for rc_april_tag_detect.
This module offers the following run-time parameters:
<|end_chunk_425|><|start_chunk_426|>
### Page 100
Table 6.25: The rc_qr_code_detect module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :-- | :--: | :--: | :--: | :--: | :--: |
| detect_inverted_tags | bool | false | true | false | Detect tags with black and white exchanged |
| forget_after_n_detections | int32 | 1 | 1000 | 30 | Number of detection runs after <br> which to forget about a previous tag <br> during tag re-identification |
| max_corner_distance | float64 | 0.001 | 0.01 | 0.005 | Maximum distance of corresponding tag corners in meters during tag re-identification |
| quality | string | - | - | High | Quality of tag detection: [Low, <br> Medium, High] |
| use_cached_images | bool | false | true | false | Use most recently received image <br> pair instead of waiting for a new pair |

Via the REST-API, these parameters can be set as follows.
<|end_chunk_426|><|start_chunk_427|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/<rc_qr_code_detect|rc_april_tag_detect>/ ...parameters/parameters?<parameter-name>=<value>
<|end_chunk_427|><|start_chunk_428|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/<rc_qr_code_detect|rc_april_tag_detect>/parameters?
...<parameter-name>=<value>
<|end_chunk_428|><|start_chunk_429|>
### 6.4.3.7 Status values

The TagDetect modules reports the following status values:
Table 6.26: The rc_qr_code_detect and rc_april_tag_detect module's status values

| Name | Description |
| :-- | :-- |
| data_acquisition_time | Time in seconds required to acquire image pair |
| last_timestamp_processed | The timestamp of the last processed image pair |
| processing_time | Processing time of the last detection in seconds |
| state | The current state of the node |

The reported state can take one of the following values.
Table 6.27: Possible states of the TagDetect modules

| State name | Description |
| :-- | :-- |
| IDLE | The module is idle. |
| RUNNING | The module is running and ready for tag detection. |
| FATAL | A fatal error has occurred. |
<|end_chunk_429|><|start_chunk_430|>
### 6.4.3.8 Services

The TagDetect modules implement a state machine for starting and stopping. The actual tag detection can be triggered via detect.
<|end_chunk_430|><|start_chunk_431|>
### Page 101
The user can explore and call the rc_qr_code_detect and rc_april_tag_detect modules' services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1).
detect

Triggers a tag detection.
<|end_chunk_431|><|start_chunk_432|>
 Details 

Depending on the use_cached_images parameter, the module will use the latest received image pair (if set to true) or wait for a new pair that is captured after the service call was triggered (if set to false, this is the default). Even if set to true, tag detection will never use one image pair twice.

It is recommended to call detect in state RUNNING only. It is also possible to be called in state IDLE, resulting in an auto-start and stop of the module. This, however, has some drawbacks: First, the call will take considerably longer; second, tag re-identification will not work. It is therefore highly recommended to manually start the module before calling detect.

Tags might be omitted from the detect response due to several reasons, e.g., if a tag is visible in only one of the cameras or if pose estimation did not succeed. These filtered-out tags are noted in the log, which can be accessed as described in Downloading log files (Section 8.8).

A visualization of the latest detection is shown on the Web GUI tabs of the TagDetect modules. Please note that this visualization will only be shown after calling the detection service at least once. On the Web GUI, one can also manually try the detection by clicking the Detect button.

Due to changes in system time on the $r c \_v i s a r d$ there might occur jumps of timestamps, forward as well as backward (see Time synchronization, Section 7.8). Forward jumps do not have an effect on the TagDetect module. Backward jumps, however, invalidate already received images. Therefore, in case a backwards time jump is detected, an error of value -102 will be issued on the next detect call, also to inform the user that the timestamps included in the response will jump back. This service can be called as follows.
<|end_chunk_432|><|start_chunk_433|>
## API version 2

PUT http://<host>/api/v2/pipeLines/0/nodes/<rc_qr_code_detect|rc_april_tag_ $\sim$ detect $>$ /services/detect
<|end_chunk_433|><|start_chunk_434|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/<rc_qr_code_detect|rc_april_tag_detect $>$ / $\sim$ services/detect
<|end_chunk_434|><|start_chunk_435|>
## Request

Optional arguments:
tags is the list of tag IDs that the TagDetect module should detect. For QR codes, the ID is the contained data. For AprilTags, it is "<family>_<id>", so, e.g., for a tag of family 36 h 11 and ID 5, it is "36h11_5". Naturally, the AprilTag module can only be triggered for AprilTags, and the QR code module only for QR codes.

The tags list can also be left empty. In that case, all detected tags will be returned. This feature should be used only during development and debugging of an application. Whenever possible, the concrete tag IDs
<|end_chunk_435|><|start_chunk_436|>
### Page 102
should be listed, on the one hand avoiding some false positives, on the other hand speeding up tag detection by filtering tags not of interest.

For AprilTags, the user can not only specify concrete tags but also a complete family by setting the ID to "<family>", so, e.g., "36h11". All tags of this family will then be detected. It is further possible to specify multiple complete tag families or a combination of concrete tags and complete tag families; for instance, triggering for "36h11", "25h9_3", and "36h10" at the same time.

In addition to the ID, the approximate size $( \pm 10 \%)$ of a tag can be set with the size parameter. As described in Pose estimation (Section 6.4.3.3), this information helps to resolve ambiguities in pose estimation that may arise in certain situations and can be used to filter out tags not fulfilling the given size constraint.

The tags list is OR-connected. All tags will be returned that match any of id-size pair elements in the tags list.
pose_frame controls whether the poses of the detected tags are returned in the camera or external frame, as detailed in Hand-eye calibration (Section 6.4.3.5). The default is camera.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "pose_frame": "string",
        "robot_pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        },
        "tags": [
            {
                "id": "string",
                "size": "float64"
            }
        ]
    }
}
```

<|end_chunk_436|><|start_chunk_437|>
 Response 

timestamp is set to the timestamp of the image pair the tag detection ran on.
tags contains all detected tags.
id is the ID of the tag, similar to id in the request.
instance_id is the random unique identifier of the tag assigned by tag reidentification.
pose contains position and orientation. The orientation is in quaternion format.
pose_frame is set to the coordinate frame above pose refers to. It will either be "camera" or "external".
<|end_chunk_437|><|start_chunk_438|>
### Page 103
size will be set to the estimated tag size in meters.
return_code holds possible warnings or error codes.
The definition for the response with corresponding datatypes is:

```
{
    "name": "detect",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
    },
    "tags": [
        {
            "id": "string",
            "instance_id": "string",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            }
            },
            "pose_frame": "string",
            "size": "float64",
            "timestamp": {
                    "nsec": "int32",
                    "sec": "int32"
            }
        }
    ],
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    }
    }
}
```

start

Starts the module by transitioning from IDLE to RUNNING.
<|end_chunk_438|><|start_chunk_439|>
 Details 

When running, the module receives images from the stereo camera and is ready to perform tag detections. To save computing resources, the module should only be running when necessary.

This service can be called as follows.
<|end_chunk_439|><|start_chunk_440|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/<rc_qr_code_detect|rc_april_tag_detect>/ $\sim$ services/start
<|end_chunk_440|><|start_chunk_441|>
## API version 1 (deprecated)
<|end_chunk_441|><|start_chunk_442|>
### Page 104
PUT http://<host>/api/v1/nodes/<rc_qr_code_detect|rc_april_tag_detect>/services/start
<|end_chunk_442|><|start_chunk_443|>
 Request 

This service has no arguments.
<|end_chunk_443|><|start_chunk_444|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "start",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
stop
```

Stops the module by transitioning to IDLE.
<|end_chunk_444|><|start_chunk_445|>
## Details

This transition can be performed from state RUNNING and FATAL. All tag reidentification information is cleared during stopping.

This service can be called as follows.
<|end_chunk_445|><|start_chunk_446|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/<rc_qr_code_detect|rc_april_tag_ $\sim$ detect $>$ /services/stop
<|end_chunk_446|><|start_chunk_447|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/<rc_qr_code_detect|rc_april_tag_detect>/ $\sim$ services/stop
<|end_chunk_447|><|start_chunk_448|>
## Request

This service has no arguments.
<|end_chunk_448|><|start_chunk_449|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "stop",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

restart

Restarts the module.
<|end_chunk_449|><|start_chunk_450|>
## Details

If in RUNNING or FATAL, the module will be stopped and then started. If in IDLE, the module will be started.
<|end_chunk_450|><|start_chunk_451|>
### Page 105
This service can be called as follows.
<|end_chunk_451|><|start_chunk_452|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/<rc_qr_code_detect|rc_april_tag_ $\sim$ detect $>$ /services/restart
<|end_chunk_452|><|start_chunk_453|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/<rc_qr_code_detect|rc_april_tag_detect>/ $\sim$ services/restart
<|end_chunk_453|><|start_chunk_454|>
## Request

This service has no arguments.
<|end_chunk_454|><|start_chunk_455|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "restart",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

reset_defaults

Resets all parameters of the module to its default values, as listed in above table.
<|end_chunk_455|><|start_chunk_456|>
## Details

This service can be called as follows.
<|end_chunk_456|><|start_chunk_457|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/<rc_qr_code_detect|rc_april_tag_detect>/ $\sim$ services/reset_defaults
<|end_chunk_457|><|start_chunk_458|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/<rc_qr_code_detect|rc_april_tag_detect>/services/reset_ $\sim$ defaults
<|end_chunk_458|><|start_chunk_459|>
## Request

This service has no arguments.
<|end_chunk_459|><|start_chunk_460|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```
<|end_chunk_460|><|start_chunk_461|>
### Page 106<|end_chunk_461|><|start_chunk_462|>
 6.4.3.9 Return codes 

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.
The following table contains a list of common return codes:

| Code | Description |
| :-- | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -4 | A timeout occurred while waiting for the image pair |
| -9 | The license is not valid |
| -11 | Sensor not connected, not supported or not ready |
| -101 | Internal error during tag detection |
| -102 | There was a backwards jump of system time |
| -103 | Internal error during tag pose estimation |
| -200 | A fatal internal error occurred |
| 200 | Multiple warnings occurred; see list in message |
| 201 | The module was not in state RUNNING |
<|end_chunk_462|><|start_chunk_463|>
### 6.4.4 ItemPick
<|end_chunk_463|><|start_chunk_464|>
### 6.4.4.1 Introduction

The ItemPick module provides an out-of-the-box perception solution for robotic pick-and-place applications. ItemPick targets the detection of flat surfaces on unknown objects for picking with a suction gripper.
In addition, the module offers:

- A dedicated page on the rc_visard Web GUI (Section 7.1) for easy setup, configuration, testing, and application tuning.
- The definition of regions of interest to select relevant volumes in the scene (see RoiDB, Section 6.6.2).
- A load carrier detection functionality for bin-picking applications (see LoadCarrier, Section 6.4.2), to provide grasps for items inside a bin only.
- The definition of compartments inside a load carrier to provide grasps for specific volumes of the bin only.
- Support for static and robot-mounted cameras and optional integration with the Hand-eye calibration (Section 6.5.1) module, to provide grasps in the user-configured external reference frame.
- A quality value associated to each suggested grasp and related to the flatness of the grasping surface.
- Selection of a sorting strategy to sort the returned grasps.
- 3D visualization of the detection results with grasp points and gripper animations in the Web GUI.

Note: In this chapter, cluster and surface are used as synonyms and identify a set of points (or pixels) with defined geometrical properties.

The module is an optional on-board module of the $r c \_v i s a r d$ and requires a separate ItemPick license (Section 8.7) to be purchased.
<|end_chunk_464|><|start_chunk_465|>
### Page 107<|end_chunk_465|><|start_chunk_466|>
 6.4.4.2 Computation of grasps 

The ItemPick module offers a service for computing grasps for suction grippers. The gripper is defined by its suction surface length and width.
The ItemPick module identifies flat surfaces in the scene and supports flexible and/or deformable items. The type of these item models is called UNKNOWN since they don't need to have a standard geometrical shape. Optionally, the user can also specify the minimum and maximum size of the item.
Optionally, further information can be given to the modules in a grasp computation request:

- The ID of the load carrier which contains the items to be grasped.
- A compartment inside the load carrier where to compute grasps (see Load carrier compartments, Section 6.6.1.3).
- The ID of the 3D region of interest where to search for the load carriers if a load carrier is set. Otherwise, the ID of the 3D region of interest where to compute grasps.
- Collision detection information: The ID of the gripper to enable collision checking and optionally a pre-grasp offset to define a pre-grasp position. Details on collision checking are given below in CollisionCheck (Section 6.4.4.4).
A grasp provided by the ItemPick module represents the recommended pose of the TCP (Tool Center Point) of the suction gripper. The grasp type is always set to SUCTION.

For ItemPick with an UNKNOWN item model, the computed grasp pose is the center of the biggest ellipse that can be inscribed in each surface.

The grasp orientation is a right-handed coordinate system and is defined such that its $z$ axis is normal to the surface pointing inside the object at the grasp position and its $x$ axis is directed along the maximum elongation of the ellipse. Since the $x$ axis can have two possible directions, the one that better fits to the preferred TCP orientation (see Setting the preferred orientation of the TCP, Section 6.4.4.3) is selected. If the run-time parameter allow_any_grasp_z_rotation is set to true, the $x$ axis will not be forced to be aligned with the maximum elongation of the graspable ellipse, but can have any rotation around the $z$ axis. In this case, the returned grasp will have the orientation that best fits to the preferred TCP orientation and is collision free, if collision checking.
![img-37.jpeg](img-37.jpeg)

Fig. 6.15: Illustration of a suction grasp with coordinate system and ellipse representing the maximum suction surface

Each grasp includes the dimensions of the maximum suction surface available, modelled as an ellipse of axes max_suction_surface_length and max_suction_surface_width. The user is enabled to filter grasps by specifying the minimum suction surface required by the suction device in use. If the run-time parameter allow_any_grasp_z_rotation is set to true, max_suction_surface_length and max_suction_surface_width will be equal and correspond to the shortest axis of the largest graspable ellipse.
Each grasp also includes a quality value, which gives an indication of the flatness of the grasping surface. The quality value varies between 0 and 1 , where higher numbers correspond to a flatter reconstructed surface.
<|end_chunk_466|><|start_chunk_467|>
### Page 108
The grasp definition is complemented by a uuid (Universally Unique Identifier) and the timestamp of the oldest image that was used to compute the grasp.

Grasp sorting is performed based on the selected sorting strategy. The following sorting strategies are available and can be set in the Web GUI (Section 7.1) or using the set_sorting_strategies service call:

- gravity: highest grasp points along the gravity direction are returned first,
- surface_area: grasp points with the largest surface area are returned first,
- direction: grasp points with the shortest distance along a defined direction vector in a given pose_frame are returned first.
- distance_to_point: grasp points with the shortest or farthest (if farthest_first is true) distance from a point in a given pose_frame are returned first.
If no sorting strategy is set or default sorting is chosen in the Web GUI, sorting is done based on a combination of gravity and surface_area.

<|end_chunk_467|><|start_chunk_468|>
 6.4.4.3 Setting the preferred orientation of the TCP 

The ItemPick module determines the reachability of grasp points based on the preferred orientation of the TCP. The preferred orientation can be set via the set_preferred_orientation service or on the ItemPick page in the Web GUI. The resulting direction of the TCP's z axis is used to reject grasps which cannot be reached by the gripper. Furthermore, the preferred orientation is used to select one grasp of several possible symmetries that is best reachable for the robot.

The preferred orientation can be set in the camera coordinate frame or in the external coordinate frame, in case a hand-eye calibration is available. If the preferred orientation is specified in the external coordinate frame and the sensor is robot mounted, the current robot pose has to be given to each object detection call. If no preferred orientation is set, the orientation of the left camera (see Coordinate frames ) will be used as the preferred orientation of the TCP.
<|end_chunk_468|><|start_chunk_469|>
### 6.4.4.4 Interaction with other modules

Internally, the ItemPick module depends on, and interacts with other on-board modules as listed below.
Note: All changes and configuration updates to these modules will affect the performance of the ItemPick module.
<|end_chunk_469|><|start_chunk_470|>
## Camera and depth data

The ItemPick module makes internally use of the following data:

- Rectified images from the Camera module (rc_camera, Section 6.1);
- Disparity, error, and confidence images from the Stereo matching module (rc_stereomatching, Section 6.2)

All processed images are guaranteed to be captured after the module trigger time.
<|end_chunk_470|><|start_chunk_471|>
## IO and Projector Control

In case the $r c \_v i s a r d$ is used in conjunction with an external random dot projector and the IO and Projector Control module (rc_iocontrol, Section 6.5.4), it is recommended to connect the projector to GPIO Out 1 and set the stereo-camera module's acquisition mode to SingleFrameOut1 (see Stereo matching parameters, Section 6.2.1), so that on each image acquisition trigger an image with and without projector pattern is acquired.
<|end_chunk_471|><|start_chunk_472|>
### Page 109
Alternatively, the output mode for the GPIO output in use should be set to ExposureAlternateActive (see Description of run-time parameters, Section 6.5.4.1).
In either case, the Auto Exposure Mode exp...auto...mode should be set to AdaptiveOut1 to optimize the exposure of both images.
<|end_chunk_472|><|start_chunk_473|>
 Hand-eye calibration 

In case the camera has been calibrated to a robot, the ItemPick module can automatically provide poses in the robot coordinate frame. For the ItemPick node's Services (Section 6.4.4.7), the frame of the output poses can be controlled with the pose...frame argument.
Two different pose...frame values can be chosen:

1. Camera frame (camera). All poses provided by the modules are in the camera frame, and no prior knowledge about the pose of the camera in the environment is required. This means that the configured regions of interest and load carriers move with the camera. It is the user's responsibility to update the configured poses if the camera frame moves (e.g. with a robot-mounted camera).
2. External frame (external). All poses provided by the modules are in the external frame, configured by the user during the hand-eye calibration process. The module relies on the onboard Hand-eye calibration module (Section 6.5.1) to retrieve the sensor mounting (static or robot mounted) and the hand-eye transformation. If the mounting is static, no further information is needed. If the sensor is robot-mounted, the robot...pose is required to transform poses to and from the external frame.

Note: If no hand-eye calibration is available, all pose...frame values should be set to camera.

All pose...frame values that are not camera or external are rejected.
If the sensor is robot-mounted, the current robot...pose has to be provided depending on the value of pose...frame and the definition of the sorting direction or sorting point:

- If pose...frame is set to external, providing the robot pose is obligatory.
- If the sorting direction is defined in external, providing the robot pose is obligatory.
- If the distance-to-point sorting strategy is defined in external, providing the robot pose is obligatory.
- In all other cases, providing the robot pose is optional.

<|end_chunk_473|><|start_chunk_474|>
## LoadCarrier

The ItemPick module uses the load carrier detection functionality provided by the LoadCarrier module (rc...load...carrier, Section 6.4.2), with the run-time parameters specified for this module. However, only one load carrier will be returned and used in case multiple matching load carriers could be found in the scene. In case multiple load carriers of the same type are visible, a 3D region of interest should be set to ensure that always the same load carrier is used for the ItemPick module.
<|end_chunk_474|><|start_chunk_475|>
## CollisionCheck

Collision checking can be easily enabled for grasp computation of the ItemPick module by passing the ID of the used gripper and optionally a pre-grasp offset to the compute...grasps service call. The gripper has to be defined in the GripperDB module (see Setting a gripper, Section 6.6.3.2) and details about collision checking are given in Collision checking within other modules (Section 6.5.2.2).
If collision checking is enabled, only grasps which are collision free will be returned. However, the visualization images on the ItemPick page of the Web GUI also show colliding grasp points as black ellipses.
<|end_chunk_475|><|start_chunk_476|>
### Page 110
The CollisionCheck module's run-time parameters affect the collision detection as described in CollisionCheck Parameters (Section 6.5.2.3).
<|end_chunk_476|><|start_chunk_477|>
 6.4.4.5 Parameters 

ItemPick is represented by the rc_itempick node in the REST-API and are reached in the Web GUI (Section 7.1) under Modules $\rightarrow$ ItemPick. The user can explore and configure the rc_itempick module's run-time parameters, e.g. for development and testing, using the Web GUI or the REST-API interface
:(Section 7.3).
The user can explore and configure the rc_itempick module's run-time parameters, e.g. for development and testing, using the Web GUI or the REST-API interface (Section 7.3).
<|end_chunk_477|><|start_chunk_478|>
## Parameter overview

This module offers the following run-time parameters:
Table 6.28: The rc_itempick module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :--: | :--: | :--: | :--: | :--: | :--: |
| allow_any_grasp_z_rotation | bool | false | true | false | Whether the grasps are allowed to have arbitrary rotation instead being aligned with the major axis of the graspable ellipse |
| cluster_max_curvature | float64 | 0.005 | 0.5 | 0.11 | Maximum curvature allowed within one cluster. The smaller this value, the more clusters will be split apart. |
| cluster_max_dimension | float64 | 0.05 | 2.0 | 0.3 | Maximum allowed diameter for a cluster in meters. Clusters with a diameter larger than this value are not used for grasp computation. |
| clustering_discontinuity_factor | float64 | 0.1 | 5.0 | 1.0 | Factor used to discriminate depth discontinuities within a patch. The smaller this value, the more clusters will be split apart. |
| clustering_max_surface_rmse | float64 | 0.0005 | 0.01 | 0.004 | Maximum root-mean-square error (RMSE) in meters of points belonging to a surface |
| clustering_patch_size | int32 | 3 | 10 | 4 | Size in pixels of the square patches the depth map is subdivided into during the first clustering step |
| grasp_filter_orientation_threshold | float64 | 0.0 | 180.0 | 45.0 | Maximum allowed orientation change between grasp and preferred orientation in degrees |
| max_grasps | int32 | 1 | 20 | 5 | Maximum number of provided grasps |
<|end_chunk_478|><|start_chunk_479|>
## Description of run-time parameters

Each run-time parameter is represented by a row on the Web GUI's ItemPick page. The name in the Web GUI is given in brackets behind the parameter name and the parameters are listed in the order they appear in the Web GUI:
<|end_chunk_479|><|start_chunk_480|>
### Page 111<|end_chunk_480|><|start_chunk_481|>
 max_grasps (Maximum Grasps) 

sets the maximum number of provided grasps.
Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/parameters/parameters?max_ -grasps=<value>

API version 1 (deprecated)
PUT http://<host>/api/v1/nodes/rc_itempick/parameters?max_grasps=<value>
cluster_max_dimension (Cluster Maximum Dimension)
is the maximum allowed diameter for a cluster in meters. Clusters with a diameter larger than this value are not used for grasp computation.

Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/parameters/parameters?cluster_ ...max_dimension=<value>

API version 1 (deprecated)
PUT http://<host>/api/v1/nodes/rc_itempick/parameters?cluster_max_dimension=<value>
cluster_max_curvature (Cluster Maximum Curvature)
is the maximum curvature allowed within one cluster. The smaller this value, the more clusters will be split apart.

Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/parameters/parameters?cluster_ ...max_curvature=<value>

API version 1 (deprecated)
PUT http://<host>/api/v1/nodes/rc_itempick/parameters?cluster_max_curvature=<value>
clustering_patch_size (Patch Size)
is the size of the square patches the depth map is subdivided into during the first clustering step in pixels.

Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/parameters/parameters?
...clustering_patch_size=<value>

API version 1 (deprecated)
<|end_chunk_481|><|start_chunk_482|>
### Page 112
PUT http://<host>/api/v1/nodes/rc_itempick/parameters?clustering_patch_size=<value>
<|end_chunk_482|><|start_chunk_483|>
 clustering_discontinuity_factor (Discontinuity Factor) 

is the factor used to discriminate depth discontinuities within a patch. The smaller this value, the more clusters will be split apart.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_483|><|start_chunk_484|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/parameters/parameters?
...clustering_discontinuity_factor=<value>
<|end_chunk_484|><|start_chunk_485|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/parameters?clustering_discontinuity_factor= $\ldots<$ value $>$
clustering_max_surface_rmse (Maximum Surface RMSE)
is the maximum root-mean-square error (RMSE) in meters of points belonging to a surface.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_485|><|start_chunk_486|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/parameters/parameters?
...clustering_max_surface_rmse=<value>
<|end_chunk_486|><|start_chunk_487|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/parameters?clustering_max_surface_rmse= $\ldots<$ value $>$
grasp_filter_orientation_threshold (Grasp Orientation Threshold)
is the maximum deviation of the TCP's $z$ axis at the grasp point from the $z$ axis of the TCP's preferred orientation in degrees. Only grasp points which are within this threshold are returned. When set to zero, any deviations are valid.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_487|><|start_chunk_488|>
## API version 2

PUT http://<host>/api/v2/pipelines/<0,1,2,3>/nodes/rc_itempick/parameters?grasp_filter_ ...orientation_threshold=<value>
<|end_chunk_488|><|start_chunk_489|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/parameters?grasp_filter_orientation_ ...threshold=<value>
<|end_chunk_489|><|start_chunk_490|>
### Page 113
allow_any_grasp_z_rotation (Allow Any Grasp Z Rotation)

If set to true, the returned grasps are no longer forced to have their $x$ axes aligned with the maximum elongation of the graspable ellipse, but can have any rotation around the $z$ axis. The returned max suction surface length and max suction surface width will be equal and correspond to the shortest diameter of the largest graspable ellipse. This parameter enables the robot to get more options for grasping objects, especially in scenes where collisions can occur. However, in case of UNKNOWN item models, since the grasp is no longer aligned with the graspable ellipse, the correct orientation for placing the object must be determined by other means.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_490|><|start_chunk_491|>
 API version 2 

PUT http://<host>/api/v2/pipelines/<0,1,2,3>/nodes/rc_itempick/parameters?allow_any_
...grasp_z_rotation=<value>
<|end_chunk_491|><|start_chunk_492|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/parameters?allow_any_grasp_z_rotation= ...<value>
<|end_chunk_492|><|start_chunk_493|>
### 6.4.4.6 Status values

The rc_itempick node reports the following status values:
Table 6.29: The rc_itempick node's status values

| Name | Description |
| :-- | :-- |
| data_acquisition_time | Time in seconds required by the last active service to acquire <br> images |
| grasp_computation_time | Processing time of the last grasp computation in seconds |
| last_timestamp_processed | The timestamp of the last processed dataset |
| load_carrier_detection_time | Processing time of the last load carrier detection in seconds |
| processing_time | Processing time of the last detection (including load carrier <br> detection) in seconds |
| state | The current state of the rc_itempick node |

The reported state can take one of the following values.
Table 6.30: Possible states of the ItemPick module

| State name | Description |
| :-- | :-- |
| IDLE | The module is idle. |
| RUNNING | The module is running and ready for load carrier detection and grasp computation. |
| FATAL | A fatal error has occurred. |
<|end_chunk_493|><|start_chunk_494|>
### 6.4.4.7 Services

The user can explore and call the rc_itempick node's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1).

The ItemPick module offers the following services.
<|end_chunk_494|><|start_chunk_495|>
### Page 114<|end_chunk_495|><|start_chunk_496|>
 compute_grasps 

Triggers the computation of grasping poses for a suction device as described in Computation of grasps (Section 6.4.4.2).
<|end_chunk_496|><|start_chunk_497|>
## Details

This service can be called as follows.
<|end_chunk_497|><|start_chunk_498|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/compute_grasps
<|end_chunk_498|><|start_chunk_499|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/services/compute_grasps
<|end_chunk_499|><|start_chunk_500|>
## Request

Required arguments:
pose_frame: see Hand-eye calibration (Section 6.4.4.4).
suction_surface_length: length of the suction device grasping surface.
suction_surface_width: width of the suction device grasping surface.
Potentially required arguments:
robot_pose: see Hand-eye calibration (Section 6.4.4.4).
Optional arguments:
load_carrier_id: ID of the load carrier which contains the items to be grasped.
load_carrier_compartment: compartment inside the load carrier where to compute grasps (see Load carrier compartments, Section 6.6.1.3).
region_of_interest_id: if load_carrier_id is set, ID of the 3D region of interest where to search for the load carriers. Otherwise, ID of the 3D region of interest where to compute grasps.
item_models: list of items to be detected. In case of ItemPick, currently only a single item model of type UNKNOWN with minimum and maximum dimensions is supported, with the minimum dimensions strictly smaller than the maximum dimensions.
collision_detection: see Collision checking within other modules (Section 6.5.2.2).

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
    "collision_detection": {
        "gripper_id": "string",
        "pre_grasp_offset": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "item_models": [
        {
            "type": "string",
            "unknown": {
                "max_dimensions": {
```
<|end_chunk_500|><|start_chunk_501|>
### Page 115
![img-38.jpeg](img-38.jpeg)
<|end_chunk_501|><|start_chunk_502|>
 Response 

load_carriers: list of detected load carriers.
grasps: sorted list of suction grasps.
items: sorted list of items corresponding to the returned grasps. In case of ItemPick, this list is always empty.
timestamp: timestamp of the image set the detection ran on.
<|end_chunk_502|><|start_chunk_503|>
### Page 116
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "compute_grasps",
    "response": {
        "grasps": [
            {
            "item_uuid": "string",
            "max_suction_surface_length": "float64",
            "max_suction_surface_width": "float64",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "pose_frame": "string",
            "quality": "float64",
            "timestamp": {
                "nsec": "int32",
                "sec": "int32"
            },
            "type": "string",
            "uuid": "string"
        }
    ],
    "items": [
        {
            "bounding_box": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "grasp_uuids": [
                "string"
            ],
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "pose_frame": "string",
            "template_id": "string",
            "timestamp": {
                "nsec": "int32",
                "sec": "int32"
```
<|end_chunk_503|><|start_chunk_504|>
### Page 117
(continued from previous page)

```
    },
    "type": "string",
    "uuid": "string",
    "view_name": "string",
    "view_pose_set": "bool",
    "view_uuid": "string"
    }
    ],
    "load_carriers": [
        {
            "height_open_side": "float64",
            "id": "string",
            "inner_dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "outer_dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "overfilled": "bool",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    }
            },
            "pose_frame": "string",
            "rim_ledge": {
                    "x": "float64",
                    "y": "float64"
            },
            "rim_step_height": "float64",
            "rim_thickness": {
                    "x": "float64",
                    "y": "float64"
            },
            "type": "string"
        }
    ],
    "return_code": {
        "message": "string",
        "value": "int16"
    },
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    }
    }
}
```
<|end_chunk_504|><|start_chunk_505|>
### Page 118<|end_chunk_505|><|start_chunk_506|>
 set_preferred_orientation 

Persistently stores the preferred orientation of the TCP to compute the reachability of the grasps, which is used for filtering and the grasps returned by the compute_grasps service (see Setting the preferred orientation of the TCP, Section 6.4.4.3).
<|end_chunk_506|><|start_chunk_507|>
## Details

This service can be called as follows.
<|end_chunk_507|><|start_chunk_508|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/set_preferred_ ...orientation
<|end_chunk_508|><|start_chunk_509|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/services/set_preferred_orientation
<|end_chunk_509|><|start_chunk_510|>
## Request

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string"
    }
}
```

<|end_chunk_510|><|start_chunk_511|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_preferred_orientation",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_preferred_orientation

Returns the preferred orientation of the TCP to compute the reachability of the grasps, which is used for filtering the grasps returned by the compute_grasps service (see Setting the preferred orientation of the TCP, Section 6.4.4.3).
<|end_chunk_511|><|start_chunk_512|>
## Details

This service can be called as follows.
<|end_chunk_512|><|start_chunk_513|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/get_preferred_ ...orientation
<|end_chunk_513|><|start_chunk_514|>
### Page 119<|end_chunk_514|><|start_chunk_515|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_itempick/services/get_preferred_orientation
<|end_chunk_515|><|start_chunk_516|>
## Request

This service has no arguments.
<|end_chunk_516|><|start_chunk_517|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_preferred_orientation",
    "response": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string",
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

set_sorting_strategies

Persistently stores the sorting strategy for sorting the grasps returned by the compute_grasps service (see Computation of grasps, Section 6.4.4.2).
<|end_chunk_517|><|start_chunk_518|>
## Details

This service can be called as follows.
<|end_chunk_518|><|start_chunk_519|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/set_sorting_strategies
<|end_chunk_519|><|start_chunk_520|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/services/set_sorting_strategies
<|end_chunk_520|><|start_chunk_521|>
## Request

Only one strategy may have a weight greater than 0 . If all weight values are set to 0 , the module will use the default sorting strategy.
If the weight for direction is set, the vector must contain the direction vector and pose_frame must be either camera or external.

If the weight for distance_to_point is set, point must contain the sorting point and pose_frame must be either camera or external.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "direction": {
            "pose_frame": "string",
            "vector": {
```
<|end_chunk_521|><|start_chunk_522|>
### Page 120
(continued from previous page)

```
            "x": "float64",
            "y": "float64",
            "z": "float64"
        ),
        "weight": "float64"
    },
    "distance_to_point": {
        "farthest_first": "bool",
        "point": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string",
        "weight": "float64"
    },
    "gravity": {
        "weight": "float64"
    },
    "surface_area": {
        "weight": "float64"
    }
    }
}
```

<|end_chunk_522|><|start_chunk_523|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_sorting_strategies",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_sorting_strategies

Returns the sorting strategy for sorting the grasps returned by the compute-grasps service (see Computation of grasps, Section 6.4.4.2).
<|end_chunk_523|><|start_chunk_524|>
## Details

This service can be called as follows.
<|end_chunk_524|><|start_chunk_525|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/get_sorting_strategies
<|end_chunk_525|><|start_chunk_526|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/services/get_sorting_strategies
<|end_chunk_526|><|start_chunk_527|>
## Request

This service has no arguments.
<|end_chunk_527|><|start_chunk_528|>
## Re
<|end_chunk_528|><|start_chunk_529|>
## Re
<|end_chunk_529|><|start_chunk_530|>
### Page 121
All weight values are 0 when the module uses the default sorting strategy.
The definition for the response with corresponding datatypes is:

```
{
    "name": "get_sorting_strategies",
    "response": {
        "direction": {
            "pose_frame": "string",
            "vector": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "weight": "float64"
        },
        "distance_to_point": {
            "farthest_first": "bool",
            "point": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "pose_frame": "string",
            "weight": "float64"
        },
        "gravity": {
            "weight": "float64"
        },
        "return_code": {
            "message": "string",
            "value": "int16"
        },
        "surface_area": {
            "weight": "float64"
        }
    }
}
```

start

Starts the module. If the command is accepted, the module moves to state RUNNING.
<|end_chunk_530|><|start_chunk_531|>
 Details 

This service can be called as follows.
<|end_chunk_531|><|start_chunk_532|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/start
<|end_chunk_532|><|start_chunk_533|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/services/start
<|end_chunk_533|><|start_chunk_534|>
## Request

This service has no arguments.
<|end_chunk_534|><|start_chunk_535|>
## Response

The current_state value in the service response may differ from RUNNING if the state transition is still in process when the service returns.
<|end_chunk_535|><|start_chunk_536|>
### Page 122
The definition for the response with corresponding datatypes is:

```
{
    "name": "start",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
stop
```

Stops the module. If the command is accepted, the module moves to state IDLE.
<|end_chunk_536|><|start_chunk_537|>
 Details 

This service can be called as follows.
<|end_chunk_537|><|start_chunk_538|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/stop
<|end_chunk_538|><|start_chunk_539|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/services/stop
<|end_chunk_539|><|start_chunk_540|>
## Request

This service has no arguments.
<|end_chunk_540|><|start_chunk_541|>
## Response

The current_state value in the service response may differ from IDLE if the state transition is still in process when the service returns.

The definition for the response with corresponding datatypes is:

```
{
    "name": "stop",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

reset_defaults

Resets all parameters of the module to its default values, as listed in above table. Also resets sorting strategies.
<|end_chunk_541|><|start_chunk_542|>
## Details

This service can be called as follows.
<|end_chunk_542|><|start_chunk_543|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_itempick/services/reset_defaults
<|end_chunk_543|><|start_chunk_544|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_itempick/services/reset_defaults
<|end_chunk_544|><|start_chunk_545|>
### Page 123<|end_chunk_545|><|start_chunk_546|>
 Request 

This service has no arguments.
<|end_chunk_546|><|start_chunk_547|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_547|><|start_chunk_548|>
### 6.4.4.8 Return codes

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.

The following table contains a list of common codes:
Table 6.31: Return codes of the ItemPick services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -3 | An internal timeout occurred, e.g. during box detection if the given dimension range is too <br> large |
| -4 | Data acquisition took longer than allowed |
| -8 | The template has been deleted during detection. |
| -10 | New element could not be added as the maximum storage capacity of load carriers, regions <br> of interest or template has been exceeded |
| -11 | Sensor not connected, not supported or not ready |
| -200 | Fatal internal error |
| -301 | More than one item model provided to the compute_grasps service |
| 10 | The maximum storage capacity of load carriers, regions of interest or templates has been <br> reached |
| 11 | An existent persistent model was overwritten by the call to set._load._carrier or <br> set._region_of_interest |
| 100 | The requested load carriers were not detected in the scene |
| 101 | No valid surfaces or grasps were found in the scene |
| 102 | The detected load carrier is empty |
| 103 | All computed grasps are in collision with the load carrier |
| 112 | Rejected detections of one or more clusters, because min_cluster_coverage was not <br> reached. |
| 300 | A valid robot_pose was provided as argument but it is not required |
| 999 | Additional hints for application development |
<|end_chunk_548|><|start_chunk_549|>
### Page 124<|end_chunk_549|><|start_chunk_550|>
 6.4.5 BoxPick 
<|end_chunk_550|><|start_chunk_551|>
### 6.4.5.1 Introduction

The BoxPick module provides an out-of-the-box perception solution for robotic pick-and-place applications. It detects rectangular surfaces and determines their position, orientation and size for grasping. With the +Match extension, BoxPick can be used to detect textured rectangles with consistent orientations, such as printed product packaging, labels, brochures or books.

In addition, the module offers:

- A dedicated page on the rc_visard Web GUI (Section 7.1) for easy setup, configuration, testing, and application tuning.
- The definition of regions of interest to select relevant volumes in the scene (see RoiDB, Section 6.6.2).
- A load carrier detection functionality for bin-picking applications (see LoadCarrier, Section 6.4.2), to provide grasps for items inside a bin only.
- The definition of compartments inside a load carrier to provide grasps for specific volumes of the bin only.
- Support for static and robot-mounted cameras and optional integration with the Hand-eye calibration (Section 6.5.1) module, to provide grasps in the user-configured external reference frame.
- A quality value associated to each suggested grasp and related to the flatness of the grasping surface.
- Selection of a sorting strategy to sort the returned grasps.
- 3D visualization of the detection results with grasp points and gripper animations in the Web GUI.

Note: In this chapter, cluster and surface are used as synonyms and identify a set of points (or pixels) with defined geometrical properties.

The module is an optional on-board module of the $r c \_v i s a r d$ and requires a separate BoxPick license (Section 8.7) to be purchased. The +Match extension requires an extra license.
<|end_chunk_551|><|start_chunk_552|>
### 6.4.5.2 Detection of items

There are two different types of models for the rectangles to be detected by the BoxPick module.
Per default, BoxPick only supports item_models of type RECTANGLE. With the +Match extension, also item models of type TEXTURED_BOX can be detected. The detection of the different item model types is described below.
Optionally, further information can be given to the BoxPick module:

- The ID of the load carrier which contains the items to be detected.
- A compartment inside the load carrier where to detect items.
- The ID of the region of interest where to search for the load carriers if a load carrier is set. Otherwise, the ID of the region of interest where to search for the items.
- The current robot pose in case the camera is mounted on the robot and the chosen coordinate frame for the poses is external or the chosen region of interest is defined in the external frame.
The returned pose of a detected item is the pose of the center of the detected rectangle in the desired reference frame (pose_frame), with its $z$ axis pointing towards the camera and the $x$ axis aligned with the long side of the item. This pose has a $180^{\circ}$ rotation ambiguity around the $z$ axis, which can be resolved by using the +Match extension with a TEXTURED_BOX item model. Each detected item includes a uuid (Universally Unique Identifier) and the timestamp of the oldest image that was used to detect it.
<|end_chunk_552|><|start_chunk_553|>
### Page 125<|end_chunk_553|><|start_chunk_554|>
 Detection of items of type RECTANGLE 

BoxPick supports multiple item_models of type RECTANGLE. Each item model is defined by its minimum and maximum size, with the minimum dimensions strictly smaller than the maximum dimensions. The dimensions should be given fairly accurately to avoid misdetections, while still considering a certain tolerance to account for possible production variations and measurement inaccuracies.

The detection of the rectangles runs in several steps. First, the point cloud is segmented into preferably plane clusters. Then, straight line segments are detected in the 2D images and projected onto the corresponding clusters. The clusters and the detected lines are visualized in the "Intermediate Result" visualization on the Web GUI's BoxPick page. Finally, for each cluster, the set of rectangles best fitting to the detected line segments is extracted.
<|end_chunk_554|><|start_chunk_555|>
## Detection of items of type TEXTURED_BOX (BoxPick+Match)

With the +Match extension, BoxPick additionally supports item_models of type TEXTURED_BOX. When this item model type is used, only one item model can be given for each request.

The TEXTURED_BOX item model type should be used to detect multiple rectangles that have the same texture, i.e. the same look or print, such as printed product packaging, labels, brochures or books. It is required that for all objects the texture is at the same position with respect to the object geometry. Furthermore, the texture should not be repetitive.

A TEXTURED_BOX item is defined by the item's exact dimensions $x, y$ and $z$ (only $z$ is allowed to be 0 ) with a tolerance dimensions_tolerance_m that indicates, how much the detected dimensions are allowed to deviate from the given dimensions. By default, a tolerance of 0.01 m is assumed. Furthermore, a template_id must be given, which will be used to refer to the specified dimensions and the textures of the detected rectangles. Additionally, the maximum possible deformation of the items max_deformation_m can be given in meters (default 0.004 m ), to account for rigid or more flexible objects.

If a template_id is used for the first time, BoxPick will run the detection of rectangles as for the item model type RECTANGLE, and use the given dimensions and tolerance to specify the dimensions range. If the $z$ dimension is given in addition to $x$ and $y$, rectangles with all possible combinations of the three dimensions will be detected. From the detected rectangles, so-called views are created, which contain the shape and the image intensity values of the rectangles, and are stored in a newly created template with the given template_id. The views are created iteratively: Starting from the detected rectangle with the highest score, a view is created and then used to detect more rectangles with the same texture. Then, all remaining clusters are used to detect further rectangles by the given dimensions range and again a view is created from the best rectangle and used for further detections. Each template can store up to 10 different views, for example corresponding to different types of the same product packaging. Each view will be assigned a unique ID (view_uuid) and all rectangle items with a matching texture will be assigned the same view_uuid. That also means that all items with the same view_uuid will have consistent orientations, because the orientation of each item is aligned with its texture. The views can be displayed, deleted and the orientation of each view can be set via the Web GUI (Section 7.1) by clicking on the template or its edit symbol in the template list. Each detected item contains a field view_pose_set indicating whether the orientation of the item's view was explicitly set or is still unset at its original random state, which has a $180^{\circ}$ ambiguity. Additionally, a user-defined name can be set for each view, that is returned along with the view_uuid for all items and allows an easier identification of a specific view. The type of a returned item with a view_uuid will be TEXTURED_RECTANGLE.

If the template with the given template_id already exists, the existing views will be used to detect rectangles based on their texture. If additional rectangles are found with matching dimensions, but different texture, new views will be generated and added to the template. When the maximum number of views is reached, views that are matched only rarely will be deleted so that newly generated views can be added to the template and the template is kept up-to-date. To prevent a template from being updated, automatic view updating can be disabled and enabled for each template in the Web GUI by clicking on the template or the edit symbol in the template list. The dimension tolerance and the maximum deformation can also be changed there for each template. The maximum deformation determines
<|end_chunk_555|><|start_chunk_556|>
### Page 126
the tolerance for the texture matching, representing possible shifts within the texture, e.g. caused by deformations of the object surface. For rigid objects the max_deformation_m should be set to a low value in meters to ensure accurate matching.
The template's dimensions can only be specified when creating a new template. Once the template is generated, the dimensions cannot be changed and do not need to be given in the detect request. If the dimensions are still given in the request, they must match the existing dimensions in the template. However, the dimensions_tolerance_m and max_deformation_m can be set differently in every detect request and their values will also be updated in the stored template.
<|end_chunk_556|><|start_chunk_557|>
 6.4.5.3 Computation of grasps 

The BoxPick module offers a service for computing grasps for suction grippers. The gripper is defined by its suction surface length and width.
The grasps are computed on the detected rectangular items (see Detection of items, Section 6.4.5.2).
Optionally, further information can be given to the module in a grasp computation request:

- The ID of the load carrier which contains the items to be grasped.
- A compartment inside the load carrier where to compute grasps (see Load carrier compartments, Section 6.6.1.3).
- The ID of the 3D region of interest where to search for the load carriers if a load carrier is set. Otherwise, the ID of the 3D region of interest where to compute grasps.
- Collision detection information: The ID of the gripper to enable collision checking and optionally a pre-grasp offset to define a pre-grasp position. Details on collision checking are given below in CollisionCheck (Section 6.4.5.5).
A grasp provided by the BoxPick module represents the recommended pose of the TCP (Tool Center Point) of the suction gripper. The grasp type is always set to SUCTION. The computed grasp pose is the center of the biggest ellipse that can be inscribed in each surface. The grasp orientation is a right-handed coordinate system and is defined such that its $z$ axis is normal to the surface pointing inside the object at the grasp position and its $x$ axis is directed along the maximum elongation of the ellipse. Since the $x$ axis can have two possible directions, the one that better fits to the preferred TCP orientation (see Setting the preferred orientation of the TCP, Section 6.4.5.4) is selected. If the run-time parameter allow_any_grasp_z_rotation is set to true, the $x$ axis will not be forced to be aligned with the maximum elongation of the graspable ellipse, but can have any rotation around the $z$ axis. In this case, the returned grasp will have the orientation that best fits to the preferred TCP orientation and is collision free, if collision checking is enabled.
![img-39.jpeg](img-39.jpeg)

Fig. 6.16: Illustration of a suction grasp with coordinate system and ellipse representing the maximum suction surface

Each grasp includes the dimensions of the maximum suction surface available, modelled as an ellipse of axes max_suction_surface_length and max_suction_surface_width. The user is enabled to filter grasps by specifying the minimum suction surface required by the suction device in use. If
<|end_chunk_557|><|start_chunk_558|>
### Page 127
the run-time parameter allow_any_grasp_z_rotation is set to true, max_suction_surface_length and max_suction_surface_width will be equal and correspond to the shortest axis of the largest graspable ellipse.

In the BoxPick module, the grasp position corresponds to the center of the detected rectangle. When BoxPick is called with item models of type RECTANGLE, the dimensions of the maximum suction surface available matches the estimated rectangle dimensions. In this case, detected rectangles with missing data or occlusions by other objects for more than $15 \%$ of their surface do not get an associated grasp.
When BoxPick is called with item models of type TEXTURED_BOX, grasps can also be computed on partly occluded boxes. The maximum suction surface available matches the free surface that is not occluded by other clusters.

Each grasp also includes a quality value, which gives an indication of the flatness of the grasping surface. The quality value varies between 0 and 1, where higher numbers correspond to a flatter reconstructed surface.

The grasp definition is complemented by a uuid (Universally Unique Identifier) and the timestamp of the oldest image that was used to compute the grasp.

Grasp sorting is performed based on the selected sorting strategy. The following sorting strategies are available and can be set in the Web GUI (Section 7.1) or using the set_sorting_strategies service call:

- gravity: highest grasp points along the gravity direction are returned first,
- surface_area: grasp points with the largest surface area are returned first,
- direction: grasp points with the shortest distance along a defined direction vector in a given pose_frame are returned first.
- distance_to_point: grasp points with the shortest or farthest (if farthest_first is true) distance from a point in a given pose_frame are returned first.

If no sorting strategy is set or default sorting is chosen in the Web GUI, sorting is done based on a combination of gravity and surface_area.
<|end_chunk_558|><|start_chunk_559|>
 6.4.5.4 Setting the preferred orientation of the TCP 

The BoxPick module determines the reachability of grasp points based on the preferred orientation of the TCP. The preferred orientation can be set via the set_preferred_orientation service or on the BoxPick page in the Web GUI. The resulting direction of the TCP's z axis is used to reject grasps which cannot be reached by the gripper. Furthermore, the preferred orientation is used to select one grasp of several possible symmetries that is best reachable for the robot.

The preferred orientation can be set in the camera coordinate frame or in the external coordinate frame, in case a hand-eye calibration is available. If the preferred orientation is specified in the external coordinate frame and the sensor is robot mounted, the current robot pose has to be given to each object detection call. If no preferred orientation is set, the orientation of the left camera (see Coordinate frames ) will be used as the preferred orientation of the TCP.used.
<|end_chunk_559|><|start_chunk_560|>
### 6.4.5.5 Interaction with other modules

Internally, the BoxPick module depends on, and interacts with other on-board modules as listed below.
Note: All changes and configuration updates to these modules will affect the performance of the BoxPick module.
<|end_chunk_560|><|start_chunk_561|>
## Camera and depth data

The BoxPick module makes internally use of the following data:
<|end_chunk_561|><|start_chunk_562|>
### Page 128
- Rectified images from the Camera module (rc_camera, Section 6.1)
- Disparity, error, and confidence images from the Stereo matching module (rc_stereomatching, Section 6.2)

All processed images are guaranteed to be captured after the module trigger time.
<|end_chunk_562|><|start_chunk_563|>
 IO and Projector Control 

In case the $r c \_v i s a r d$ is used in conjunction with an external random dot projector and the IO and Projector Control module (rc_iocontrol, Section 6.5.4), it is recommended to connect the projector to GPIO Out 1 and set the stereo-camera module's acquisition mode to SingleFrameOut1 (see Stereo matching parameters, Section 6.2.1), so that on each image acquisition trigger an image with and without projector pattern is acquired.

Alternatively, the output mode for the GPIO output in use should be set to ExposureAlternateActive (see Description of run-time parameters, Section 6.5.4.1).
In either case, the Auto Exposure Mode exp_auto_mode should be set to AdaptiveOut1 to optimize the exposure of both images.
<|end_chunk_563|><|start_chunk_564|>
## Hand-eye calibration

In case the camera has been calibrated to a robot, the BoxPick module can automatically provide poses in the robot coordinate frame. For the BoxPick node's Services (Section 6.4.5.8), the frame of the output poses can be controlled with the pose_frame argument.

Two different pose_frame values can be chosen:

1. Camera frame (camera). All poses provided by the modules are in the camera frame, and no prior knowledge about the pose of the camera in the environment is required. This means that the configured regions of interest and load carriers move with the camera. It is the user's responsibility to update the configured poses if the camera frame moves (e.g. with a robot-mounted camera).
2. External frame (external). All poses provided by the modules are in the external frame, configured by the user during the hand-eye calibration process. The module relies on the onboard Hand-eye calibration module (Section 6.5.1) to retrieve the sensor mounting (static or robot mounted) and the hand-eye transformation. If the mounting is static, no further information is needed. If the sensor is robot-mounted, the robot_pose is required to transform poses to and from the external frame.

Note: If no hand-eye calibration is available, all pose_frame values should be set to camera.

All pose_frame values that are not camera or external are rejected.
If the sensor is robot-mounted, the current robot_pose has to be provided depending on the value of pose_frame and the definition of the sorting direction or sorting point:

- If pose_frame is set to external, providing the robot pose is obligatory.
- If the sorting direction is defined in external, providing the robot pose is obligatory.
- If the distance-to-point sorting strategy is defined in external, providing the robot pose is obligatory.
- In all other cases, providing the robot pose is optional.

<|end_chunk_564|><|start_chunk_565|>
## LoadCarrier

The BoxPick module uses the load carrier detection functionality provided by the LoadCarrier module (rc_load_carrier, Section 6.4.2), with the run-time parameters specified for this module. However,
<|end_chunk_565|><|start_chunk_566|>
### Page 129
only one load carrier will be returned and used in case multiple matching load carriers could be found in the scene. In case multiple load carriers of the same type are visible, a 3D region of interest should be set to ensure that always the same load carrier is used for the BoxPick module.

The load carrier is used to filter false detections when BoxPick is triggered with an item model of type TEXTURED_BOX and all three dimensions $x, y, z$ are given. In this case, 3D boxes are created internally by adding the missing dimensions to the detected rectangles and only detections corresponding to boxes which are fully inside the detected load carrier are returned.
<|end_chunk_566|><|start_chunk_567|>
 CollisionCheck 

Collision checking can be easily enabled for grasp computation of the BoxPick module by passing the ID of the used gripper and optionally a pre-grasp offset to the compute_grasps service call. The gripper has to be defined in the GripperDB module (see Setting a gripper, Section 6.6.3.2) and details about collision checking are given in Collision checking within other modules (Section 6.5.2.2).

If collision checking is enabled, only grasps which are collision free will be returned. However, the visualization images on the BoxPick page of the Web GUI also show colliding grasp points as black ellipses.

The CollisionCheck module's run-time parameters affect the collision detection as described in CollisionCheck Parameters (Section 6.5.2.3).
<|end_chunk_567|><|start_chunk_568|>
### 6.4.5.6 Parameters

The BoxPick module is called rc_boxpick in the REST-API and is represented in the Web GUI (Section 7.1) under Modules $\rightarrow$ BoxPick. The user can explore and configure the rc_boxpick module's run-time parameters, e.g. for development and testing, using the Web GUI or the REST-API interface (Section 7.3).
<|end_chunk_568|><|start_chunk_569|>
## Parameter overview

This module offers the following run-time parameters:
<|end_chunk_569|><|start_chunk_570|>
### Page 130
Table 6.32: The rc_boxpick module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :--: | :--: | :--: | :--: | :--: | :--: |
| allow_any_grasp_z_rotation | bool | false | true | false | Whether the grasps are allowed to have arbitrary rotation instead being aligned with the major axis of the graspable ellipse |
| allow_untextured_detections | bool | false | true | false | Whether to return also untextured detections in case a textured box was given |
| cluster_max_curvature | float64 | 0.005 | 0.5 | 0.11 | Maximum curvature allowed within one cluster. The smaller this value, the more clusters will be split apart. |
| clustering_discontinuity_factor | float64 | 0.1 | 5.0 | 1.0 | Factor used to discriminate depth discontinuities within a patch. The smaller this value, the more clusters will be split apart. |
| clustering_max_surface_rmse | float64 | 0.0005 | 0.01 | 0.004 | Maximum root-mean-square error (RMSE) in meters of points belonging to a surface |
| grasp_filter_orientation_threshold | float64 | 0.0 | 180.0 | 45.0 | Maximum allowed orientation change between grasp and preferred orientation in degrees |
| line_sensitivity | float64 | 0.1 | 1.0 | 0.1 | Sensitivity of the line detector |
| manual_line_sensitivity | bool | false | true | false | Indicates whether the user-defined line sensitivity should be used or the automatic one |
| max_grasps | int32 | 1 | 20 | 5 | Maximum number of provided grasps |
| min_cluster_coverage | float64 | 0.0 | 0.99 | 0.0 | Gives the minimal ratio of points per cluster that must be covered with detected items. |
| mode | string | - | - | Unconstrained | Mode of the rectangle detection: [Unconstrained, PackedGridLayout, PackedLayers] |
| prefer_splits | bool | false | true | false | Indicates whether rectangles are split into smaller ones when possible |
<|end_chunk_570|><|start_chunk_571|>
 Description of run-time parameters 

Each run-time parameter is represented by a row on the Web GUI's BoxPick page. The name in the Web GUI is given in brackets behind the parameter name and the parameters are listed in the order they appear in the Web GUI:
max_grasps (Maximum Grasps)
sets the maximum number of provided grasps.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_571|><|start_chunk_572|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?max_grasps= $\ldots<$ value $>$
<|end_chunk_572|><|start_chunk_573|>
## API version 1 (deprecated)
<|end_chunk_573|><|start_chunk_574|>
### Page 131
PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?max_grasps=<value>
cluster_max_curvature (Cluster Maximum Curvature)
is the maximum curvature allowed within one cluster. The smaller this value, the more clusters will be split apart.

Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?cluster_ ...max_curvature=<value>
<|end_chunk_574|><|start_chunk_575|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?cluster_max_curvature=<value>
clustering_discontinuity_factor (Discontinuity Factor)
is the factor used to discriminate depth discontinuities within a patch. The smaller this value, the more clusters will be split apart.

Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?clustering_ ...discontinuity_factor=<value>
<|end_chunk_575|><|start_chunk_576|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?clustering_discontinuity_factor= ...<value>
clustering_max_surface_rmse (Maximum Surface RMSE)
is the maximum root-mean-square error (RMSE) in meters of points belonging to a surface.

Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?clustering_ ...max_surface_rmse=<value>
<|end_chunk_576|><|start_chunk_577|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?clustering_max_surface_rmse= ...<value>
mode (Mode)
determines the mode of the rectangle detection. Possible values are Unconstrained, PackedGridLayout and PackedLayers. In PackedGridLayout mode, rectangles of a cluster are detected in a dense grid pattern. In
<|end_chunk_577|><|start_chunk_578|>
### Page 132
PackedLayers mode, boxes are assumed to form layers and box detection will start searching for items at the cluster corners. Use this mode in de-palletizing applications. In Unconstrained mode (default), rectangles are detected without posing any constraints on their relative locations or their positions in the segmented cluster. Fig. 6.17 illustrates the modes for different scenarios.
![img-40.jpeg](img-40.jpeg)

Fig. 6.17: Illustration of appropriate BoxPick modes for different scenes. Modes marked with yellow are applicable but not recommended for the corresponding scene. The gray areas indicate the rectangles to be detected.

Via the REST-API, this parameter can be set as follows.
API version 2
PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?mode= ...<value>

API version 1 (deprecated)
PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?mode=<value>
manual_line_sensitivity (Manual Line Sensitivity)
determines whether the user-defined line sensitivity should be used to extract the lines for rectangle detection. If this parameter is set to true, the user-defined line_sensitivity value will be used. If this parameter is set to false, automatic line sensitivity will be used. This parameter should be set to true when automatic line sensitivity does not give enough lines at the box boundaries so that boxes cannot be detected. The detected line segments are visualized in the "Intermediate Result" visualization on the Web GUI's BoxPick page.
<|end_chunk_578|><|start_chunk_579|>
### Page 133
Via the REST-API, this parameter can be set as follows.
<|end_chunk_579|><|start_chunk_580|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?manual_...line_sensitivity=<value>
<|end_chunk_580|><|start_chunk_581|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?manual_line_sensitivity=<value>
<|end_chunk_581|><|start_chunk_582|>
## line_sensitivity (Line Sensitivity)

determines the line sensitivity for extracting the lines for rectangle detection, if the parameter manual_line_sensitivity is set to true. Otherwise, the value of this parameter has no effect on the rectangle detection. Higher values give more line segments, but also increase the runtime of the box detection. This parameter should be increased when boxes cannot be detected because their boundary edges are not detected. The detected line segments are visualized in the "Intermediate Result" visualization on the Web GUI's BoxPick page.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_582|><|start_chunk_583|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?line_...sensitivity=<value>
<|end_chunk_583|><|start_chunk_584|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?line_sensitivity=<value>
prefer_splits (Prefer Splits)
determines whether rectangles should be split into smaller ones if the smaller ones also match the given item models. This parameter should be set to true for packed box layouts in which the given item models would also match a rectangle of the size of two adjoining boxes. If this parameter is set to false, the larger rectangles will be preferred in these cases.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_584|><|start_chunk_585|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?prefer_...splits=<value>
<|end_chunk_585|><|start_chunk_586|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?prefer_splits=<value>
min_cluster_coverage (Minimum Cluster Coverage)
determines which ratio of each segmented cluster must be covered with rectangle detections to consider the detections to be valid. If the minimum cluster coverage is not reached for a cluster, no rectangle detections will be returned for this cluster and a warning will be given. This parameter should be used to verify that all items on a layer in a de-palletizing scenario are detected.
<|end_chunk_586|><|start_chunk_587|>
### Page 134
Via the REST-API, this parameter can be set as follows.
<|end_chunk_587|><|start_chunk_588|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?min_ ...cluster_coverage=<value>
<|end_chunk_588|><|start_chunk_589|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?min_cluster_coverage=<value>
allow_untextured_detections (Only for BoxPick+Match, Allow Untextured Detections)
enables returning all rectangles matching the given template dimensions, even when they cannot be matched to an existing view or when they do not have enough texture to create a new view from them. This parameter is only used when item models of type TEXTURED...BOX are detected. Disabling this parameter leads to faster detections when used with a template for which the automatic view updating is disabled.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_589|><|start_chunk_590|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/parameters/parameters?allow_ ...untextured_detections=<value>
<|end_chunk_590|><|start_chunk_591|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?allow_untextured_detections= ...<value>
grasp_filter_orientation_threshold (Grasp Orientation Threshold)
is the maximum deviation of the TCP's $z$ axis at the grasp point from the $z$ axis of the TCP's preferred orientation in degrees. Only grasp points which are within this threshold are returned. When set to zero, any deviations are valid.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_591|><|start_chunk_592|>
## API version 2

PUT http://<host>/api/v2/pipelines/<0,1,2,3>/nodes/rc_boxpick/parameters?grasp_filter_ ...orientation_threshold=<value>
<|end_chunk_592|><|start_chunk_593|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?grasp_filter_orientation_ ...threshold=<value>
allow_any_grasp_z_rotation (Allow Any Grasp Z Rotation)

If set to true, the returned grasps are no longer forced to have their $x$ axes aligned with the maximum elongation of the graspable ellipse, but can have any rotation around the $z$ axis. The returned max suction...surface length and max suction...surface...width will be equal and correspond to the shortest diameter of the largest graspable ellipse. This parameter enables the robot to get
<|end_chunk_593|><|start_chunk_594|>
### Page 135
more options for grasping objects, especially in scenes where collisions can occur. However, since the grasp is no longer aligned with the graspable ellipse, the correct orientation for placing the object must be determined from the corresponding item's pose.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_594|><|start_chunk_595|>
 API version 2 

PUT http://<host>/api/v2/pipelines/ $<0,1,2,3>/$ nodes/rc_boxpick/parameters?allow_any_ grasp_z_rotation=<value>
<|end_chunk_595|><|start_chunk_596|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/parameters?allow_any_grasp_z_rotation=<value>
<|end_chunk_596|><|start_chunk_597|>
### 6.4.5.7 Status values

The rc_boxpick module reports the following status values:
Table 6.33: The rc_boxpick module's status values

| Name | Description |
| :-- | :-- |
| data_acquisition_time | Time in seconds required by the last active service to acquire <br> images |
| grasp_computation_time | Processing time of the last grasp computation in seconds |
| last_timestamp_processed | The timestamp of the last processed dataset |
| load_carrier_detection_time | Processing time of the last load carrier detection in seconds |
| processing_time | Processing time of the last detection (including load carrier <br> detection) in seconds |
| state | The current state of the rc_boxpick node |

The reported state can take one of the following values.
Table 6.34: Possible states of the BoxPick module

| State name | Description |
| :-- | :-- |
| IDLE | The module is idle. |
| RUNNING | The module is running and ready for load carrier detection and grasp computation. |
| FATAL | A fatal error has occurred. |
<|end_chunk_597|><|start_chunk_598|>
### 6.4.5.8 Services

The user can explore and call the rc_boxpick module's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1).
The BoxPick module offers the following services.
detect_items

Triggers the detection of rectangles as described in Detection of items (Section 6.4.5.2).
<|end_chunk_598|><|start_chunk_599|>
## Details

This service can be called as follows.
<|end_chunk_599|><|start_chunk_600|>
## API version 2
<|end_chunk_600|><|start_chunk_601|>
### Page 136
PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/detect_items
<|end_chunk_601|><|start_chunk_602|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_boxpick/services/detect_items
<|end_chunk_602|><|start_chunk_603|>
## Request

Required arguments:
pose_frame: see Hand-eye calibration (Section 6.4.5.5).
item_models: list of item models to be detected. The type of the item model must be RECTANGLE or TEXTURED_BOX. For type RECTANGLE, rectangle must be filled, while for TEXTURED_BOX, textured_box must be filled. See Detection of items (Section 6.4.5.2) for a detailed description of the item model types.

Potentially required arguments:
robot posse: see Hand-eye calibration (Section 6.4.5.5).
Optional arguments:
load_carrier_id: ID of the load carrier which contains the items to be detected.
load_carrier compartment: compartment inside the load carrier where to detect items (see Load carrier compartments, Section 6.6.1.3).
region_of_interest_id: if load_carrier_id is set, ID of the 3D region of interest where to search for the load carriers. Otherwise, ID of the 3D region of interest where to search for the items.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "item models": [
            {
            "rectangle": {
                "max_dimensions": {
                    "x": "float64",
                    "y": "float64"
            },
            "min_dimensions": {
                "x": "float64",
                "y": "float64"
            }
            },
            "textured_box": {
                "dimensions": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "dimensions_tolerance_m": "float64",
            "max_deformation_m": "float64",
            "template_id": "string"
            },
            "type": "string"
        }
    ],
    "load_carrier_compartment": {
        "box": {
            "x": "float64",
            "y": "float64",
```
<|end_chunk_603|><|start_chunk_604|>
### Page 137
(continued from previous page)

```
            "z": "float64"
        },
        "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        }
    },
    "load_carrier_id": "string",
    "pose_frame": "string",
    "region_of_interest_id": "string",
    "robot_pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    }
    }
}
```

<|end_chunk_604|><|start_chunk_605|>
 Response 

load_carriers: list of detected load carriers.
items: list of detected rectangles.
timestamp: timestamp of the image set the detection ran on.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "detect_items",
    "response": {
        "items": [
            {
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        }
    }
}
```

<|end_chunk_605|><|start_chunk_606|>
## Response

load_carriers: list of detected load carriers.
items: list of detected rectangles.
timestamp: timestamp of the image set the detection ran on.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "detect_items",
    "response": {
        "items": [
            {
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        }
    }
}
```
<|end_chunk_606|><|start_chunk_607|>
### Page 138
(continued from previous page)

```
        }
    },
    "pose_frame": "string",
    "rectangle": {
        "x": "float64",
        "y": "float64"
    },
    "template_id": "string",
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    },
    "type": "string",
    "uuid": "string",
    "view_name": "string",
    "view_pose_set": "bool",
    "view_uuid": "string"
    }
],
"load_carriers": [
    {
        "height_open_side": "float64",
        "id": "string",
        "inner_dimensions": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
    },
    "outer_dimensions": {
        "x": "float64",
        "y": "float64",
        "z": "float64"
    },
    "overfilled": "bool",
    "pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "pose_frame": "string",
    "rim_ledge": {
        "x": "float64",
        "y": "float64"
    },
    "rim_step_height": "float64",
    "rim_thickness": {
        "x": "float64",
        "y": "float64"
    },
    "type": "string"
    }
],
"return_code": {
```
<|end_chunk_607|><|start_chunk_608|>
### Page 139
(continued from previous page)

```
        "message": "string",
        "value": "int16"
    },
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    }
    }
}
```

compute_grasps

Triggers the detection of rectangles and the computation of grasping poses for the detected rectangles as described in Computation of grasps (Section 6.4.5.3).
<|end_chunk_608|><|start_chunk_609|>
 Details 

This service can be called as follows.
<|end_chunk_609|><|start_chunk_610|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/compute_grasps
<|end_chunk_610|><|start_chunk_611|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/compute_grasps
<|end_chunk_611|><|start_chunk_612|>
## Request

Required arguments:
pose_frame: see Hand-eye calibration (Section 6.4.5.5).
item_models: list of item models to be detected. The type of the item model must be RECTANGLE or TEXTURED_BOX. For type RECTANGLE, rectangle must be filled, while for TEXTURED_BOX, textured_box must be filled. See Detection of items (Section 6.4.5.2) for a detailed description of the item model types.
suction_surface_length: length of the suction device grasping surface.
suction_surface_width: width of the suction device grasping surface.
Potentially required arguments:
robot_pose: see Hand-eye calibration (Section 6.4.5.5).
Optional arguments:
load_carrier_id: ID of the load carrier which contains the items to be grasped.
load_carrier_compartment: compartment inside the load carrier where to compute grasps (see Load carrier compartments, Section 6.6.1.3).
region_of_interest_id: if load_carrier_id is set, ID of the 3D region of interest where to search for the load carriers. Otherwise, ID of the 3D region of interest where to compute grasps.
collision_detection: see Collision checking within other modules (Section 6.5.2.2).

The definition for the request arguments with corresponding datatypes is:
<|end_chunk_612|><|start_chunk_613|>
### Page 140
```
{
    "args": {
        "collision_detection": {
            "gripper_id": "string",
            "pre_grasp_offset": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "item_models": [
        {
            "rectangle": {
                "max_dimensions": {
                    "x": "float64",
                    "y": "float64"
            },
                "min_dimensions": {
                    "x": "float64",
                    "y": "float64"
            }
        },
        "textured_box": {
            "dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
                "dimensions_tolerance_m": "float64",
                "max_deformation_m": "float64",
                "template_id": "string"
            },
            "type": "string"
        }
    ],
    "load_carrier_compartment": {
        "box": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        }
    },
    "load_carrier_id": "string",
    "pose_frame": "string",
    "region_of_interest_id": "string",
    "robot_pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
```
<|end_chunk_613|><|start_chunk_614|>
### Page 141
(continued from previous page)

```
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "suction_surface_length": "float64",
    "suction_surface_width": "float64"
    }
}
```

<|end_chunk_614|><|start_chunk_615|>
 Response 

load_carriers: list of detected load carriers.
grasps: sorted list of suction grasps.
items: list of detected rectangles corresponding to the returned grasps.
timestamp: timestamp of the image set the detection ran on.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "compute_grasps",
    "response": {
        "grasps": [
        {
            "item_uuid": "string",
            "max_suction_surface_length": "float64",
            "max_suction_surface_width": "float64",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
            }
            },
            "pose_frame": "string",
            "quality": "float64",
            "timestamp": {
                    "nsec": "int32",
                    "sec": "int32"
            },
            "type": "string",
            "uuid": "string"
        }
    },
    "items": [
        {
            "grasp_uuids": [
                "string"
```
<|end_chunk_615|><|start_chunk_616|>
### Page 142
(continued from previous page)
],
"pose": {
"orientation": {
"w": "float64",
"x": "float64",
"y": "float64",
"z": "float64"
},
"position": {
"x": "float64",
"y": "float64",
"z": "float64"
}
},
"pose_frame": "string",
"rectangle": {
"x": "float64",
"y": "float64"
},
"template_id": "string",
"timestamp": {
"nsec": "int32",
"sec": "int32"
},
"type": "string",
"uuid": "string",
"view_name": "string",
"view_pose_set": "bool",
"view_uuid": "string"
}
],
"load_carriers": [
{
"height_open_side": "float64",
"id": "string",
"inner_dimensions": {
"x": "float64",
"y": "float64",
"z": "float64"
},
"outer_dimensions": {
"x": "float64",
"y": "float64",
"z": "float64"
},
"overfilled": "bool",
"pose": {
"orientation": {
"w": "float64",
"x": "float64",
"y": "float64",
"z": "float64"
},
"position": {
"x": "float64",
"y": "float64",
"z": "float64"
}
},
"pose_frame": "string",
"rim_ledge": {
<|end_chunk_616|><|start_chunk_617|>
### Page 143
(continued from previous page)

```
            "x": "float64",
            "y": "float64"
            },
            "rim_step_height": "float64",
            "rim_thickness": {
                "x": "float64",
                "y": "float64"
            },
            "type": "string"
        }
    ],
    "return_code": {
        "message": "string",
        "value": "int16"
    },
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    }
    }
}
```

<|end_chunk_617|><|start_chunk_618|>
 set_preferred_orientation 

Persistently stores the preferred orientation of the TCP to compute the reachability of the grasps, which is used for filtering and the grasps returned by the compute_grasps service (see Setting the preferred orientation of the TCP, Section 6.4.5.4).
<|end_chunk_618|><|start_chunk_619|>
## Details

This service can be called as follows.
<|end_chunk_619|><|start_chunk_620|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/set_preferred_ --orientation
<|end_chunk_620|><|start_chunk_621|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/set_preferred_orientation
<|end_chunk_621|><|start_chunk_622|>
## Request

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string"
    }
}
```

<|end_chunk_622|><|start_chunk_623|>
## Response

The definition for the response with corresponding datatypes is:
<|end_chunk_623|><|start_chunk_624|>
### Page 144
```
{
    "name": "set_preferred_orientation",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_preferred_orientation

Returns the preferred orientation of the TCP to compute the reachability of the grasps, which is used for filtering the grasps returned by the compute_grasps service (see Setting the preferred orientation of the TCP, Section 6.4.5.4).
<|end_chunk_624|><|start_chunk_625|>
 Details 

This service can be called as follows.
<|end_chunk_625|><|start_chunk_626|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/get_preferred_ ...orientation
<|end_chunk_626|><|start_chunk_627|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/get_preferred_orientation
<|end_chunk_627|><|start_chunk_628|>
## Request

This service has no arguments.
<|end_chunk_628|><|start_chunk_629|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_preferred_orientation",
    "response": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string",
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

set_sorting_strategies

Persistently stores the sorting strategy for sorting the grasps returned by the compute_grasps service (see Computation of grasps, Section 6.4.5.3).
<|end_chunk_629|><|start_chunk_630|>
## Details

This service can be called as follows.
<|end_chunk_630|><|start_chunk_631|>
### Page 145<|end_chunk_631|><|start_chunk_632|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/set_sorting_strategies
<|end_chunk_632|><|start_chunk_633|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/set_sorting_strategies
<|end_chunk_633|><|start_chunk_634|>
## Request

Only one strategy may have a weight greater than 0 . If all weight values are set to 0 , the module will use the default sorting strategy.

If the weight for direction is set, the vector must contain the direction vector and pose_frame must be either camera or external.

If the weight for distance_to_point is set, point must contain the sorting point and pose_frame must be either camera or external.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "direction": {
            "pose_frame": "string",
            "vector": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "weight": "float64"
        },
        "distance_to_point": {
            "farthest_first": "bool",
            "point": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "pose_frame": "string",
            "weight": "float64"
        },
        "gravity": {
            "weight": "float64"
        },
        "surface_area": {
            "weight": "float64"
        }
    }
}
```

<|end_chunk_634|><|start_chunk_635|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_sorting_strategies",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```
<|end_chunk_635|><|start_chunk_636|>
### Page 146<|end_chunk_636|><|start_chunk_637|>
 get_sorting_strategies 

Returns the sorting strategy for sorting the grasps returned by the compute-grasps service (see Computation of grasps, Section 6.4.5.3).
<|end_chunk_637|><|start_chunk_638|>
## Details

This service can be called as follows.
<|end_chunk_638|><|start_chunk_639|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/get_sorting_strategies
<|end_chunk_639|><|start_chunk_640|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/get_sorting_strategies
<|end_chunk_640|><|start_chunk_641|>
## Request

This service has no arguments.
<|end_chunk_641|><|start_chunk_642|>
## Response

All weight values are 0 when the module uses the default sorting strategy.
The definition for the response with corresponding datatypes is:

```
{
    "name": "get_sorting_strategies",
    "response": {
        "direction": {
            "pose_frame": "string",
            "vector": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "weight": "float64"
    },
    "distance_to_point": {
        "farthest_first": "bool",
        "point": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string",
        "weight": "float64"
    },
    "gravity": {
        "weight": "float64"
    },
    "return_code": {
        "message": "string",
        "value": "int16"
    },
    "surface_area": {
        "weight": "float64"
    }
    }
}
```
<|end_chunk_642|><|start_chunk_643|>
### Page 147<|end_chunk_643|><|start_chunk_644|>
 start 

Starts the module. If the command is accepted, the module moves to state RUNNING.
<|end_chunk_644|><|start_chunk_645|>
## Details

This service can be called as follows.
<|end_chunk_645|><|start_chunk_646|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/start
<|end_chunk_646|><|start_chunk_647|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/start
<|end_chunk_647|><|start_chunk_648|>
## Request

This service has no arguments.
<|end_chunk_648|><|start_chunk_649|>
## Response

The current state value in the service response may differ from RUNNING if the state transition is still in process when the service returns.

The definition for the response with corresponding datatypes is:

```
{
    "name": "start",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
stop
```

Stops the module. If the command is accepted, the module moves to state IDLE.
<|end_chunk_649|><|start_chunk_650|>
## Details

This service can be called as follows.
<|end_chunk_650|><|start_chunk_651|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/stop
<|end_chunk_651|><|start_chunk_652|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/stop
<|end_chunk_652|><|start_chunk_653|>
## Request

This service has no arguments.
<|end_chunk_653|><|start_chunk_654|>
## Response

The current state value in the service response may differ from IDLE if the state transition is still in process when the service returns.

The definition for the response with corresponding datatypes is:
<|end_chunk_654|><|start_chunk_655|>
### Page 148
```
{
    "name": "stop",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
}
```

reset_defaults

Resets all parameters of the module to its default values, as listed in above table. Also resets sorting strategies.
<|end_chunk_655|><|start_chunk_656|>
 Details 

This service can be called as follows.
<|end_chunk_656|><|start_chunk_657|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_boxpick/services/reset_defaults
<|end_chunk_657|><|start_chunk_658|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_boxpick/services/reset_defaults
<|end_chunk_658|><|start_chunk_659|>
## Request

This service has no arguments.
<|end_chunk_659|><|start_chunk_660|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_660|><|start_chunk_661|>
### 6.4.5.9 Return codes

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.

The following table contains a list of common codes:
<|end_chunk_661|><|start_chunk_662|>
### Page 149
Table 6.35: Return codes of the BoxPick services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -3 | An internal timeout occurred, e.g. during box detection if the given dimension range is too <br> large |
| -4 | Data acquisition took longer than allowed |
| -8 | The template has been deleted during detection. |
| -10 | New element could not be added as the maximum storage capacity of load carriers, regions <br> of interest or template has been exceeded |
| -11 | Sensor not connected, not supported or not ready |
| -200 | Fatal internal error |
| -301 | More than one item model provided to the compute_grasps service |
| 10 | The maximum storage capacity of load carriers, regions of interest or templates has been <br> reached |
| 11 | An existent persistent model was overwritten by the call to set_load_carrier or <br> set_region_of_interest |
| 100 | The requested load carriers were not detected in the scene |
| 101 | No valid surfaces or grasps were found in the scene |
| 102 | The detected load carrier is empty |
| 103 | All computed grasps are in collision with the load carrier |
| 112 | Rejected detections of one or more clusters, because min_cluster_coverage was not <br> reached. |
| 300 | A valid robot pose was provided as argument but it is not required |
| 999 | Additional hints for application development |
<|end_chunk_662|><|start_chunk_663|>
 6.4.5.10 BoxPick Template API 

BoxPick templates are only available with the +Match extension of BoxPick. For template upload, download, listing and removal, special REST-API endpoints are provided. Templates can also be uploaded, downloaded and removed via the Web GUI. The templates include the dimensions, the views and their poses, if set. Up to 100 templates can be stored persistently on the rc_visard.
<|end_chunk_663|><|start_chunk_664|>
## GET /templates/rc_boxpick

Get list of all rc_boxpick templates.
<|end_chunk_664|><|start_chunk_665|>
## Template request

GET /api/v2/templates/rc_boxpick HTTP/1.1
<|end_chunk_665|><|start_chunk_666|>
## Template response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    {
        "id": "string"
    }
}
```

<|end_chunk_666|><|start_chunk_667|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_667|><|start_chunk_668|>
## Status Codes

- 200 OK - successful operation (returns array of Template)
<|end_chunk_668|><|start_chunk_669|>
### Page 150
- 404 Not Found - node not found

<|end_chunk_669|><|start_chunk_670|>
 Referenced Data Models 

- Template (Section 7.3.4)

GET /templates/rc_boxpick/\{id\}
Get a rc_boxpick template. If the requested content-type is application/octet-stream, the template is returned as file.
<|end_chunk_670|><|start_chunk_671|>
## Template request

GET /api/v2/templates/rc_boxpick/<id> HTTP/1.1
<|end_chunk_671|><|start_chunk_672|>
## Template response

HTTP/1.1 200 OK
Content-Type: application/json
\{
"id": "string"
\}
<|end_chunk_672|><|start_chunk_673|>
## Parameters

- id (string) - id of the template (required)

<|end_chunk_673|><|start_chunk_674|>
## Response Headers

- Content-Type - application/json application/ubjson application/octet-stream

<|end_chunk_674|><|start_chunk_675|>
## Status Codes

- 200 OK - successful operation (returns Template)
- 404 Not Found - node or template not found

<|end_chunk_675|><|start_chunk_676|>
## Referenced Data Models

- Template (Section 7.3.4)

PUT /templates/rc_boxpick/\{id\}
Create or update a rc_boxpick template.
<|end_chunk_676|><|start_chunk_677|>
## Template request

PUT /api/v2/templates/rc_boxpick/<id> HTTP/1.1
Accept: multipart/form-data application/json
<|end_chunk_677|><|start_chunk_678|>
## Template response

HTTP/1.1 200 OK
Content-Type: application/json
\{
"id": "string"
\}
<|end_chunk_678|><|start_chunk_679|>
## Parameters

- id (string) - id of the template (required)

<|end_chunk_679|><|start_chunk_680|>
## Form Parameters

- file - template file (required)

<|end_chunk_680|><|start_chunk_681|>
## Request Headers
<|end_chunk_681|><|start_chunk_682|>
### Page 151
- Accept - multipart/form-data application/json

<|end_chunk_682|><|start_chunk_683|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_683|><|start_chunk_684|>
## Status Codes

- 200 OK - successful operation (returns Template)
- 400 Bad Request - Template is not valid or max number of templates reached
- 403 Forbidden - forbidden, e.g. because there is no valid license for this module.
- 404 Not Found - node or template not found
- 413 Request Entity Too Large - Template too large

<|end_chunk_684|><|start_chunk_685|>
## Referenced Data Models

- Template (Section 7.3.4)

DELETE /templates/rc_boxpick/\{id\}
Remove a rc_boxpick template.
Template request
DELETE /api/v2/templates/rc_boxpick/<id> HTTP/1.1
Accept: application/json application/ubjson
<|end_chunk_685|><|start_chunk_686|>
## Parameters

- id (string) - id of the template (required)

<|end_chunk_686|><|start_chunk_687|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_687|><|start_chunk_688|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_688|><|start_chunk_689|>
## Status Codes

- 200 OK - successful operation
- 403 Forbidden - forbidden, e.g. because there is no valid license for this module.
- 404 Not Found - node or template not found

<|end_chunk_689|><|start_chunk_690|>
### 6.4.6 SilhouetteMatch
<|end_chunk_690|><|start_chunk_691|>
### 6.4.6.1 Introduction

The SilhouetteMatch module is an optional on-board module of the rc_visard and requires a separate SilhouetteMatch license (Section 8.7) to be purchased.

The module detects objects by matching a predefined silhouette ("template") to edges in the image.
The SilhouetteMatch module can detect objects in two different scenarios:
With calibrated base plane: The objects are placed on a common base plane, which must be calibrated before the detection, and the objects have significant edges on a common plane that is parallel to the base plane.
<|end_chunk_691|><|start_chunk_692|>
### Page 152
With object plane detection: The objects can be placed at different, previously unknown heights, if the objects have a planar surface and their outer contours are well visible in the images (e.g. stacked flat objects).

Templates for object detection can be created by uploading a DXF file and specifying the object height. The correct scale and unit of the contours are extracted from the DXF file. If no units are present in the DXF file, the user has to specify which units should be used. When the outer contour of the object in the DXF file is closed, a 3D collision model is created automatically by extruding the contour by the given object height. This model will then be used for collision checking and in 3D visualizations. Uploading a DXF file can be done in the Web GUI via the + Create a new Template button in the SilhouetteMatch Templates and Grasps section on the Modules $\rightarrow$ SilhouetteMatch or Database $\rightarrow$ Templates pages.
Roboception also offers a template generation service on their website (https://roboception.com/en/ template-request/), where the user can upload CAD files or recorded data of the objects and request object templates for the SilhouetteMatch module.

The object templates consist of significant edges of each object. These template edges are matched to the edges detected in the left and right camera images, considering the actual size of the objects and their distance from the camera. The poses of the detected objects are returned and can be used for grasping, for example.
The SilhouetteMatch module offers:

- A dedicated page on the rc_visard Web GUI (Section 7.1) for easy setup, configuration, testing, and application tuning.
- A REST-API interface (Section 7.3) and a KUKA Ethernet KRL Interface (Section 7.5).
- The definition of 2D regions of interest to select relevant parts of the camera image (see Setting a region of interest, Section 6.4.6.3).
- A load carrier detection functionality for bin-picking applications (see LoadCarrier, Section 6.4.2), to provide grasps for objects inside a bin only.
- Storing of up to 50 templates.
- The definition of up to 50 grasp points for each template via an interactive visualization in the Web GUI.
- Collision checking between the gripper and the load carrier, the calibrated base plane, other detected objects and/or the point cloud.
- Support for static and robot-mounted cameras and optional integration with the Hand-eye calibration (Section 6.5.1) module, to provide grasps in the user-configured external reference frame.
- Selection of a sorting strategy to sort the detected objects and returned grasps.
- 3D visualization of the detection results with grasp points and gripper animations in the Web GUI.

<|end_chunk_692|><|start_chunk_693|>
 Suitable objects 

The SilhouetteMatch module is intended for objects which have significant edges on a common plane that is parallel to the plane on which the objects are placed. This applies to flat, nontransparent objects, such as routed, laser-cut or water-cut 2D parts and flat-machined parts. More complex parts can also be detected if there are significant edges on a common plane, e.g. a special pattern printed on a flat surface. The detection works best for objects on a texture-free plane. The color of the base plane should be chosen such that a clear contrast between the objects and the base plane appears in the intensity image.
In case the objects are not placed on a common base plane or the base plane cannot be calibrated beforehand, the objects need to have a planar surface and their outer contour must be well visible in the left and right images. Furthermore, the template for these objects must have a closed outer contour.
<|end_chunk_693|><|start_chunk_694|>
### Page 153<|end_chunk_694|><|start_chunk_695|>
 Suitable scene 

The scene must meet the following conditions to be suitable for the SilhouetteMatch module:

- The objects to be detected must be suitable for the SilhouetteMatch module as described above.
- Only objects belonging to one specific template are visible at a time (unmixed scenario). In case other objects are visible as well, a proper region of interest (ROI) must be set.
- In case a calibrated base plane is used: The offset between the base plane normal and the camera's line of sight does not exceed 10 degrees.
- In case the object planes are detected automatically: The offset between the object's planar surface normal and the camera's line of sight does not exceed 25 degrees.
- The objects are not partially or fully occluded.
- All visible objects are right side up (no flipped objects).
- The object edges to be matched are visible in both, left and right camera images.

<|end_chunk_695|><|start_chunk_696|>
### 6.4.6.2 Base-plane calibration

In case all objects are placed on a common plane that is known beforehand, a base-plane calibration should be performed before triggering a detection. Thereby, the distance and angle of the plane on which the objects are placed is measured and stored persistently on the $r c \_v i s a r d$.
Separating the detection of the base plane from the actual object detection renders scenarios possible in which the base plane is temporarily occluded. Moreover, it increases performance of the object detection for scenarios where the base plane is fixed for a certain time; thus, it is not necessary to continuously re-detect the base plane.
The base-plane calibration can be performed in three different ways, which will be explained in more detail further down:

- AprilTag based
- Stereo based
- Manual

The base-plane calibration is successful if the normal vector of the estimated base plane is at most 10 degrees offset to the camera's line of sight. If the base-plane calibration is successful, it will be stored persistently on the $r c \_v i s a r d$ until it is removed or a new base-plane calibration is performed.

Note: To avoid privacy issues, the image of the persistently stored base-plane calibration will appear blurred after rebooting the $r c \_v i s a r d$.

In scenarios where the base plane is not accessible for calibration, a plane parallel to the base plane can be calibrated. Then an offset parameter can be used to shift the estimated plane onto the actual base plane where the objects are placed. The offset parameter gives the distance in meters by which the estimated plane is shifted towards the camera.
In the REST-API, a plane is defined by a normal and a distance. normal is a normalized 3-vector, specifying the normal of the plane. The normal points away from the camera. distance represents the distance of the plane from the camera along the normal. Normal and distance can also be interpreted as $a, b, c$, and $d$ components of the plane equation, respectively:

$$
a x+b y+c z+d=0
$$
<|end_chunk_696|><|start_chunk_697|>
### Page 154<|end_chunk_697|><|start_chunk_698|>
 AprilTag based base-plane calibration 

AprilTag detection (ref. TagDetect, Section 6.4.3) is used to find AprilTags in the scene and fit a plane through them. At least three AprilTags must be placed on the base plane so that they are visible in the left and right camera images. The tags should be placed such that they are spanning a triangle that is as large as possible. The larger the triangle, the more accurate is the resulting base-plane estimate. Use this method if the base plane is untextured and no external random dot projector is available. This calibration mode is available via the REST-API interface (Section 7.3) and the rc_visard Web GUI.
<|end_chunk_698|><|start_chunk_699|>
## Stereo based base-plane calibration

The 3D point cloud computed by the stereo matching module is used to fit a plane through its 3D points. Therefore, the region of interest (ROI) for this method must be set such that only the relevant base plane is included. The plane_preference parameter allows to select whether the plane closest to or farthest from the camera should be used as base plane. Selecting the closest plane can be used in scenarios where the base plane is completely occluded by objects or not accessible for calibration. Use this method if the base plane is well textured or you can make use of a random dot projector to project texture on the base plane. This calibration mode is available via the REST-API interface (Section 7.3) and the $r c \_v i s a r d$ Web GUI.
<|end_chunk_699|><|start_chunk_700|>
## Manual base-plane calibration

The base plane can be set manually if its parameters are known, e.g. from previous calibrations. This calibration mode is only available via the REST-API interface (Section 7.3) and not the rc_visard Web GUI.
<|end_chunk_700|><|start_chunk_701|>
### 6.4.6.3 Setting a region of interest

If objects are to be detected only in part of the camera's field of view, a 2D region of interest (ROI) can be set accordingly as described in Region of interest (Section 6.6.2.2).
<|end_chunk_701|><|start_chunk_702|>
### 6.4.6.4 Setting of grasp points

To use SilhouetteMatch directly in a robot application, up to 50 grasp points can be defined for each template. A grasp point represents the desired position and orientation of the robot's TCP (Tool Center Point) to grasp an object as shown in Fig. 6.18.
![img-41.jpeg](img-41.jpeg)

Fig. 6.18: Definition of grasp points with respect to the robot's TCP

Each grasp consists of an id which must be unique within all grasps for an object template, the template_id representing the template to which the grasp should be attached, and the pose in the coordinate frame of the object template. Grasp points can be set via the REST-API interface (Section 7.3), or by using the interactive visualization in the Web GUI. Furthermore, a priority (spanning -2 for very low to 2 for very high) can be assigned to a grasp. Priorities can facilitate robot applications and shorten response times when the run-time parameter only_highest_priority_grasps is set to
<|end_chunk_702|><|start_chunk_703|>
### Page 155
true. In this case collision checking concludes when grasps with the highest possible priority have been found. Finally, different grasps can be associated with different grippers by specifying a gripper_id. These individual grippers are then used for collision checking of the corresponding grasps instead of the gripper defined in the detect_object request. If no gripper_id is given, the gripper defined in the detect_object request will be used for collision checking.
When a grasp is defined on a symmetric object, all grasps symmetric to the defined one will automatically be considered in the SilhouetteMatch module's detect_object service call. Symmetric grasps for a given grasp point can be retrieved using the get_symmetric_grasps service call and visualized in the Web GUI.

Users can also define replications of grasps around a custom axis. These replications spawn multiple grasps and free users from setting too many grasps manually. The replication origin is defined as a coordinate frame in the object's coordinate frame and the $x$ axis of the replication origin frame corresponds to the replication axis. The grasp is replicated by rotating it around this $x$ axis starting from its original pose. The replication is done in steps of size step_x_deg degrees. The range is defined by the minimal and maximal boundaries min_x_deg and max_x_deg. The minimal (maximal) boundary must be a non-positive (non-negative) number up to (minus) 180 degrees.
<|end_chunk_703|><|start_chunk_704|>
 Setting grasp points in the Web GUI 

The rc_visard Web GUI provides an intuitive and interactive way of defining grasp points for object templates. In a first step, the object template has to be uploaded to the $r c \_$visard. This can be done in the Web GUI in any pipeline under Modules $\rightarrow$ SilhouetteMatch by clicking on + Add a new Template in the Templates and Grasps section, or in Database $\rightarrow$ Templates in the SilhouetteMatch Templates and Grasps section. Once the template upload is complete, a dialog with a 3D visualization of the object template is shown for adding or editing grasp points. The same dialog appears when editing an existing template. If the template contains a collision model or a visualization model, this 3D model is visualized as well.

This dialog provides two ways for setting grasp points:

1. Adding grasps manually: By clicking on the + symbol, a new grasp is placed in the object origin. The grasp can be given a unique name which corresponds to its ID. The desired pose of the grasp can be entered in the fields for Position and Roll/Pitch/Yaw which are given in the coordinate frame of the object template represented by the long $x, y$ and $z$ axes in the visualization. The grasp point can be placed freely with respect to the object template - inside, outside or on the surface. The grasp point and its orientation are visualized in 3D for verification.
2. Adding grasps interactively: Grasp points can be added interactively by first clicking on the Add Grasp button in the upper right corner of the visualization and then clicking on the desired point on the object template visualization. If the 3D model is displayed, the grasps will be attached to the surface of the 3D model. Otherwise, the grasp is attached to the template surface. The grasp orientation is a right-handed coordinate system and is chosen such that its $z$ axis is perpendicular to the surface pointing inside the template at the grasp position. The position and orientation in the object coordinate frame is displayed on the right. The position and orientation of the grasp can also be changed interactively. In case Snap to surface is disabled (default), the grasp can be translated and rotated freely in all three dimensions by clicking on Move Grasp in the visualization menu and then dragging the grasp along the appropriate axis to the desired position. The orientation of the grasp can also be changed by rotating the axis with the mouse. In case Snap to surface is enabled in the visualization, the grasp can only be moved along the model surface.
Users can also specify a grasp priority by changing the Priority slider. A dedicated gripper can be selected in the Gripper drop down field.
By activating the Replication check box, users can replicate the grasp around a custom axis. The replication axis and the resulting replicated grasps are visualized. The position and orientation of the replication axis relative to the object coordinate frame can be adjusted interactively by clicking on Move Replication Axis in the visualization menu and then dragging the axis to the desired position and orientation. The grasps are replicated within the specified rotation range at the selected rotation step size. Users can cycle through a visualization of the replicated grasps by dragging the bar below Cycle through
<|end_chunk_704|><|start_chunk_705|>
### Page 156
$n$ replicated grasps in the View Options section of the visualization menu. If a gripper is selected for the grasp or a gripper has been chosen in the visualization menu, the gripper is also shown at the currently selected grasp.
If the object template has symmetries, the grasps which are symmetric to the defined grasps can be displayed along with their replications (if defined) by enabling ... symmetries in the View Options section of the visualization menu. The user can also cycle through a visualization of the symmetric grasps by dragging the bar below Cycle through $n$ symmetric grasps.
<|end_chunk_705|><|start_chunk_706|>
 Setting grasp points via the REST-API 

Grasp points can be set via the REST-API interface (Section 7.3) using the set_grasp or set_all_grasps services (see Internal services, Section 6.4.6.12). A grasp consists of the template_id of the template to which the grasp should be attached, an id uniquely identifying the grasp point and the pose. The pose is given in the coordinate frame of the object template and consists of a position in meters and an orientation as quaternion. A dedicated gripper can be specified through setting the gripper_id field. The priority is specified by an integer value, ranging from -2 for very low, to 2 for very high with a step size of 1 . The replication origin is defined as a transformation in the object's coordinate frame and the $x$ axis of the transformation corresponds to the replication axis. The replication range is controlled by the min_x_deg and max_x_deg fields and the step size step_x_deg.
<|end_chunk_706|><|start_chunk_707|>
### 6.4.6.5 Setting the preferred orientation of the TCP

The SilhouetteMatch module determines the reachability of grasp points based on the preferred orientation of the TCP. The preferred orientation can be set via the set_preferred_orientation service or on the SilhouetteMatch page in the Web GUI. The resulting direction of the TCP's z axis is used to reject grasps which cannot be reached by the gripper. Furthermore, the preferred orientation can be used to sort the reachable grasps by setting the corresponding sorting strategy.
The preferred orientation can be set in the camera coordinate frame or in the external coordinate frame, in case a hand-eye calibration is available. If the preferred orientation is specified in the external coordinate frame and the sensor is robot mounted, the current robot pose has to be given to each object detection call. If no preferred orientation is set, the orientation of the left camera (see Coordinate frames ) will be used as the preferred orientation of the TCP.
<|end_chunk_707|><|start_chunk_708|>
### 6.4.6.6 Setting the sorting strategies

The objects and grasps returned by the detect_object service call are sorted according to a sorting strategy which can be chosen by the user. The following sorting strategies are available and can be set in the Web GUI (Section 7.1) or using the set_sorting_strategies service call:

- preferred_orientation: objects and grasp points with minimal rotation difference between their orientation and the preferred orientation of the TCP are returned first,
- direction: objects and grasp points with the shortest distance along a defined direction vector in a given pose_frame are returned first.
- distance_to_point: objects and grasp points with the shortest or farthest (if farthest_first is true) distance from a point in a given pose_frame are returned first.

If no sorting strategy is set or default sorting is chosen in the Web GUI, sorting is done based on a combination of preferred_orientation and the minimal distance from the camera along the z axis of the preferred orientation of the TCP.
<|end_chunk_708|><|start_chunk_709|>
### 6.4.6.7 Detection of objects

For triggering the object detection, in general, the following information must be provided to the SilhouetteMatch module:
<|end_chunk_709|><|start_chunk_710|>
### Page 157
- The template of the object to be detected in the scene.
- The coordinate frame in which the poses of the detected objects shall be returned (ref. Hand-eye calibration, Section 6.4.6.8).
Optionally, further information can be given to the SilhouetteMatch module:
- A flag object..plane..detection determining whether the surface plane of the objects should be used for the detection instead of the calibrated base plane.
- An offset, in case the calibrated base plane should be used but the objects are not lying on this plane but on a plane parallel to it. The offset is the distance between both planes given in the direction towards the camera. If omitted, an offset of 0 is assumed. It must not be set if object..plane..detection is true.
- The ID of the load carrier which contains the objects to be detected.
- The ID of the region of interest where to search for the load carrier if a load carrier is set. Otherwise, the ID of the region of interest where the objects should be detected. If omitted, objects are matched in the whole image.
- The current robot pose in case the camera is mounted on the robot and the chosen coordinate frame for the poses is external or the preferred orientation is given in the external frame.
- Collision detection information: The ID of the gripper to enable collision checking and optionally a pre-grasp offset to define a pre-grasp position. Details on collision checking are given below in CollisionCheck (Section 6.4.6.8).
In case the object..plane..detection flag is not true, objects can only be detected after a successful base-plane calibration. It must be ensured that the position and orientation of the base plane does not change before the detection of objects. Otherwise, the base-plane calibration must be renewed.
When object..plane..detection is set to true, a base-plane calibration is not required and an existing base-plane calibration will be ignored. During detection, the scene is clustered into planar surfaces and template matching is performed on each plane whose tilt with respect to the camera's line of sight is less than $25^{\circ}$ and whose size is large enough to contain the selected template. When a match is found, its position and orientation are refined using the image edges and the point cloud inside the template's outer contour. For this, it is required that the outer contour of the template is closed and that the object's surface is planar.
On the Web GUI the detection can be tested in the Try Out section of the SilhouetteMatch page. Different image streams can be selected to show intermediate results and the final matches as shown in Fig. 6.19.

The "Template" image stream shows the template to be matched in red with the defined grasp points in green (see Setting of grasp points, Section 6.4.6.4). The template is warped to the size and tilt matching objects on the calibrated base plane or, in case object..plane..detection was used, the highest segmented plane, would have. The corresponding plane is shown in dark blue.
The "Intermediate Result" image stream shows the edges of the left image that were used to search for matches in light blue. The chosen region of interest is shown as bold petrol rectangle. A shaded blue area on the left visualizes the region of the left camera image which does not overlap with the right image, and in which no objects can be detected. If object..plane..detection was used, this image stream also shows the detected planar clusters in the scene. Clusters that were not used for matching, because they were too small or too tilted, are visualized with a stripe pattern.
The "Intermediate Result Right" image stream shows the edges of the right image that were used to search for matches in light blue. The chosen region of interest is shown as bold petrol rectangle. A shaded blue area on the right visualizes the region of the right camera image which does not overlap with the left image, and in which no objects can be detected.

The "Result" image shows the detection result. The image edges that were used to refine the match poses are shown in light blue and the matches (instances) with the template
<|end_chunk_710|><|start_chunk_711|>
### Page 158
edges are shown in red. The blue circles are the origins of the detected objects as defined in the template and the green circles are the collision-free grasp points. Colliding grasp points are visualized as red dots and grasp points that were not checked for collisions are drawn in yellow.
![img-42.jpeg](img-42.jpeg)

Fig. 6.19: "Template", "Intermediate Result" and "Result" image streams of the SilhouetteMatch module as shown in the Web GUI for a detection with object_plane_detection set to true

The poses of the object origins in the chosen coordinate frame are returned as results in a list of instances. In case the calibrated base plane was used for the detection (object_plane_detection not set or false), the orientations of the detected objects are aligned with the normal of the base plane. Otherwise, the orientations of the detected objects are aligned with the normal of a plane fitted to the object points in the 3D point cloud.

If the chosen template also has grasp points attached, a list of grasps for all objects is returned in addition to the list of detected objects. The grasp poses are given in the desired coordinate frame and the grasps are sorted according to the selected sorting strategy (see Setting the sorting strategies, Section 6.4.6.6). There are references between the detected object instances and the grasps via their uuids.

In case the templates have a continuous rotational symmetry (e.g. cylindrical objects), all returned object poses will have the same orientation. Furthermore, all grasps symmetric to each grasp point on an object are checked for reachability and collisions, and only the best one according to the given sorting strategy is returned.

For objects with a discrete symmetry (e.g. prismatic objects), all collision-free symmetries of each grasp point which are reachable according to the given preferred TCP orientation are returned, ordered by the given sorting strategy.

The detection results and run times are affected by several run-time parameters which are listed and explained further down. Improper parameters can lead to timeouts of the SilhouetteMatch module's detection process.
<|end_chunk_711|><|start_chunk_712|>
 6.4.6.8 Interaction with other modules 

Internally, the SilhouetteMatch module depends on, and interacts with other on-board modules as listed below.

Note: All changes and configuration updates to these modules will affect the performance of the SilhouetteMatch module.
<|end_chunk_712|><|start_chunk_713|>
## Camera and depth data

The SilhouetteMatch module makes internally use of the rectified images from the Camera module (rc_camera, Section 6.1). Thus, the exposure time should be set properly to achieve the optimal performance of the module.
<|end_chunk_713|><|start_chunk_714|>
### Page 159
For base-plane calibration in stereo mode, for load carrier detection, for automatic object plane detection and for collision checking with the point cloud, the disparity images from the Stereo matching module (rc_stereomatching, Section 6.2) are used.

For detecting objects with a calibrated base plane, without load carrier and without collision checking with the point cloud, the stereo-matching module should not be run in parallel to the SilhouetteMatch module, because the detection runtime increases.

For best results it is recommended to enable smoothing (Section 6.2.1.2) for Stereo matching module.
<|end_chunk_714|><|start_chunk_715|>
 IO and Projector Control 

In case the rc_visard is used in conjunction with an external random dot projector and the IO and Projector Control module (rc_iocontrol, Section 6.5.4), the projector should be used for the stereobased base-plane calibration, for automatic object plane detection and for collision checking with the point cloud.

The projected pattern must not be visible in the left and right camera images during object detection as it interferes with the matching process. Therefore, it is recommended to connect the projector to GPIO Out 1 and set the stereo-camera module's acquisition mode to SingleFrameOut1 (see Stereo matching parameters, Section 6.2.1), so that on each image acquisition trigger an image with and without projector pattern is acquired.

Alternatively, the output mode for the GPIO output in use should be set to ExposureAlternateActive (see Description of run-time parameters, Section 6.5.4.1).

In either case, the Auto Exposure Mode exp_auto_mode should be set to AdaptiveOut1 to optimize the exposure of both images.
<|end_chunk_715|><|start_chunk_716|>
## Hand-eye calibration

In case the camera has been calibrated to a robot, the SilhouetteMatch module can automatically provide poses in the robot coordinate frame. For the SilhouetteMatch node's Services (Section 6.4.6.11), the frame of the input and output poses and plane coordinates can be controlled with the pose_frame argument.

Two different pose_frame values can be chosen:

1. Camera frame (camera). All poses and plane coordinates provided to and by the module are in the camera frame.
2. External frame (external). All poses and plane coordinates provided to and by the module are in the external frame, configured by the user during the hand-eye calibration process. The module relies on the on-board Hand-eye calibration module (Section 6.5.1) to retrieve the camera mounting (static or robot mounted) and the hand-eye transformation. If the sensor mounting is static, no further information is needed. If the sensor is robot-mounted, the robot pose is required to transform poses to and from the external frame.

All pose_frame values that are not camera or external are rejected.
Note: If no hand-eye calibration is available, all pose_frame values should be set to camera.

Note: If the hand-eye calibration has changed after base-plane calibration, the base-plane calibration will be marked as invalid and must be renewed.

If the sensor is robot-mounted, the current robot pose has to be provided depending on the value of pose_frame, the definition of the preferred TCP orientation and the sorting direction or sorting point:

- If pose_frame is set to external, providing the robot pose is obligatory.
- If the preferred TCP orientation is defined in external, providing the robot pose is obligatory.
<|end_chunk_716|><|start_chunk_717|>
### Page 160
- If the sorting direction is defined in external, providing the robot pose is obligatory.
- If the distance-to-point sorting strategy is defined in external, providing the robot pose is obligatory.
- In all other cases, providing the robot pose is optional.

If the current robot pose is provided during calibration, it is stored persistently on the $r c \_v i s a r d$. If the updated robot pose is later provided during get_base_plane_calibration or detect_object as well, the base-plane calibration will be transformed automatically to this new robot pose. This enables the user to change the robot pose (and thus camera position) between base-plane calibration and object detection.

Note: Object detection can only be performed if the limit of 10 degrees angle offset between the base plane normal and the camera's line of sight is not exceeded.
<|end_chunk_717|><|start_chunk_718|>
 LoadCarrier 

The SilhouetteMatch module uses the load carrier detection functionality provided by the LoadCarrier module (rc_load_carrier, Section 6.4.2), with the run-time parameters specified for this module. However, only one load carrier will be returned and used in case multiple matching load carriers could be found in the scene. In case multiple load carriers of the same type are visible, a region of interest should be set to ensure that always the same load carrier is used for the SilhouetteMatch module.
<|end_chunk_718|><|start_chunk_719|>
## CollisionCheck

Collision checking can be easily enabled for grasp computation of the SilhouetteMatch module by passing a collision_detection argument to the detect_object service call. It contains the ID of the used gripper and optionally a pre-grasp offset. The gripper has to be defined in the GripperDB module (see Setting a gripper, Section 6.6.3.2) and details about collision checking are given in Collision checking within other modules (Section 6.5.2.2).

Alternatively, grasp points can be assigned individual gripper IDs, and collision checking can be enabled for all grasp points with gripper IDs by enabling the run-time parameter check_collisions.

In addition to collision checking between the gripper and the detected load carrier, collisions between the gripper and the calibrated base plane will be checked, if the run-time parameter check_collisions_with_base_plane is true. If the selected SilhouetteMatch template contains a collision model and the run-time parameter check_collisions_with_matches is true, also collisions between the gripper and all other detected objects (not limited to max_number_of_detected_objects) will be checked. The object on which the grasp point to be checked is located, is excluded from the collision check.

If the run-time parameter check_collisions_with_point_cloud is true, also collisions between the gripper and a watertight version of the point cloud are checked. If this feature is used with suctions grippers, it should be ensured that the TCP is defined to be outside the gripper geometry, or that the grasp points are defined above the object surface. Otherwise every grasp will result in a collision between the gripper and the point cloud.

If the run-time parameter check_collisions_during_retraction is true and a load carrier and a pregrasp offset are given, each grasp point will be checked for collisions between the object in the gripper and the load carrier walls during retraction. This collision check is performed along the full linear trajectory from the grasp point back to the pre-grasp position.

If collision checking is enabled, only grasps which are collision free or could not be checked for collisions (e.g. because no gripper was given) will be returned. The visualization images on the SilhouetteMatch page of the Web GUI shows collision-free grasps in green, unchecked grasps in yellow and colliding grasp points in red. The detected objects which are considered in the collision check are also visualized with their edges in red.
<|end_chunk_719|><|start_chunk_720|>
### Page 161
The CollisionCheck module's run-time parameters affect the collision detection as described in CollisionCheck Parameters (Section 6.5.2.3).
<|end_chunk_720|><|start_chunk_721|>
 6.4.6.9 Parameters 

The SilhouetteMatch software module is called rc_silhouettematch in the REST-API and is represented in the Web GUI (Section 7.1) under Modules $\rightarrow$ SilhouetteMatch. The user can explore and configure the rc_silhouettematch module's run-time parameters, e.g. for development and testing, using the Web GUI or the REST-API interface (Section 7.3).
<|end_chunk_721|><|start_chunk_722|>
## Parameter overview

This module offers the following run-time parameters:
Table 6.36: The rc_silhouettematch module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :--: | :--: | :--: | :--: | :--: | :--: |
| check_collisions | bool | false | true | false | Whether to check for collisions when a gripper is defined for a grasp |
| check_collisions_during_retraction | bool | false | true | false | Whether to check for collisions between the object in the gripper and the load carrier during retraction |
| check_collisions_with_base_plane | bool | false | true | true | Whether to check for collisions between gripper and base plane |
| check_collisions_with_matches | bool | false | true | true | Whether to check for collisions between gripper and detected matches |
| check_collisions_with_point_cloud | bool | false | true | false | Whether to check for collisions between gripper and the point cloud |
| edge_sensitivity | float64 | 0.1 | 1.0 | 0.7 | Sensitivity of the edge detector |
| match_max_distance | float64 | 0.1 | 10.0 | 3.0 | Maximum allowed distance in pixels between the template and the detected edges in the image |
| match_percentile | float64 | 0.7 | 1.0 | 0.8 | Percentage of template pixels that must be within the maximum distance to successfully match the template |
| max_number_of_detected_objects | int32 | 1 | 20 | 10 | Maximum number of detected objects |
| only_highest_priority_grasps | bool | false | true | false | Whether to return only the highest priority level grasps |
| point_cloud_enhancement | string | - | - | Off | Type of enhancement of the point cloud using the base plane: [Off, ReplaceBright] |
| quality | string | - | - | High | Quality: [Low, Medium, High] |
<|end_chunk_722|><|start_chunk_723|>
## Description of run-time parameters

Each run-time parameter is represented by a row on the Web GUI's SilhouetteMatch page. The name in the Web GUI is given in brackets behind the parameter name and the parameters are listed in the order they appear in the Web GUI:
<|end_chunk_723|><|start_chunk_724|>
### Page 162<|end_chunk_724|><|start_chunk_725|>
 max_number_of_detected_objects (Maximum Object Number) 

This parameter gives the maximum number of objects to detect in the scene. If more than the given number of objects can be detected in the scene, only the objects matching best to the given sorting strategy are returned.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_725|><|start_chunk_726|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/parameters/parameters? ...max_number_of_detected_objects=<value>
<|end_chunk_726|><|start_chunk_727|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?max_number_of_detected_ $\ldots$ objects $=$ <value>
<|end_chunk_727|><|start_chunk_728|>
## quality (Quality)

Object detection can be performed on images with different resolutions: High (full image resolution), Medium (half image resolution) and Low (quarter image resolution). The lower the resolution, the lower the detection time, but the fewer details of the objects are visible.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_728|><|start_chunk_729|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/parameters/parameters? ...quality=<value>
<|end_chunk_729|><|start_chunk_730|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?quality=<value>
match_max_distance (Maximum Matching Distance)

This parameter gives the maximum allowed pixel distance of an image edge pixel from the object edge pixel in the template to be still considered as matching. If the object is not perfectly represented in the template, it might not be detected when this parameter is low. High values, however, might lead to false detections in case of a cluttered scene or the presence of similar objects, and also increase runtime.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_730|><|start_chunk_731|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/parameters/parameters? ...match_max_distance=<value>
<|end_chunk_731|><|start_chunk_732|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?match_max_distance=<value>
match_percentile (Matching Percentile)

This parameter indicates how strict the matching process should be. The matching percentile is the ratio of template pixels that must be within the Maximum Matching
<|end_chunk_732|><|start_chunk_733|>
### Page 163
Distance to successfully match the template. The higher this number, the more accurate the match must be to be considered as valid.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_733|><|start_chunk_734|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/parameters/parameters? ...match_percentile=<value>
<|end_chunk_734|><|start_chunk_735|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?match_percentile=<value>
edge_sensitivity (Edge Sensitivity)

This parameter influences how many edges are detected in the left and right camera images. The higher this number, the more edges are found in the intensity images. That means, for lower numbers, only the most significant edges are considered for template matching. A large number of edges in the image might increase the detection time. It must be ensured that the edges of the objects to be detected are detected in both, the left and the right camera images.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_735|><|start_chunk_736|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/parameters/parameters? ...edge_sensitivity=<value>
<|end_chunk_736|><|start_chunk_737|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?edge_sensitivity=<value>
only_highest_priority_grasps (Only Highest Priority Grasps)
If set to true, only grasps with the highest priority will be returned. If collision checking is enabled, only the collision-free grasps among the group of grasps with the highest priority are returned. This can save computation time and reduce the number of grasps to be parsed on the application side.

Without collision checking, only grasps of highest priority are returned.
<|end_chunk_737|><|start_chunk_738|>
## API version 2

PUT http://<host>/api/v2/pipelines/ $<0,1,2,3>$ /nodes/rc_silhouettematch/parameters?only_ ...highest_priority_grasps=<value>
<|end_chunk_738|><|start_chunk_739|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?only_highest_priority... ...grasps=<value>
check_collisions (Check Collisions)

If this parameter is enabled, collision checking will be performed for all grasps which have a gripper ID assigned, even when no default gripper is given in the detect object service call. If a load carrier is used, the collision check will always be performed between the gripper and the load carrier. Collision checking with the
<|end_chunk_739|><|start_chunk_740|>
### Page 164
point cloud and other matches is only performed when the corresponding runtime parameters are enabled.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_740|><|start_chunk_741|>
 API version 2 

PUT http://<host>/api/v2/pipelines/<0,1,2,3>/nodes/rc_silhouettematch/parameters?check_ $\ldots$ collisions=<value>
<|end_chunk_741|><|start_chunk_742|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?check_collisions=<value>
<|end_chunk_742|><|start_chunk_743|>
## check_collisions_with_base_plane (Check Collisions with Base Plane)

This parameter is only used when collision checking is enabled by passing a gripper to the detect_object service call or by enabling the check_collisions runtime parameter. If check_collisions_with_base_plane is set to true, all grasp points will be checked for collisions between the gripper and the calibrated base plane, and only grasp points at which the gripper would not collide with the base plane will be returned.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_743|><|start_chunk_744|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/parameters/parameters? ...check_collisions_with_base_plane=<value>
<|end_chunk_744|><|start_chunk_745|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?check_collisions_with_ ...base_plane=<value>
check_collisions_with_matches (Check Collisions with Matches)

This parameter is only used when collision checking is enabled by passing a gripper to the detect_object service call or by enabling the check_collisions runtime parameter. If check_collisions_with_matches is set to true, all grasp points will be checked for collisions between the gripper and all other detected objects (not limited to max_number_of_detected_objects, and only grasp points at which the gripper would not collide with any other detected object will be returned.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_745|><|start_chunk_746|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/parameters/parameters? ...check_collisions_with_matches=<value>
<|end_chunk_746|><|start_chunk_747|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?check_collisions_with_ ...matches=<value>
<|end_chunk_747|><|start_chunk_748|>
### Page 165<|end_chunk_748|><|start_chunk_749|>
 check_collisions_with_point_cloud (Check Collisions with Point Cloud) 

This parameter is only used when collision checking is enabled by passing a gripper to the detect_object service call or by enabling the check_collisions runtime parameter. If check_collisions_with_point_cloud set to true, all grasp points will be checked for collisions between the gripper a watertight version of the point cloud, and only grasp points at which the gripper would not collide with this point cloud will be returned.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_749|><|start_chunk_750|>
## API version 2

PUT http://<host>/api/v2/pipelines/<0,1,2,3>/nodes/rc_silhouettematch/parameters?check_ ...collisions_with_point_cloud=<value>
<|end_chunk_750|><|start_chunk_751|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?check_collisions_with_ ...point_cloud=<value>
point_cloud_enhancement (Enhance with Base Plane)

This parameter is only considered when check_collisions_with_point_cloud is true and the object detection was triggered without object_plane_detection. By default, point_cloud_enhancement is set to off (Off). If point_cloud_enhancement is set to ReplaceBright (Replace Bright Image Pixels), the calibrated base plane will be used to enhance the point cloud that is used for collision checking. For this, the depth values of all bright image pixels inside the image or, if set, the 2D region of interest will be set to the depth of the calibrated base plane. This parameter should be used when dark objects are placed on an untextured bright background, e.g. on a light table.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_751|><|start_chunk_752|>
## API version 2

PUT http://<host>/api/v2/pipelines/<0,1,2,3>/nodes/rc_silhouettematch/parameters?point_ ...cloud_enhancement=<value>
<|end_chunk_752|><|start_chunk_753|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?point_cloud_enhancement= ...<value>
check_collisions_during_retraction (Check Collisions during Retraction)

This parameter is only used when collision checking is enabled by passing a gripper to the detect_object service call or by enabling the check_collisions runtime parameter. When check_collisions_during_retraction is enabled and a load carrier and a pre-grasp offset are given, each grasp point will be checked for collisions between the object in the gripper and the load carrier walls during retraction. This collision checking is performed along the full linear trajectory from the grasp point back to the pre-grasp position. Only collision-free grasp points will be returned.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_753|><|start_chunk_754|>
## API version 2
<|end_chunk_754|><|start_chunk_755|>
### Page 166
PUT http://<host>/api/v2/pipelines/ $<0,1,2,3>$ /nodes/rc_silhouettematch/parameters?check_ $\ldots$ collisions_during_retraction=<value>
<|end_chunk_755|><|start_chunk_756|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_silhouettematch/parameters?check_collisions_during_ $\ldots$ retraction=<value>
<|end_chunk_756|><|start_chunk_757|>
### 6.4.6.10 Status values

This module reports the following status values:
Table 6.37: The rc_silhouettematch module's status values

| Name | Description |
| :-- | :-- |
| data_acquisition_time | Time in seconds required by the last active service to acquire <br> images |
| last_timestamp_processed | The timestamp of the last processed dataset |
| load_carrier_detection_time | Processing time of the last load carrier detection in seconds |
| processing_time | Processing time of the last detection (including load carrier <br> detection) in seconds |
<|end_chunk_757|><|start_chunk_758|>
### 6.4.6.11 Services

The user can explore and call the rc_silhouettematch module's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1).
The SilhouetteMatch module offers the following services.
detect_object
Triggers an object detection as described in Detection of objects (Section 6.4.6.7) and returns the pose of all found object instances.
<|end_chunk_758|><|start_chunk_759|>
## Details

All images used by the service are guaranteed to be newer than the service trigger time.
This service can be called as follows.
<|end_chunk_759|><|start_chunk_760|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/detect_object
<|end_chunk_760|><|start_chunk_761|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/detect_object
<|end_chunk_761|><|start_chunk_762|>
## Request

Required arguments:
object_id in object_to_detect: ID of the template which should be detected.
pose_frame: see Hand-eye calibration (Section 6.4.6.8).
Potentially required arguments:
robot_pose: see Hand-eye calibration (Section 6.4.6.8).
Optional arguments:
<|end_chunk_762|><|start_chunk_763|>
### Page 167
object_plane_detection: false if the objects are placed on a calibrated base plane, true if the objects' surfaces are planar and the base plane is unknown or the objects are located on multiple different planes, e.g. stacks.
offset: offset in meters by which the base-plane calibration will be shifted towards the camera.
load_carrier_id: ID of the load carrier which contains the items to be detected.
collision_detection: see Collision checking within other modules (Section 6.5.2.2).

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "collision_detection": {
            "gripper_id": "string",
            "pre_grasp_offset": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "load_carrier_id": "string",
    "object_plane_detection": "bool",
    "object_to_detect": {
        "object_id": "string",
        "region_of_interest_2d_id": "string"
    },
    "offset": "float64",
    "pose_frame": "string",
    "robot_pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
        }
    }
}
```

<|end_chunk_763|><|start_chunk_764|>
 Response 

The maximum number of returned instances can be controlled with the max_number_of_detected_objects parameter.
object_id: ID of the detected template.
instances: list of detected object instances, ordered according to the chosen sorting strategy.
grasps: list of grasps on the detected objects, ordered according to the chosen sorting strategy. The instance_uuid gives the reference to the detected object in instances this grasp belongs to. The list of returned grasps will be trimmed to the 100 best grasps if more reachable grasps are found. Each grasp contains a flag collision_checked and a gripper_id (see Collision checking within other modules, Section 6.5.2.2).
load_carriers: list of detected load carriers.
<|end_chunk_764|><|start_chunk_765|>
### Page 168
timestamp: timestamp of the image set the detection ran on.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "detect_object",
    "response": {
        "grasps": [
            {
                "collision_checked": "bool",
                "gripper_id": "string",
                "id": "string",
                "instance_uuid": "string",
                "pose": {
                    "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                },
                    "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                }
            },
            "pose_frame": "string",
            "priority": "int8",
            "timestamp": {
                    "nsec": "int32",
                    "sec": "int32"
            },
            "uuid": "string"
        }
    ],
    "instances": [
        {
            "grasp_uuids": [
                "string"
            ],
            "id": "string",
            "object_id": "string",
            "pose": {
                    "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            }
            },
            "pose_frame": "string",
            "timestamp": {
                    "nsec": "int32",
                    "sec": "int32"
            },
            "uuid": "string"
```

(continues on next page)
<|end_chunk_765|><|start_chunk_766|>
### Page 169
(continued from previous page)

```
    }
    ],
    "load_carriers": [
        {
            "height_open_side": "float64",
            "id": "string",
            "inner_dimensions": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "outer_dimensions": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "overfilled": "bool",
        "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        },
        "pose_frame": "string",
        "rim_ledge": {
            "x": "float64",
            "y": "float64"
        },
        "rim_step_height": "float64",
        "rim_thickness": {
            "x": "float64",
            "y": "float64"
        },
        "type": "string"
        }
    ],
    "object_id": "string",
    "return_code": {
        "message": "string",
        "value": "int16"
    },
    "timestamp": {
        "nsec": "int32",
        "sec": "int32"
    }
    }
}
```

calibrate_base_plane

Triggers the calibration of the base plane, as described in Base-plane calibration (Section 6.4.6.2).
<|end_chunk_766|><|start_chunk_767|>
### Page 170<|end_chunk_767|><|start_chunk_768|>
 Details 

A successful base-plane calibration is stored persistently on the $r c \_v i s a r d$ and returned by this service. The base-plane calibration is persistent over firmware updates and rollbacks.

All images used by the service are guaranteed to be newer than the service trigger time.
This service can be called as follows.
<|end_chunk_768|><|start_chunk_769|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/calibrate_base_ -plane
<|end_chunk_769|><|start_chunk_770|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/calibrate_base_plane
<|end_chunk_770|><|start_chunk_771|>
## Request

Required arguments:
plane_estimation_method: method to use for base-plane calibration. Valid values are STEREO, APRILTAG, MANUAL.
pose_frame: see Hand-eye calibration (Section 6.4.6.8).
Potentially required arguments:
plane if plane_estimation_method is MANUAL: plane that will be set as base-plane calibration.
robot posse: see Hand-eye calibration (Section 6.4.6.8).
region_of_interest_2d_id: ID of the region of interest for base-plane calibration.
Optional arguments:
offset: offset in meters by which the estimated plane will be shifted towards the camera.
plane_preference in stereo: whether the plane closest to or farthest from the camera should be used as base plane. This option can be set only if plane_estimation_method is STEREO. Valid values are CLOSEST and FARTHEST. If not set, the default is FARTHEST.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
    "offset": "float64",
    "plane": {
        "distance": "float64",
        "normal": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "plane_estimation_method": "string",
    "pose_frame": "string",
    "region_of_interest_2d_id": "string",
    "robot_pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
```
<|end_chunk_771|><|start_chunk_772|>
### Page 171
(continued from previous page)

```
            "z": "float64"
            },
            "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "stereo": {
        "plane_preference": "string"
        }
    }
}
```

<|end_chunk_772|><|start_chunk_773|>
 Response 

plane: calibrated base plane.
timestamp: timestamp of the image set the calibration ran on.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "calibrate_base_plane",
    "response": {
        "plane": {
            "distance": "float64",
            "normal": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "pose_frame": "string"
        },
        "return_code": {
            "message": "string",
            "value": "int16"
        },
        "timestamp": {
            "nsec": "int32",
            "sec": "int32"
        }
    }
}
```

get_base_plane_calibration

Returns the configured base-plane calibration.
<|end_chunk_773|><|start_chunk_774|>
## Details

This service can be called as follows.
<|end_chunk_774|><|start_chunk_775|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/get_base_plane_ -calibration
<|end_chunk_775|><|start_chunk_776|>
## API version 1 (deprecated)
<|end_chunk_776|><|start_chunk_777|>
### Page 172
PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/get_base_plane_calibration
<|end_chunk_777|><|start_chunk_778|>
 Request 

Required arguments:
pose_frame: see Hand-eye calibration (Section 6.4.6.8).
Potentially required arguments:
robot...pose: see Hand-eye calibration (Section 6.4.6.8).
The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "pose_frame": "string",
        "robot...pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        }
    }
}
```

<|end_chunk_778|><|start_chunk_779|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_base_plane_calibration",
    "response": {
        "plane": {
            "distance": "float64",
            "normal": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "pose_frame": "string"
        },
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

delete_base_plane_calibration

Deletes the configured base-plane calibration.
<|end_chunk_779|><|start_chunk_780|>
## Details

This service can be called as follows.
<|end_chunk_780|><|start_chunk_781|>
### Page 173<|end_chunk_781|><|start_chunk_782|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/delete_base_ $\ldots$ plane_calibration
<|end_chunk_782|><|start_chunk_783|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/delete_base_plane_ $\ldots$ calibration
<|end_chunk_783|><|start_chunk_784|>
## Request

This service has no arguments.
<|end_chunk_784|><|start_chunk_785|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "delete_base_plane_calibration",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

set_preferred_orientation

Persistently stores the preferred orientation of the TCP to compute the reachability of the grasps, which is used for filtering and, optionally, sorting the grasps returned by the detect_object service (see Setting the preferred orientation of the TCP, Section 6.4.6.5).
<|end_chunk_785|><|start_chunk_786|>
## Details

This service can be called as follows.
<|end_chunk_786|><|start_chunk_787|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/set_preferred_ $\ldots$ orientation
<|end_chunk_787|><|start_chunk_788|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/set_preferred_orientation
<|end_chunk_788|><|start_chunk_789|>
## Request

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string"
    }
}
```
<|end_chunk_789|><|start_chunk_790|>
### Page 174<|end_chunk_790|><|start_chunk_791|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_preferred_orientation",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_preferred_orientation

Returns the preferred orientation of the TCP to compute the reachability of the grasps, which is used for filtering and, optionally, sorting the grasps returned by the detect_object service (see Setting the preferred orientation of the TCP, Section 6.4.6.5).
<|end_chunk_791|><|start_chunk_792|>
## Details

This service can be called as follows.
<|end_chunk_792|><|start_chunk_793|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/get_preferred_ ...orientation
<|end_chunk_793|><|start_chunk_794|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/get_preferred_orientation
<|end_chunk_794|><|start_chunk_795|>
## Request

This service has no arguments.
<|end_chunk_795|><|start_chunk_796|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_preferred_orientation",
    "response": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string",
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

set_sorting_strategies

Persistently stores the sorting strategy for sorting the grasps and detected objects returned by the detect_object service (see Detection of objects, Section 6.4.6.7).
<|end_chunk_796|><|start_chunk_797|>
### Page 175<|end_chunk_797|><|start_chunk_798|>
 Details 

This service can be called as follows.
<|end_chunk_798|><|start_chunk_799|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/set_sorting...strategies
<|end_chunk_799|><|start_chunk_800|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/set_sorting_strategies
<|end_chunk_800|><|start_chunk_801|>
## Request

Only one strategy may have a weight greater than 0 . If all weight values are set to 0 , the module will use the default sorting strategy.

If the weight for direction is set, the vector must contain the direction vector and pose_frame must be either camera or external.

If the weight for distance_to_point is set, point must contain the sorting point and pose_frame must be either camera or external.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "direction": {
            "pose_frame": "string",
            "vector": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "weight": "float64"
        },
        "distance_to_point": {
            "farthest_first": "bool",
            "point": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "pose_frame": "string",
            "weight": "float64"
        },
        "preferred_orientation": {
            "weight": "float64"
        }
    }
}
```

<|end_chunk_801|><|start_chunk_802|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_sorting_strategies",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
```
<|end_chunk_802|><|start_chunk_803|>
### Page 176
get_sorting_strategies

Returns the sorting strategy for sorting the grasps and detected objects returned by the detect_object service (see Detection of objects, Section 6.4.6.7).
<|end_chunk_803|><|start_chunk_804|>
 Details 

This service can be called as follows.
<|end_chunk_804|><|start_chunk_805|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/get_sorting...
...strategies
<|end_chunk_805|><|start_chunk_806|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/get_sorting_strategies
<|end_chunk_806|><|start_chunk_807|>
## Request

This service has no arguments.
<|end_chunk_807|><|start_chunk_808|>
## Response

All weight values are 0 when the module uses the default sorting strategy.
The definition for the response with corresponding datatypes is:

```
{
    "name": "get_sorting_strategies",
    "response": {
        "direction": {
            "pose_frame": "string",
            "vector": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "weight": "float64"
    },
    "distance_to_point": {
        "farthest_first": "bool",
        "point": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose_frame": "string",
        "weight": "float64"
    },
    "preferred_orientation": {
        "weight": "float64"
    },
    "return_code": {
        "message": "string",
        "value": "int16"
    }
    }
}
```
<|end_chunk_808|><|start_chunk_809|>
### Page 177<|end_chunk_809|><|start_chunk_810|>
 reset_defaults 

Resets all parameters of the module to its default values, as listed in above table. Also resets preferred orientation and sorting strategies. The reset does not apply to templates and base-plane calibration.
<|end_chunk_810|><|start_chunk_811|>
## Details

This service can be called as follows.
<|end_chunk_811|><|start_chunk_812|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/reset_defaults
<|end_chunk_812|><|start_chunk_813|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/reset_defaults
<|end_chunk_813|><|start_chunk_814|>
## Request

This service has no arguments.
<|end_chunk_814|><|start_chunk_815|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_815|><|start_chunk_816|>
### 6.4.6.12 Internal services

The following services for configuring grasps can change in future without notice. Setting, retrieving and deleting grasps is recommend to be done via the Web GUI.
set_grasp
Persistently stores a grasp for the given object template on the rc_visard. All configured grasps are persistent over firmware updates and rollbacks.
<|end_chunk_816|><|start_chunk_817|>
## Details

This service can be called as follows.
<|end_chunk_817|><|start_chunk_818|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/set_grasp
<|end_chunk_818|><|start_chunk_819|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/set_grasp
<|end_chunk_819|><|start_chunk_820|>
## Request

Details for the definition of the grasp type are given in Setting of grasp points (Section 6.4.6.4).
<|end_chunk_820|><|start_chunk_821|>
### Page 178
The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "grasp": {
            "gripper_id": "string",
            "id": "string",
            "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        },
        "priority": "int8",
        "replication": {
            "max_x_deg": "float64",
            "min_x_deg": "float64",
            "origin": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
                "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            }
            },
            "step_x_deg": "float64"
        },
        "template_id": "string"
    }
    }
}
```

<|end_chunk_821|><|start_chunk_822|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_grasp",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

set_all_grasps

Replaces the list of grasps for the given object template on the $r c \_v i s a r d$.
<|end_chunk_822|><|start_chunk_823|>
### Page 179<|end_chunk_823|><|start_chunk_824|>
 Details 

This service can be called as follows.
<|end_chunk_824|><|start_chunk_825|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/set_all_grasps
<|end_chunk_825|><|start_chunk_826|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/set_all_grasps
<|end_chunk_826|><|start_chunk_827|>
## Request

Details for the definition of the grasp type are given in Setting of grasp points (Section 6.4.6.4).

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "grasps": [
            {
            "gripper_id": "string",
            "id": "string",
            "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "priority": "int8",
            "replication": {
            "max_x_deg": "float64",
            "min_x_deg": "float64",
            "origin": {
                    "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    }
                    },
                    "step_x_deg": "float64"
                    },
                    "template_id": "string"
            }
        ],
        "template_id": "string"
    }
}
```

Response
<|end_chunk_827|><|start_chunk_828|>
### Page 180
The definition for the response with corresponding datatypes is:

```
{
    "name": "set_all_grasps",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_grasps

Returns all configured grasps which have the requested grasp_ids and belong to the requested template_ids.
<|end_chunk_828|><|start_chunk_829|>
 Details 

This service can be called as follows.
<|end_chunk_829|><|start_chunk_830|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/get_grasps
<|end_chunk_830|><|start_chunk_831|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/get_grasps
<|end_chunk_831|><|start_chunk_832|>
## Request

If no grasp_ids are provided, all grasps belonging to the requested template_ids are returned. If no template_ids are provided, all grasps with the requested grasp_ids are returned. If neither IDs are provided, all configured grasps are returned.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "grasp_ids": [
            "string"
        ],
        "template_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_832|><|start_chunk_833|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_grasps",
    "response": {
        "grasps": [
            {
            "gripper_id": "string",
            "id": "string",
            "pose": {
                    "orientation": {
                        "w": "float64",
```
<|end_chunk_833|><|start_chunk_834|>
### Page 181
(continued from previous page)

```
            "x": "float64",
            "y": "float64",
            "z": "float64"
            },
            "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
        },
        "priority": "int8",
        "replication": {
            "max_x_deg": "float64",
            "min_x_deg": "float64",
            "origin": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "step_x_deg": "float64"
        },
        "template_id": "string"
    }
    ],
    "return_code": {
        "message": "string",
        "value": "int16"
    }
    }
}
```

delete_grasps

Deletes all grasps with the requested grasp_ids that belong to the requested template_ids.
<|end_chunk_834|><|start_chunk_835|>
 Details 

This service can be called as follows.
<|end_chunk_835|><|start_chunk_836|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/delete_grasps
<|end_chunk_836|><|start_chunk_837|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/delete_grasps
<|end_chunk_837|><|start_chunk_838|>
## Request

If no grasp_ids are provided, all grasps belonging to the requested template_ids are deleted. The template_ids list must not be empty.

The definition for the request arguments with corresponding datatypes is:
<|end_chunk_838|><|start_chunk_839|>
### Page 182
```
{
    "args": {
        "grasp_ids": [
            "string"
        ],
        "template_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_839|><|start_chunk_840|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "delete_grasps",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_symmetric_grasps

Returns all grasps that are symmetric to the given grasp.
<|end_chunk_840|><|start_chunk_841|>
## Details

This service can be called as follows.
<|end_chunk_841|><|start_chunk_842|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_silhouettematch/services/get_symmetric_ -grasps
<|end_chunk_842|><|start_chunk_843|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_silhouettematch/services/get_symmetric_grasps
<|end_chunk_843|><|start_chunk_844|>
## Request

Details for the definition of the grasp type are given in Setting of grasp points (Section 6.4.6.4).

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "grasp": {
            "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
```
<|end_chunk_844|><|start_chunk_845|>
### Page 183
![img-43.jpeg](img-43.jpeg)
<|end_chunk_845|><|start_chunk_846|>
 Response 

The first grasp in the returned list is the one that was passed with the service call. If the object template does not have an exact symmetry, only the grasp passed with the service call will be returned. If the object template has a continuous symmetry (e.g. a cylindrical object), only 12 equally spaced sample grasps will be returned.

Details for the definition of the grasp type are given in Setting of grasp points (Section 6.4.6.4).

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_symmetric_grasps",
    "response": {
        "grasps": [
            {
                "pose": {
                    "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    }
            },
            "replication": {
            "max_x_deg": "float64",
            "min_x_deg": "float64",
            "origin": {
            "orientation": {
                    "w": "float64",
```
<|end_chunk_846|><|start_chunk_847|>
### Page 184
![img-44.jpeg](img-44.jpeg)
<|end_chunk_847|><|start_chunk_848|>
 6.4.6.13 Return codes 

Each service response contains a return. code, which consists of a value plus an optional message. A successful service returns with a return. code value of $\theta$. Negative return. code values indicate that the service failed. Positive return. code values indicate that the service succeeded with additional information.
<|end_chunk_848|><|start_chunk_849|>
### Page 185
Table 6.38: Return codes of the SilhouetteMatch module services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| $-1$ | An invalid argument was provided. |
| $-3$ | An internal timeout occurred, e.g. during object detection. |
| $-4$ | Data acquisition took longer than allowed. |
| $-7$ | Data could not be read or written to persistent storage. |
| $-8$ | Module is not in a state in which this service can be called. E.g. detect...object cannot be <br> called if there is no base-plane calibration. |
| $-10$ | New element could not be added as the maximum storage capacity of regions of interest or <br> templates has been exceeded. |
| $-100$ | An internal error occurred. |
| $-101$ | Detection of the base plane failed. |
| $-102$ | The hand-eye calibration changed since the last base-plane calibration. |
| $-104$ | Offset between the base plane normal and the camera's line of sight exceeds 10 degrees. |
| 10 | The maximum storage capacity of regions of interest or templates has been reached. |
| 11 | An existing element was overwritten. |
| 100 | The requested load carrier was not detected in the scene. |
| 101 | None of the detected grasps is reachable. |
| 102 | The detected load carrier is empty. |
| 103 | All detected grasps are in collision. |
| 107 | The base plane was not transformed to the current camera pose, e.g. because no robot <br> pose was provided during base-plane calibration. |
| 108 | The template is deprecated. |
| 109 | The plane for object detection does not fit to the load carrier, e.g. objects are below the load <br> carrier floor. |
| 111 | The detection result's pose could not be refined with the point cloud because the template's <br> outer contour is not closed. |
| 113 | No gripper was found for collision checking. |
| 114 | Collision checking during retraction was skipped, e.g. because no load carrier or no <br> pre-grasp offset were given. |
| 151 | The object template has a continuous symmetry. |
| 999 | Additional hints for application development |
<|end_chunk_849|><|start_chunk_850|>
 6.4.6.14 Template API 

For template upload, download, listing and removal, special REST-API endpoints are provided. Templates can also be uploaded, downloaded and removed via the Web GUI. The templates include the grasp points, if grasp points have been configured. Up to 50 templates can be stored persistently on the $r c \_v i s a r d$.
<|end_chunk_850|><|start_chunk_851|>
## GET /templates/rc_silhouettematch

Get list of all rc_silhouettematch templates.
<|end_chunk_851|><|start_chunk_852|>
## Template request

GET /api/v2/templates/rc_silhouettematch HTTP/1.1
<|end_chunk_852|><|start_chunk_853|>
## Template response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": "string"
```

(continues on next page)
<|end_chunk_853|><|start_chunk_854|>
### Page 186<|end_chunk_854|><|start_chunk_855|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_855|><|start_chunk_856|>
## Status Codes

- 200 OK - successful operation (returns array of Template)
- 404 Not Found - node not found

<|end_chunk_856|><|start_chunk_857|>
## Referenced Data Models

- Template (Section 7.3.4)

GET /templates/rc_silhouettematch/\{id\}
Get a rc_silhouettematch template. If the requested content-type is application/octet-stream, the template is returned as file.
<|end_chunk_857|><|start_chunk_858|>
## Template request

GET /api/v2/templates/rc_silhouettematch/<id> HTTP/1.1
<|end_chunk_858|><|start_chunk_859|>
## Template response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": "string"
}
```

<|end_chunk_859|><|start_chunk_860|>
## Parameters

- id (string) - id of the template (required)

<|end_chunk_860|><|start_chunk_861|>
## Response Headers

- Content-Type - application/json application/ubjson application/octet-stream

<|end_chunk_861|><|start_chunk_862|>
## Status Codes

- 200 OK - successful operation (returns Template)
- 404 Not Found - node or template not found

<|end_chunk_862|><|start_chunk_863|>
## Referenced Data Models

- Template (Section 7.3.4)

PUT /templates/rc_silhouettematch/\{id\}
Create or update a rc_silhouettematch template.
<|end_chunk_863|><|start_chunk_864|>
## Template request

PUT /api/v2/templates/rc_silhouettematch/<id> HTTP/1.1
Accept: multipart/form-data application/json
<|end_chunk_864|><|start_chunk_865|>
## Template response
<|end_chunk_865|><|start_chunk_866|>
### Page 187
```
MTTP/1.1 200 OK
Content-Type: application/json
{
    "id": "string"
}
```

<|end_chunk_866|><|start_chunk_867|>
 Parameters 

- id (string) - id of the template (required)

<|end_chunk_867|><|start_chunk_868|>
## Form Parameters

- file - template or dxf file (required)
- object_height - object height in meters, required when uploading dxf (optional)
- units - Units for dxf file if not included in dxf (one of mm, cm, m, in, ft) (optional)

<|end_chunk_868|><|start_chunk_869|>
## Request Headers

- Accept - multipart/form-data application/json

<|end_chunk_869|><|start_chunk_870|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_870|><|start_chunk_871|>
## Status Codes

- 200 OK - successful operation (returns Template)
- 400 Bad Request - Template is not valid or max number of templates reached
- 403 Forbidden - forbidden, e.g. because there is no valid license for this module.
- 404 Not Found - node or template not found
- 413 Request Entity Too Large - Template too large

<|end_chunk_871|><|start_chunk_872|>
## Referenced Data Models

- Template (Section 7.3.4)

DELETE /templates/rc_silhouettematch/\{id\}
Remove a rc_silhouettematch template.
<|end_chunk_872|><|start_chunk_873|>
## Template request

DELETE /api/v2/templates/rc_silhouettematch/<id> HTTP/1.1
Accept: application/json application/ubjson
<|end_chunk_873|><|start_chunk_874|>
## Parameters

- id (string) - id of the template (required)

<|end_chunk_874|><|start_chunk_875|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_875|><|start_chunk_876|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_876|><|start_chunk_877|>
## Status Codes

- 200 OK - successful operation
- 403 Forbidden - forbidden, e.g. because there is no valid license for this module.
<|end_chunk_877|><|start_chunk_878|>
### Page 188
- 404 Not Found - node or template not found

<|end_chunk_878|><|start_chunk_879|>
 6.5 Configuration modules 

The $r c \_v i s a r d$ provides several configuration modules which enable the user to configure the $r c \_v i s a r d$ for specific applications.

The configuration modules are:

- Hand-eye calibration (rc_hand_eye_calibration, Section 6.5.1) enables the user to calibrate the camera with respect to a robot, either via the Web GUI or the REST-API.
- CollisionCheck (rc_collision_check, Section 6.5.2) provides an easy way to check if a gripper is in collision.
- Camera calibration (rc_stereocalib, Section 6.5.3) enables the user to check and perform camera calibration via the WEB GUI (Section 7.1).
- IO and Projector Control (rc_iocontrol, Section 6.5.4) provides control over the sensor's general purpose inputs and outputs with special modes for controlling an external random dot projector.

<|end_chunk_879|><|start_chunk_880|>
### 6.5.1 Hand-eye calibration

For applications, in which the camera is integrated into one or more robot systems, it needs to be calibrated w.r.t. some robot reference frames. For this purpose, the $r c \_v i s a r d$ is shipped with an onboard calibration routine called the hand-eye calibration module. It is a base module which is available on every $r c \_v i s a r d$.

Note: The implemented calibration routine is completely agnostic about the user-defined robot frame to which the camera is calibrated. It might be a robot's end-effector (e.g., flange or tool center point) or any point on the robot structure. The method's only requirement is that the pose (i.e., translation and rotation) of this robot frame w.r.t. a user-defined external reference frame (e.g., world or robot mounting point) is exactly observable by the robot controller and can be reported to the calibration module.

The Calibration routine (Section 6.5.1.3) itself is an easy-to-use multi-step procedure using a calibration grid which can be obtained from Roboception.
<|end_chunk_880|><|start_chunk_881|>
### 6.5.1.1 Calibration interfaces

The following two interfaces are offered to conduct hand-eye calibration:

1. All services and parameters of this module required to conduct the hand-eye calibration programmatically are exposed by the $r c \_v i s a r d$ 's REST-API interface (Section 7.3). The respective node name of this module is rc_hand_eye_calibration and the respective service calls are documented Services (Section 6.5.1.5).

Note: The described approach requires a network connection between the $r c \_v i s a r d$ and the robot controller to pass robot poses from the controller to the $r c \_v i s a r d$ 's calibration module.
2. For use cases where robot poses cannot be passed programmatically to the $r c \_v i s a r d$ 's hand-eye calibration module, the Web GUI's Hand-Eye Calibration page under Configuration offers a guided process to conduct the calibration routine manually.
<|end_chunk_881|><|start_chunk_882|>
### Page 189
Note: During the process, the described approach requires the user to manually enter into the Web GUI robot poses, which need to be accessed from the respective robot-teaching or handheld device.
<|end_chunk_882|><|start_chunk_883|>
 6.5.1.2 Camera mounting 

As illustrated in Fig. 6.20 and Fig. 6.22, two different use cases w.r.t. to the mounting of the camera generally have to be considered:
a. The camera is mounted on the robot, i.e., it is mechanically fixed to a robot link (e.g., at its flange or a flange-mounted tool), and hence moves with the robot.
b. The camera is not mounted on the robot but is fixed to a table or other place in the robot's vicinity and remains at a static position w.r.t. the robot.
While the general Calibration routine (Section 6.5.1.3) is very similar in both use cases, the calibration process's output, i.e., the resulting calibration transform, will be semantically different, and the fixture of the calibration grid will also differ.
Calibration with a robot-mounted camera When calibrating a robot-mounted camera with the robot, the calibration grid has to be secured in a static position w.r.t. the robot, e.g., on a table or some other fixed-base coordinate system as sketched in Fig. 6.20.

Warning: It is extremely important that the calibration grid does not move during step 2 of the Calibration routine (Section 6.5.1.3). Securely fixing its position to prevent unintended movements such as those caused by vibrations, moving cables, or the like is therefore strongly recommended.

The result of the calibration (step 3 of the Calibration routine, Section 6.5.1.3) is a pose $\mathrm{T}_{\text {camera }}^{\text {robot }}$ describing the (previously unknown) relative positional and rotational transformation from the camera frame into the user-selected robot frame such that

$$
\mathbf{p}_{\text {robot }}=\mathbf{R}_{\text {camera }}^{\text {robot }} \cdot \mathbf{p}_{\text {camera }}+\mathbf{t}_{\text {camera }}^{\text {robot }}
$$

where $\mathbf{p}_{\text {robot }}=(x, y, z)^{T}$ is a 3D point with its coordinates expressed in the robot frame, $\mathbf{p}_{\text {camera }}$ is the same point represented in the camera coordinate frame, and $\mathbf{R}_{\text {camera }}^{\text {robot }}$ as well as $\mathbf{t}_{\text {camera }}^{\text {robot }}$ are the corresponding $3 \times 3$ rotation matrix and $3 \times 1$ translation vector of the pose $\mathbf{T}_{\text {camera }}^{\text {robot }}$, respectively. In practice, in the calibration result and in the provided robot poses, the rotation is defined by Euler angles or as quaternion instead of a rotation matrix (see Pose formats, Section 12.1).
<|end_chunk_883|><|start_chunk_884|>
### Page 190
![img-45.jpeg](img-45.jpeg)

Fig. 6.20: Important frames and transformations for calibrating a camera that is mounted on a general robot. The camera is mounted with a fixed relative position to a user-defined robot frame (e.g., flange or TCP). It is important that the pose $\mathbf{T}_{\text {robot }}^{\text {ext }}$ of this robot frame w.r.t. a user-defined external reference frame ext is observable during the calibration routine. The result of the calibration process is the desired calibration transformation $\mathbf{T}_{\text {camera }}^{\text {robot }}$, i.e., the pose of the camera frame within the user-defined robot frame.

Additional user input is required if the movement of the robot is constrained and the robot can rotate the Tool Center Point (TCP) only around one axis. This is typically the case for robots with four Degrees Of Freedom (4DOF) that are often used for palletizing tasks. In this case, the user must specify which axis of the robot frame is the rotation axis of the TCP. Further, the signed offset from the TCP to the camera coordinate system along the TCP rotation axis has to be provided. Fig. 6.21 illustrates the situation.

For the $r c \_v i s a r d$, the camera coordinate system is located in the optical center of the left camera. The approximate location is given in section Coordinate frames (Section 3.7).
![img-46.jpeg](img-46.jpeg)

Fig. 6.21: In case of a 4DOF robot, the TCP rotation axis and the offset from the TCP to the camera coordinate system along the TCP rotation axis must be provided. In the illustrated case, this offset is negative.

Calibration with a statically-mounted camera In use cases where the camera is positioned statically w.r.t. the robot, the calibration grid needs to be mounted to the robot as shown for example in Fig. 6.22 and Fig. 6.23.
<|end_chunk_884|><|start_chunk_885|>
### Page 191
Note: The hand-eye calibration module is completely agnostic about the exact mounting and positioning of the calibration grid w.r.t. the user-defined robot frame. That means, the relative positioning of the calibration grid to that frame neither needs to be known, nor it is relevant for the calibration routine, as shown in Fig. 6.23.

Warning: It is extremely important that the calibration grid is attached securely to the robot such that it does not change its relative position w.r.t. the user-defined robot frame during step 2 of the Calibration routine (Section 6.5.1.3).

In this use case, the result of the calibration (step 3 of the Calibration routine, Section 6.5.1.3) is the pose $\mathbf{T}_{\text {camera }}^{\text {ext }}$ describing the (previously unknown) relative positional and rotational transformation between the camera frame and the user-selected external reference frame ext such that

$$
\mathbf{p}_{\text {ext }}=\mathbf{R}_{\text {camera }}^{\text {ext }} \cdot \mathbf{p}_{\text {camera }}+\mathbf{t}_{\text {camera }}^{\text {ext }}
$$

where $\mathbf{p}_{\text {ext }}=(x, y, z)^{T}$ is a 3D point with its coordinates expressed in the external reference frame ext, $\mathbf{p}_{\text {camera }}$ is the same point represented in the camera coordinate frame, and $\mathbf{R}_{\text {camera }}^{\text {ext }}$ as well as $\mathbf{t}_{\text {camera }}^{\text {ext }}$ are the corresponding $3 \times 3$ rotation matrix and $3 \times 1$ translation vector of the pose $\mathbf{T}_{\text {camera }}^{\text {ext }}$, respectively. In practice, in the calibration result and in the provided robot poses, the rotation is defined by Euler angles or as quaternion instead of a rotation matrix (see Pose formats, Section 12.1).
![img-47.jpeg](img-47.jpeg)

Fig. 6.22: Important frames and transformations for calibrating a statically mounted camera: The latter is mounted with a fixed position relative to a user-defined external reference frame ext (e.g., the world coordinate frame or the robot's mounting point). It is important that the pose $\mathbf{T}_{\text {robot }}^{\text {ext }}$ of the user-defined robot frame w.r.t. this frame is observable during the calibration routine. The result of the calibration process is the desired calibration transformation $\mathbf{T}_{\text {camera }}^{\text {ext }}$, i.e., the pose of the camera frame in the userdefined external reference frame ext.
<|end_chunk_885|><|start_chunk_886|>
### Page 192
![img-48.jpeg](img-48.jpeg)

Fig. 6.23: Alternate mounting options for attaching the calibration grid to the robot

Additional user input is required if the movement of the robot is constrained and the robot can rotate the Tool Center Point (TCP) only around one axis. This is typically the case for robots with four Degrees Of Freedom (4DOF) that are often used for palletizing tasks. In this case, the user must specify which axis of the robot frame is the rotation axis of the TCP. Further, the signed offset from the TCP to the visible surface of the calibration grid along the TCP rotation axis has to be provided. The grid must be mounted such that the TCP rotation axis is orthogonal to the grid. Fig. 6.24 illustrates the situation.
![img-49.jpeg](img-49.jpeg)

Fig. 6.24: In case of a 4DOF robot, the TCP rotation axis and the offset from the TCP to the visible surface of the grid along the TCP rotation axis must be provided. In the illustrated case, this offset is negative.
<|end_chunk_886|><|start_chunk_887|>
 6.5.1.3 Calibration routine 

The hand-eye calibration can be performed manually using the Web GUI (Section 7.1) or programmatically via the REST-API interface (Section 7.3). The general calibration routine will be described by following the steps of the hand-eye calibration wizard provided on the Web GUI. This wizard can be found in the rc_visard's Web GUI under Configuration $\rightarrow$ Hand-Eye Calibration. References to the corresponding REST-API calls are provided at the appropriate places.
<|end_chunk_887|><|start_chunk_888|>
### Page 193<|end_chunk_888|><|start_chunk_889|>
 Step 1: Hand-Eye Calibration Status 

The starting page of the hand-eye calibration wizard shows the current status of the hand-eye calibration. If a hand-eye calibration is saved on the $r c \_v i s a r d$, the calibration transformation is displayed here (see Fig. 6.25).
![img-50.jpeg](img-50.jpeg)

Fig. 6.25: Current status of the hand-eye calibration in case a hand-eye calibration is saved

To query the hand-eye calibration status programmatically, the module's REST-API offers the get_calibration service call (see Services, Section 6.5.1.5). An existing hand-eye calibration can be removed by pressing Remove Calibration or using remove_calibration in the REST-API (see Services, Section 6.5.1.5).

To start a new hand-eye calibration, click on Perform Hand-Eye Calibration or Next.
<|end_chunk_889|><|start_chunk_890|>
## Step 2: Checking Grid Detection

To achieve good calibration results, the images should be well exposed so that the calibration grid can be detected accurately and reliably. In this step, the grid detection can be checked and the camera settings can be adjusted if necessary. In case parts of the calibration grid are overexposed, the respective squares of the calibration grid will be highlighted in red. A successful grid detection is visualized by green check marks on every square of the calibration grid and a thick green border around the grid as shown in Fig. 6.26.
<|end_chunk_890|><|start_chunk_891|>
### Page 194
![img-51.jpeg](img-51.jpeg)

Fig. 6.26: Checking the calibration grid detection
<|end_chunk_891|><|start_chunk_892|>
 Step 3: Record Poses 

In this step, the user records images of the calibration grid at several different robot poses. These poses must each ensure that the calibration grid is completely visible in the left camera image. Furthermore, the robot poses need to be selected properly to achieve a variety of different perspectives for the camera to perceive the calibration grid. Fig. 6.27 shows a schematic recommendation of four different grid positions which should be recorded from a close and a far point of view, resulting in eight images for the calibration.
<|end_chunk_892|><|start_chunk_893|>
### Page 195
![img-52.jpeg](img-52.jpeg)

Fig. 6.27: Recommended views on the calibration grid during the calibration procedure. In case of a 4DOF robot, other views have to be chosen, which should be as different as possible.

Warning: Calibration quality, i.e., the accuracy of the calculated calibration result, depends on the calibration-grid views provided. The more diverse the perspectives are, the better is the calibration. Choosing very similar views, i.e., varying the robot pose only slightly before recording a new calibration pose, may lead to inaccurate estimation of the desired calibration transformation.

After the robot reaches each calibration pose, the corresponding pose $\mathrm{T}_{\text {robot }}^{\text {ext }}$ of the user-defined robot frame in the user-defined external reference frame ext needs to be reported to the hand-eye calibration module. For this purpose, the module offers different slots to store the reported poses and the corresponding left camera images. All filled slots will then be used to calculate the desired calibration transformation between the camera frame and either the user-defined robot frame (robot-mounted camera) or the user-defined external reference frame ext (static camera).
In the Web GUI, the user can choose between many different pose formats for providing the calibration poses (see Pose formats, Section 12.1). When calibrating using the REST-API, the poses are always given in $X Y Z+q u a t e r n i o n$. The Web GUI offers eight slots (Close View 1, Close View 2, etc.) for the user to fill manually with robot poses. Next to each slot, a figure suggests a respective dedicated viewpoint on the grid. For each slot, the robot should be operated to achieve the suggested view.
<|end_chunk_893|><|start_chunk_894|>
### Page 196
![img-53.jpeg](img-53.jpeg)

Fig. 6.28: Filling the first slot in the hand-eye calibration process for a statically mounted camera

To record a calibration pose, click on Set Pose for the respective slot and enter the robot frame's pose into the respective text fields. The pose is then stored with the corresponding camera image by clicking the Take Picture to Proceed button. This will save the calibration pose in the respective slot.

To transmit the poses programmatically, the module's REST-API offers the set_pose service call (see Services, Section 6.5.1.5).

Note: The user's acquisition of robot pose data depends on the robot model and manufacturer - it might be read from a teaching or handheld device, which is shipped with the robot.

Warning: Please be careful to correctly and accurately enter the values; even small variations or typos may lead to calibration-process failure.

The Web GUI displays the currently saved poses (only with slot numbers from 0 to 7 ) with their camera
<|end_chunk_894|><|start_chunk_895|>
### Page 197
images and also allows to delete them by clicking Delete Pose to remove a single pose, or clicking Clear all Poses to remove all poses. In the REST-API the currently stored poses can be retrieved via get_poses and removed via delete_poses for single poses or reset_calibration for removing all poses (see Services, Section 6.5.1.5).
When at least four poses are set, the user can continue to the computation of the calibration result by pressing Next.

Note: To successfully calculate the hand-eye calibration transformation, at least four different robot calibration poses need to be reported and stored in slots. However, to prevent errors induced by possible inaccurate measurements, at least eight calibration poses are recommended.
<|end_chunk_895|><|start_chunk_896|>
 Step 4: Compute Calibration 

Before computing the calibration result, the user has to provide the correct calibration parameters. These include the exact calibration grid dimensions and the sensor mounting type. The Web GUI also offers settings for calibrating 4DOF robots. In this case, the rotation axis, as well as the offset from the TCP to the camera coordinate system (robot-mounted camera) or grid surface (statically mounted camera) must be given. For the REST-API, the respective parameters are listed in Parameters (Section 6.5.1.4).
![img-54.jpeg](img-54.jpeg)

Fig. 6.29: Defining hand-eye calibration parameters and computing the calibration result via the rc_visard's Web GUI
<|end_chunk_896|><|start_chunk_897|>
### Page 198
When the parameters are correct, the desired calibration transformation can be computed from the collected poses and camera images by clicking Compute Calibration. The REST-API offers this functionality via the calibrate service call (see Services, Section 6.5.1.5).

Depending on the way the camera is mounted, the calibration result contains the transformation (i.e., the pose) between the camera frame and either the user-defined robot frame (robot-mounted camera) or the user-defined external reference frame ext (statically mounted camera); see Camera mounting (Section 6.5.1.2).

To enable users to judge the quality of the resulting calibration transformation, the translational and rotational calibration errors are reported, which are computed from the variance of the calibration result.

If the calibration error is not acceptable, the user can change the calibration parameters and recompute the result, or return to step 3 of the calibration procedure and add more poses or update poses.

To save the calibration result, press Save Calibration or use the REST-API save_calibration service call (see Services, Section 6.5.1.5).
<|end_chunk_897|><|start_chunk_898|>
 6.5.1.4 Parameters 

The hand-eye calibration module is called rc_hand_eye_calibration in the REST-API and is represented in the Web GUI (Section 7.1) under Configuration $\rightarrow$ Hand-Eye Calibration. The user can change the calibration parameters there or use the REST-API interface (Section 7.3).
<|end_chunk_898|><|start_chunk_899|>
## Parameter overview

This module offers the following run-time parameters:
Table 6.39: The rc_hand_eye_calibration module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :-- | :--: | :--: | :--: | :--: | :-- |
| grid_height | float64 | 0.0 | 10.0 | 0.0 | The height of the calibration pattern <br> in meters |
| grid_width | float64 | 0.0 | 10.0 | 0.0 | The width of the calibration pattern <br> in meters |
| robot_mounted | bool | false | true | true | Whether the camera is mounted on <br> the robot |
| tag_ids | string | - | - | - | Optional, comma separated list of <br> AprilTag IDs that will be calibrated <br> too |
| tcp_offset | float64 | -10.0 | 10.0 | 0.0 | Offset from TCP along <br> tcp_rotation_axis |
| tcp_rotation_axis | int32 | -1 | 2 | -1 | -1 for off, 0 for x, 1 for y, 2 for z |
<|end_chunk_899|><|start_chunk_900|>
## Description of run-time parameters

The parameter descriptions are given with the corresponding Web GUI names in brackets.
grid_width (Width)
Width of the calibration grid in meters. The width should be given with a very high accuracy, preferably with sub-millimeter accuracy.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_900|><|start_chunk_901|>
## API version 2
<|end_chunk_901|><|start_chunk_902|>
### Page 199
PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/parameters? ...grid_width=<value>
<|end_chunk_902|><|start_chunk_903|>
 API version 1 (deprecated) 

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/parameters?grid_width=<value>
<|end_chunk_903|><|start_chunk_904|>
## grid_height (Height)

Height of the calibration grid in meters. The height should be given with a very high accuracy, preferably with sub-millimeter accuracy.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_904|><|start_chunk_905|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/parameters? ...grid_height=<value>
<|end_chunk_905|><|start_chunk_906|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/parameters?grid_height=<value>
<|end_chunk_906|><|start_chunk_907|>
## robot_mounted (Sensor Mounting)

If set to true, the camera is mounted on the robot. If set to false, the camera is mounted statically and the calibration grid is mounted on the robot.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_907|><|start_chunk_908|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/parameters? ...robot_mounted=<value>
<|end_chunk_908|><|start_chunk_909|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/parameters?robot_mounted=<value>
<|end_chunk_909|><|start_chunk_910|>
## tcp_offset (TCP Offset)

The signed offset from the TCP to the camera coordinate system (robot-mounted sensor) or the visible surface of the calibration grid (statically mounted sensor) along the TCP rotation axis in meters. This is required if the robot's movement is constrained and it can rotate its TCP only around one axis (e.g., 4DOF robot).

Via the REST-API, this parameter can be set as follows.
<|end_chunk_910|><|start_chunk_911|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/parameters? ...tcp_offset=<value>
<|end_chunk_911|><|start_chunk_912|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/parameters?tcp_offset=<value>
<|end_chunk_912|><|start_chunk_913|>
### Page 200<|end_chunk_913|><|start_chunk_914|>
 tcp_rotation_axis (TCP Rotation Axis) 

The axis of the robot frame around which the robot can rotate its TCP. 0 is used for $X, 1$ for $Y$ and 2 for the $Z$ axis. This is required if the robot's movement is constrained and it can rotate its TCP only around one axis (e.g., 4DOF robot). -1 means that the robot can rotate its TCP around two independent rotation axes. tcp_offset is ignored in this case.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_914|><|start_chunk_915|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/parameters? --tcp_rotation_axis=<value>
<|end_chunk_915|><|start_chunk_916|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/parameters?tcp_rotation_axis= --<value>
<|end_chunk_916|><|start_chunk_917|>
### 6.5.1.5 Services

The REST-API service calls offered to programmatically conduct the hand-eye calibration and to restore this module's parameters are explained below.
get_calibration
returns the hand-eye calibration currently stored on the rc_visard.
<|end_chunk_917|><|start_chunk_918|>
## Details

This service can be called as follows.
<|end_chunk_918|><|start_chunk_919|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/get_ --calibration
<|end_chunk_919|><|start_chunk_920|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/get_calibration
<|end_chunk_920|><|start_chunk_921|>
## Request

This service has no arguments.
<|end_chunk_921|><|start_chunk_922|>
## Response

The field error gives the calibration error in pixels which is computed from the translational error translation_error_meter and the rotational error rotation_error_degree. This value is only given for compatibility with older versions. The translational and rotational errors should be preferred.

Table 6.40: Return codes of the get_calibration service call

| status | success | Description |
| :--: | :--: | :-- |
| 0 | true | returned valid calibration pose |
| 2 | false | calibration result is not available |

The definition for the response with corresponding datatypes is:
<|end_chunk_922|><|start_chunk_923|>
### Page 201
```
{
    "name": "get_calibration",
    "response": {
        "error": "float64",
        "message": "string",
        "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
        },
        "robot_mounted": "bool",
        "rotation_error_degree": "float64",
        "status": "int32",
        "success": "bool",
        "tags": [
            {
                "id": "string",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    }
            },
            "size": "float64"
        }
        ],
        "translation_error_meter": "float64"
    }
}
```

remove_calibration
removes the persistent hand-eye calibration on the rc_visard. After this call the get_calibration service reports again that no hand-eye calibration is available. This service call will also delete all the stored calibration poses and corresponding camera images in the slots.
<|end_chunk_923|><|start_chunk_924|>
 Details 

This service can be called as follows.
<|end_chunk_924|><|start_chunk_925|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/remove_ $\ldots$ calibration
<|end_chunk_925|><|start_chunk_926|>
## API version 1 (deprecated)
<|end_chunk_926|><|start_chunk_927|>
### Page 202
PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/remove_calibration
<|end_chunk_927|><|start_chunk_928|>
 Request 

This service has no arguments.
<|end_chunk_928|><|start_chunk_929|>
## Response

Table 6.41: Return codes of the get_calibration service call

| status | success | Description |
| :--: | :--: | :-- |
| 0 | true | removed persistent calibration, device reports as uncalibrated |
| 1 | true | no persistent calibration found, device reports as uncalibrated |
| 2 | false | could not remove persistent calibration |

The definition for the response with corresponding datatypes is:

```
{
    "name": "remove_calibration",
    "response": {
        "message": "string",
        "status": "int32",
        "success": "bool"
    }
}
```

set_pose
allows to provide a robot pose as calibration pose to the hand-eye calibration routine and records the current image of the calibration grid.
<|end_chunk_929|><|start_chunk_930|>
## Details

This service can be called as follows.
<|end_chunk_930|><|start_chunk_931|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/set_pose
<|end_chunk_931|><|start_chunk_932|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/set_pose
<|end_chunk_932|><|start_chunk_933|>
## Request

The slot argument is used to assign unique numbers to the different calibration poses. The range for slot is from 0 to 15 . At each instant when set. pose is called, an image is recorded. This service call fails if the grid was undetectable in the current image.
The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "pose": {
            "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
```
<|end_chunk_933|><|start_chunk_934|>
### Page 203
(continued from previous page)

```
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "slot": "uint32"
    }
}
```

<|end_chunk_934|><|start_chunk_935|>
 Response 

Table 6.42: Return codes of the set..pose service call

| status | success | Description |
| :--: | :--: | :-- |
| 1 | true | pose stored successfully |
| 3 | true | pose stored successfully; collected enough poses for calibration, <br> i.e., ready to calibrate |
| 4 | false | calibration grid was not detected, e.g., not fully visible in camera <br> image |
| 8 | false | no image data available |
| 12 | false | given orientation values are invalid |
| 13 | false | invalid slot number |

The field overexposed indicates if parts of the calibration grid were overexposed in this image.
The definition for the response with corresponding datatypes is:

```
{
    "name": "set..pose",
    "response": {
        "message": "string",
        "overexposed": "bool",
        "status": "int32",
        "success": "bool"
    }
}
```

get_poses
returns the robot poses that are currently stored for the hand-eye calibration routine.
<|end_chunk_935|><|start_chunk_936|>
## Details

This service can be called as follows.
<|end_chunk_936|><|start_chunk_937|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/get_poses
<|end_chunk_937|><|start_chunk_938|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/get_poses
<|end_chunk_938|><|start_chunk_939|>
## Request

This service has no arguments.
<|end_chunk_939|><|start_chunk_940|>
## Response
<|end_chunk_940|><|start_chunk_941|>
### Page 204
Table 6.43: Return codes of the get_poses service call

| status | success | Description |
| :--: | :--: | :-- |
| 0 | true | stored poses are returned |
| 1 | true | no calibration pose available |

The field overexposed indicates if parts of the calibration grid were overexposed in this image.

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_poses",
    "response": {
        "message": "string",
        "poses": [
            {
            "overexposed": "bool",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "slot": "uint32",
            "tag_ids": [
                "string"
            ]
        }
    ],
    "status": "int32",
    "success": "bool"
    }
}
```

delete_poses
deletes the calibration poses and corresponding images with the specified slots.
<|end_chunk_941|><|start_chunk_942|>
 Details 

This service can be called as follows.
<|end_chunk_942|><|start_chunk_943|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/delete_ -poses
<|end_chunk_943|><|start_chunk_944|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/delete_poses
<|end_chunk_944|><|start_chunk_945|>
## Request
<|end_chunk_945|><|start_chunk_946|>
### Page 205
The slots argument specifies which calibration poses should be deleted. If no slots are provided, nothing will be deleted.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "slots": [
            "uint32"
        ]
    }
}
```

<|end_chunk_946|><|start_chunk_947|>
 Response 

Table 6.44: Return codes of the delete_poses service call

| status | success | Description |
| :--: | :--: | :-- |
| 0 | true | poses successfully deleted |
| 1 | true | no slots given |

The definition for the response with corresponding datatypes is:

```
{
    "name": "delete_poses",
    "response": {
        "message": "string",
        "status": "int32",
        "success": "bool"
    }
}
```

reset_calibration
deletes all previously provided poses and corresponding images. The last saved calibration result is reloaded. This service might be used to (re-)start the hand-eye calibration from scratch.
<|end_chunk_947|><|start_chunk_948|>
## Details

This service can be called as follows.
<|end_chunk_948|><|start_chunk_949|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/reset_ $\ldots$ calibration
<|end_chunk_949|><|start_chunk_950|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/reset_calibration
<|end_chunk_950|><|start_chunk_951|>
## Request

This service has no arguments.
<|end_chunk_951|><|start_chunk_952|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_calibration",
    "response": {
```

(continues on next page)
<|end_chunk_952|><|start_chunk_953|>
### Page 206
(continued from previous page)

```
        "message": "string",
        "status": "int32",
        "success": "bool"
    }
}
```

calibrate
calculates and returns the hand-eye calibration transformation with the robot poses configured by the set...pose service.
<|end_chunk_953|><|start_chunk_954|>
 Details 

save_calibration must be called to make the calibration available for other modules via the get_calibration service call and to store it persistently.

Note: For calculating the hand-eye calibration transformation at least four robot calibration poses are required (see set...pose service). However, eight calibration poses are recommended.

This service can be called as follows.
<|end_chunk_954|><|start_chunk_955|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/calibrate
<|end_chunk_955|><|start_chunk_956|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/calibrate
<|end_chunk_956|><|start_chunk_957|>
## Request

This service has no arguments.
<|end_chunk_957|><|start_chunk_958|>
## Response

The field error gives the calibration error in pixels which is computed from the translational error translation_error_meter and the rotational error rotation_error_degree. This value is only given for compatibility with older versions. The translational and rotational errors should be preferred.

Table 6.45: Return codes of the calibrate service call

| status | success | Description |
| :--: | :--: | :-- |
| 0 | true | calibration successful, returned calibration result |
| 1 | false | not enough poses to perform calibration |
| 2 | false | calibration result is invalid, please verify the input data |
| 3 | false | given calibration grid dimensions are not valid |
| 4 | false | insufficient rotation, tcp_offset and tcp_rotation_axis must be <br> specified |
| 5 | false | sufficient rotation available, tcp_rotation_axis must be set to -1 |
| 6 | false | poses are not distinct enough from each other |

The definition for the response with corresponding datatypes is:

```
{
    "name": "calibrate",
    "response": {
        "error": "float64",
```
<|end_chunk_958|><|start_chunk_959|>
### Page 207
(continued from previous page)

```
    "message": "string",
    "pose": {
        "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        }
    },
    "robot_mounted": "bool",
    "rotation_error_degree": "float64",
    "status": "int32",
    "success": "bool",
    "tags": [
        {
            "id": "string",
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
                    }
                    },
                    "size": "float64"
        }
    ],
    "translation_error_meter": "float64"
    }
}
```

<|end_chunk_959|><|start_chunk_960|>
 save_calibration 

persistently saves the result of hand-eye calibration to the $r c \_v i s a r d$ and overwrites the existing one. The stored result can be retrieved any time by the get_calibration service. This service call will also delete all the stored calibration poses and corresponding camera images in the slots.
<|end_chunk_960|><|start_chunk_961|>
## Details

This service can be called as follows.
<|end_chunk_961|><|start_chunk_962|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/save_ -calibration
<|end_chunk_962|><|start_chunk_963|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/save_calibration
<|end_chunk_963|><|start_chunk_964|>
### Page 208<|end_chunk_964|><|start_chunk_965|>
 Request 

This service has no arguments.
<|end_chunk_965|><|start_chunk_966|>
## Response

Table 6.46: Return codes of the save_calibration service call

| status | success | Description |
| :--: | :--: | :-- |
| 0 | true | calibration saved successfully |
| 1 | false | could not save calibration file |
| 2 | false | calibration result is not available |

The definition for the response with corresponding datatypes is:

```
{
    "name": "save_calibration",
    "response": {
        "message": "string",
        "status": "int32",
        "success": "bool"
    }
}
```

set_calibration
sets the hand-eye calibration transformation with arguments of this call.
<|end_chunk_966|><|start_chunk_967|>
## Details

The calibration transformation is expected in the same format as returned by the calibrate and get_calibration calls. The given calibration information is also stored persistently on the sensor by internally calling save_calibration.

This service can be called as follows.
<|end_chunk_967|><|start_chunk_968|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/set_ $\ldots$ calibration
<|end_chunk_968|><|start_chunk_969|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/set_calibration
<|end_chunk_969|><|start_chunk_970|>
## Request

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "pose": {
            "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
```
<|end_chunk_970|><|start_chunk_971|>
### Page 209
(continued from previous page)

```
    }
    },
    "robot_mounted": "bool",
    "tags": [
        {
            "id": "string",
            "pose": {
            "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "size": "float64"
        }
    ]
    }
}
```

<|end_chunk_971|><|start_chunk_972|>
 Response 

Table 6.47: Return codes of the set_calibration service call

| status | success | Description |
| :--: | :--: | :-- |
| 0 | true | setting the calibration transformation was successful |
| 12 | false | given orientation values are invalid |

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_calibration",
    "response": {
        "message": "string",
        "status": "int32",
        "success": "bool"
    }
}
```

reset_defaults
restores and applies the default values for this module's parameters ("factory reset"). Does not affect the calibration result itself or any of the slots saved during calibration. Only parameters such as the grid dimensions and the mount type will be reset.
<|end_chunk_972|><|start_chunk_973|>
## Details

This service can be called as follows.
<|end_chunk_973|><|start_chunk_974|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services/reset_
$\sim$ defaults
<|end_chunk_974|><|start_chunk_975|>
## API version 1 (deprecated)
<|end_chunk_975|><|start_chunk_976|>
### Page 210
PUT http://<host>/api/v1/nodes/rc_hand_eye_calibration/services/reset_defaults
<|end_chunk_976|><|start_chunk_977|>
 Request 

This service has no arguments.
<|end_chunk_977|><|start_chunk_978|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_978|><|start_chunk_979|>
### 6.5.2 CollisionCheck
<|end_chunk_979|><|start_chunk_980|>
### 6.5.2.1 Introduction

The CollisionCheck module is an optional on-board module of the rc_visard and is licensed with any of the modules ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5) or SilhouetteMatch (Section 6.4.6). Otherwise it requires a separate CollisionCheck license (Section 8.7) to be purchased.

The module provides an easy way to check if a gripper is in collision with a load carrier, the point cloud (only in combination with SilhouetteMatch (Section 6.4.6)), or other detected objects (only in combination with SilhouetteMatch (Section 6.4.6)). It is integrated with the ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5) and SilhouetteMatch (Section 6.4.6) modules, but can be used as standalone product. The models of the grippers for collision checking have to be defined in the GripperDB (Section 6.6.3) module.

Warning: Collisions are checked only between the load carrier and the gripper, not the robot itself, the flange, other objects or the item located in the robot gripper. Only in combination with SilhouetteMatch (Section 6.4.6), and only in case the selected template contains a collision geometry and check_collisions_with_matches is enabled in the respective detection module, also collisions between the gripper and other detected objects will be checked. Collisions with objects that cannot be detected will not be checked. Only in combination with SilhouetteMatch (Section 6.4.6) and only if check_collisions_with_point_cloud is enabled in the respective detection module, collisions between the gripper and a watertight version of the point cloud will be checked.

Table 6.48: Specifications of the CollisionCheck module

| Collision checking with | detected load carrier, detected objects (only <br> SilhouetteMatch (Section 6.4.6)), baseplane (only SilhouetteMatch, <br> Section 6.4.6), point cloud (only SilhouetteMatch (Section 6.4.6)) |
| :-- | :-- |
| Collision checking available in | ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5), <br> SilhouetteMatch (Section 6.4.6) |
<|end_chunk_980|><|start_chunk_981|>
### 6.5.2.2 Collision checking
<|end_chunk_981|><|start_chunk_982|>
### Page 211<|end_chunk_982|><|start_chunk_983|>
 Stand-alone collision checking 

The check_collisions service call triggers collision checking between the chosen gripper and the provided load carriers for each of the provided grasps. Checking collisions with other objects or the point cloud is not possible with the stand-alone check_collisions service. The CollisionCheck module checks if the chosen gripper is in collision with at least one of the load carriers, when the TCP of the gripper is positioned in the grasp position. It is possible to check the collision with multiple load carriers simultaneously. The grasps which are in collision with any of the defined load carriers will be returned as colliding.
The pre_grasp_offset can be used for additional collision checking. The pre-grasp offset $P_{\text {off }}$ is the offset between the grasp point $P_{\text {grasp }}$ and the pre-grasp position $P_{\text {pre }}$ in the grasp's coordinate frame (see Fig. 6.30). If the pre-grasp offset is defined, the grasp will be detected as colliding if the gripper is in collision at any point during motion from the pre-grasp position to the grasp position (assuming a linear movement).
![img-55.jpeg](img-55.jpeg)

Fig. 6.30: Illustration of the pre-grasp offset parameter for collision checking. In this case, the pre-grasp position as well as the grasp position are collision free. However, the trajectory between these poses would have collisions. Thus, this grasp pose would be marked as colliding.
<|end_chunk_983|><|start_chunk_984|>
## Collision checking within other modules

Collision checking is integrated in the following modules' services:

- ItemPick (Section 6.4.4): compute_grasps (see compute_grasps, Section 6.4.4.7)
- BoxPick (Section 6.4.5): compute_grasps (see compute_grasps, Section 6.4.5.8)
- SilhouetteMatch (Section 6.4.6): detect_object (see detect_object, Section 6.4.6.11)

Each of these services can take a collision_detection argument consisting of the gripper_id of the default gripper and the pre_grasp_offset as described in the previous section Stand-alone collision checking (Section 6.5.2.2). The default gripper given by the gripper_id argument is only used for grasp points which do not have an individual gripper ID assigned. When the collision_detection argument is given, these services only return the grasps at which the gripper is not in collision or which could not be checked for collisions. When a load carrier ID is provided to these services, collision checking will always be performed between the gripper and the load carrier. Additional collision check features can be enabled depending on the module.

Only for SilhouetteMatch (Section 6.4.6), and only in case the selected template contains a collision geometry and check_collisions_with_matches is enabled in the respective detection module, grasp points at which the gripper would be in collision with other detected objects are also rejected. The object on which the grasp point to be checked is located, is excluded from the collision check.

When a gripper is defined for a grasp point in the object template for SilhouetteMatch (Section 6.4.6), then this gripper will be used for collision checking at that specific grasp point instead of the default
<|end_chunk_984|><|start_chunk_985|>
### Page 212
gripper defined in the collision_detection argument of the detect_object service (see Setting of grasp points, Section 6.4.6.4). The grasps returned by the detect_object service contain a flag collision_checked, indicating whether the grasp was checked for collisions, and the field gripper_id. If collision_checked is true, the returned gripper_id contains the ID of the gripper that was used for the collision check. That is the ID of the gripper defined for that specific grasp, or, if empty, the gripper that was given in the collision_detection argument of the request. If collision_checked is false, the returned gripper_id is the gripper ID that was defined for that grasp.
In SilhouetteMatch, Section 6.4.6, collisions between the gripper and the base plane can be checked, if check_collisions_with_base_plane is enabled in SilhouetteMatch.
Collisions between the gripper and a watertight version of the point cloud can be checked in SilhouetteMatch (Section 6.4.6) if check_collisions_with_point_cloud is enabled in the respective module.

Warning: Collisions are checked only between the load carrier and the gripper, not the robot itself, the flange or other objects. Only in combination with SilhouetteMatch (Section 6.4.6), and only in case the selected template contains a collision geometry and check_collisions_with_matches is enabled in the respective detection module, also collisions between the gripper and other detected objects are checked. Collisions with objects that cannot be detected will not be checked. Only in combination with SilhouetteMatch (Section 6.4.6), and only if check_collisions_with_point_cloud is enabled, collisions between the gripper and a watertight version of the point cloud are checked.

The collision-check results are affected by run-time parameters, which are listed and explained further below.
<|end_chunk_985|><|start_chunk_986|>
 6.5.2.3 Parameters 

The CollisionCheck module is called rc_collision_check in the REST-API and is represented in the Web GUI (Section 7.1) under Configuration $\rightarrow$ CollisionCheck. The user can explore and configure the rc_collision_check module's run-time parameters, e.g. for development and testing, using the Web GUI or the REST-API interface (Section 7.3).
<|end_chunk_986|><|start_chunk_987|>
## Parameter overview

This module offers the following run-time parameters:
Table 6.49: The rc_collision_check module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :-- | :--: | :--: | :--: | :--: | :-- |
| check_bottom | bool | false | true | true | Whether to enable collision check- <br> ing with the bottom of the load car- <br> rier |
| check_flange | bool | false | true | true | Whether all grasps with the flange <br> inside the load carrier should be <br> marked as colliding |
| collision_dist | float64 | 0.0 | 0.1 | 0.01 | Minimum distance in meters be- <br> tween any element of the gripper <br> and the load carrier or the base <br> plane (only SilhouetteMatch) for a <br> collision-free grasp |
<|end_chunk_987|><|start_chunk_988|>
### Page 213<|end_chunk_988|><|start_chunk_989|>
 Description of run-time parameters 

Each run-time parameter is represented by a row in the Web GUI's Settings section under Configuration $\rightarrow$ CollisionCheck. The name in the Web GUI is given in brackets behind the parameter name:
collision_dist (Collision Distance)

Minimal distance in meters between any part of the gripper and the load carrier and/or the base plane (only SilhouetteMatch) for a grasp to be considered collision free.

Note: The collision distance is not applied when checking collisions between the gripper and the point cloud, or the gripper and other detected objects. It is not applied when checking if the flange is inside the load carrier (check_flange), either.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_989|><|start_chunk_990|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_collision_check/parameters?collision_ $\ldots$ dist=<value>
<|end_chunk_990|><|start_chunk_991|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_collision_check/parameters?collision_dist=<value>
check_flange (Check Flange)

Performs an additional safety check as described in Robot flange radius (Section 6.6.3.2). If this parameter is set, all grasps in which any part of the robot's flange is inside the load carrier are marked as colliding.

Via the REST-API, this parameter can be set as follows.
<|end_chunk_991|><|start_chunk_992|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_collision_check/parameters?check_flange- $\ldots<$ value $>$
<|end_chunk_992|><|start_chunk_993|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_collision_check/parameters?check_flange=<value>
check_bottom (Check Bottom)

When this check is enabled the collisions will be checked not only with the side walls of the load carrier but also with its bottom. It might be necessary to disable this check if the TCP is inside the collision geometry (e.g. is defined inside a suction cup).

Via the REST-API, this parameter can be set as follows.
<|end_chunk_993|><|start_chunk_994|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_collision_check/parameters?check_bottom- $\ldots<$ value $>$

API version 1 (deprecated)
<|end_chunk_994|><|start_chunk_995|>
### Page 214
PUT http://<host>/api/v1/nodes/rc_collision_check/parameters?check_bottom=<value>
<|end_chunk_995|><|start_chunk_996|>
 6.5.2.4 Status values 

The rc_collision_check module reports the following status values:
Table 6.50: The rc_collision_check module status values

| Name | Description |
| :-- | :-- |
| last_evaluated_grasps | Number of evaluated grasps |
| last_collision_free_grasps | Number of collision-free grasps |
| collision_check_time | Collision checking runtime |
<|end_chunk_996|><|start_chunk_997|>
### 6.5.2.5 Services

The user can explore and call the rc_collision_check module's services, e.g. for development and testing, using REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1).
The CollisionCheck module offers the following services.
reset_defaults

Resets all parameters of the module to its default values, as listed in above table.
<|end_chunk_997|><|start_chunk_998|>
## Details

This service can be called as follows.
<|end_chunk_998|><|start_chunk_999|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_collision_check/services/reset_defaults
<|end_chunk_999|><|start_chunk_1000|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_collision_check/services/reset_defaults
<|end_chunk_1000|><|start_chunk_1001|>
## Request

This service has no arguments.
<|end_chunk_1001|><|start_chunk_1002|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

check_collisions (deprecated)

Triggers a collision check between a gripper and a load carrier.
<|end_chunk_1002|><|start_chunk_1003|>
## Details
<|end_chunk_1003|><|start_chunk_1004|>
### Page 215
This service can be called as follows.
<|end_chunk_1004|><|start_chunk_1005|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_collision_check/services/check_collisions
<|end_chunk_1005|><|start_chunk_1006|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_collision_check/services/check_collisions
<|end_chunk_1006|><|start_chunk_1007|>
## Request

Required arguments:
grasps: list of grasps that should be checked.
load_carriers: list of load carriers against which the collision should be checked. The fields of the load carrier definition are described in Detection of load carriers (Section 6.4.2.2). The position frame of the grasps and load carriers has to be the same.
gripper_id: the id of the gripper that is used to check the collisions. The gripper has to be configured beforehand.

Optional arguments:
pre_grasp_offset: the offset in meters from the grasp position to the pre-grasp position in the grasp frame. If this argument is set, the collisions will not only be checked in the grasp point, but also on the path from the pre-grasp position to the grasp position (assuming a linear movement).

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "grasps": [
            {
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "pose_frame": "string",
            "uuid": "string"
        }
    ],
    "gripper_id": "string",
    "load_carriers": [
        {
            "id": "string",
            "inner_dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "outer_dimensions": {
                "x": "float64",
```
<|end_chunk_1007|><|start_chunk_1008|>
### Page 216
![img-56.jpeg](img-56.jpeg)
<|end_chunk_1008|><|start_chunk_1009|>
 Response 

colliding_grasps: list of grasps in collision with one or more load carriers.
collision_free_grasps: list of collision-free grasps.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "check_collisions",
    "response": {
        "colliding_grasps": [
            {
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    },
                    "position": {
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
                    }
                    },
                    "pose_frame": "string",
                    "rim_thickness": {
                        "x": "float64",
                        "y": "float64"
                    }
                    }
            ],
            "pre_grasp_offset": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
            }
        }
}
```

<|end_chunk_1009|><|start_chunk_1010|>
## Response

colliding_grasps: list of grasps in collision with one or more load carriers.
collision_free_grasps: list of collision-free grasps.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "check_collisions",
    "response": {
        "colliding_grasps": [
            {
                "pose": {
                    "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "y": "float64"
                    },
                    "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                    }
                    },
                    "pose_frame": "string",
                    "uuid": "string"
            }
                },
                    "pose_frame": "string",
                    "uuid": "string"
            }
```
<|end_chunk_1010|><|start_chunk_1011|>
### Page 217
(continued from previous page)

```
    ],
    "collision_free_grasps": [
        {
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                },
                "position": {
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
                }
                },
                "pose_frame": "string",
                "uuid": "string"
            }
    ],
    "return_code": {
        "message": "string",
        "value": "int16"
    }
    }
}
```

set_gripper (deprecated)

Persistently stores a gripper on the rc_visard.
<|end_chunk_1011|><|start_chunk_1012|>
 API version 2 

This service is not available in API version 2. Use set_gripper (Section 6.6.3.3) in rc_gripper_db instead.
<|end_chunk_1012|><|start_chunk_1013|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_collision_check/services/set_gripper
The definitions of the request and response are the same as described in set_gripper (Section 6.6.3.3) in rc_gripper_db.
get_grippers (deprecated)

Returns the configured grippers with the requested gripper_ids.
<|end_chunk_1013|><|start_chunk_1014|>
## API version 2

This service is not available in API version 2. Use get_grippers (Section 6.6.3.3) in rc_gripper_db instead.
<|end_chunk_1014|><|start_chunk_1015|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_collision_check/services/get_grippers
<|end_chunk_1015|><|start_chunk_1016|>
### Page 218
The definitions of the request and response are the same as described in get_grippers (Section 6.6.3.3) in rc_gripper_db.
delete_grippers (deprecated)
Deletes the configured grippers with the requested gripper_ids.
<|end_chunk_1016|><|start_chunk_1017|>
 API version 2 

This service is not available in API version 2. Use delete_grippers (Section 6.6.3.3) in rc_gripper_db instead.
<|end_chunk_1017|><|start_chunk_1018|>
## API version 1 (deprecated)

This service can be called as follows.
PUT http://<host>/api/v1/nodes/rc_collision_check/services/delete_grippers
The definitions of the request and response are the same as described in delete_grippers (Section 6.6.3.3) in rc_gripper_db.
<|end_chunk_1018|><|start_chunk_1019|>
### 6.5.2.6 Return codes

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.

The following table contains a list of common codes:
Table 6.51: Return codes of the CollisionCheck services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -7 | Data could not be read or written to persistent storage |
| -9 | No valid license for the module |
| -10 | New gripper could not be added as the maximum storage capacity of grippers has been <br> exceeded |
| 10 | The maximum storage capacity of grippers has been reached |
| 11 | Existing gripper was overwritten |
<|end_chunk_1019|><|start_chunk_1020|>
### 6.5.3 Camera calibration

The camera calibration module is a base module which is available on every rc_visard.
To use the camera as measuring instrument, camera parameters such as focal length, lens distortion, and the relationship of the cameras to each other must be exactly known. The parameters are determined by calibration and used for image rectification (see Rectification, Section 6.1.1), which is the basis for all other image processing modules.

The $r c \_v i s a r d$ is calibrated at production time. Nevertheless, checking calibration and recalibration might be necessary if the $r c \_v i s a r d$ was exposed to strong mechanical impact.

The camera calibration module is responsible for checking calibration and calibrating.
<|end_chunk_1020|><|start_chunk_1021|>
### Page 219<|end_chunk_1021|><|start_chunk_1022|>
 6.5.3.1 Self-calibration 

The camera calibration module automatically runs in self-calibration mode at a low frequency in the background. In this mode, the $r c \_$visard observes the alignment of image rows of both rectified images. A mechanical impact, such as one caused by dropping the $r c \_$visard, might result in a misalignment. If a significant misalignment is detected, then it is automatically corrected. After each reboot and after each correction, the current self-calibration offset is reported in the camera module's log file (see Downloading log files, Section 8.8) as:
"rc_stereocalib: Current self-calibration offset is 0.00, update counter is 0"
The update counter is incremented after each automatic correction. It is reset to 0 after manual recalibration of the $r c \_$visard.

Under normal conditions, such as the absence of mechanical impact on the $r c \_$visard, self-calibration should never occur. Self-calibration allows the $r c \_$visard to work normally even after misalignment is detected, since it is automatically corrected. Nevertheless, recalibrating the camera manually is recommended if the update counter is not 0 . The Web GUI displays a warning when self calibration has occurred.
<|end_chunk_1022|><|start_chunk_1023|>
### 6.5.3.2 Calibration process

Manual calibration can be done through the Web GUI (Section 7.1) under Configuration $\rightarrow$ Camera Calibration. This page provides a wizard to guide the user through the calibration process.

Note: Camera calibration is normally unnecessary for the $r c \_$visard since it is calibrated at production time. Therefore, calibration is only required after strong mechanical impacts, such as occur when dropping the $r c \_$visard.

During calibration, the calibration grid must be detected in different poses. When holding the calibration grid, make sure that all black squares of the grid are completely visible and not occluded in both camera images. A green check mark overlays each correctly detected square. The correct detection of the grid is only possible if all of the black squares are detected. Some of the squares not being detected, or being detected only briefly might indicate bad lighting conditions, or a damaged grid. Squares in overexposed parts of the calibration grid are highlighted in red. In this case, the lighting conditions or exposure setting must be adjusted. A thick green border around the calibration grid indicates that it was detected correctly in both camera images.
<|end_chunk_1023|><|start_chunk_1024|>
## Calibration settings

The quality of camera calibration heavily depends on the quality of the calibration grid. Calibration grids can be obtained from Roboception.
<|end_chunk_1024|><|start_chunk_1025|>
### Page 220
![img-57.jpeg](img-57.jpeg)

Fig. 6.31: Calibration settings

In the first step, the calibration grid must be specified. The Next button proceeds to the next step.
<|end_chunk_1025|><|start_chunk_1026|>
 Verify calibration 

In the next step, the current calibration can be verified. To perform the verification, the grid must be held such that it is simultaneously visible in both cameras. When the grid is detected, the calibration error is automatically computed and the result is displayed on the screen.
<|end_chunk_1026|><|start_chunk_1027|>
### Page 221
![img-58.jpeg](img-58.jpeg)

Fig. 6.32: Verification of calibration

Note: To compute a meaningful calibration error, the grid should be held as close as possible to the cameras. If the grid only covers a small section of the camera images, the calibration error will always be less than when the grid covers the full image. For this reason, the minimal and maximal calibration error during verification are shown in addition to the calibration error at the current grid position.

The typical calibration error is below 0.2 pixels. If the error is in this range, then the calibration procedure can be skipped. If the calibration error is greater, the calibration procedure should be performed to guarantee full sensor performance. The button Next starts the procedure.

Warning: A large error during verification can be due to miscalibrated cameras, an inaccurate calibration grid, or wrong grid width or height. In case you use a custom calibration grid, please make sure that the grid is accurate and the entered grid width and height are correct. Otherwise, manual calibration will actually decalibrate the cameras!
<|end_chunk_1027|><|start_chunk_1028|>
### Page 222<|end_chunk_1028|><|start_chunk_1029|>
 Calibrate 

The camera's exposure time should be set appropriately before starting the calibration. To achieve good calibration results, the images should be well-exposed and motion blur should be avoided. Thus, the maximum auto-exposure time should be as short as possible, but still allow a good exposure. The current exposure time is displayed below the camera images as shown in Fig. 6.34.

Full calibration consists of calibrating each camera individually (monocalibration) and then performing a stereo calibration to determine the relationship between them. In most cases, the intrinsic calibration of each camera does not get corrupted. For this reason, monocalibration is skipped by default during a recalibration, but can be performed by clicking Perform Monocalibration in the Calibrate tab. This should only be done if the result of the stereo calibration is not satisfactory.
<|end_chunk_1029|><|start_chunk_1030|>
## Stereo calibration

During stereo calibration, both cameras are calibrated to each other to find their relative rotation and translation.

The camera images can also be displayed mirrored to simplify the correct positioning of the calibration grid.

First, the grid should be held as close as possible to the camera and very still. It must be fully visible in both images and the cameras should look perpendicularly onto the grid. If the grid is not perpendicular to the line of sight of the cameras, this will be indicated by small green arrows pointing to the expected positions of the grid corners (see Fig. 6.33).
![img-59.jpeg](img-59.jpeg)

Fig. 6.33: Arrows indicating that the grid is not perpendicular to the camera's line of sight during stereo calibration

The grid must be kept very still for detection. If motion blur occurs, the grid will not be detected. All grid cells that are drawn onto the image have to be covered by the calibration grid. This is visualized by filling the covered cells in green (see Fig. 6.34).

For the $r c \_v i s a r d$ all cells can be covered at once by holding the grid close enough.
<|end_chunk_1030|><|start_chunk_1031|>
### Page 223
![img-60.jpeg](img-60.jpeg)

Fig. 6.34: Stereo calibration: Hold the grid as close as possible to fill all visualized cells

Note: If the check marks on the calibration grid all vanish, then either the camera does not look perpendicularly onto the grid, or the grid is too far away from the camera.

Once all grid cells are covered, they disappear and a single far cell is visualized. Now, the grid should be held as far as possible from the cameras, so that the small cell is covered. Arrows will indicate if the grid is still too close to the camera. When the grid is successfully detected at the far pose, the cell is filled in green and the result can be computed (see Fig. 6.35).
<|end_chunk_1031|><|start_chunk_1032|>
### Page 224
![img-61.jpeg](img-61.jpeg)

Fig. 6.35: Holding the grid far away during stereo calibration

If stereo calibration yields an unsatisfactory calibration error, then calibration should be repeated with monocalibration (see next Section Monocalibration).
<|end_chunk_1032|><|start_chunk_1033|>
 Monocalibration 

Monocalibration is the intrinsic calibration of each camera individually. Since the intrinsic calibration normally does not get corrupted, the monocalibration should only be performed if the result of stereo calibration is not satisfactory.

Click Perform Monocalibration in the Calibrate tab to start monocalibration.
For monocalibration, the grid has to be held in certain poses. The arrows from the grid corners to the green areas indicate that all grid corners should be placed inside the green areas. The green areas are called sensitive areas. The Size of Sensitive Area slider can control their size to ease calibration. However, please be aware that increasing their size too much may result in slightly lower calibration accuracy.

Holding the grid upside down is a common mistake made during calibration. Spotting this in this case is easy because the green lines from the grid corners into the green areas will cross each other as shown in Fig. 6.36.
![img-62.jpeg](img-62.jpeg)

Fig. 6.36: Wrongly holding the grid upside down leads to crossed green lines.

Note: Calibration might appear cumbersome as it involves holding the grid in certain predefined poses. However, these poses are required to ensure an unbiased, high-quality calibration result.
<|end_chunk_1033|><|start_chunk_1034|>
### Page 225
The monocalibration process involves five poses for each camera as shown in Fig. 6.37.
![img-63.jpeg](img-63.jpeg)

Fig. 6.37: Poses required for monocamera calibration

After the corners or sides of the grid are placed on top of the sensitive areas, the process automatically shows the next pose required. When the process is finished for the left camera, the same procedure is repeated for the right one.

Continue with the guidelines given in the previous Section Stereo calibration.
<|end_chunk_1034|><|start_chunk_1035|>
 Storing the calibration result 

Clicking the Compute Calibration button finishes the process and displays the final result. The indicated result is the mean reprojection error of all calibration points. It is given in pixels and typically has a value below 0.2 .

Pressing Save Calibration applies the calibration and saves it to the device.
Note: The given result is the minimum error left after calibration. The real error is definitely not less than this, but could in theory be larger. This is true for every camera-calibration algorithm and the reason why we enforce holding the grid in very specific poses. Doing so ensures that the real calibration error cannot significantly exceed the reported error.

Warning: If a hand-eye calibration was stored on the rc_visard before camera calibration, the handeye calibration values could have become invalid. Please repeat the hand-eye calibration procedure.
<|end_chunk_1035|><|start_chunk_1036|>
### 6.5.3.3 Parameters

The module is called rc_stereocalib in the REST-API.
Note: The camera calibration module's available parameters and status values are for internal use only and may change in the future without further notice. Calibration should only be performed through the Web GUI as described above.
<|end_chunk_1036|><|start_chunk_1037|>
### 6.5.3.4 Services

Note: The camera calibration module's available service calls are for internal use only and may change in the future without further notice. Calibration should only be performed through the Web GUI as described above.
<|end_chunk_1037|><|start_chunk_1038|>
### Page 226<|end_chunk_1038|><|start_chunk_1039|>
 6.5.4 IO and Projector Control 

The IOControl module is an on-board module of the rc_visard.
The IOControl module allows reading the status of the general purpose digital inputs and controlling the digital general purpose outputs (GPIOs) of the rc_visard. The outputs can be set to LOW or HIGH, or configured to be HIGH for the exposure time of every image or every second image.
The purpose of the IOControl module is the control of an external light source or a projector, which is connected to one of the $r c \_$visard's GPIOs to be synchronized by the image acquisition trigger. In case a pattern projector is used to improve stereo matching, the intensity images also show the projected pattern, which might be a disadvantage for image processing tasks that are based on the intensity image (e.g. edge detection). For this reason, the IOControl module allows setting GPIO outputs to HIGH for the exposure time of every second image, so that intensity images without the projected pattern are also available.

Note: For more details on the rc_visard's GPIOs please refer to Wiring, Section 3.5.
<|end_chunk_1039|><|start_chunk_1040|>
### 6.5.4.1 Parameters

The IOControl module is called rc_iocontrol in the REST-API and is represented in the Web GUI (Section 7.1) under Configuration $\rightarrow$ IOControl. The user can change the parameters via the Web GUI, the REST-API interface (Section 7.3), or via GigE Vision using the DigitalIOControl parameters LineSelector and LineSource (Category: DigitalIOControl, Section 7.2.3.4).
<|end_chunk_1040|><|start_chunk_1041|>
## Parameter overview

This module offers the following run-time parameters:
Table 6.52: The rc_iocontrol module's run-time parameters

| Name | Type | Min | Max | Default | Description |
| :--: | :--: | :--: | :--: | :--: | :--: |
| out1_inverted | bool | false | true | false | Inverting out1 |
| out1_mode | string | - | - | Low | Out1 mode: [Low, High, ExposureActive, ExposureAlternateActive] |
| out1_ratio | float64 | 0.0 | 1.0 | 1.0 | Ratio of exposure time that Out1 is high in ExposureActive and ExposureAlternateActive mode |
| out2_inverted | bool | false | true | false | Inverting out2 |
| out2_mode | string | - | - | Low | Out2 mode: [Low, High, ExposureActive, ExposureAlternateActive] |
| out2_ratio | float64 | 0.0 | 1.0 | 1.0 | Ratio of exposure time that Out2 is high in ExposureActive and ExposureAlternateActive mode |

Description of run-time parameters
out1_mode and out2_mode (Out1 / Projector and Out2)
The output modes for GPIO Out 1 and Out 2 can be set individually:
Low sets the output permanently to LOW. This is the factory default.
High sets the output permanently to HIGH.
ExposureActive sets the output to HIGH for the exposure time of every image.
<|end_chunk_1041|><|start_chunk_1042|>
### Page 227
ExposureAlternateActive sets the output to HIGH for the exposure time of every second image.
Via the REST-API, this parameter can be set as follows.
<|end_chunk_1042|><|start_chunk_1043|>
 API version 2 

PUT http://<host>/api/v2/pipelines/0/nodes/rc_iocontrol/parameters/parameters?<out1_ $\ldots$ mode|out2_mode $==<$ value $>$
<|end_chunk_1043|><|start_chunk_1044|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_iocontrol/parameters?<out1_mode|out2_mode>=<value>
Fig. 6.38 shows which images are used for stereo matching and transmission via GigE Vision in ExposureActive mode with a user-defined frame rate of 8 Hz .

| Internal acquisition |  |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| GPIO Out 1 |  |  |  |  |  |  |  |  |  |  |  |
| Disparity image |  |  |  |  |  |  |  |  |  |  |  |
| Camera image |  |  |  |  |  |  |  |  |  |  |  |

Fig. 6.38: Example of using the ExposureActive mode for GPIO Out 1 with a user-defined frame rate of 8 Hz . The internal image acquisition is always 25 Hz . GPIO Out 1 is HIGH for the exposure time of every image. A disparity image is computed for camera images that are sent out via GigE Vision according to the user-defined frame rate.

The mode ExposureAlternateActive is meant to be used when an external random dot projector is connected to the rc_visard's GPIO Out 1. When setting Out 1 to ExposureAlternateActive, the stereo matching (Section 6.2) module only uses images with GPIO Out 1 being HIGH, i.e. projector is on. The maximum frame rate that is used for stereo matching is therefore half of the frame rate configured by the user. All modules which make use of the intensity image, like TagDetect (Section 6.4.3) and ItemPick (Section 6.4.4), use the intensity images with GPIO Out 1 being LOW, i.e. projector is off. Fig. 6.39 shows an example.
![img-64.jpeg](img-64.jpeg)

Fig. 6.39: Example of using the ExposureAlternateActive mode for GPIO Out 1 with a user-defined frame rate of 8 Hz . The internal image acquisition is always 25 Hz . GPIO Out 1 is HIGH for the exposure time of every second image. A disparity image is computed for images where Out 1 is HIGH and that are sent out via GigE Vision according to the user-defined frame rate. In ExposureAlternateActive mode, intensity images are always transmitted pairwise: one with GPIO Out 1 HIGH, for which a disparity image might be available, and one with GPIO Out 1 LOW.

Note: In ExposureAlternateActive mode, an intensity image with GPIO Out 1 being HIGH (i.e. with projection) is always 40 ms away from an intensity image with Out 1 being LOW (i.e. without projection), regardless of the user-defined frame rate. This needs to be considered when synchronizing disparity images and camera images without projection in this special mode.

The functionality can also be controlled by the DigitalIOControl parameters of the GenICam interface (Category: DigitalIOControl, Section 7.2.3.4).
<|end_chunk_1044|><|start_chunk_1045|>
### Page 228<|end_chunk_1045|><|start_chunk_1046|>
 6.5.4.2 Services 

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information.

The IOControl module offers the following services.
get_io_values
Retrieves the current state of the $r c \_v i s a r d$ 's general purpose inputs and outputs (GPIOs).
<|end_chunk_1046|><|start_chunk_1047|>
## Details

This service can be called as follows.
<|end_chunk_1047|><|start_chunk_1048|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_iocontrol/services/get_io_values
<|end_chunk_1048|><|start_chunk_1049|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_iocontrol/services/get_io_values
<|end_chunk_1049|><|start_chunk_1050|>
## Request

This service has no arguments.
<|end_chunk_1050|><|start_chunk_1051|>
## Response

The returned timestamp is the time of measurement.
input_mask and output_mask are bit masks defining which bits are used for input and output values, respectively.
values holds the values of the bits corresponding to input and output as given by the input_mask and output_mask.
return_code holds possible warnings or error codes and messages. Possible return_code values are shown below.

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -2 | Internal error |
| -9 | License for IOControl is not available |

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_io_values",
    "response": {
        "input_mask": "uint32",
        "inverter_mask": "uint32",
        "output_mask": "uint32",
        "ratio_mask": "uint32",
        "return_code": {
            "message": "string",
            "value": "int16"
    },
    "timestamp": {
        "nsec": "int32",
```
<|end_chunk_1051|><|start_chunk_1052|>
### Page 229
```
            "sec": "int32"
        },
        "values": "uint32"
    }
}
```

reset_defaults

Restores and applies the default values for this module's parameters ("factory reset").
<|end_chunk_1052|><|start_chunk_1053|>
 Details 

This service can be called as follows.
<|end_chunk_1053|><|start_chunk_1054|>
## API version 2

PUT http://<host>/api/v2/pipelines/0/nodes/rc_iocontrol/services/reset_defaults
<|end_chunk_1054|><|start_chunk_1055|>
## API version 1 (deprecated)

PUT http://<host>/api/v1/nodes/rc_iocontrol/services/reset_defaults
<|end_chunk_1055|><|start_chunk_1056|>
## Request

This service has no arguments.
<|end_chunk_1056|><|start_chunk_1057|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "reset_defaults",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_1057|><|start_chunk_1058|>
### 6.6 Database modules

The rc_visard provides several database modules which enable the user to configure global data which is used in many detection modules, such as load carriers and regions of interest. Via the REST-API interface (Section 7.3) the database modules are only available in API version 2.

The database modules are:

- LoadCarrierDB (rc_load_carrier_db, Section 6.6.1) allows setting, retrieving and deleting load carriers.
- RoIDB (rc_roi_db, Section 6.6.2) allows setting, retrieving and deleting 2D and 3D regions of interest.
- GripperDB (rc_gripper_db, Section 6.6.3) allows setting, retrieving and deleting grippers for collision checking.
<|end_chunk_1058|><|start_chunk_1059|>
### Page 230<|end_chunk_1059|><|start_chunk_1060|>
 6.6.1 LoadCarrierDB 
<|end_chunk_1060|><|start_chunk_1061|>
### 6.6.1.1 Introduction

The LoadCarrierDB module (Load carrier database module) allows the global definition of load carriers, which can then be used in many detection modules. The specified load carriers are available for all modules supporting load carriers on the rc_visard.

The LoadCarrierDB module is a base module which is available on every rc_visard.
Table 6.53: Specifications of the LoadCarrierDB module

| Supported load carrier types | 4 -sided or 3 -sided |
| :-- | :-- |
| Supported rim types | solid rim, stepped rim or ledged rim |
| Min. load carrier dimensions | $0.1 \mathrm{~m} \times 0.1 \mathrm{~m} \times 0.05 \mathrm{~m}$ |
| Max. load carrier dimensions | $2 \mathrm{~m} \times 2 \mathrm{~m} \times 2 \mathrm{~m}$ |
| Max. number of load carriers | 50 |
| Load carriers available in | ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5) and <br> SilhouetteMatch (Section 6.4.6) |
| Supported pose types | no pose, orientation prior, exact pose |
| Supported reference frames | camera, external |
<|end_chunk_1061|><|start_chunk_1062|>
### 6.6.1.2 Load carrier definition

A load carrier (bin) is a container with four walls, a floor and a rectangular rim, which can contain objects. It can be used to limit the volume in which to search for objects or grasp points.

A load carrier is defined by its outer_dimensions and inner_dimensions. The maximum outer_dimensions are 2.0 meters in every dimension.

The origin of the load carrier reference frame is in the center of the load carrier's outer box and its z axis is perpendicular to the load carrier's floor pointing outwards (see Fig. 6.40).
![img-65.jpeg](img-65.jpeg)

Fig. 6.40: Load carrier with reference frame and inner and outer dimensions

Note: Typically, outer and inner dimensions of a load carrier are available in the specifications of the load carrier manufacturer.
<|end_chunk_1062|><|start_chunk_1063|>
### Page 231
The inner volume of the load carrier is defined by its inner dimensions, but includes a region of 10 cm height above the load carrier, so that also items protruding from the load carrier are considered for detection or grasp computation. Furthermore, an additional crop_distance is subtracted from the inner volume in every dimension, which acts as a safety margin and can be configured as run-time parameter in the LoadCarrier module (see Parameters, Section 6.4.2.5). Fig. 6.41 visualizes the inner volume of a load carrier. Only points which are inside this volume are considered for detections.
![img-66.jpeg](img-66.jpeg)

Fig. 6.41: Visualization of the inner volume of a load carrier. Only points which are inside this volume are considered for detections.

Since the load carrier detection is based on the detection of the load carrier's rim, the rim geometry must be specified if it cannot be determined from the difference between outer and inner dimensions. A load carrier with a stepped rim can be defined by setting a rim_thickness. The rim thickness gives the thickness of the outer part of the rim in the $x$ and $y$ direction. When a rim thickness is given, an optional rim_step_height can also be specified, which gives the height of the step between the outer and the inner part of the rim. When the step height is given, it will also be considered during collision checking (see CollisionCheck, Section 6.5.2). Examples of load carriers with stepped rims are shown in Fig. 6.42 A, B. In addition to the rim_thickness and rim_step_height the rim_ledge can be specified for defining load carriers whose inner rim protrudes into the interior of the load carrier, such as pallet cages. The rim_ledge gives the thickness of the inner part of the rim in the x and y direction. An example of a load carrier with a ledged rim is shown in Fig. 6.42 C.
<|end_chunk_1063|><|start_chunk_1064|>
### Page 232
![img-67.jpeg](img-67.jpeg)

Fig. 6.42: Examples of load carriers with stepped rim (A, B) or ledged rim (C)

The different rim types are applicable to both, standard 4-sided and 3-sided load carriers. For a 3sided load carrier, the type must be THREE_SIDED. If the type is set to STANDARD or left empty, a 4 -sided load carrier is specified. A 3 -sided load carrier has one side that is lower than the other three sides. This height_open_side is measured from the outer bottom of the load carrier. The open side is at the negative $y$-axis of the load carrier's coordinate system. Examples of the two load carrier types are given in Fig. 6.43. The height of the lower side is only considered during collision checking and not required for the detection of the load carrier.
![img-68.jpeg](img-68.jpeg)

Fig. 6.43: Examples of a standard 4-sided load carrier (A) and a 3 -sided load carrier (B)

A load carrier can be specified with a full 3D pose consisting of a position and an orientation quaternion, given in a pose_frame. Based on the given pose_type this pose is either used as an orientation prior (pose_type is ORIENTATION_PRIOR or empty), or as the exact pose of the load carrier (pose_type is EXACT_POSE).

In case the pose serves as orientation prior, the detected load carrier pose is guaranteed to have the minimum rotation with respect to the load carrier's prior pose. This pose type is useful for detecting tilted load carriers and for resolving the orientation ambiguity in the $x$ and $y$ direction caused by the symmetry of the load carrier model.
<|end_chunk_1064|><|start_chunk_1065|>
### Page 233
In case the pose type is set to EXACT. POSE, no load carrier detection will be performed on the scene data, but the given pose will be used in exactly the same way as if the load carrier is detected at that pose. This pose type is especially useful in cases where load carriers do not change their positions and/or are hard to detect (e.g. because their rim is too thin or the material is too shiny).
The $r c \_v i s a r d$ can persistently store up to 50 different load carrier models, each one identified by a different id. The configuration of a load carrier model is normally performed offline, during the set up the desired application. This can be done via the REST-API interface (Section 7.3) or in the rc_visard Web GUI.

Note: The configured load carrier models are persistent even over firmware updates and rollbacks.
<|end_chunk_1065|><|start_chunk_1066|>
 6.6.1.3 Load carrier compartments 

Some detection modules can make use of a load_carrier compartment to further limit the volume for the detection, for example ItemPick's compute_grasps service (see 6.4.4.7). A load carrier compartment is a box whose pose is defined as the transformation from the load carrier reference frame to the compartment reference frame, which is located in the center of the compartment box (see Fig. 6.44). The load carrier compartment is defined for each detection call separately and is not part of the load carrier definition in the LoadCarrierDB module.
![img-69.jpeg](img-69.jpeg)

Fig. 6.44: Sample compartment inside a load carrier. The coordinate frame shown in the image is the reference frame of the compartment.

The compartment volume is intersected with the load carrier inner volume to compute the volume for the detection. If this intersection should also contain the 10 cm region above the load carrier, the height of the compartment box must be increased accordingly.
<|end_chunk_1066|><|start_chunk_1067|>
### 6.6.1.4 Interaction with other modules

Internally, the LoadCarrierDB module depends on, and interacts with other on-board modules as listed below.
<|end_chunk_1067|><|start_chunk_1068|>
### Page 234<|end_chunk_1068|><|start_chunk_1069|>
 Hand-eye calibration 

In case the camera has been calibrated to a robot, the load carrier's exact pose or orientation prior can be provided in the robot coordinate frame by setting the corresponding pose_frame argument to external.

Two different pose_frame values can be chosen:

1. Camera frame (camera). The load carrier pose or orientation prior is provided in the camera frame, and no prior knowledge about the pose of the camera in the environment is required. This means that the configured load carriers move with the camera. It is the user's responsibility to update the configured poses if the camera frame moves (e.g. with a robot-mounted camera).
2. External frame (external). The load carrier pose or orientation prior is provided in the external frame, configured by the user during the hand-eye calibration process. The module relies on the on-board Hand-eye calibration module (Section 6.5.1) to retrieve the sensor mounting (static or robot mounted) and the hand-eye transformation.

Note: If no hand-eye calibration is available, all pose_frame values should be set to camera.

All pose_frame values that are not camera or external are rejected.
<|end_chunk_1069|><|start_chunk_1070|>
### 6.6.1.5 Services

The LoadCarrierDB module is called rc_load_carrier_db in the REST-API and is represented in the Web GUI (Section 7.1) under Database $\rightarrow$ Load Carriers. The user can explore and call the LoadCarrierDB module's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the Web GUI.

The LoadCarrierDB module offers the following services.
set_load_carrier

Persistently stores a load carrier on the $r c \_v i s a r d$. All configured load carriers are persistent over firmware updates and rollbacks.
<|end_chunk_1070|><|start_chunk_1071|>
## Details

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_load_carrier_db/services/set_load_carrier
<|end_chunk_1071|><|start_chunk_1072|>
## Request

Details for the definition of the load_carrier type are given in Load carrier definition (Section 6.6.1.2).

The field type is optional and accepts STANDARD and THREE_SIDED.
The field pose_type is optional and accepts NO_POSE, EXACT_POSE and ORIENTATION_PRIOR.
The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "load_carrier": {
            "height_open_side": "float64",
            "id": "string",
            "inner_dimensions": {
            "x": "float64",
            "y": "float64",
```
<|end_chunk_1072|><|start_chunk_1073|>
### Page 235
(continued from previous page)

```
            "z": "float64"
        },
        "outer_dimensions": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "pose": {
            "orientation": {
                "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                    "y": "float64",
                    "z": "float64"
            }
        },
        "pose_frame": "string",
        "pose_type": "string",
        "rim_ledge": {
            "x": "float64",
            "y": "float64"
        },
        "rim_step_height": "float64",
        "rim_thickness": {
            "x": "float64",
            "y": "float64"
        },
        "type": "string"
        }
    }
}
```

<|end_chunk_1073|><|start_chunk_1074|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_load_carrier",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_load_carriers

Returns the configured load carriers with the requested load_carrier_ids. If no load_carrier_ids are provided, all configured load carriers are returned.
<|end_chunk_1074|><|start_chunk_1075|>
## Details

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_load_carrier_db/services/get_load_carriers
<|end_chunk_1075|><|start_chunk_1076|>
### Page 236<|end_chunk_1076|><|start_chunk_1077|>
 Request 

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "load_carrier_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1077|><|start_chunk_1078|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_load_carriers",
    "response": {
        "load_carriers": [
            {
            "height_open_side": "float64",
            "id": "string",
            "inner_dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "outer_dimensions": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "pose": {
                "orientation": {
                    "w": "float64",
                    "x": "float64",
                    "y": "float64",
                    "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "pose_frame": "string",
            "pose_type": "string",
            "rim_ledge": {
                "x": "float64",
                "y": "float64"
            },
            "rim_step_height": "float64",
            "rim_thickness": {
                "x": "float64",
                "y": "float64"
            },
            "type": "string"
        }
    },
    "return_code": {
        "message": "string",
        "value": "int16"
```
<|end_chunk_1078|><|start_chunk_1079|>
### Page 237
$\square$
delete_load_carriers

Deletes the configured load carriers with the requested load_carrier_ids. All load carriers to be deleted must be explicitly stated in load_carrier_ids.
<|end_chunk_1079|><|start_chunk_1080|>
 Details 

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_load_carrier_db/services/delete_load_carriers
<|end_chunk_1080|><|start_chunk_1081|>
## Request

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "load_carrier_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1081|><|start_chunk_1082|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "delete_load_carriers",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_1082|><|start_chunk_1083|>
### 6.6.1.6 Return codes

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.
The following table contains a list of common codes:
Table 6.54: Return codes of the LoadCarrierDB module's services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -10 | New element could not be added as the maximum storage capacity of load carriers has <br> been exceeded |
| 10 | The maximum storage capacity of load carriers has been reached |
| 11 | An existent persistent model was overwritten by the call to set_load_carrier |
<|end_chunk_1083|><|start_chunk_1084|>
### Page 238<|end_chunk_1084|><|start_chunk_1085|>
 6.6.2 RoiDB 
<|end_chunk_1085|><|start_chunk_1086|>
### 6.6.2.1 Introduction

The RoiDB module (region of interest database module) allows the global definition of 2D and 3D regions of interest, which can then be used in many detection modules. The ROIs are available for all modules supporting 2D or 3D ROIs on the rc_visard.

The RoiDB module is a base module which is available on every rc_visard.
3D ROIs can be used in ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5). 2D ROIs can be used in SilhouetteMatch (Section 6.4.6), and LoadCarrier (Section 6.4.2).

Table 6.55: Specifications of the RoiDB module

| Supported ROI types | 2D, 3D |
| :-- | :-- |
| Supported ROI geometries | 2D ROI: rectangle, 3D ROI: box, sphere |
| Max. number of ROIs | 2D: 100, 3D: 100 |
| ROIs available in | 2D: SilhouetteMatch (Section 6.4.6), LoadCarrier (Section 6.4.2), <br> 3D: ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5) |
| Supported reference frames | camera, external |
<|end_chunk_1086|><|start_chunk_1087|>
### 6.6.2.2 Region of interest

A region of interest (ROI) defines a volume in space (3D region of interest, region_of_interest), or a rectangular region in the left camera image (2D region of interest, region_of_interest_2d) which is of interest for a specific user-application.

A ROI can narrow the volume where a load carrier is searched for, or select a volume which only contains items to be detected and/or grasped. Processing times can significantly decrease when using a ROI.

3D regions of interest of the following types (type) are supported:

- BOX, with dimensions box.x, box.y, box.z.
- SPHERE, with radius sphere.radius.

The user can specify the 3D region of interest pose in the camera or the external coordinate system. External can only be chosen if a Hand-eye calibration (Section 6.5.1) is available. When the sensor is robot mounted, and the region of interest is defined in the external frame, the current robot pose must be given to every detect service call that uses this region of interest.

A 2D ROI is defined as a rectangular part of the left camera image, and can be set via the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1) on the page Regions of Interest under Database. The Web GUI offers an easy-to-use selection tool. Each ROI must have a unique name to address a specific 2D ROI.

In the REST-API, a 2D ROI is defined by the following values:

- id: Unique name of the region of interest
- offset_x, offset_y: offset in pixels along the x-axis and y-axis from the top-left corner of the image, respectively
- width, height: width and height in pixels

The $r c \_v i s a r d$ can persistently store up to 100 different 3D regions of interest and the same number of 2D regions of interest. The configuration of regions of interest is normally performed offline, during the set up of the desired application. This can be done via the REST-API interface (Section 7.3) of RoiDB module, or in the rc_visard Web GUI (Section 7.1) on the page Regions of Interest under Database.

Note: The configured regions of interest are persistent even over firmware updates and rollbacks.
<|end_chunk_1087|><|start_chunk_1088|>
### Page 239<|end_chunk_1088|><|start_chunk_1089|>
 6.6.2.3 Interaction with other modules 

Internally, the RoiDB module depends on, and interacts with other on-board modules as listed below.
<|end_chunk_1089|><|start_chunk_1090|>
## Hand-eye calibration

In case the camera has been calibrated to a robot, the pose of a 3D ROI can be provided in the robot coordinate frame by setting the corresponding pose_frame argument.

Two different pose_frame values can be chosen:

1. Camera frame (camera). The ROI pose is provided in the camera frame, and no prior knowledge about the pose of the camera in the environment is required. This means that the configured load carriers move with the camera. It is the user's responsibility to update the configured poses if the camera frame moves (e.g. with a robot-mounted camera).
2. External frame (external). The ROI pose is provided in the external frame, configured by the user during the hand-eye calibration process. The module relies on the on-board Hand-eye calibration module (Section 6.5.1) to retrieve the sensor mounting (static or robot mounted) and the hand-eye transformation.

Note: If no hand-eye calibration is available, all pose_frame values should be set to camera.

All pose_frame values that are not camera or external are rejected.
<|end_chunk_1090|><|start_chunk_1091|>
### 6.6.2.4 Services

The RoiDB module is called rc_roi_db in the REST-API and is represented in the Web GUI (Section 7.1) under Database $\rightarrow$ Regions of Interest. The user can explore and call the RoiDB module's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the Web GUI.

The RoiDB module offers the following services.
set_region_of_interest
Persistently stores a 3D region of interest on the rc_visard. All configured 3D regions of interest are persistent over firmware updates and rollbacks.
<|end_chunk_1091|><|start_chunk_1092|>
## Details

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_roi_db/services/set_region_of_interest
<|end_chunk_1092|><|start_chunk_1093|>
## Request

Details for the definition of the region_of_interest type are given in Region of interest (Section 6.6.2.2).

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
    "region_of_interest": {
        "box": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
```

(continues on next page)
<|end_chunk_1093|><|start_chunk_1094|>
### Page 240
![img-70.jpeg](img-70.jpeg)
<|end_chunk_1094|><|start_chunk_1095|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_region_of_interest",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

set_region_of_interest_2d

Persistently stores a 2D region of interest on the rc_visard. All configured 2D regions of interest are persistent over firmware updates and rollbacks.
<|end_chunk_1095|><|start_chunk_1096|>
## Details

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_roi_db/services/set_region_of_interest_2d
<|end_chunk_1096|><|start_chunk_1097|>
## Request

Details for the definition of the region_of_interest_2d type are given in Region of interest (Section 6.6.2.2).

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "region_of_interest_2d": {
            "height": "uint32",
            "id": "string",
            "offset_x": "uint32",
```
<|end_chunk_1097|><|start_chunk_1098|>
### Page 241
```
            "offset_y": "uint32",
            "width": "uint32"
        }
    }
}
```

<|end_chunk_1098|><|start_chunk_1099|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "set_region_of_interest_2d",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

get_regions_of_interest

Returns the configured 3D regions of interest with the requested region_of_interest_ids.
<|end_chunk_1099|><|start_chunk_1100|>
## Details

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_roi_db/services/get_regions_of_interest
<|end_chunk_1100|><|start_chunk_1101|>
## Request

If no region_of_interest_ids are provided, all configured 3D regions of interest are returned.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "region_of_interest_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1101|><|start_chunk_1102|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_regions_of_interest",
    "response": {
        "regions_of_interest": [
            {
            "box": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "id": "string",
            "pose": {
```
<|end_chunk_1102|><|start_chunk_1103|>
### Page 242
![img-71.jpeg](img-71.jpeg)
get_regions_of_interest_2d

Returns the configured 2D regions of interest with the requested region_of_interest_2d_ids.
<|end_chunk_1103|><|start_chunk_1104|>
 Details 

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_roi_db/services/get_regions_of_interest_2d
<|end_chunk_1104|><|start_chunk_1105|>
## Request

If no region_of_interest_2d_ids are provided, all configured 2D regions of interest are returned.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "region_of_interest_2d_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1105|><|start_chunk_1106|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_regions_of_interest_2d",
    "response": {
        "regions_of_interest": [
            {
```
<|end_chunk_1106|><|start_chunk_1107|>
### Page 243
(continued from previous page)

```
            "height": "uint32",
            "id": "string",
            "offset_x": "uint32",
            "offset_y": "uint32",
            "width": "uint32"
        }
    ],
    "return_code": {
        "message": "string",
        "value": "int16"
    }
    }
}
```

delete_regions_of_interest

Deletes the configured 3D regions of interest with the requested region_of_interest_ids.
<|end_chunk_1107|><|start_chunk_1108|>
 Details 

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_roi_db/services/delete_regions_of_interest
<|end_chunk_1108|><|start_chunk_1109|>
## Request

All regions of interest to be deleted must be explicitly stated in region_of_interest_ids.
The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "region_of_interest_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1109|><|start_chunk_1110|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "delete_regions_of_interest",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

delete_regions_of_interest_2d

Deletes the configured 2D regions of interest with the requested region_of_interest_2d_ids.
<|end_chunk_1110|><|start_chunk_1111|>
## Details

This service can be called as follows.
<|end_chunk_1111|><|start_chunk_1112|>
### Page 244
PUT http://<host>/api/v2/nodes/rc_roi_db/services/delete_regions_of_interest_2d
<|end_chunk_1112|><|start_chunk_1113|>
 Request 

All 2D regions of interest to be deleted must be explicitly stated in region_of_interest_2d_ids.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "region_of_interest_2d_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1113|><|start_chunk_1114|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "delete_regions_of_interest_2d",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_1114|><|start_chunk_1115|>
### 6.6.2.5 Return codes

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.

The following table contains a list of common codes:
Table 6.56: Return codes of the RoiDB module's services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -10 | New element could not be added as the maximum storage capacity of regions of interest <br> has been exceeded |
| 10 | The maximum storage capacity of regions of interest has been reached |
| 11 | An existent persistent model was overwritten by the call to set...region...of...interest or <br> set...region...of...interest...2d |
<|end_chunk_1115|><|start_chunk_1116|>
### 6.6.3 GripperDB
<|end_chunk_1116|><|start_chunk_1117|>
### 6.6.3.1 Introduction

The GripperDB module (gripper database module) is an optional on-board module of the $r c \_v i s a r d$ and is licensed with any of the modules ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5) or Silhouet-
<|end_chunk_1117|><|start_chunk_1118|>
### Page 245
teMatch (Section 6.4.6). Otherwise it requires a separate CollisionCheck license (Section 8.7) to be purchased.

The module provides services to set, retrieve and delete grippers which can then be used for checking collisions with a load carrier or other detected objects (only in combination with SilhouetteMatch (Section 6.4.6)). The specified grippers are available for all modules supporting collision checking on the rc_visard.

Table 6.57: Specifications of the GripperDB module

| Max. number of grippers | 50 |
| :-- | :-- |
| Supported gripper element geometries | Box, Cylinder, CAD Element |
| Max. number of elements per gripper | 15 |
| Collision checking available in | ItemPick (Section 6.4.4) and BoxPick (Section 6.4.5), <br> SilhouetteMatch (Section 6.4.6) |
<|end_chunk_1118|><|start_chunk_1119|>
 6.6.3.2 Setting a gripper 

The gripper is a collision geometry used to determine whether the grasp is in collision with the load carrier. The gripper consists of up to 15 elements connected to each other.

At this point, the gripper can be built of elements of the following types:

- BOX, with dimensions box.x, box.y, box.z.
- CYLINDER, with radius cylinder.radius and height cylinder.height.
- CAD, with the id cad.id of the chosen CAD element.

Additionally, for each gripper the flange radius, and information about the Tool Center Point (TCP) have to be defined.

The configuration of the gripper is normally performed offline during the setup of the desired application. This can be done via the REST-API interface (Section 7.3) or the rc_visard Web GUI (Section 7.1).
<|end_chunk_1119|><|start_chunk_1120|>
## Robot flange radius

Collisions are checked only with the gripper, the robot body is not considered. As a safety feature, to prevent collisions between the load carrier and the robot, all grasps having any part of the robot's flange inside the load carrier can be designated as colliding (see Fig. 6.45). This check is based on the defined gripper geometry and the flange radius value. It is optional to use this functionality, and it can be turned on and off with the CollisionCheck module's run-time parameter check_flange as described in Parameter overview (Section 6.5.2.3).
![img-72.jpeg](img-72.jpeg)

Fig. 6.45: Case A would be marked as collision only if check_flange is true, because the robot's flange (red) is inside the load carrier. Case B is collision free independent of check_flange.
<|end_chunk_1120|><|start_chunk_1121|>
## Uploading gripper CAD elements

A gripper can consist of boxes, cylinders and CAD elements. While boxes and cylinders can be parameterized when the gripper is created, the CAD elements must be uploaded beforehand to be available
<|end_chunk_1121|><|start_chunk_1122|>
### Page 246
during gripper creation. A CAD element can be uploaded via the REST-API interface (Section 7.3) as described in Section CAD element API (Section 6.6.3.5) or via the rc_visard Web GUI (Section 7.1). Supported file formats are STEP (*.stp, *.step), STL (*.stl), OBJ (*.obj) and PLY (*.ply). The maximum file size to be uploaded is limited to 10 MB . The files are internally converted to PLY and, if necessary, simplified. The CAD elements can be referenced during gripper creation by their ID.
<|end_chunk_1122|><|start_chunk_1123|>
 Creating a gripper via the REST-API or the Web GUI 

When creating a gripper via the REST-API interface (Section 7.3) or the Web GUI (Section 7.1), each element of the gripper has a parent element, which defines how they are connected. The gripper is always built in the direction from the robot flange to the TCP, and at least one element must have 'flange' as parent. The elements' IDs must be unique and must not be 'tcp' or 'flange'. The pose of the child element has to be given in the coordinate frame of the parent element. The coordinate frame of an element is always in its geometric center. Accordingly, for a child element to be exactly below the parent element, the position of the child element must be computed from the heights of both parent and child element (see Fig. 6.46).
![img-73.jpeg](img-73.jpeg)

Fig. 6.46: Reference frames for gripper creation via the REST-API and the Web GUI

In case a CAD element is used, the element's origin is defined in the CAD data and is not necessarily located in the center of the element's bounding box.

It is recommended to create a gripper via the Web GUI, because it provides a 3D visualization of the gripper geometry and also allows to automatically attach the child element to the bottom of its parent element, when the corresponding option for this element is activated. In this case, the elements also stay attached when any of their sizes change. Automatic attachment of CAD elements uses the element's bounding box as reference. Automatic attachment is only possible when the child element is not rotated around the $x$ or $y$ axis with respect to its parent.

The reference frame for the first element for the gripper creation is always the center of the robot's flange with the $z$ axis pointing outwards. It is possible to create a gripper with a tree structure, corresponding to multiple elements having the same parent element, as long as they are all connected.
<|end_chunk_1123|><|start_chunk_1124|>
## Calculated TCP position

After gripper creation via the set_gripper service call, the TCP position in the flange coordinate system is calculated and returned as tcp. pose. flange. It is important to check if this value is the same as the robot's true TCP position. When creating a gripper in the Web GUI the current TCP position is always displayed in the 3D gripper visualization.
<|end_chunk_1124|><|start_chunk_1125|>
### Page 247<|end_chunk_1125|><|start_chunk_1126|>
 Creating rotationally asymmetric grippers 

For grippers which are not rotationally symmetric around the $z$ axis, it is crucial to ensure that the gripper is properly mounted, so that the representation stored in the GripperDB module corresponds to reality.
<|end_chunk_1126|><|start_chunk_1127|>
### 6.6.3.3 Services

The GripperDB module is called rc_gripper_db in the REST-API and is represented in the Web GUI (Section 7.1) under Database $\rightarrow$ Grippers. The user can explore and call the GripperDB module's services, e.g. for development and testing, using the REST-API interface (Section 7.3) or the Web GUI.

The GripperDB module offers the following services.
set_gripper
Persistently stores a gripper on the rc_visard. All configured grippers are persistent over firmware updates and rollbacks.
<|end_chunk_1127|><|start_chunk_1128|>
## Details

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_gripper_db/services/set_gripper
<|end_chunk_1128|><|start_chunk_1129|>
## Request

Required arguments:
elements: list of geometric elements for the gripper. Each element must be of type 'CYLINDER' or 'BOX' with the corresponding dimensions in the cylinder or box field, or of type 'CAD' with the corresponding id in the cad field. The pose of each element must be given in the coordinate frame of the parent element (see Setting a gripper (Section 6.6.3.2) for an explanation of the coordinate frames). The element's id must be unique and must not be 'tcp' or 'flange'. The parent_id is the ID of the parent element. It can either be 'flange' or it must correspond to another element in list.
flange_radius: radius of the flange used in case the check_flange run-time parameter is active.
id: unique name of the gripper
tcp_parent_id: ID of the element on which the TCP is defined
tcp pose parent: The pose of the TCP with respect to the coordinate frame of the element specified in tcp_parent_id.

The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "elements": [
            {
            "box": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "cad": {
                "id": "string"
            },
```

(continues on next page)
<|end_chunk_1129|><|start_chunk_1130|>
### Page 248
![img-74.jpeg](img-74.jpeg)
<|end_chunk_1130|><|start_chunk_1131|>
 Response 

gripper: returns the gripper as defined in the request with an additional field tcp_pose.flange. This gives the coordinates of the TCP in the flange coordinate frame for comparison with the true settings of the robot's TCP.
return_code: holds possible warnings or error codes and messages.
The definition for the response with corresponding datatypes is:

```
{
    "name": "set_gripper",
    "response": {
        "gripper": {
            "elements": [
            {
            "box": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
            },
```

        \},
    (continues on next page)
<|end_chunk_1131|><|start_chunk_1132|>
### Page 249
(continued from previous page)
![img-75.jpeg](img-75.jpeg)
<|end_chunk_1132|><|start_chunk_1133|>
### Page 250
get_grippers

Returns the configured grippers with the requested gripper_ids.
<|end_chunk_1133|><|start_chunk_1134|>
 Details 

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_gripper_db/services/get_grippers
<|end_chunk_1134|><|start_chunk_1135|>
## Request

If no gripper_ids are provided, all configured grippers are returned.
The definition for the request arguments with corresponding datatypes is:

```
{
    "args": {
        "gripper_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1135|><|start_chunk_1136|>
## Response

The definition for the response with corresponding datatypes is:

```
{
    "name": "get_grippers",
    "response": {
        "grippers": [
            {
            "elements": [
                {
                    "box": {
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
            },
            "cad": {
                "id": "string"
            },
            "cylinder": {
                "height": "float64",
                    "radius": "float64"
            },
            "id": "string",
            "parent_id": "string",
            "pose": {
                    "orientation": {
                        "w": "float64",
                        "x": "float64",
                        "y": "float64",
                        "z": "float64"
            },
            "position": {
                    "x": "float64",
                    "y": "float64",
```
<|end_chunk_1136|><|start_chunk_1137|>
### Page 251
(continued from previous page)

```
                    "z": "float64"
                }
                },
                "type": "string"
            }
            ],
            "flange_radius": "float64",
            "id": "string",
            "tcp_parent_id": "string",
            "tcp_pose_flange": {
                "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "tcp_pose_parent": {
                "orientation": {
                "w": "float64",
                "x": "float64",
                "y": "float64",
                "z": "float64"
            },
            "position": {
                "x": "float64",
                "y": "float64",
                "z": "float64"
            }
            },
            "type": "string"
        }
    ],
    "return_code": {
        "message": "string",
        "value": "int16"
    }
    }
}
```

delete_grippers

Deletes the configured grippers with the requested gripper_ids.
<|end_chunk_1137|><|start_chunk_1138|>
 Details 

This service can be called as follows.
PUT http://<host>/api/v2/nodes/rc_gripper_db/services/delete_grippers
<|end_chunk_1138|><|start_chunk_1139|>
## Request

All grippers to be deleted must be explicitly stated in gripper_ids.
The definition for the request arguments with corresponding datatypes is:
<|end_chunk_1139|><|start_chunk_1140|>
### Page 252
```
{
    "args": {
        "gripper_ids": [
            "string"
        ]
    }
}
```

<|end_chunk_1140|><|start_chunk_1141|>
 Response 

The definition for the response with corresponding datatypes is:

```
{
    "name": "delete_grippers",
    "response": {
        "return_code": {
            "message": "string",
            "value": "int16"
        }
    }
}
```

<|end_chunk_1141|><|start_chunk_1142|>
### 6.6.3.4 Return codes

Each service response contains a return_code, which consists of a value plus an optional message. A successful service returns with a return_code value of 0 . Negative return_code values indicate that the service failed. Positive return_code values indicate that the service succeeded with additional information. The smaller value is selected in case a service has multiple return_code values, but all messages are appended in the return_code message.

The following table contains a list of common codes:
Table 6.58: Return codes of the GripperDB services

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | An invalid argument was provided |
| -7 | Data could not be read or written to persistent storage |
| -9 | No valid license for the module |
| -10 | New gripper could not be added as the maximum storage capacity of grippers has been <br> exceeded |
| 10 | The maximum storage capacity of grippers has been reached |
| 11 | Existing gripper was overwritten |
<|end_chunk_1142|><|start_chunk_1143|>
### 6.6.3.5 CAD element API

For gripper CAD element upload, download, listing and removal, special REST-API endpoints are provided. CAD elements can also be uploaded, downloaded and removed via the Web GUI. Up to 50 CAD elements can be stored persistently on the $r c \_v i s a r d$.

The maximum file size to be uploaded is limited to 10 MB .
GET /cad/gripper_elements
Get list of all CAD gripper elements.
Template request
GET /api/v2/cad/gripper_elements HTTP/1.1
Template response
<|end_chunk_1143|><|start_chunk_1144|>
### Page 253
```
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "id": "string"
    }
]
```

<|end_chunk_1144|><|start_chunk_1145|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_1145|><|start_chunk_1146|>
## Status Codes

- 200 OK - successful operation (returns array of GripperElement)
- 404 Not Found - element not found

<|end_chunk_1146|><|start_chunk_1147|>
## Referenced Data Models

- GripperElement (Section 7.3.4)

GET /cad/gripper_elements/\{id\}
Get a CAD gripper element. If the requested content-type is application/octet-stream, the gripper element is returned as file.
<|end_chunk_1147|><|start_chunk_1148|>
## Template request

GET /api/v2/cad/gripper_elements/<id> HTTP/1.1
<|end_chunk_1148|><|start_chunk_1149|>
## Template response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": "string"
}
```

<|end_chunk_1149|><|start_chunk_1150|>
## Parameters

- id (string) - id of the element (required)

<|end_chunk_1150|><|start_chunk_1151|>
## Response Headers

- Content-Type - application/json application/ubjson application/octet-stream

<|end_chunk_1151|><|start_chunk_1152|>
## Status Codes

- 200 OK - successful operation (returns GripperElement)
- 404 Not Found - element not found

<|end_chunk_1152|><|start_chunk_1153|>
## Referenced Data Models

- GripperElement (Section 7.3.4)

PUT /cad/gripper_elements/\{id\}
Create or update a CAD gripper element.
<|end_chunk_1153|><|start_chunk_1154|>
## Template request

PUT /api/v2/cad/gripper_elements/<id> HTTP/1.1
Accept: multipart/form-data application/json
<|end_chunk_1154|><|start_chunk_1155|>
## Template response
<|end_chunk_1155|><|start_chunk_1156|>
### Page 254
```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": "string"
}
```

<|end_chunk_1156|><|start_chunk_1157|>
 Parameters 

- id (string) - id of the element (required)

<|end_chunk_1157|><|start_chunk_1158|>
## Form Parameters

- file - CAD file (required)

<|end_chunk_1158|><|start_chunk_1159|>
## Request Headers

- Accept - multipart/form-data application/json

<|end_chunk_1159|><|start_chunk_1160|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1160|><|start_chunk_1161|>
## Status Codes

- 200 OK - successful operation (returns GripperElement)
- 400 Bad Request - CAD is not valid or max number of elements reached
- 404 Not Found - element not found
- 413 Request Entity Too Large - File too large

<|end_chunk_1161|><|start_chunk_1162|>
## Referenced Data Models

- GripperElement (Section 7.3.4)

DELETE /cad/gripper_elements/\{id\}
Remove a CAD gripper element.
Template request
DELETE /api/v2/cad/gripper_elements/<id> HTTP/1.1
Accept: application/json application/ubjson
<|end_chunk_1162|><|start_chunk_1163|>
## Parameters

- id (string) - id of the element (required)

<|end_chunk_1163|><|start_chunk_1164|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1164|><|start_chunk_1165|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1165|><|start_chunk_1166|>
## Status Codes

- 200 OK - successful operation
- 404 Not Found - element not found
<|end_chunk_1166|><|start_chunk_1167|>
### Page 255<|end_chunk_1167|><|start_chunk_1168|>
 7 Interfaces 

The following interfaces are provided for configuring and obtaining data from the rc_visard:

- Web GUI (Section 7.1)

Easy-to-use graphical interface to configure the $r c \_v i s a r d$, do calibrations, view live images, do service calls, visualize results, etc.

- GigE Vision 2.0/GenICam (Section 7.2)

Images and camera related configuration.

- REST API (Section 7.3)

API to configure the $r c \_v i s a r d$, query status information, do service calls, etc.

- rc_dynamics streams (Section 7.4)

Real-time streams containing state estimates with poses, velocities, etc. are provided over the $r c \_d y n a m i c s$ interface. It sends protobuf-encoded messages via UDP.

- Ethernet KRL Interface (EKI) (Section 7.5)

API to configure the $r c \_v i s a r d$ and do service calls from KUKA KSS robots.

- gRPC image stream (Section 7.6)

Stream synchronized image sets via gRPC.

- Time synchronization (Section 7.8)

Time synchronization between the $r c \_v i s a r d$ and the application host.
<|end_chunk_1168|><|start_chunk_1169|>
### 7.1 Web GUI

The $r c \_v i s a r d ' s$ Web GUI can be used to test, calibrate, and configure the device.
<|end_chunk_1169|><|start_chunk_1170|>
### 7.1.1 Accessing the Web GUI

The Web GUI can be accessed from any web browser, such as Firefox, Google Chrome, or Microsoft Edge, via the $r c \_v i s a r d ' s$ IP address. The easiest way to access the Web GUI is to simply double click on the desired device using the rcdiscover-gui tool as explained in Discovery of rc_visard devices (Section 4.3).
Alternatively, some network environments automatically configure the unique host name of the $r c \_v i s a r d$ in their Domain Name Server (DNS). In this case, the Web GUI can also be accessed directly using the URL http://<host-name> by replacing <host-name> with the device's host name.
For Linux and Mac operating systems, this even works without DNS via the multicast Domain Name System (mDNS), which is automatically used if .local is appended to the host name. Thus, the URL simply becomes http://<host-name>.local.
<|end_chunk_1170|><|start_chunk_1171|>
### Page 256<|end_chunk_1171|><|start_chunk_1172|>
 7.1.2 Exploring the Web GUI 

The Web GUI's dashboard page gives the most important information about the device and the software modules.
![img-76.jpeg](img-76.jpeg)

Fig. 7.1: Dashboard page of the rc_visard's Web GUI

The page's side menu permits access to the individual pages of the rc_visard's Web GUI:
Camera shows a live stream of the rectified camera images. The frame rate can be reduced to save bandwidth when streaming to a GigE Vision ${ }^{\circledR}$ client. Furthermore, exposure can be set manually or automatically. See Camera module (Section 6.1) for more information.

Depth Image shows a live stream of the left rectified, disparity, and confidence images. The page contains various settings for depth-image computation and filtering. See Stereo matching module (Section 6.2) for more information.

Dynamics shows the location and movement of image features that are used to compute the rc_visard's egomotion. Settings include the number of corners and features that should be used. See Parameters (Section 6.3.2.1) for more information.

Modules gives access to the detection modules of the rc_visard (see Detection \& Measure modules, Section 6.4).

Configuration gives access to the configuration modules of the rc_visard (see Configuration modules, Section 6.5).

Database gives access to the database modules of the rc_visard (see Database modules, Section 6.6).

System gives access to general settings, device information and to the log files, and permits the firmware or the license file to be updated.

Note: Further information on all parameters in the Web GUI can be obtained by pressing the Info button next to each parameter.
<|end_chunk_1172|><|start_chunk_1173|>
### 7.1.3 Web GUI access control

The Web GUI has a simple mechanism to lock the UI against casual and accidental changes.
When enabling Web GUI access control via the System page, you will be asked to set a password. Now the Web GUI is in a locked mode indicated by the lock symbol in the top bar. All pages, camera streams, parameters and detections can be inspected as usual, but changes are not possible.
<|end_chunk_1173|><|start_chunk_1174|>
### Page 257
To temporarily unlock the Web GUI and make changes, click the lock symbol and enter the password. While enabling or disabling Web GUI access control affects anyone accessing this rc_visard, the unlocked state is only valid for the browser where it was unlocked and indicated by the open lock symbol. It is automatically locked again after 10 minutes of inactivity.
Web GUI access control can also be disabled again on the System page after providing the current password.

Warning: This is not a security feature! It only locks the Web GUI and not the REST-API. It is meant to prevent accidental and casual changes e.g. via a connected screen.

Note: In case the password is lost, this can be disabled via the REST-API delete ui_lock (Section 7.3.3.3).
<|end_chunk_1174|><|start_chunk_1175|>
 7.1.4 Downloading camera images 

The Web GUI provides an easy way to download a snapshot of the current scene as a .tar.gz file by clicking on the camera icon below the image live streams on the Camera page. This snapshot contains:

- the rectified camera images in full resolution as .png files,
- a camera parameter file containing the camera matrix, image dimensions, exposure time, gain value and the stereo baseline,
- the current IMU readings as imu.csv file,
- a pipeline_status.json file containing information about all 3D-camera, detection and configuration nodes running on the $r c \_v i s a r d$,
- a backup.json file containing the settings of the $r c \_v i s a r d$ including grippers, load carriers and regions of interest,
- a system_info.json file containing system information about the $r c \_v i s a r d$.

The filenames contain the timestamps.
<|end_chunk_1175|><|start_chunk_1176|>
### 7.1.5 Downloading depth images and point clouds

The Web GUI provides an easy way to download the depth data of the current scene as a .tar.gz file by clicking on the camera icon below the image live streams on the Depth Image page. This snapshot contains:

- the rectified left and right camera images in full resolution as .png files,
- an image parameter file corresponding to the left image containing the camera matrix, image dimensions, exposure time, gain value and the stereo baseline,
- the disparity, error and confidence images in the resolution corresponding to the currently chosen quality as .png files,
- a disparity parameter file corresponding to the disparity image containing the camera matrix, image dimensions, exposure time, gain value and the stereo baseline, and information about the disparity values (i.e. invalid values, scale, offset),
- the current IMU readings as imu.csv file,
- a pipeline_status.json file containing information about all 3D-camera, detection and configuration nodes running on the $r c \_v i s a r d$,
- a backup.json file containing the settings of the $r c \_v i s a r d$ including grippers, load carriers and regions of interest,
<|end_chunk_1176|><|start_chunk_1177|>
### Page 258
- a system_info.json file containing system information about the rc_visard.

The filenames contain the timestamps.
When clicking on the mesh icon below the image live streams on the Depth Image page, a snapshot is downloaded which additionally includes a mesh of the point cloud in the current depth quality (resolution) as .ply file.

Note: Downloading a depth snapshot will trigger an acquisition in the same way as clicking on the "Acquire" button on the Depth Image page of the Web GUI, and, thus, might affect running applications.
<|end_chunk_1177|><|start_chunk_1178|>
 7.2 GigE Vision 2.0/GenICam image interface 

Gigabit Ethernet for Machine Vision ("GigE Vision®" for short) is an industrial camera interface standard based on UDP/IP (see http://www.gigevision.com). The $r c \_v i s a r d$ is a GigE Vision® version 2.0 device and is hence compatible with all GigE Vision® 2.0 compliant frameworks and libraries.
GigE Vision® uses GenICam to describe the camera/device features. For more information about this Generic Interface for Cameras see http://www.genicam.org/.
Via this interface the $r c \_v i s a r d$ provides features such as

- discovery,
- IP configuration,
- configuration of camera related parameters,
- image grabbing, and
- time synchronization via IEEE 1588-2008 PrecisionTimeProtocol (PTPv2).

Note: The $r c \_v i s a r d$ supports jumbo frames of up to 9000 bytes. Setting an MTU of 9000 on your GigE Vision client side is recommended for best performance.

Note: Roboception provides tools and a C++ API with examples for discovery, configuration, and image streaming via the GigE Vision/GenICam interface. See http://www.roboception.com/download.
<|end_chunk_1178|><|start_chunk_1179|>
### 7.2.1 GigE Vision ports

GigE Vision is a UDP based protocol. On the $r c \_v i s a r d$ the UDP ports are fixed and known:

- UDP port 3956: GigE Vision Control Protocol (GVCP). Used for discovery, control and configuration.
- UDP port 50010: Stream channel source port for GigE Vision Stream Protocol (GVSP) used for image streaming.

<|end_chunk_1179|><|start_chunk_1180|>
### 7.2.2 Important GenICam parameters

The following list gives an overview of the relevant GenICam features of the $r c \_v i s a r d$ that can be read and/or changed via the GenICam interface. In addition to the standard parameters, which are defined in the Standard Feature Naming Convention (SFNC, see http://www.emva.org/standards-technology/ genicam/genicam-downloads/), rc_visard devices also offer custom parameters that account for special features of the Camera module (Section 6.1) and the Stereo matching module (Section 6.2) module.
<|end_chunk_1180|><|start_chunk_1181|>
### Page 259<|end_chunk_1181|><|start_chunk_1182|>
 7.2.3 Important standard GenICam features 
<|end_chunk_1182|><|start_chunk_1183|>
### 7.2.3.1 Category: ImageFormatControl
<|end_chunk_1183|><|start_chunk_1184|>
## ComponentSelector

- type: Enumeration, one of Intensity, IntensityCombined, Disparity, Confidence, or Error
- default: -
- description: Allows the user to select one of the five image streams for configuration (see Provided image streams, Section 7.2.6).

<|end_chunk_1184|><|start_chunk_1185|>
## ComponentIDValue (read-only)

- type: Integer
- description: The ID of the image stream selected by the ComponentSelector.

<|end_chunk_1185|><|start_chunk_1186|>
## ComponentEnable

- type: Boolean
- default: -
- description: If set to true, it enables the image stream selected by ComponentSelector; otherwise, it disables the stream. Using ComponentSelector and ComponentEnable, individual image streams can be switched on and off.

<|end_chunk_1186|><|start_chunk_1187|>
## Width (read-only)

- type: Integer
- description: Image width in pixel of image stream that is currently selected by ComponentSelector.

<|end_chunk_1187|><|start_chunk_1188|>
## Height (read-only)

- type: Integer
- description: Image height in pixel of image stream that is currently selected by ComponentSelector.

<|end_chunk_1188|><|start_chunk_1189|>
## WidthMax (read-only)

- type: Integer
- description: Maximum width of an image.

<|end_chunk_1189|><|start_chunk_1190|>
## HeightMax (read-only)

- type: Integer
- description: Maximum height of an image in the streams. This is always 1920 pixels due to the stacked left and right images in the IntensityCombined stream (see Provided image streams, Section 7.2.6).

<|end_chunk_1190|><|start_chunk_1191|>
## PixelFormat

- type: Enumeration, one of Mono8, YCbCr411_8 (color cameras only), Coord3D_C16, Confidence8 and Error8
- description: Pixel format of the selected component. The enumeration only permits to choose the format among the possibly formats for the selected component. For a color camera, Mono8 or YCbCr411_8 can be chosen for the Intensity and IntensityCombined component.
<|end_chunk_1191|><|start_chunk_1192|>
### Page 260<|end_chunk_1192|><|start_chunk_1193|>
 7.2.3.2 Category: AcquisitionControl 
<|end_chunk_1193|><|start_chunk_1194|>
## AcquisitionFrameRate

- type: Float, ranges from 1 Hz to 25 Hz
- default: 25 Hz
- description: Frame rate of the camera

<|end_chunk_1194|><|start_chunk_1195|>
## ExposureAuto

- type: Enumeration, one of Continuous, Out1High, AdaptiveOut1, HDR or Off
- default: Continuous
- description: Combines exp_control and exp_auto_mode. Off maps to Manual exposure control. Continuous, Out1High or AdaptiveOut1 enable Auto exposure control with the respective auto exposure mode where Continuous maps to the Normal exp_auto_mode. HDR enables high-dynamic-range exposure control.

<|end_chunk_1195|><|start_chunk_1196|>
## ExposureTime

- type: Float, ranges from $66 \mu \mathrm{~s}$ to $18000 \mu \mathrm{~s}$
- default: $5000 \mu \mathrm{~s}$
- description: The cameras' exposure time in microseconds for the manual exposure mode.

<|end_chunk_1196|><|start_chunk_1197|>
### 7.2.3.3 Category: AnalogControl

GainSelector (read-only)

- type: Enumeration, is always All
- default: All
- description: The rc_visard currently supports only one overall gain setting.

<|end_chunk_1197|><|start_chunk_1198|>
## Gain

- type: Float, ranges from 0 dB to 18 dB
- default: 0 dB
- description: The cameras' gain value in decibel that is used in manual exposure mode.

<|end_chunk_1198|><|start_chunk_1199|>
## BalancewhiteAuto (color cameras only)

- type: Enumeration, one of Continuous or Off
- default: Continuous
- description: Can be set to off for manual white balancing mode or to Continuous for auto white balancing. This feature is only available on color cameras.

<|end_chunk_1199|><|start_chunk_1200|>
## BalanceRatioSelector (color cameras only)

- type: Enumeration, one of Red or Blue
- default: Red
- description: Selects ratio to be modified by BalanceRatio. Red means red to green ratio and Blue means blue to green ratio. This feature is only available on color cameras.

<|end_chunk_1200|><|start_chunk_1201|>
## BalanceRatio (color cameras only)

- type: Float, ranges from 0.125 to 8
- default: 1.2 if Red and 2.4 if Blue is selected in BalanceRatioSelector
<|end_chunk_1201|><|start_chunk_1202|>
### Page 261
- description: Weighting of red or blue to green color channel. This feature is only available on color cameras.

<|end_chunk_1202|><|start_chunk_1203|>
 7.2.3.4 Category: DigitallOControl 
<|end_chunk_1203|><|start_chunk_1204|>
## LineSelector

- type: Enumeration, one of Out1, Out2, In1 or In2
- default: Out1
- description: Selects the input or output line for getting the current status or setting the source.

<|end_chunk_1204|><|start_chunk_1205|>
## LineStatus (read-only)

- type: Boolean
- description: Current status of the line selected by LineSelector.

<|end_chunk_1205|><|start_chunk_1206|>
## LineStatusAll (read-only)

- type: Integer
- description: Current status of GPIO inputs and outputs represented in the lowest four bits.

Table 7.1: Meaning of bits of LineStatusAll field.

| Bit | 4 | 3 | 2 | 1 |
| :-- | :-- | :-- | :-- | :-- |
| GPIO | $\ln 2$ | $\ln 1$ | Out 2 | Out 1 |
<|end_chunk_1206|><|start_chunk_1207|>
## LineSource

- type: Enumeration, one of ExposureActive, ExposureAlternateActive, Low or High
- default: Low
- description: Mode for output line selected by LineSelector as described in the IOControl module (out1_mode and out2_mode, Section 6.5.4.1). See also parameter AcquisitionAlternateFilter for filtering images in ExposureAlternateActive mode.

<|end_chunk_1207|><|start_chunk_1208|>
### 7.2.3.5 Category: TransportLayerControl / PtpControl
<|end_chunk_1208|><|start_chunk_1209|>
## PtpEnable

- type: Boolean
- default: false
- description: Switches PTP synchronization on and off.

<|end_chunk_1209|><|start_chunk_1210|>
### 7.2.3.6 Category: Scan3dControl
<|end_chunk_1210|><|start_chunk_1211|>
## Scan3dDistanceUnit (read-only)

- type: Enumeration, is always Pixel
- description: Unit for the disparity measurements, which is always Pixel.

<|end_chunk_1211|><|start_chunk_1212|>
## Scan3dOutputMode (read-only)

- type: Enumeration, is always DisparityC
- description: Mode for the depth measurements, which is always DisparityC.

<|end_chunk_1212|><|start_chunk_1213|>
## Scan3dFocalLength (read-only)

- type: Float
<|end_chunk_1213|><|start_chunk_1214|>
### Page 262
- description: Focal length in pixel of image stream selected by ComponentSelector. In case of the component Disparity, Confidence and Error, the value also depends on the resolution that is implicitly selected by DepthQuality.

<|end_chunk_1214|><|start_chunk_1215|>
 Scan3dBaseline (read-only) 

- type: Float
- description: Baseline of the stereo camera in meters.

<|end_chunk_1215|><|start_chunk_1216|>
## Scan3dPrinciplePointU (read-only)

- type: Float
- description: Horizontal location of the principle point in pixel of image stream selected by ComponentSelector. In case of the component Disparity, Confidence and Error, the value also depends on the resolution that is implicitly selected by DepthQuality.

<|end_chunk_1216|><|start_chunk_1217|>
## Scan3dPrinciplePointV (read-only)

- type: Float
- description: Vertical location of the principle point in pixel of image stream selected by ComponentSelector. In case of the component Disparity, Confidence and Error, the value also depends on the resolution that is implicitly selected by DepthQuality.

<|end_chunk_1217|><|start_chunk_1218|>
## Scan3dCoordinateScale (read-only)

- type: Float
- description: The scale factor that has to be multiplied with the disparity values in the disparity image stream to get the actual disparity measurements. This value is always 0.0625 .

<|end_chunk_1218|><|start_chunk_1219|>
## Scan3dCoordinateOffset (read-only)

- type: Float
- description: The offset that has to be added to the disparity values in the disparity image stream to get the actual disparity measurements. For the rc_visard, this value is always 0 and can therefore be disregarded.

<|end_chunk_1219|><|start_chunk_1220|>
## Scan3dInvalidDataFlag (read-only)

- type: Boolean
- description: Is always true, which means that invalid data in the disparity image is marked by a specific value defined by the Scan3dInvalidDataValue parameter.

<|end_chunk_1220|><|start_chunk_1221|>
## Scan3dInvalidDataValue (read-only)

- type: Float
- description: Is the value which stands for invalid disparity. This value is always 0 , which means that disparity values of 0 correspond to invalid measurements. To distinguish between invalid disparity measurements and disparity measurements of 0 for objects which are infinitely far away, the $r c \_v i s a r d$ sets the disparity value for the latter to the smallest possible disparity value of 0.0625 . This still corresponds to an object distance of several hundred meters.

<|end_chunk_1221|><|start_chunk_1222|>
### 7.2.3.7 Category: ChunkDataControl
<|end_chunk_1222|><|start_chunk_1223|>
## ChunkModeActive

- type: Boolean
- default: False
- description: Enables chunk data that is delivered with every image.
<|end_chunk_1223|><|start_chunk_1224|>
### Page 263<|end_chunk_1224|><|start_chunk_1225|>
 7.2.4 Custom GenICam features of the $r c \_v i s a r d$ 
<|end_chunk_1225|><|start_chunk_1226|>
### 7.2.4.1 Category: DeviceControl
<|end_chunk_1226|><|start_chunk_1227|>
## RcSystemReady (read-only)

- type: Boolean
- description: Returns whether the device's boot process has completed and all modules are running.

<|end_chunk_1227|><|start_chunk_1228|>
## RcParamLockDisable

- type: Boolean
- default: False
- description: If set to true, the camera and depth image parameters are not locked when a GigE Vision client is connected to the device. Please note that depending on the connected GigE Vision client, parameter changes by other applications (e.g. the Web GUI) might not be noticed by the GigE Vision client, which could lead to unwanted results.

<|end_chunk_1228|><|start_chunk_1229|>
### 7.2.4.2 Category: AcquisitionControl
<|end_chunk_1229|><|start_chunk_1230|>
## AcquisitionAlternateFilter

- type: Enumeration, one of Off, OnlyHigh or OnlyLow
- default: Off
- description: If this parameter is set to OnlyHigh (or OnlyLow) and the LineSource is set to ExposureAlternateActive for any output, then only camera images are delivered that are captured while the output is high, i.e. a potentially connected projector is on (or low, i.e. a potentially connected projector is off). This parameter is a simple means for only getting images without projected pattern. The minimal time difference between camera and disparity images will be about 40 ms in this case (see IOControl, Section 6.5.4.1).

<|end_chunk_1230|><|start_chunk_1231|>
## AcquisitionMultiPartMode

- type: Enumeration, one of SingleComponent or SynchronizedComponents
- default: SingleComponent
- description: Only effective in MultiPart mode. If this parameter is set to SingleComponent the images are sent immediately as a single component per frame/buffer when they become available. This is the same behavior as when MultiPart is not supported by the client. If set to SynchronizedComponents all enabled components are time synchronized on the rc_visard and only sent (in one frame/buffer) when they are all available for that timestamp.

<|end_chunk_1231|><|start_chunk_1232|>
## ExposureTimeAutoMax

- type: Float, ranges from $66 \mu \mathrm{~s}$ to $18000 \mu \mathrm{~s}$
- default: $18000 \mu \mathrm{~s}$
- description: Maximal exposure time in auto exposure mode.

<|end_chunk_1232|><|start_chunk_1233|>
## ExposureRegionOffsetX

- type: Integer in the range of 0 to the maximum image width
- default: 0
- description: Horizontal offset of exposure region in pixel.

<|end_chunk_1233|><|start_chunk_1234|>
## ExposureRegionOffsetY

- type: Integer in the range of 0 to the maximum image height
<|end_chunk_1234|><|start_chunk_1235|>
### Page 264
- default: 0
- description: Vertical offset of exposure region in pixel.

<|end_chunk_1235|><|start_chunk_1236|>
 ExposureRegionWidth 

- type: Integer in the range of 0 to the maximum image width
- default: 0
- description: Width of exposure region in pixel.

<|end_chunk_1236|><|start_chunk_1237|>
## ExposureRegionHeight

- type: Integer in the range of 0 to the maximum image height
- default: 0
- description: Height of exposure region in pixel.

<|end_chunk_1237|><|start_chunk_1238|>
## RcExposureAutoAverageMax

- type: Float in the range of 0 to 1
- default: 0.75
- description: Maximum brightness for the auto exposure function as value between 0 (dark) and 1 (bright).

<|end_chunk_1238|><|start_chunk_1239|>
## RcExposureAutoAverageMin

- type: Float in the range of 0 to 1
- default: 0.25
- description: Minimum brightness for the auto exposure function as value between 0 (dark) and 1 (bright).

<|end_chunk_1239|><|start_chunk_1240|>
### 7.2.4.3 Category: Scan3dControl

FocalLengthFactor (read-only)

- type: Float
- description: The focal length scaled to an image width of 1 pixel. To get the focal length in pixels for a certain image, this value must be multiplied by the width of the received image. See also parameter Scan3dFocalLength.

<|end_chunk_1240|><|start_chunk_1241|>
## Baseline (read-only)

- type: Float
- description: This parameter is deprecated. The parameter Scan3dBaseline should be used instead.

<|end_chunk_1241|><|start_chunk_1242|>
### 7.2.4.4 Category: DepthControl
<|end_chunk_1242|><|start_chunk_1243|>
## DepthAcquisitionMode

- type: Enumeration, one of SingleFrame, SingleFrameOut1 or Continuous
- default: Continuous
- description: In single frame mode, stereo matching is performed upon each call of DepthAcquisitionTrigger. The SingleFrameOut1 mode can be used to control an external projector. It sets the line source of Out1 to ExposureAlternateActive upon each trigger and resets it to Low as soon as the images for stereo matching are grabbed. In continuous mode, stereo matching is performed continuously.

<|end_chunk_1243|><|start_chunk_1244|>
## DepthAcquisitionTrigger
<|end_chunk_1244|><|start_chunk_1245|>
### Page 265
- type: Command
- description: This command triggers stereo matching of the next available stereo image pair, if DepthAcquisitionMode is set to SingleFrame or SingleFrameOut1.

<|end_chunk_1245|><|start_chunk_1246|>
 DepthQuality 

- type: Enumeration, one of Low, Medium, High, or Full (only with StereoPlus license)
- default: High
- description: Quality of disparity images. Lower quality results in disparity images with lower resolution (Quality, Section 6.2.1.2).

<|end_chunk_1246|><|start_chunk_1247|>
## DepthDoubleShot

- type: Boolean
- default: False
- description: True for improving the stereo matching result of a scene recorded with a projector by filling holes with depth information computed from images without projector pattern. (Double-Shot, Section 6.2.1.2).

<|end_chunk_1247|><|start_chunk_1248|>
## DepthStaticScene

- type: Boolean
- default: False
- description: True for averaging 8 consecutive camera images for improving the stereo matching result. (Static, Section 6.2.1.2).

<|end_chunk_1248|><|start_chunk_1249|>
## DepthSmooth (read-only if StereoPlus license is not available)

- type: Boolean
- default: False
- description: True for advanced smoothing of disparity values. (Smoothing, Section 6.2.1.2).

<|end_chunk_1249|><|start_chunk_1250|>
## DepthFill

- type: Integer, ranges from 0 pixel to 4 pixels
- default: 3 pixels
- description: Value in pixels for Fill-In (Section 6.2.1.2).

<|end_chunk_1250|><|start_chunk_1251|>
## DepthSeg

- type: Integer, ranges from 0 pixel to 4000 pixels
- default: 200 pixels
- description: Value in pixels for Segmentation (Section 6.2.1.2).

<|end_chunk_1251|><|start_chunk_1252|>
## DepthMinConf

- type: Float, ranges from 0.0 to 1.0
- default: 0.0
- description: Value for Minimum Confidence filtering (Section 6.2.1.2).

<|end_chunk_1252|><|start_chunk_1253|>
## DepthMinDepth

- type: Float, ranges from 0.1 m to 100.0 m
- default: 0.1 m
- description: Value in meters for Minimum Distance filtering (Section 6.2.1.2).

<|end_chunk_1253|><|start_chunk_1254|>
## DepthMaxDepth

- type: Float, ranges from 0.1 m to 100.0 m
<|end_chunk_1254|><|start_chunk_1255|>
### Page 266
- default: 100.0 m
- description: Value in meters for Maximum Distance filtering (Section 6.2.1.2).

<|end_chunk_1255|><|start_chunk_1256|>
 DepthMaxDepthErr 

- type: Float, ranges from 0.01 m to 100.0 m
- default: 100.0 m
- description: Value in meters for Maximum Depth Error filtering (Section 6.2.1.2).

<|end_chunk_1256|><|start_chunk_1257|>
### 7.2.5 Chunk data

The rc_visard supports chunk parameters that are transmitted with every image. Chunk parameters all have the prefix Chunk. Their meaning equals their non-chunk counterparts, except that they belong to the corresponding image, e.g. Scan3dFocalLength depends on ComponentSelector and DepthQuality as both can change the image resolution. The parameter ChunkScan3dFocalLength that is delivered with an image fits to the resolution of the corresponding image.
Particularly useful chunk parameters are:

- ChunkComponentSelector selects for which component to extract the chunk data in MultiPart mode.
- ChunkComponentID and ChunkComponentIDValue provide the relation of the image to its component (e.g. camera image or disparity image) without guessing from the image format or size.
- ChunkLineStatusAll provides the status of all GPIOs at the time of image acquisition. See LineStatusAll above for a description of bits.
- ChunkScan3d... parameters are useful for 3D reconstruction as described in Section Image stream conversions (Section 7.2.7).
- ChunkPartIndex provides the index of the image part in this MultiPart block for the selected component (ChunkComponentSelector).
- ChunkRcOut1Reduction gives a ratio of how much the brightness of the images with GPIO Out1 LOW is lower than the brightness of the images with GPIO Out1 HIGH. For example, a value of 0.2 means that the images with GPIO Out1 LOW have 20\% less brightness than the images with GPIO Out1 HIGH. This value is only available if exp_auto_mode of the stereo camera is set to AdaptiveOut1 or Out1High.
Chunk data is enabled by setting the GenICam parameter ChunkModeActive to True.

<|end_chunk_1257|><|start_chunk_1258|>
### 7.2.6 Provided image streams

The $r c \_v i s a r d$ provides the following five different image streams via the GenICam interface:
<|end_chunk_1258|><|start_chunk_1259|>
### Page 267
| Component name | PixelFormat | Description |
| :-- | :-- | :-- |
| Intensity | <br> Mono8 (monochrome <br> cameras) <br> YCbCr411_8 (color <br> cameras) | Left rectified cam- <br> era image |
| IntensityCombined | <br> Mono8 (monochrome <br> cameras) <br> YCbCr411_8 (color <br> cameras) | Left rectified cam- <br> era image stacked <br> on right rectified <br> camera image |
| Disparity | Coord3D_C16 | Disparity image in <br> desired resolution, <br> i.e., DepthQuality <br> of Full, High, <br> Medium or Low |
| Confidence | Confidence8 | Confidence image <br> Disparity error im- <br> age |
| Error | Error8 <br> 0x81080001) |  |

Each image comes with a buffer timestamp and the PixelFormat given in the above table. This PixelFormat should be used to distinguish between the different image types. Images belonging to the same acquisition timestamp can be found by comparing the GenICam buffer timestamps.
<|end_chunk_1259|><|start_chunk_1260|>
 7.2.7 Image stream conversions 

The disparity image contains 16 bit unsigned integer values. These values must be multiplied by the scale value given in the GenICam feature Scan3dCoordinateScale to get the disparity values $d$ in pixels. To compute the 3D object coordinates from the disparity values, the focal length and the baseline as well as the principle point are required. These parameters are transmitted as GenICam features Scan3dFocalLength, Scan3dBaseline, Scan3dPrincipalPointU and Scan3dPrincipalPointV. The focal length and principal point depend on the image resolution of the selected component. Knowing these values, the pixel coordinates and the disparities can be transformed into 3D object coordinates in the camera coordinate frame using the equations described in Computing depth images and point clouds (Section 5.2.2).

Note: The rc_visard's camera coordinate frame is defined as shown in sensor coordinate frame (Section 3.7).

Assuming that $d 16_{i k}$ is the 16 bit disparity value at column $i$ and row $k$ of a disparity image, the float disparity in pixels $d_{i k}$ is given by

$$
d_{i k}=d 16_{i k} \cdot \text { Scan3dCoordinateScale }
$$

The 3D reconstruction in meters can be written with the GenICam parameters as:

$$
\begin{aligned}
& P_{x}=(i+0.5-\text { Scan3dPrincipalPointU }) \frac{\text { Scan3dBaseline }}{d_{i k}} \\
& P_{y}=(k+0.5-\text { Scan3dPrincipalPointV }) \frac{\text { Scan3dBaseline }}{d_{i k}} \\
& P_{z}=\text { Scan3dFocalLength } \frac{\text { Scan3dBaseline }}{d_{i k}}
\end{aligned}
$$
<|end_chunk_1260|><|start_chunk_1261|>
### Page 268
The confidence image contains 8 bit unsigned integer values. These values have to be divided by 255 to get the confidence as value between 0 an 1.
The error image contains 8 bit unsigned integer values. The error $e_{i k}$ must be multiplied by the scale value given in the GenICam feature Scan3dCoordinateScale to get the disparity-error values $d_{e p s}$ in pixels. According to the description in Confidence and error images (Section 5.2.3), the depth error $z_{e p s}$ in meters can be computed with GenICam parameters as

$$
\begin{aligned}
d_{i k} & =d 16_{i k} \cdot \text { Scan3dCoordinateScale, } \\
z_{e p s} & =\frac{e_{i k} \cdot \text { Scan3dCoordinateScale } \cdot \text { Scan3dFocalLength } \cdot \text { Scan3dBaseline }}{\left(d_{i k}\right)^{2}}
\end{aligned}
$$

Note: It is preferable to enable chunk data with the parameter ChunkModeActive and to use the chunk parameters ChunkScan3dCoordinateScale, ChunkScan3dFocalLength, ChunkScan3dBaseline, ChunkScan3dPrincipalPointU and ChunkScan3dPrincipalPointV that are delivered with every image, because their values already fit to the image resolution of the corresponding image.

For more information about disparity, error, and confidence images, please refer to Stereo matching module (Section 6.2).
<|end_chunk_1261|><|start_chunk_1262|>
 7.3 REST-API interface 

Aside from the GenICam interface (Section 7.2), the rc_visard offers a comprehensive RESTful web interface (REST-API) which any HTTP client or library can access. Whereas most of the provided parameters, services, and functionalities can also be accessed via the user-friendly Web GUI (Section 7.1), the REST-API serves rather as a machine-to-machine interface to the rc_visard, e.g., to programmatically

- set and get run-time parameters of computation nodes, e.g., of cameras or image processing modules;
- do service calls, e.g., to start and stop individual computational nodes, or to use offered services such as the hand-eye calibration;
- read the current state of the system and individual computational nodes; or
- update the $r c \_v i s a r d$ 's firmware or license.

Note: In the rc_visard's REST-API, a node is a computational component that bundles certain algorithmic functionality and offers a holistic interface (parameters, services, current status). Examples for such nodes are the stereo matching node or the hand-eye calibration node.
<|end_chunk_1262|><|start_chunk_1263|>
### 7.3.1 General API structure

The general entry point to the $r c \_v i s a r d$ 's API is http://<host>/api/, where <host> is either the device's IP address or its host name as known by the respective DHCP server, as explained in network configuration (Section 4.4). Accessing this entry point with a web browser lets the user explore and test the full API during run-time using the Swagger UI (Section 7.3.5).
For actual HTTP requests, the current API version is appended to the entry point of the API, i.e., http://<host>/api/v2. All data sent to and received by the REST-API follows the JavaScript Object Notation (JSON). The API is designed to let the user create, retrieve, modify, and delete so-called resources as listed in Available resources and requests (Section 7.3.3) using the HTTP requests below.
<|end_chunk_1263|><|start_chunk_1264|>
### Page 269
| Request type | Description |
| :-- | :-- |
| GET | Access one or more resources <br> and return the result as JSON. |
| PUT | Modify a resource and return the <br> modified resource as JSON. |
| DELETE | Delete a resource. |
| POST | Upload file (e.g., license or <br> firmware image). |

Depending on the type and the specific request itself, arguments to HTTP requests can be transmitted as part of the path (URI) to the resource, as query string, as form data, or in the body of the request. The following examples use the command line tool curl, which is available for various operating systems. See https://curl.haxx.se.

- Get a node's current status; its name is encoded in the path (URI)
curl -X GET 'http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching'
- Get values of some of a node's parameters using a query string
curl -X GET 'http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters?
$\sim$ name=minconf\&name=maxdepth'
- Configure a new datastream; the destination parameter is transmitted as form data
curl -X PUT --header 'Content-Type: application/x-www-form-urlencoded' -d 'destination=10.0.
$\sim 1.14 \% 3 A 30000$ ' 'http://<host>/api/v2/datastreams/pose'
- Set a node's parameter as JSON-encoded text in the body of the request
curl -X PUT --header 'Content-Type: application/json' -d '[\{"name": "mindepth", "value": 0.
$\sim 1$ \}]' 'http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters'
As for the responses to such requests, some common return codes for the rc_visard's API are:

| Status Code | Description |
| :-- | :-- |
| 200 OK | The request was successful; the <br> resource is returned as JSON. |
| 400 Bad Request | A required attribute or argument <br> of the API request is missing or <br> invalid. |
| 404 Not Found | A resource could not be ac- <br> cessed; e.g., an ID for a re- <br> source could not be found. |
| 403 Forbidden | Access is (temporarily) forbid- <br> den; e.g., some parameters are <br> locked while a GigE Vision appli- <br> cation is connected. |
| 429 Too many requests | Rate limited due to excessive re- <br> quest frequency. |

The following listing shows a sample response to a successful request that accesses information about the rc_stereomatching node's minconf parameter:

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 157
```

(continues on next page)
<|end_chunk_1264|><|start_chunk_1265|>
### Page 270
```
{
    "name": "minconf",
    "min": 0,
    "default": 0,
    "max": 1,
    "value": 0,
    "type": "float64",
    "description": "Minimum confidence"
}
```

Note: The actual behavior, allowed requests, and specific return codes depend heavily on the specific resource, context, and action. Please refer to the rc_visard's available resources (Section 7.3.3) and to each software module's (Section 6) parameters and services.
<|end_chunk_1265|><|start_chunk_1266|>
 7.3.2 Migration from API version 1 

API version 1 has become deprecated with the 22.01 firmware release of the $r c \_v i s a r d$. The following changes were introduced in API version 2.

- All 3D-camera, navigation, detection and configuration modules which were located under /nodes in API version 1 are now under /pipelines/0/nodes/, e.g. /pipelines/0/nodes/rc_camera.
- Configuring load carriers, grippers and regions of interest is now only possible in the global database modules, which are located under /nodes, e.g. /nodes/rc_load_carrier_db. The corresponding services in the detection modules have been removed or deprecated.
- Templates can now be accessed under /templates, e.g. /templates/rc_silhouettematch.

<|end_chunk_1266|><|start_chunk_1267|>
### 7.3.3 Available resources and requests

The available REST-API resources are structured into the following parts:

- /nodes Access the rc_visard's global Database modules (Section 6.6) with their run-time status, parameters, and offered services, for storing data used in multiple modules, such as load carriers, grippers and regions of interest.
- /pipelines Access to the status and configuration of the camera pipelines. There is always only one camera pipeline with number 0 .
- /pipelines/0/nodes Access the rc_visard's 3D-camera, navigation, detection and configuration software modules (Section 6) with their run-time status, parameters, and offered services.
- /templates Access the object templates on the $r c \_v i s a r d$.
- /datastreams Access and manage data streams of the $r c \_v i s a r d$ 's $r c \_d y n a m i c s$ interface (Section 7.4).
- /system Access the system state, set network configuration, and manage licenses as well as firmware updates.
- /logs Access the log files on the $r c \_v i s a r d$.

<|end_chunk_1267|><|start_chunk_1268|>
### 7.3.3.1 Nodes, parameters, and services

Nodes represent the $r c \_v i s a r d$ 's software modules (Section 6), each bundling a certain algorithmic functionality. All available global REST-API database nodes can be listed with their service calls and parameters using
<|end_chunk_1268|><|start_chunk_1269|>
### Page 271
curl -X GET http://<host>/api/v2/nodes
Information about a specific node (e.g., rc_load_carrier_db) can be retrieved using
curl -X GET http://<host>/api/v2/nodes/rc_load_carrier_db
All available 3D camera, navigation, detection and configuration REST-API nodes can be listed with their service calls and parameters using
curl -X GET http://<host>/api/v2/pipelines/0/nodes
Information about a specific node (e.g., rc_camera) can be retrieved using
curl -X GET http://<host>/api/v2/pipelines/0/nodes/rc_camera
Status: During run-time, each node offers information about its current status. This includes not only the current processing status of the module (e.g., running or stale), but most nodes also offer run-time statistics or read-only parameters, so-called status values. As an example, the rc_camera values can be retrieved using
curl -X GET http://<host>/api/v2/pipelines/0/nodes/rc_camera/status
Note: The returned status values are specific to individual nodes and are documented in the respective software module (Section 6).

Note: The status values are only reported when the respective node is in the running state.

Parameters: Most nodes expose parameters via the rc_visard's REST-API to allow their run-time behaviors to be changed according to application context or requirements. The REST-API permits to read and write a parameter's value, but also provides further information such as minimum, maximum, and default values.

As an example, the rc_stereomatching parameters can be retrieved using
curl -X GET http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters
Its quality parameter could be set to Full using
curl -X PUT http://<host>/api/v2/pipelines/0/nodes/rc_stereomatching/parameters?quality=Full
or equivalently
curl -X PUT --header 'Content-Type: application/json' -d '\{ "value": "Full" \}' http://<host> .../api/v2/pipelines/0/nodes/rc_stereomatching/parameters/quality

Note: Run-time parameters are specific to individual nodes and are documented in the respective software module (Section 6).

Note: Most of the parameters that nodes offer via the REST-API can be explored and tested via the rc_visard's user-friendly Web GUI (Section 7.1).

Note: Some parameters exposed via the rc_visard's REST-API are also available from the GigE Vision 2.0/GenICam image interface (Section 7.2). Please note that setting those parameters via the REST-API or Web GUI is prohibited if a GenICam client is connected.

In addition, each node that offers run-time parameters also features a service to restore the default values for all of its parameters.
<|end_chunk_1269|><|start_chunk_1270|>
### Page 272
Services: Some nodes also offer services that can be called via REST-API, e.g., to restore parameters as discussed above, or to start and stop nodes. As an example, the services of the hand-eye calibration module (Section 6.5.1.5) could be listed using

```
curl -X GET http://<host>/api/v2/pipelines/0/nodes/rc_hand_eye_calibration/services
```

A node's service is called by issuing a PUT request for the respective resource and providing the service-specific arguments (see the "args" field of the Service data model, Section 7.3.4). As an example, the stereo matching module can be triggered to do an acquisition by:

```
curl -X PUT --header 'Content-Type: application/json' -d '{ "args": {} }' http://<host>/api/
\l-v2/pipelines/0/nodes/rc_stereomatching/services/acquisition_trigger
```

Note: The services and corresponding argument data models are specific to individual nodes and are documented in the respective software module (Section 6).

The following list includes all REST-API requests regarding the global database nodes' status, parameters, and services calls:
<|end_chunk_1270|><|start_chunk_1271|>
 GET /nodes 

Get list of all available global nodes.
<|end_chunk_1271|><|start_chunk_1272|>
## Template request

GET /api/v2/nodes HTTP/1.1
<|end_chunk_1272|><|start_chunk_1273|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "name": "rc_roi_db",
        "parameters": [],
        "services": [
            "set_region_of_interest",
            "get_regions_of_interest",
            "delete_regions_of_interest",
            "set_region_of_interest_2d",
            "get_regions_of_interest_2d",
            "delete_regions_of_interest_2d"
        ],
        "status": "running"
    },
    {
        "name": "rc_load_carrier_db",
        "parameters": [],
        "services": [
            "set_load_carrier",
            "get_load_carriers",
            "delete_load_carriers"
        ],
        "status": "running"
    },
    {
        "name": "rc_gripper_db",
        "parameters": [],
        "services": [
            "set_gripper",
            "get_grippers",
            "delete_grippers"
```

(continues on next page)
<|end_chunk_1273|><|start_chunk_1274|>
### Page 273<|end_chunk_1274|><|start_chunk_1275|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_1275|><|start_chunk_1276|>
## Status Codes

- 200 OK - successful operation (returns array of NodeInfo)

<|end_chunk_1276|><|start_chunk_1277|>
## Referenced Data Models

- NodeInfo (Section 7.3.4)

GET /nodes/\{node\}
Get info on a single global node.
Template request
GET /api/v2/nodes/<node> HTTP/1.1
<|end_chunk_1277|><|start_chunk_1278|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "name": "rc_roi_db",
    "parameters": [],
    "services": [
        "set_region_of_interest",
        "get_regions_of_interest",
        "delete_regions_of_interest",
        "set_region_of_interest_2d",
        "get_regions_of_interest_2d",
        "delete_regions_of_interest_2d"
    ],
    "status": "running"
}
```

<|end_chunk_1278|><|start_chunk_1279|>
## Parameters

- node (string) - name of the node (required)

<|end_chunk_1279|><|start_chunk_1280|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1280|><|start_chunk_1281|>
## Status Codes

- 200 OK - successful operation (returns NodeInfo)
- 404 Not Found - node not found

<|end_chunk_1281|><|start_chunk_1282|>
## Referenced Data Models

- NodeInfo (Section 7.3.4)

GET /nodes/\{node\}/services
Get descriptions of all services a global node offers.
Template request
<|end_chunk_1282|><|start_chunk_1283|>
### Page 274
GET /api/v2/nodes/<node>/services HTTP/1.1
<|end_chunk_1283|><|start_chunk_1284|>
 Template response 

```
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "args": {},
        "description": "string",
        "name": "string",
        "response": {}
    }
]
```

<|end_chunk_1284|><|start_chunk_1285|>
## Parameters

- node (string) - name of the node (required)

<|end_chunk_1285|><|start_chunk_1286|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1286|><|start_chunk_1287|>
## Status Codes

- 200 OK - successful operation (returns array of Service)
- 404 Not Found - node not found

<|end_chunk_1287|><|start_chunk_1288|>
## Referenced Data Models

- Service (Section 7.3.4)

GET /nodes/\{node\}/services/\{service\}
Get description of a global node's specific service.
<|end_chunk_1288|><|start_chunk_1289|>
## Template request

GET /api/v2/nodes/<node>/services/<service> HTTP/1.1
<|end_chunk_1289|><|start_chunk_1290|>
## Template response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "args": {},
    "description": "string",
    "name": "string",
    "response": {}
}
```

<|end_chunk_1290|><|start_chunk_1291|>
## Parameters

- node (string) - name of the node (required)
- service (string) - name of the service (required)

<|end_chunk_1291|><|start_chunk_1292|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1292|><|start_chunk_1293|>
## Status Codes

- 200 OK - successful operation (returns Service)
<|end_chunk_1293|><|start_chunk_1294|>
### Page 275
- 404 Not Found - node or service not found

<|end_chunk_1294|><|start_chunk_1295|>
 Referenced Data Models 

- Service (Section 7.3.4)

PUT /nodes/\{node\}/services/\{service\}
Call a service of a node. The required args and resulting response depend on the specific node and service.
<|end_chunk_1295|><|start_chunk_1296|>
## Template request

PUT /api/v2/nodes/<node>/services/<service> HTTP/1.1
Accept: application/json application/ubjson
\{\}
<|end_chunk_1296|><|start_chunk_1297|>
## Template response

HTTP/1.1 200 OK
Content-Type: application/json
\{
"args": \{\},
"description": "string",
"name": "string",
"response": \{\}
\}
<|end_chunk_1297|><|start_chunk_1298|>
## Parameters

- node (string) - name of the node (required)
- service (string) - name of the service (required)

<|end_chunk_1298|><|start_chunk_1299|>
## Request JSON Object

- service args (object) - example args (required)

<|end_chunk_1299|><|start_chunk_1300|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1300|><|start_chunk_1301|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1301|><|start_chunk_1302|>
## Status Codes

- 200 OK - Service call completed (returns Service)
- 403 Forbidden - Service call forbidden, e.g. because there is no valid license for this module.
- 404 Not Found - node or service not found

<|end_chunk_1302|><|start_chunk_1303|>
## Referenced Data Models

- Service (Section 7.3.4)

GET /nodes/\{node\}/status
Get status of a global node.
Template request
GET /api/v2/nodes/<node>/status HTTP/1.1
<|end_chunk_1303|><|start_chunk_1304|>
## Sample response
<|end_chunk_1304|><|start_chunk_1305|>
### Page 276
```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "status": "running",
    "timestamp": 1503075030.2335997,
    "values": []
}
```

<|end_chunk_1305|><|start_chunk_1306|>
 Parameters 

- node (string) - name of the node (required)

<|end_chunk_1306|><|start_chunk_1307|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1307|><|start_chunk_1308|>
## Status Codes

- 200 OK - successful operation (returns NodeStatus)
- 404 Not Found - node not found

<|end_chunk_1308|><|start_chunk_1309|>
## Referenced Data Models

- NodeStatus (Section 7.3.4)

The following list includes all REST-API requests regarding the 3D camera, navigation, detection and configuration nodes' status, parameters, and services calls:
<|end_chunk_1309|><|start_chunk_1310|>
## GET /pipelines/\{pipeline\}/nodes

Get list of all available nodes.
<|end_chunk_1310|><|start_chunk_1311|>
## Template request

GET /api/v2/pipelines/<pipeline>/nodes HTTP/1.1
<|end_chunk_1311|><|start_chunk_1312|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "name": "rc_stereocalib",
        "parameters": [
            "grid.width",
            "grid.height",
            "snap"
        ],
        "services": [
            "reset_defaults",
            "change_state"
        ],
        "status": "idle"
    },
    {
        "name": "rc_camera",
        "parameters": [
            "fps",
            "exp_auto",
            "exp_value",
            "exp_max"
        ],
```
<|end_chunk_1312|><|start_chunk_1313|>
### Page 277
![img-77.jpeg](img-77.jpeg)
<|end_chunk_1313|><|start_chunk_1314|>
 Parameters 

- pipeline (string) - name of the pipeline (one of 0 ) (required)

<|end_chunk_1314|><|start_chunk_1315|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1315|><|start_chunk_1316|>
## Status Codes

- 200 OK - successful operation (returns array of NodeInfo)

<|end_chunk_1316|><|start_chunk_1317|>
## Referenced Data Models

- NodeInfo (Section 7.3.4)

GET /pipelines/\{pipeline\}/nodes/\{node\}
Get info on a single node.
<|end_chunk_1317|><|start_chunk_1318|>
### Page 278<|end_chunk_1318|><|start_chunk_1319|>
 Template request 

```
GET /api/v2/pipelines/<pipeline>/nodes/<node> HTTP/1.1
```

<|end_chunk_1319|><|start_chunk_1320|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "name": "rc_camera",
    "parameters": [
        "fps",
        "exp_auto",
        "exp_value",
        "exp_max"
    ],
    "services": [
        "reset_defaults"
    ],
    "status": "running"
}
```

<|end_chunk_1320|><|start_chunk_1321|>
## Parameters

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)

<|end_chunk_1321|><|start_chunk_1322|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1322|><|start_chunk_1323|>
## Status Codes

- 200 OK - successful operation (returns NodeInfo)
- 404 Not Found - node not found

<|end_chunk_1323|><|start_chunk_1324|>
## Referenced Data Models

- NodeInfo (Section 7.3.4)

GET /pipelines/\{pipeline\}/nodes/\{node\}/parameters
Get parameters of a node.
<|end_chunk_1324|><|start_chunk_1325|>
## Template request

```
GET /api/v2/pipelines/<pipeline>/nodes/<node>/parameters?name=<name> HTTP/1.1
```

<|end_chunk_1325|><|start_chunk_1326|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
[
{
    "default": 25,
    "description": "Frames per second in Hz",
    "max": 25,
    "min": 1,
    "name": "fps",
    "type": "float64",
    "value": 25
},
```

(continues on next page)
<|end_chunk_1326|><|start_chunk_1327|>
### Page 279
(continued from previous page)

```
    {
        "default": true,
        "description": "Switching between auto and manual exposure",
        "max": true,
        "min": false,
        "name": "exp_auto",
        "type": "bool",
        "value": true
    },
    {
        "default": 0.007,
        "description": "Maximum exposure time in s if exp_auto is true",
        "max": 0.018,
        "min": 6.6e-05,
        "name": "exp_max",
        "type": "float64",
        "value": 0.007
    }
]
```

<|end_chunk_1327|><|start_chunk_1328|>
 Parameters 

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)

<|end_chunk_1328|><|start_chunk_1329|>
## Query Parameters

- name (string) - limit result to parameters with name (optional)

<|end_chunk_1329|><|start_chunk_1330|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1330|><|start_chunk_1331|>
## Status Codes

- 200 OK - successful operation (returns array of Parameter)
- 404 Not Found - node not found

<|end_chunk_1331|><|start_chunk_1332|>
## Referenced Data Models

- Parameter (Section 7.3.4)

PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters
Update multiple parameters.
<|end_chunk_1332|><|start_chunk_1333|>
## Template request

PUT /api/v2/pipelines/<pipeline>/nodes/<node>/parameters HTTP/1.1
Accept: application/json application/ubjson
[
\{
"name": "string",
"value": \{\}
\}
]
<|end_chunk_1333|><|start_chunk_1334|>
## Sample response

HTTP/1.1 200 OK
Content-Type: application/json
(continues on next page)
<|end_chunk_1334|><|start_chunk_1335|>
### Page 280
(continued from previous page)

```
{
    {
        "default": 25,
        "description": "Frames per second in Hz",
        "max": 25,
        "min": 1,
        "name": "fps",
        "type": "float64",
        "value": 10
    },
    {
        "default": true,
        "description": "Switching between auto and manual exposure",
        "max": true,
        "min": false,
        "name": "exp_auto",
        "type": "bool",
        "value": false
    },
    {
        "default": 0.005,
        "description": "Manual exposure time in s if exp_auto is false",
        "max": 0.018,
        "min": 6.6e-05,
        "name": "exp_value",
        "type": "float64",
        "value": 0.005
    }
}
```

<|end_chunk_1335|><|start_chunk_1336|>
 Parameters 

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)

<|end_chunk_1336|><|start_chunk_1337|>
## Request JSON Array of Objects

- parameters (ParameterNameValue) - array of parameters (required)

<|end_chunk_1337|><|start_chunk_1338|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1338|><|start_chunk_1339|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1339|><|start_chunk_1340|>
## Status Codes

- 200 OK - successful operation (returns array of Parameter)
- 400 Bad Request - invalid parameter value
- 403 Forbidden - Parameter update forbidden, e.g. because they are locked by a running GigE Vision application or there is no valid license for this module.
- 404 Not Found - node not found

<|end_chunk_1340|><|start_chunk_1341|>
## Referenced Data Models

- ParameterNameValue (Section 7.3.4)
- Parameter (Section 7.3.4)
<|end_chunk_1341|><|start_chunk_1342|>
### Page 281
GET /pipelines/\{pipeline\}/nodes/\{node\}/parameters/\{param\}
Get a specific parameter of a node.
<|end_chunk_1342|><|start_chunk_1343|>
 Template request 

GET /api/v2/pipelines/<pipeline>/nodes/<node>/parameters/<param> HTTP/1.1
<|end_chunk_1343|><|start_chunk_1344|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "default": 25,
    "description": "Frames per second in Hertz",
    "max": 25,
    "min": 1,
    "name": "fps",
    "type": "float64",
    "value": 10
}
```

<|end_chunk_1344|><|start_chunk_1345|>
## Parameters

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)
- param (string) - name of the parameter (required)

<|end_chunk_1345|><|start_chunk_1346|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1346|><|start_chunk_1347|>
## Status Codes

- 200 OK - successful operation (returns Parameter)
- 404 Not Found - node or parameter not found

<|end_chunk_1347|><|start_chunk_1348|>
## Referenced Data Models

- Parameter (Section 7.3.4)

PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters/\{param\}
Update a specific parameter of a node.
<|end_chunk_1348|><|start_chunk_1349|>
## Template request

PUT /api/v2/pipelines/<pipeline>/nodes/<node>/parameters/<param> HTTP/1.1
Accept: application/json application/ubjson
\{
"value": \{\}
\}
<|end_chunk_1349|><|start_chunk_1350|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "default": 25,
    "description": "Frames per second in Hertz",
    "max": 25,
    "min": 1,
```
<|end_chunk_1350|><|start_chunk_1351|>
### Page 282
| "name": "fps", |
| :--: |
| "type": "float64", |
| "value": 10 |
| \} |
<|end_chunk_1351|><|start_chunk_1352|>
 Parameters 

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)
- param (string) - name of the parameter (required)

<|end_chunk_1352|><|start_chunk_1353|>
## Request JSON Object

- parameter (ParameterValue) - parameter to be updated as JSON object (required)

<|end_chunk_1353|><|start_chunk_1354|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1354|><|start_chunk_1355|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1355|><|start_chunk_1356|>
## Status Codes

- 200 OK - successful operation (returns Parameter)
- 400 Bad Request - invalid parameter value
- 403 Forbidden - Parameter update forbidden, e.g. because they are locked by a running GigE Vision application or there is no valid license for this module.
- 404 Not Found - node or parameter not found

<|end_chunk_1356|><|start_chunk_1357|>
## Referenced Data Models

- ParameterValue (Section 7.3.4)
- Parameter (Section 7.3.4)

GET /pipelines/\{pipeline\}/nodes/\{node\}/services
Get descriptions of all services a node offers.
<|end_chunk_1357|><|start_chunk_1358|>
## Template request

GET /api/v2/pipelines/<pipeline>/nodes/<node>/services HTTP/1.1
<|end_chunk_1358|><|start_chunk_1359|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    {
        "args": {},
        "description": "Restarts the module.",
        "name": "restart",
        "response": {
            "accepted": "bool",
            "current_state": "string"
        }
    },
    {
```

(continues on next page)
<|end_chunk_1359|><|start_chunk_1360|>
### Page 283
(continued from previous page)

```
    "args": {},
    "description": "Starts the module.",
    "name": "start",
    "response": {
        "accepted": "bool",
        "current_state": "string"
    }
    },
    {
        "args": {},
        "description": "Stops the module.",
        "name": "stop",
        "response": {
            "accepted": "bool",
            "current_state": "string"
        }
    }
]
```

<|end_chunk_1360|><|start_chunk_1361|>
 Parameters 

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)

<|end_chunk_1361|><|start_chunk_1362|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1362|><|start_chunk_1363|>
## Status Codes

- 200 OK - successful operation (returns array of Service)
- 404 Not Found - node not found

<|end_chunk_1363|><|start_chunk_1364|>
## Referenced Data Models

- Service (Section 7.3.4)

GET /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\}
Get description of a node's specific service.
<|end_chunk_1364|><|start_chunk_1365|>
## Template request

```
GET /api/v2/pipelines/<pipeline>/nodes/<node>/services/<service> HTTP/1.1
```

<|end_chunk_1365|><|start_chunk_1366|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "args": {
        "pose": {
            "orientation": {
            "w": "float64",
            "x": "float64",
            "y": "float64",
            "z": "float64"
        },
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64"
```
<|end_chunk_1366|><|start_chunk_1367|>
### Page 284
(continued from previous page)

```
        }
    },
    "slot": "int32"
},
"description": "Save a pose (grid or gripper) for later calibration.",
"name": "set_pose",
"response": {
    "message": "string",
    "status": "int32",
    "success": "bool"
}
}
```

<|end_chunk_1367|><|start_chunk_1368|>
 Parameters 

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)
- service (string) - name of the service (required)

<|end_chunk_1368|><|start_chunk_1369|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1369|><|start_chunk_1370|>
## Status Codes

- 200 OK - successful operation (returns Service)
- 404 Not Found - node or service not found

<|end_chunk_1370|><|start_chunk_1371|>
## Referenced Data Models

- Service (Section 7.3.4)

PUT /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\}
Call a service of a node. The required args and resulting response depend on the specific node and service.
<|end_chunk_1371|><|start_chunk_1372|>
## Template request

PUT /api/v2/pipelines/<pipeline>/nodes/<node>/services/<service> HTTP/1.1
Accept: application/json application/ubjson
\{\}
<|end_chunk_1372|><|start_chunk_1373|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "name": "set_pose",
    "response": {
        "message": "Grid detected, pose stored.",
        "status": 1,
        "success": true
    }
}
```

<|end_chunk_1373|><|start_chunk_1374|>
## Parameters

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)
<|end_chunk_1374|><|start_chunk_1375|>
### Page 285
- service (string) - name of the service (required)

<|end_chunk_1375|><|start_chunk_1376|>
 Request JSON Object 

- service args (object) - example args (required)

Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1376|><|start_chunk_1377|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1377|><|start_chunk_1378|>
## Status Codes

- 200 OK - Service call completed (returns Service)
- 403 Forbidden - Service call forbidden, e.g. because there is no valid license for this module.
- 404 Not Found - node or service not found

<|end_chunk_1378|><|start_chunk_1379|>
## Referenced Data Models

- Service (Section 7.3.4)

GET /pipelines/\{pipeline\}/nodes/\{node\}/status
Get status of a node.
Template request
GET /api/v2/pipelines/<pipeline>/nodes/<node>/status HTTP/1.1
<|end_chunk_1379|><|start_chunk_1380|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "status": "running",
    "timestamp": 1503075030.2335997,
    "values": {
        "baseline": "0.0650542",
        "color": "0",
        "exp": "0.00426667",
        "focal": "0.844893",
        "fps": "25.1352",
        "gain": "12.0412",
        "height": "960",
        "temp_left": "39.6",
        "temp_right": "38.2",
        "time": "0.00406513",
        "width": "1280"
    }
}
```

<|end_chunk_1380|><|start_chunk_1381|>
## Parameters

- pipeline (string) - name of the pipeline (one of 0 ) (required)
- node (string) - name of the node (required)

<|end_chunk_1381|><|start_chunk_1382|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1382|><|start_chunk_1383|>
## Status Codes
<|end_chunk_1383|><|start_chunk_1384|>
### Page 286
- 200 OK - successful operation (returns NodeStatus)
- 404 Not Found - node not found

<|end_chunk_1384|><|start_chunk_1385|>
 Referenced Data Models 

- NodeStatus (Section 7.3.4)

<|end_chunk_1385|><|start_chunk_1386|>
### 7.3.3.2 Datastreams

The following resources and requests allow access to and configuration of the rc_dynamics interface data streams (Section 7.4). These REST-API requests offer

- showing available and currently running data streams, e.g.,

```
curl -X GET http://<host>/api/v1/datastreams
```

- starting a data stream to a destination, e.g.,

```
curl -X PUT --header 'Content-Type: application/x-www-form-urlencoded' -d 'destination=
\l<target-ip>:<target-port>' http://<host>/api/v1/datastreams/pose
```

- and stopping data streams, e.g.,

```
curl -X DELETE http://<host>/api/v1/datastreams/pose?destination=<target-ip>:<target-port>
```

The following list includes all REST-API requests associated with data streams:
<|end_chunk_1386|><|start_chunk_1387|>
## GET /datastreams

Get list of available data streams.
<|end_chunk_1387|><|start_chunk_1388|>
## Template request

```
GET /api/v2/datastreams HTTP/1.1
```

<|end_chunk_1388|><|start_chunk_1389|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
[
{
    "description": "Pose of left camera at VisualOdometry rate (~10Hz)",
    "destinations": [
        "192.168.1.13:30000"
    ],
    "name": "pose",
    "protobuf": "Frame",
    "protocol": "UDP"
    },
    {
        "description": "Pose of left camera (RealTime 200Hz)",
        "destinations": [
            "192.168.1.100:20000",
            "192.168.1.42:45000"
    ],
    "name": "pose_rt",
    "protobuf": "Frame",
    "protocol": "UDP"
    },
    {
        "description": "Raw IMU (InertialMeasurementUnit) values (RealTime 200Hz)",
        "destinations": [],
```
<|end_chunk_1389|><|start_chunk_1390|>
### Page 287
(continued from previous page)

```
    "name": "imu",
    "protobuf": "Imu",
    "protocol": "UDP"
},
{
    "description": "Dynamics of sensor (pose, velocity, acceleration) (RealTime 200Hz)",
    "destinations": [
        "192.168.1.100:20001"
    ],
    "name": "dynamics",
    "protobuf": "Dynamics",
    "protocol": "UDP"
}
]
```

<|end_chunk_1390|><|start_chunk_1391|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_1391|><|start_chunk_1392|>
## Status Codes

- 200 OK - successful operation (returns array of Stream)

<|end_chunk_1392|><|start_chunk_1393|>
## Referenced Data Models

- Stream (Section 7.3.4)

GET /datastreams/\{stream\}
Get datastream configuration.
<|end_chunk_1393|><|start_chunk_1394|>
## Template request

```
GET /api/v2/datastreams/<stream> HTTP/1.1
```

<|end_chunk_1394|><|start_chunk_1395|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "description": "Pose of left camera at VisualOdometry rate (~10Hz)",
    "destinations": [
        "192.168.1.13:30000"
    ],
    "name": "pose",
    "protobuf": "Frame",
    "protocol": "UDP"
}
```

<|end_chunk_1395|><|start_chunk_1396|>
## Parameters

- stream (string) - name of the stream (required)

<|end_chunk_1396|><|start_chunk_1397|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1397|><|start_chunk_1398|>
## Status Codes

- 200 OK - successful operation (returns Stream)
- 404 Not Found - datastream not found

<|end_chunk_1398|><|start_chunk_1399|>
## Referenced Data Models
<|end_chunk_1399|><|start_chunk_1400|>
### Page 288
- Stream (Section 7.3.4)

PUT /datastreams/\{stream\}
Update a datastream configuration.
<|end_chunk_1400|><|start_chunk_1401|>
 Template request 

PUT /api/v2/datastreams/<stream> HTTP/1.1
Accept: application/x-www-form-urlencoded
<|end_chunk_1401|><|start_chunk_1402|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "description": "Pose of left camera at VisualOdometry rate (-10Hz)",
    "destinations": [
        "192.168.1.13:30000",
        "192.168.1.25:40000"
    ],
    "name": "pose",
    "protobuf": "Frame",
    "protocol": "UDP"
}
```

<|end_chunk_1402|><|start_chunk_1403|>
## Parameters

- stream (string) - name of the stream (required)

<|end_chunk_1403|><|start_chunk_1404|>
## Form Parameters

- destination - destination ("IP:port") to add (required)

<|end_chunk_1404|><|start_chunk_1405|>
## Request Headers

- Accept - application/x-www-form-urlencoded

<|end_chunk_1405|><|start_chunk_1406|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1406|><|start_chunk_1407|>
## Status Codes

- 200 OK - successful operation (returns Stream)
- 404 Not Found - datastream not found

<|end_chunk_1407|><|start_chunk_1408|>
## Referenced Data Models

- Stream (Section 7.3.4)

DELETE /datastreams/\{stream\}
Delete a destination from the datastream configuration.
<|end_chunk_1408|><|start_chunk_1409|>
## Template request

DELETE /api/v2/datastreams/<stream>?destination=<destination> HTTP/1.1
<|end_chunk_1409|><|start_chunk_1410|>
## Sample response

HTTP/1.1 200 OK
Content-Type: application/json
\{
"description": "Pose of left camera at VisualOdometry rate $(-10 \mathrm{~Hz}) "$,
<|end_chunk_1410|><|start_chunk_1411|>
### Page 289
| "destinations": [], |
| :-- |
| "name": "pose", |
| "protobuf": "Frame", |
| "protocol": "UDP" |
| \} |
<|end_chunk_1411|><|start_chunk_1412|>
 Parameters 

- stream (string) - name of the stream (required)

<|end_chunk_1412|><|start_chunk_1413|>
## Query Parameters

- destination (string) - destination IP:port to delete, if not specified all destinations are deleted (optional)

<|end_chunk_1413|><|start_chunk_1414|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1414|><|start_chunk_1415|>
## Status Codes

- 200 OK - successful operation (returns Stream)
- 404 Not Found - datastream not found

<|end_chunk_1415|><|start_chunk_1416|>
## Referenced Data Models

- Stream (Section 7.3.4)

<|end_chunk_1416|><|start_chunk_1417|>
### 7.3.3.3 System and logs

The following resources and requests expose the $r c \_v i s a r d$ 's system-level API. They enable

- access to log files (system-wide or module-specific)
- access to information about the device and run-time statistics such as date, MAC address, clocktime synchronization status, and available resources;
- management of installed software licenses; and
- the $r c \_v i s a r d$ to be updated with a new firmware image.

<|end_chunk_1417|><|start_chunk_1418|>
## GET /logs

Get list of available log files.
<|end_chunk_1418|><|start_chunk_1419|>
## Template request

GET /api/v2/logs HTTP/1.1
<|end_chunk_1419|><|start_chunk_1420|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "date": 1503060035.0625782,
        "name": "rcsense-api.log",
        "size": 730
    },
    {
        "date": 1503060035.741574,
        "name": "stereo.log",
        "size": 39024
    },
```
<|end_chunk_1420|><|start_chunk_1421|>
### Page 290
(continued from previous page)

```
    {
        "date": 1503060044.0475223,
        "name": "camera.log",
        "size": 1091
    },
    {
        "date": 1503060035.2115774,
        "name": "dynamics.log"
    }
]
```

<|end_chunk_1421|><|start_chunk_1422|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_1422|><|start_chunk_1423|>
## Status Codes

- 200 OK - successful operation (returns array of LogInfo)

<|end_chunk_1423|><|start_chunk_1424|>
## Referenced Data Models

- LogInfo (Section 7.3.4)

GET /logs/\{log\}
Get a log file. Content type of response depends on parameter 'format'.
<|end_chunk_1424|><|start_chunk_1425|>
## Template request

GET /api/v2/logs/<log=?format=<format>&limit=<limit> HTTP/1.1
<|end_chunk_1425|><|start_chunk_1426|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "date": 1503060035.2115774,
    "log": [
        {
            "component": "rc_stereo_ins",
            "level": "INFO",
            "message": "Running rc_stereo_ins version 2.4.0",
            "timestamp": 1503060034.083
        },
        {
            "component": "rc_stereo_ins",
            "level": "INFO",
            "message": "Starting up communication interfaces",
            "timestamp": 1503060034.085
        },
        {
            "component": "rc_stereo_ins",
            "level": "INFO",
            "message": "Autostart disabled",
            "timestamp": 1503060034.098
        },
        {
            "component": "rc_stereo_ins",
            "level": "INFO",
            "message": "Initializing realtime communication",
            "timestamp": 1503060034.209
        },
```
<|end_chunk_1426|><|start_chunk_1427|>
### Page 291
(continued from previous page)

```
    {
        "component": "rc_stereo_ins",
        "level": "INFO",
        "message": "Startet state machine in state IDLE",
        "timestamp": 1503060034.383
    },
    {
        "component": "rc_stereovisodo",
        "level": "INFO",
        "message": "Init stereovisodo ...",
        "timestamp": 1503060034.814
    },
    {
        "component": "rc_stereovisodo",
        "level": "INFO",
        "message": "rc_stereovisodo: Using standard V0",
        "timestamp": 1503060034.913
    },
    {
        "component": "rc_stereovisodo",
        "level": "INFO",
        "message": "rc_stereovisodo: Playback mode: false",
        "timestamp": 1503060035.132
    },
    {
        "component": "rc_stereovisodo",
        "level": "INFO",
        "message": "rc_stereovisodo: Ready",
        "timestamp": 1503060035.212
    }
    ],
    "name": "dynamics.log",
    "size": 695
}
```

<|end_chunk_1427|><|start_chunk_1428|>
 Parameters 

- $\log$ (string) - name of the log file (required)

<|end_chunk_1428|><|start_chunk_1429|>
## Query Parameters

- format (string) - return log as JSON or raw (one of json, raw; default: json) (optional)
- limit (integer) - limit to last x lines in JSON format (default: 100) (optional)

<|end_chunk_1429|><|start_chunk_1430|>
## Response Headers

- Content-Type - text/plain application/json

<|end_chunk_1430|><|start_chunk_1431|>
## Status Codes

- 200 OK - successful operation (returns Log)
- 404 Not Found - log not found

<|end_chunk_1431|><|start_chunk_1432|>
## Referenced Data Models

- Log (Section 7.3.4)

<|end_chunk_1432|><|start_chunk_1433|>
## GET / system

Get system information on sensor.
Template request
<|end_chunk_1433|><|start_chunk_1434|>
### Page 292
GET /api/v2/system HTTP/1.1
<|end_chunk_1434|><|start_chunk_1435|>
 Sample response 

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "dns": {
        "dns_servers": [
            "10.0.0.1",
            "1.1.1.1"
        ],
        "manual_dns_servers": [
            "1.1.1.1"
        ]
    },
    "firmware": {
        "active_image": {
            "image_version": "rc_visard_v1.1.0"
        },
        "fallback_booted": true,
        "inactive_image": {
            "image_version": "rc_visard_v1.0.0"
        },
        "next_boot_image": "active_image"
    },
    "hostname": "rc-visard-02873515",
    "link_speed": 1000,
    "mac": "00:14:2D:2B:D8:AB",
    "ntp": {
        "enabled": true,
        "manual_ntp_servers": [
            "10.0.0.1"
        ],
        "offset": -3.2666e-05,
        "selected_ntp_servers": [
            "10.0.0.1"
        ],
        "synchronized": true
    },
    "ptp_status": {
        "master_ip": "",
        "offset": 0,
        "offset_dev": 0,
        "offset_mean": 0,
        "state": "off"
    },
    "ready": true,
    "serial": "02873515",
    "time": 1504080462.641875,
    "uptime": 65457.42
}
```

<|end_chunk_1435|><|start_chunk_1436|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1436|><|start_chunk_1437|>
## Status Codes

- 200 OK - successful operation (returns SysInfo)

<|end_chunk_1437|><|start_chunk_1438|>
## Referenced Data Models
<|end_chunk_1438|><|start_chunk_1439|>
### Page 293
- SysInfo (Section 7.3.4)

GET /system/backup
Get backup.
Template request
GET /api/v2/system/backup?pipelines=<pipelines>\&load_carriers=<load_carriers>\&regions_of_ ...interest=<regions_of_interest>\&grippers=<grippers> HTTP/1.1
<|end_chunk_1439|><|start_chunk_1440|>
 Query Parameters 

- pipelines (boolean) - backup pipelines with node settings, i.e. parameters and preferred_orientation (default: True) (optional)
- load_carriers (boolean) - backup load_carriers (default: True) (optional)
- regions_of_interest (boolean) - backup regions_of_interest (default: True) (optional)
- grippers (boolean) - backup grippers (default: True) (optional)

<|end_chunk_1440|><|start_chunk_1441|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1441|><|start_chunk_1442|>
## Status Codes

- 200 OK - successful operation

POST /system/backup
Restore backup.
Template request

```
POST /api/v2/system/backup HTTP/1.1
Accept: application/json application/ubjson
{}
```

<|end_chunk_1442|><|start_chunk_1443|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "return_code": {
        "message": "backup restored",
        "value": 0
    },
    "warnings": []
}
```

<|end_chunk_1443|><|start_chunk_1444|>
## Request JSON Object

- backup (object) - backup data as json object (required)

<|end_chunk_1444|><|start_chunk_1445|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1445|><|start_chunk_1446|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1446|><|start_chunk_1447|>
## Status Codes

- 200 OK - successful operation
<|end_chunk_1447|><|start_chunk_1448|>
### Page 294<|end_chunk_1448|><|start_chunk_1449|>
 GET /system/dns 

Get DNS settings.
<|end_chunk_1449|><|start_chunk_1450|>
## Template request

```
GET /api/v2/system/dns HTTP/1.1
```

<|end_chunk_1450|><|start_chunk_1451|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "dns": {
        "dns_servers": [
            "10.0.0.1",
            "1.1.1.1"
        ],
        "manual_dns_servers": [
            "1.1.1.1"
        ]
    }
}
```

<|end_chunk_1451|><|start_chunk_1452|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1452|><|start_chunk_1453|>
## Status Codes

- 200 OK - successful operation (returns DNS)

Referenced Data Models

- DNS (Section 7.3.4)

PUT /system/dns
Set manual DNS servers.
<|end_chunk_1453|><|start_chunk_1454|>
## Template request

PUT /api/v2/system/dns HTTP/1.1
Accept: application/json application/ubjson
\{\}
<|end_chunk_1454|><|start_chunk_1455|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "dns": {
        "dns_servers": [
            "10.0.0.1",
            "1.1.1.1"
        ],
        "manual_dns_servers": [
            "1.1.1.1"
        ]
    }
}
```

<|end_chunk_1455|><|start_chunk_1456|>
## Request JSON Object
<|end_chunk_1456|><|start_chunk_1457|>
### Page 295
- manual_dns_servers (ManualDNSServers) - Manual DNS servers (required)

<|end_chunk_1457|><|start_chunk_1458|>
 Request Headers 

- Accept - application/json application/ubjson

<|end_chunk_1458|><|start_chunk_1459|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1459|><|start_chunk_1460|>
## Status Codes

- 200 OK - successful operation (returns DNS)
- 400 Bad Request - invalid/missing arguments

<|end_chunk_1460|><|start_chunk_1461|>
## Referenced Data Models

- DNS (Section 7.3.4)
- ManualDNSServers (Section 7.3.4)

GET /system/license
Get information about licenses installed on sensor.
Template request
GET /api/v2/system/license HTTP/1.1
<|end_chunk_1461|><|start_chunk_1462|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "components": {
        "calibration": true,
        "fusion": true,
        "hand_eye_calibration": true,
        "rectification": true,
        "self_calibration": true,
        "slam": false,
        "stereo": true,
        "svo": true
    },
    "valid": true
}
```

<|end_chunk_1462|><|start_chunk_1463|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1463|><|start_chunk_1464|>
## Status Codes

- 200 OK - successful operation (returns LicenseInfo)

<|end_chunk_1464|><|start_chunk_1465|>
## Referenced Data Models

- LicenseInfo (Section 7.3.4)

POST /system/license
Update license on sensor with a license file.
Template request
POST /api/v2/system/license HTTP/1.1
Accept: multipart/form-data
<|end_chunk_1465|><|start_chunk_1466|>
### Page 296<|end_chunk_1466|><|start_chunk_1467|>
 Form Parameters 

- file - license file (required)

<|end_chunk_1467|><|start_chunk_1468|>
## Request Headers

- Accept - multipart/form-data

<|end_chunk_1468|><|start_chunk_1469|>
## Status Codes

- 200 OK - successful operation
- 400 Bad Request - not a valid license

GET /system/max_power_test
Get last max power test result.
Template request
GET /api/v2/system/max_power_test HTTP/1.1
<|end_chunk_1469|><|start_chunk_1470|>
## Response Headers

- Content-Type - application/json

<|end_chunk_1470|><|start_chunk_1471|>
## Status Codes

- 200 OK - successful operation

POST /system/max_power_test
Run max power test. Fully load GPU (and CPU) to consume max power for 10 seconds to test the power supply. WARNING: The system might not return a response due to immediate reboot if the power supply is insufficient.
<|end_chunk_1471|><|start_chunk_1472|>
## Template request

POST /api/v2/system/max_power_test?nocpu=<nocpu> HTTP/1.1
<|end_chunk_1472|><|start_chunk_1473|>
## Query Parameters

- nocpu (boolean) - Don't run CPU workers and only load the GPU. (optional)

<|end_chunk_1473|><|start_chunk_1474|>
## Response Headers

- Content-Type - application/json

<|end_chunk_1474|><|start_chunk_1475|>
## Status Codes

- 200 OK - Test finished. See return_code for result.
- 400 Bad Request - Test already running.

<|end_chunk_1475|><|start_chunk_1476|>
## GET /system/network

Get current network configuration.
Template request
GET /api/v2/system/network HTTP/1.1
<|end_chunk_1476|><|start_chunk_1477|>
## Sample response

HTTP/1.1 200 OK
Content-Type: application/json
\{
"current_method": "DHCP",
"default_gateway": "10.0.3.254",
(continues on next page)
<|end_chunk_1477|><|start_chunk_1478|>
### Page 297
(continued from previous page)

```
"ip_address": "10.0.1.41",
"settings": {
    "dhcp_enabled": true,
    "persistent_default_gateway": "",
    "persistent_ip_address": "192.168.0.10",
    "persistent_ip_enabled": false,
    "persistent_subnet_mask": "255.255.255.0"
},
"subnet_mask": "255.255.252.0"
}
```

<|end_chunk_1478|><|start_chunk_1479|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_1479|><|start_chunk_1480|>
## Status Codes

- 200 OK - successful operation (returns NetworkInfo)

Referenced Data Models

- NetworkInfo (Section 7.3.4)

GET /system/network/settings
Get current network settings.
Template request
GET /api/v2/system/network/settings HTTP/1.1
<|end_chunk_1480|><|start_chunk_1481|>
## Sample response

HTTP/1.1 200 OK
Content-Type: application/json
\{
"dhcp_enabled": true,
"persistent_default_gateway": "",
"persistent_ip_address": "192.168.0.10",
"persistent_ip_enabled": false,
"persistent_subnet_mask": "255.255.255.0"
\}
<|end_chunk_1481|><|start_chunk_1482|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1482|><|start_chunk_1483|>
## Status Codes

- 200 OK - successful operation (returns NetworkSettings)

<|end_chunk_1483|><|start_chunk_1484|>
## Referenced Data Models

- NetworkSettings (Section 7.3.4)

PUT /system/network/settings
Set current network settings.
Template request
PUT /api/v2/system/network/settings HTTP/1.1
Accept: application/json application/ubjson
\{\}
```
<|end_chunk_1484|><|start_chunk_1485|>
### Page 298<|end_chunk_1485|><|start_chunk_1486|>
 Sample response 

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "dhcp_enabled": true,
    "persistent_default_gateway": "",
    "persistent_ip_address": "192.168.0.10",
    "persistent_ip_enabled": false,
    "persistent_subnet_mask": "255.255.255.0"
}
```

<|end_chunk_1486|><|start_chunk_1487|>
## Request JSON Object

- settings (NetworkSettings) - network settings to apply (required)

<|end_chunk_1487|><|start_chunk_1488|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1488|><|start_chunk_1489|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1489|><|start_chunk_1490|>
## Status Codes

- 200 OK - successful operation (returns NetworkSettings)
- 400 Bad Request - invalid/missing arguments
- 403 Forbidden - Changing network settings forbidden because this is locked by a running GigE Vision application.

<|end_chunk_1490|><|start_chunk_1491|>
## Referenced Data Models

- NetworkSettings (Section 7.3.4)

GET /system/ntp
Get NTP settings.
Template request
GET /api/v2/system/ntp HTTP/1.1
<|end_chunk_1491|><|start_chunk_1492|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "ntp": {
        "enabled": true,
        "manual_ntp_servers": [
            "10.0.0.1"
        ],
        "offset": -3.2666e-05,
        "selected_ntp_servers": [
            "10.0.0.1"
        ],
        "synchronized": true
    }
}
```

<|end_chunk_1492|><|start_chunk_1493|>
## Response Headers
<|end_chunk_1493|><|start_chunk_1494|>
### Page 299
- Content-Type - application/json application/ubjson

<|end_chunk_1494|><|start_chunk_1495|>
 Status Codes 

- 200 OK - successful operation (returns NTP)

Referenced Data Models

- NTP (Section 7.3.4)

PUT /system/ntp
Set manual NTP servers.
Template request

```
PUT /api/v2/system/ntp HTTP/1.1
Accept: application/json application/ubjson
{}
```

<|end_chunk_1495|><|start_chunk_1496|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "ntp": {
        "enabled": true,
        "manual_ntp_servers": [
            "10.0.0.1"
        ],
        "offset": -3.2666e-05,
        "selected_ntp_servers": [
            "10.0.0.1"
        ],
        "synchronized": true
    }
}
```

<|end_chunk_1496|><|start_chunk_1497|>
## Request JSON Object

- manual_ntp_servers (ManualNTPServers) - Manual NTP servers (required)

<|end_chunk_1497|><|start_chunk_1498|>
## Request Headers

- Accept - application/json application/ubjson

<|end_chunk_1498|><|start_chunk_1499|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1499|><|start_chunk_1500|>
## Status Codes

- 200 OK - successful operation (returns NTP)
- 400 Bad Request - invalid/missing arguments

<|end_chunk_1500|><|start_chunk_1501|>
## Referenced Data Models

- NTP (Section 7.3.4)
- ManualNTPServers (Section 7.3.4)

PUT /system/reboot
Reboot the sensor.
Template request
<|end_chunk_1501|><|start_chunk_1502|>
### Page 300
PUT /api/v2/system/reboot HTTP/1.1
<|end_chunk_1502|><|start_chunk_1503|>
 Status Codes 

- 200 OK - successful operation

GET /system/rollback
Get information about currently active and inactive firmware/system images on sensor.
Template request
GET /api/v2/system/rollback HTTP/1.1
<|end_chunk_1503|><|start_chunk_1504|>
## Sample response

HTTP/1.1 200 OK
Content-Type: application/json
\{
"active_image": \{
"image_version": "rc_visard_v1.1.0"
\},
"fallback_booted": false,
"inactive_image": \{
"image_version": "rc_visard_v1.0.0"
\},
"next_boot_image": "active_image"
\}
<|end_chunk_1504|><|start_chunk_1505|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1505|><|start_chunk_1506|>
## Status Codes

- 200 OK - successful operation (returns FirmwareInfo)

<|end_chunk_1506|><|start_chunk_1507|>
## Referenced Data Models

- FirmwareInfo (Section 7.3.4)

PUT /system/rollback
Rollback to previous firmware version (inactive system image).
Template request
PUT /api/v2/system/rollback HTTP/1.1
<|end_chunk_1507|><|start_chunk_1508|>
## Status Codes

- 200 OK - successful operation
- 400 Bad Request - already set to use inactive partition on next boot
- 500 Internal Server Error - internal error

GET /system/time
Get system time in UTC as string with format "YYYY-MM-DD hh:mm:ss"
Template request
GET /api/v2/system/time HTTP/1.1
<|end_chunk_1508|><|start_chunk_1509|>
## Sample response
<|end_chunk_1509|><|start_chunk_1510|>
### Page 301
```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "utc": "2023-10-05 08:35:26"
}
```

<|end_chunk_1510|><|start_chunk_1511|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_1511|><|start_chunk_1512|>
## Status Codes

- 200 OK - successful operation

PUT /system/time
Set system time in UTC as string with format "YYYY-MM-DD hh:mm:ss"
<|end_chunk_1512|><|start_chunk_1513|>
## Template request

PUT /api/v2/system/time?utc=<utc> HTTP/1.1
<|end_chunk_1513|><|start_chunk_1514|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "utc": "2023-10-05 08:35:26"
}
```

<|end_chunk_1514|><|start_chunk_1515|>
## Query Parameters

- utc (string) - Time in UTC as string with format "YYYY-MM-DD hh:mm:ss" (required)

<|end_chunk_1515|><|start_chunk_1516|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1516|><|start_chunk_1517|>
## Status Codes

- 200 OK - successful operation
- 400 Bad Request - invalid/missing arguments
- 403 Forbidden - Changing time forbidden because time is synchronized via NTP or PTP.

GET /system/ui_lock
Get UI lock status.
<|end_chunk_1517|><|start_chunk_1518|>
## Template request

GET /api/v2/system/ui_lock HTTP/1.1
<|end_chunk_1518|><|start_chunk_1519|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "enabled": false
}
```
<|end_chunk_1519|><|start_chunk_1520|>
### Page 302<|end_chunk_1520|><|start_chunk_1521|>
 Response Headers 

- Content-Type - application/json application/ubjson

<|end_chunk_1521|><|start_chunk_1522|>
## Status Codes

- 200 OK - successful operation (returns UILock)

<|end_chunk_1522|><|start_chunk_1523|>
## Referenced Data Models

- UILock (Section 7.3.4)

DELETE /system/ui_lock
Remove UI lock.
Template request
DELETE /api/v2/system/ui_lock HTTP/1.1
<|end_chunk_1523|><|start_chunk_1524|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "enabled": false,
    "valid": false
}
```

<|end_chunk_1524|><|start_chunk_1525|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1525|><|start_chunk_1526|>
## Status Codes

- 200 OK - successful operation

POST /system/ui_lock
Verify or set UI lock.
Template request
POST /api/v2/system/ui_lock?hash=<hash>\&set=<set> HTTP/1.1
<|end_chunk_1526|><|start_chunk_1527|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "enabled": true,
    "valid": true
}
```

<|end_chunk_1527|><|start_chunk_1528|>
## Query Parameters

- hash (string) - hash of the UI lock password (required)
- set (boolean) - set new hash instead of veryfing (optional)

<|end_chunk_1528|><|start_chunk_1529|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1529|><|start_chunk_1530|>
## Status Codes

- 200 OK - successful operation
<|end_chunk_1530|><|start_chunk_1531|>
### Page 303<|end_chunk_1531|><|start_chunk_1532|>
 GET /system/update 

Get information about currently active and inactive firmware/system images on sensor.
<|end_chunk_1532|><|start_chunk_1533|>
## Template request

GET /api/v2/system/update HTTP/1.1
<|end_chunk_1533|><|start_chunk_1534|>
## Sample response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "active_image": {
        "image_version": "rc_visard_v1.1.0"
    },
    "fallback_booted": false,
    "inactive_image": {
        "image_version": "rc_visard_v1.0.0"
    },
    "next_boot_image": "active_image"
}
```

<|end_chunk_1534|><|start_chunk_1535|>
## Response Headers

- Content-Type - application/json application/ubjson

<|end_chunk_1535|><|start_chunk_1536|>
## Status Codes

- 200 OK - successful operation (returns FirmwareInfo)

<|end_chunk_1536|><|start_chunk_1537|>
## Referenced Data Models

- FirmwareInfo (Section 7.3.4)

POST /system/update
Update firmware/system image with a mender artifact. Reboot is required afterwards in order to activate updated firmware version.
<|end_chunk_1537|><|start_chunk_1538|>
## Template request

POST /api/v2/system/update HTTP/1.1
Accept: multipart/form-data
<|end_chunk_1538|><|start_chunk_1539|>
## Form Parameters

- file - mender artifact file (required)

<|end_chunk_1539|><|start_chunk_1540|>
## Request Headers

- Accept - multipart/form-data

<|end_chunk_1540|><|start_chunk_1541|>
## Status Codes

- 200 OK - successful operation
- 400 Bad Request - client error, e.g. no valid mender artifact

<|end_chunk_1541|><|start_chunk_1542|>
### 7.3.4 Data type definitions

The REST-API defines the following data models, which are used to access or modify the available resources (Section 7.3.3) either as required attributes/parameters of the requests or as return types.
DNS: DNS settings.
An object of type DNS has the following properties:
<|end_chunk_1542|><|start_chunk_1543|>
### Page 304
- dns_servers (array of string)
- manual_dns_servers (array of string)

<|end_chunk_1543|><|start_chunk_1544|>
 Template object 

```
{
    "dns_servers": [
        "string",
        "string"
    ],
    "manual_dns_servers": [
        "string",
        "string"
    ]
}
```

DNS objects are nested in SysInfo, and are used in the following requests:

- GET / system/dns
- PUT / system/dns

FirmwareInfo: Information about currently active and inactive firmware images, and what image is/will be booted.

An object of type FirmwareInfo has the following properties:

- active_image (ImageInfo) - see description of ImageInfo
- fallback_booted (boolean) - true if desired image could not be booted and fallback boot to the previous image occurred
- inactive_image (ImageInfo) - see description of ImageInfo
- next_boot_image (string) - firmware image that will be booted next time (one of active_image, inactive_image)

<|end_chunk_1544|><|start_chunk_1545|>
## Template object

```
{
    "active_image": {
        "image_version": "string"
    },
    "fallback_booted": false,
    "inactive_image": {
        "image_version": "string"
    },
    "next_boot_image": "string"
}
```

FirmwareInfo objects are nested in SysInfo, and are used in the following requests:

- GET / system/rollback
- GET / system/update

GripperElement: CAD gripper element
An object of type GripperElement has the following properties:

- id (string) - Unique identifier of the element

Template object

```
{
    "id": "string"
}
```
<|end_chunk_1545|><|start_chunk_1546|>
### Page 305
GripperElement objects are used in the following requests:

- GET / cad/gripper_elements
- GET / cad/gripper_elements/\{id\}
- PUT / cad/gripper_elements/\{id\}

ImageInfo: Information about specific firmware image.
An object of type ImageInfo has the following properties:

- image_version (string) - image version

<|end_chunk_1546|><|start_chunk_1547|>
 Template object 

```
{
    "image_version": "string"
}
```

ImageInfo objects are nested in FirmwareInfo.
LicenseComponentConstraint: Constraints on the module version.
An object of type LicenseComponentConstraint has the following properties:

- max_version (string) - optional maximum supported version (exclusive)
- min_version (string) - optional minimum supported version (inclusive)

<|end_chunk_1547|><|start_chunk_1548|>
## Template object

```
{
    "max_version": "string",
    "min_version": "string"
}
```

LicenseComponentConstraint objects are nested in LicenseConstraints.
LicenseComponents: List of the licensing status of the individual software modules. The respective flag is true if the module is unlocked with the currently applied software license.
An object of type LicenseComponents has the following properties:

- calibration (boolean) - camera calibration module
- fusion (boolean) - stereo ins/fusion modules
- hand_eye_calibration (boolean) - hand-eye calibration module
- rectification (boolean) - image rectification module
- self_calibration (boolean) - camera self-calibration module
- slam (boolean) - SLAM module
- stereo (boolean) - stereo matching module
- svo (boolean) - visual odometry module

<|end_chunk_1548|><|start_chunk_1549|>
## Template object

```
{
    "calibration": false,
    "fusion": false,
    "hand_eye_calibration": false,
    "rectification": false,
    "self_calibration": false,
    "slam": false,
    "stereo": false,
```
<|end_chunk_1549|><|start_chunk_1550|>
### Page 306<|end_chunk_1550|><|start_chunk_1551|>
 roboception 

(continued from previous page)

```
"svo": false
}
```

LicenseComponents objects are nested in LicenseInfo.
LicenseConstraints: Version constrains for modules.
An object of type LicenseConstraints has the following properties:

- image_version (LicenseComponentConstraint) - see description of LicenseComponentConstraint

<|end_chunk_1551|><|start_chunk_1552|>
## Template object

```
{
    "image_version": {
        "max_version": "string",
        "min_version": "string"
    }
}
```

LicenseConstraints objects are nested in LicenseInfo.
LicenseInfo: Information about the currently applied software license on the sensor.
An object of type LicenseInfo has the following properties:

- components (LicenseComponents) - see description of LicenseComponents
- components_constraints (LicenseConstraints) - see description of LicenseConstraints
- valid (boolean) - indicates whether the license is valid or not

Template object

```
{
    "components": {
        "calibration": false,
        "fusion": false,
        "hand_eye_calibration": false,
        "rectification": false,
        "self_calibration": false,
        "slam": false,
        "stereo": false,
        "svo": false
    },
    "components_constraints": {
        "image_version": {
            "max_version": "string",
            "min_version": "string"
        }
    },
    "valid": false
}
```

LicenseInfo objects are used in the following requests:

- GET / system/license

Log: Content of a specific log file represented in JSON format.
An object of type Log has the following properties:

- date (float) - UNIX time when log was last modified
- log (array of LogEntry) - the actual log entries
<|end_chunk_1552|><|start_chunk_1553|>
### Page 307
- name (string) - name of log file
- size (integer) - size of log file in bytes

Template object

```
{
    "date": 0,
    "log": [
        {
            "component": "string",
            "level": "string",
            "message": "string",
            "timestamp": 0
        },
        {
            "component": "string",
            "level": "string",
            "message": "string",
            "timestamp": 0
        }
    ],
    "name": "string",
    "size": 0
}
```

Log objects are used in the following requests:

- GET / logs/\{log\}

LogEntry: Representation of a single log entry in a log file.
An object of type LogEntry has the following properties:

- component (string) - module name that created this entry
- level (string) - log level (one of DEBUG, INFO, WARN, ERROR, FATAL)
- message (string) - actual log message
- timestamp (float) - Unix time of log entry

Template object

```
{
    "component": "string",
    "level": "string",
    "message": "string",
    "timestamp": 0
}
```

LogEntry objects are nested in Log.
LogInfo: Information about a specific log file.
An object of type LogInfo has the following properties:

- date (float) - UNIX time when log was last modified
- name (string) - name of log file
- size (integer) - size of log file in bytes

Template object

```
{
    "date": 0,
    "name": "string",
```
<|end_chunk_1553|><|start_chunk_1554|>
### Page 308<|end_chunk_1554|><|start_chunk_1555|>
 roboception 

(continued from previous page)

```
"size": 0
}
```

LogInfo objects are used in the following requests:

- GET / logs

ManualDNSServers: List of manual DNS servers.
An object of type ManualDNSServers has the following properties:

- manual_dns_servers (array of string)

<|end_chunk_1555|><|start_chunk_1556|>
## Template object

```
{
    "manual_dns_servers": [
        "string",
        "string"
    ]
}
```

ManualDNSServers objects are used in the following requests:

- PUT / system/dns

ManualNTPServers: List of manual NTP servers.
An object of type ManualNTPServers has the following properties:

- manual_ntp_servers (array of string)

<|end_chunk_1556|><|start_chunk_1557|>
## Template object

```
{
    "manual_ntp_servers": [
        "string",
        "string"
    ]
}
```

ManualNTPServers objects are used in the following requests:

- PUT / system/ntp

NTP: Status of the NTP time sync.
An object of type NTP has the following properties:

- enabled (boolean) - NTP is enabled
- manual_ntp_servers (array of string)
- offset (string) - time sync offset reported by NTP
- selected_ntp_servers (array of string)
- synchronized (boolean) - synchronized with NTP server

<|end_chunk_1557|><|start_chunk_1558|>
## Template object

```
{
    "enabled": false,
    "manual_ntp_servers": [
        "string",
        "string"
    ],
    "offset": "string",
```
<|end_chunk_1558|><|start_chunk_1559|>
### Page 309
```
"selected_ntp_servers": [
    "string",
    "string"
    ],
    "synchronized": false
}
```

NTP objects are nested in SysInfo, and are used in the following requests:

- GET / system/ntp
- PUT / system/ntp

NetworkInfo: Current network configuration.
An object of type NetworkInfo has the following properties:

- current_method (string) - method by which current settings were applied (one of INIT, LinkLocal, DHCP, PersistentIP, TemporaryIP)
- default_gateway (string) - current default gateway
- ip_address (string) - current IP address
- settings (NetworkSettings) - see description of NetworkSettings
- subnet_mask (string) - current subnet mask

<|end_chunk_1559|><|start_chunk_1560|>
 Template object 

```
{
    "current_method": "string",
    "default_gateway": "string",
    "ip_address": "string",
    "settings": {
        "dhcp_enabled": false,
        "persistent_default_gateway": "string",
        "persistent_ip_address": "string",
        "persistent_ip_enabled": false,
        "persistent_subnet_mask": "string"
    },
    "subnet_mask": "string"
}
```

NetworkInfo objects are nested in SysInfo, and are used in the following requests:

- GET / system/network

NetworkSettings: Current network settings.
An object of type NetworkSettings has the following properties:

- dhcp_enabled (boolean) - DHCP enabled
- persistent_default_gateway (string) - Persistent default gateway
- persistent_ip_address (string) - Persistent IP address
- persistent_ip_enabled (boolean) - Persistent IP enabled
- persistent_subnet_mask (string) - Persistent subnet mask

Template object

```
{
    "dhcp_enabled": false,
    "persistent_default_gateway": "string",
    "persistent_ip_address": "string",
```
<|end_chunk_1560|><|start_chunk_1561|>
### Page 310
```
"persistent_ip_enabled": false,
"persistent_subnet_mask": "string"
}
```

NetworkSettings objects are nested in NetworkInfo, and are used in the following requests:

- GET / system/network/settings
- PUT / system/network/settings

NodeInfo: Description of a computational node running on sensor.
An object of type NodeInfo has the following properties:

- name (string) - name of the node
- parameters (array of string) - list of the node's run-time parameters
- services (array of string) - list of the services this node offers
- status (string) - status of the node (one of unknown, down, idle, running)

<|end_chunk_1561|><|start_chunk_1562|>
 Template object 

```
{
    "name": "string",
    "parameters": [
        "string",
        "string"
    ],
    "services": [
        "string",
        "string"
    ],
    "status": "string"
}
```

NodeInfo objects are used in the following requests:

- GET /nodes
- GET /nodes/\{node\}
- GET /pipelines/\{pipeline\}/nodes
- GET /pipelines/\{pipeline\}/nodes/\{node\}

NodeStatus: Detailed current status of the node including run-time statistics.
An object of type NodeStatus has the following properties:

- status (string) - status of the node (one of unknown, down, idle, running)
- timestamp (float) - Unix time when values were last updated
- values (object) - dictionary with current status/statistics of the node

Template object

```
{
    "status": "string",
    "timestamp": 0,
    "values": {}
}
```

NodeStatus objects are used in the following requests:

- GET /nodes/\{node\}/status
<|end_chunk_1562|><|start_chunk_1563|>
### Page 311
- GET /pipelines/\{pipeline\}/nodes/\{node\}/status

Parameter: Representation of a node's run-time parameter. The parameter's 'value' type (and hence the types of the 'min', 'max' and 'default' fields) can be inferred from the 'type' field and might be one of the built-in primitive data types.
An object of type Parameter has the following properties:

- default (type not defined) - the parameter's default value
- description (string) - description of the parameter
- max (type not defined) - maximum value this parameter can be assigned to
- min (type not defined) - minimum value this parameter can be assigned to
- name (string) - name of the parameter
- type (string) - the parameter's primitive type represented as string (one of bool, int8, uint8, int16, uint16, int32, uint32, int64, uint64, float32, float64, string)
- value (type not defined) - the parameter's current value

<|end_chunk_1563|><|start_chunk_1564|>
 Template object 

```
{
    "default": {},
    "description": "string",
    "max": {},
    "min": {},
    "name": "string",
    "type": "string",
    "value": {}
}
```

Parameter objects are used in the following requests:

- GET /pipelines/\{pipeline\}/nodes/\{node\}/parameters
- PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters
- GET /pipelines/\{pipeline\}/nodes/\{node\}/parameters/\{param\}
- PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters/\{param\}

ParameterNameValue: Parameter name and value. The parameter's 'value' type (and hence the types of the 'min', 'max' and 'default' fields) can be inferred from the 'type' field and might be one of the built-in primitive data types.
An object of type ParameterNameValue has the following properties:

- name (string) - name of the parameter
- value (type not defined) - the parameter's current value

Template object

```
{
    "name": "string",
    "value": {}
}
```

ParameterNameValue objects are used in the following requests:

- PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters

ParameterValue: Parameter value. The parameter's 'value' type (and hence the types of the 'min', 'max' and 'default' fields) can be inferred from the 'type' field and might be one of the built-in primitive data types.
An object of type ParameterValue has the following properties:
<|end_chunk_1564|><|start_chunk_1565|>
### Page 312
- value (type not defined) - the parameter's current value

Template object

```
{
    "value": {}
}
```

ParameterValue objects are used in the following requests:

- PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters/\{param\}

PtpStatus: Status of the IEEE1588 (PTP) time sync.
An object of type PtpStatus has the following properties:

- master_ip (string) - IP of the master clock
- offset (float) - time offset in seconds to the master
- offset_dev (float) - standard deviation of time offset in seconds to the master
- offset_mean (float) - mean time offset in seconds to the master
- state (string) - state of PTP (one of off, unknown, INITIALIZING, FAULTY, DISABLED, LISTENING, PASSIVE, UNCALIBRATED, SLAVE)

<|end_chunk_1565|><|start_chunk_1566|>
 Template object 

```
{
    "master_ip": "string",
    "offset": 0,
    "offset_dev": 0,
    "offset_mean": 0,
    "state": "string"
}
```

PtpStatus objects are nested in SysInfo.
Service: Representation of a service that a node offers.
An object of type Service has the following properties:

- args (ServiceArgs) - see description of ServiceArgs
- description (string) - short description of this service
- name (string) - name of the service
- response (ServiceResponse) - see description of ServiceResponse

Template object

```
{
    "args": {},
    "description": "string",
    "name": "string",
    "response": {}
}
```

Service objects are used in the following requests:

- GET /nodes/\{node\}/services
- GET /nodes/\{node\}/services/\{service\}
- PUT /nodes/\{node\}/services/\{service\}
- GET /pipelines/\{pipeline\}/nodes/\{node\}/services
- GET /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\}
<|end_chunk_1566|><|start_chunk_1567|>
### Page 313
- PUT /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\}

ServiceArgs: Arguments required to call a service with. The general representation of these arguments is a (nested) dictionary. The specific content of this dictionary depends on the respective node and service call.

ServiceArgs objects are nested in Service.
ServiceResponse: The response returned by the service call. The general representation of this response is a (nested) dictionary. The specific content of this dictionary depends on the respective node and service call.

ServiceResponse objects are nested in Service.
Stream: Representation of a data stream offered by the rc_dynamics interface.
An object of type Stream has the following properties:

- destinations (array of StreamDestination) - list of destinations this data is currently streamed to
- name (string) - the data stream's name specifying which rc_dynamics data is streamed
- type (StreamType) - see description of StreamType

<|end_chunk_1567|><|start_chunk_1568|>
 Template object 

```
{
    "destinations": [
        "string",
        "string"
    ],
    "name": "string",
    "type": {
        "protobuf": "string",
        "protocol": "string"
    }
}
```

Stream objects are used in the following requests:

- GET /datastreams
- GET /datastreams/\{stream\}
- PUT /datastreams/\{stream\}
- DELETE /datastreams/\{stream\}

StreamDestination: A destination of an rc_dynamics data stream represented as string such as 'IP:port'

An object of type StreamDestination is of primitive type string.
StreamDestination objects are nested in Stream.
StreamType: Description of a data stream's protocol.
An object of type StreamType has the following properties:

- protobuf (string) - type of data-serialization, i.e. name of protobuf message definition
- protocol (string) - network protocol of the stream [UDP]

Template object

```
{
    "protobuf": "string",
    "protocol": "string"
}
```
<|end_chunk_1568|><|start_chunk_1569|>
### Page 314
StreamType objects are nested in Stream.
SysInfo: System information about the sensor.
An object of type SysInfo has the following properties:

- dns (DNS) - see description of DNS
- firmware (FirmwareInfo) - see description of FirmwareInfo
- hostname (string) - Hostname
- link_speed (integer) - Ethernet link speed in Mbps
- mac (string) - MAC address
- network (NetworkInfo) - see description of NetworkInfo
- ntp (NTP) - see description of NTP
- ptp_status (PtpStatus) - see description of PtpStatus
- ready (boolean) - system is fully booted and ready
- serial (string) - sensor serial number
- time (float) - system time as Unix timestamp
- ui_lock (UILock) - see description of UILock
- uptime (float) - system uptime in seconds

<|end_chunk_1569|><|start_chunk_1570|>
 Template object 

```
{
    "dns": {
        "dns_servers": [
            "string",
            "string"
        },
        "manual_dns_servers": [
            "string",
            "string"
        ]
    },
    "firmware": {
        "active_image": {
            "image_version": "string"
        },
        "fallback_booted": false,
        "inactive_image": {
            "image_version": "string"
        },
        "next_boot_image": "string"
    },
    "hostname": "string",
    "link_speed": 0,
    "mac": "string",
    "network": {
        "current_method": "string",
        "default_gateway": "string",
        "ip_address": "string",
        "settings": {
            "dhcp_enabled": false,
            "persistent_default_gateway": "string",
            "persistent_ip_address": "string",
            "persistent_ip_enabled": false,
            "persistent_subnet_mask": "string"
```

(continues on next page)
<|end_chunk_1570|><|start_chunk_1571|>
### Page 315
(continued from previous page)

```
    },
    "subnet_mask": "string"
},
"ntp": {
    "enabled": false,
    "manual_ntp_servers": [
        "string",
        "string"
    ],
    "offset": "string",
    "selected_ntp_servers": [
        "string",
        "string"
    ],
    "synchronized": false
},
"ptp_status": {
    "master_ip": "string",
    "offset": 0,
    "offset_dev": 0,
    "offset_mean": 0,
    "state": "string"
},
"ready": false,
"serial": "string",
"time": 0,
"ui_lock": {
    "enabled": false
},
"uptime": 0
}
```

SysInfo objects are used in the following requests:

- GET / system

Template: Detection template
An object of type Template has the following properties:

- id (string) - Unique identifier of the template

Template object

```
{
    "id": "string"
}
```

Template objects are used in the following requests:

- GET /templates/rc_boxpick
- GET /templates/rc_boxpick/\{id\}
- PUT /templates/rc_boxpick/\{id\}
- GET /templates/rc_silhouettematch
- GET /templates/rc_silhouettematch/\{id\}
- PUT /templates/rc_silhouettematch/\{id\}

UILock: UI lock status.
An object of type UILock has the following properties:

- enabled (boolean)
<|end_chunk_1571|><|start_chunk_1572|>
### Page 316<|end_chunk_1572|><|start_chunk_1573|>
 Template object 

```
{
    "enabled": false
}
```

UILock objects are nested in SysInfo, and are used in the following requests:

- GET / system/ui_lock

<|end_chunk_1573|><|start_chunk_1574|>
### 7.3.5 Swagger UI

The rc_visard's Swagger UI allows developers to easily visualize and interact with the REST-API, e.g., for development and testing. Accessing http://<host>/api/ or http://<host>/api/swagger (the former will automatically be redirected to the latter) opens a visualization of the rc_visard's general API structure including all available resources and requests (Section 7.3.3) and offers a simple user interface for exploring all of its features.

Note: Users must be aware that, although the $r c_{-}$visard's Swagger UI is designed to explore and test the REST-API, it is a fully functional interface. That is, any issued requests are actually processed and particularly PUT, POST, and DELETE requests might change the overall status and/or behavior of the device.
<|end_chunk_1574|><|start_chunk_1575|>
### Page 317
![img-78.jpeg](img-78.jpeg)

Fig. 7.2: Initial view of the rc_visard's Swagger UI with its resources and requests

Using this interface, available resources and requests can be explored by clicking on them to uncollapse or recollapse them. The following figure shows an example of how to get a node's current status by filling in the necessary parameters (pipeline number and node name) and clicking Execute. This action results in the Swagger UI showing, amongst others, the actual curl command that was executed when issuing the request as well as the response body showing the current status of the requested node in a JSON-formatted string.
<|end_chunk_1575|><|start_chunk_1576|>
### Page 318
![img-79.jpeg](img-79.jpeg)

Fig. 7.3: Result of requesting the rc_stereomatching node's status

Some actions, such as setting parameters or calling services, require more complex parameters to an HTTP request. The Swagger UI allows developers to explore the attributes required for these actions during run-time, as shown in the next example. In the figure below, the attributes required for the the rc_hand_eye_calibration node's set_pose service are explored by performing a GET request on this resource. The response features a full description of the service offered, including all required arguments with their names and types as a JSON-formatted string.
<|end_chunk_1576|><|start_chunk_1577|>
### Page 319
![img-80.jpeg](img-80.jpeg)

Fig. 7.4: The result of the GET request on the set_pose service shows the required arguments for this service call.

Users can easily use this preformatted JSON string as a template for the service arguments to actually call the service:
<|end_chunk_1577|><|start_chunk_1578|>
### Page 320
![img-81.jpeg](img-81.jpeg)

Fig. 7.5: Filling in the arguments of the set...pose service request
<|end_chunk_1578|><|start_chunk_1579|>
 7.4 The rc_dynamics interface 

The rc_dynamics interface offers continuous, real-time data-stream access to rc_visard's several dynamic state estimates (Section 6.3.1.2) as continuous, real-time data streams. It allows state estimates of all offered types to be configured to be streamed to any host in the network. The Data-stream protocol (Section 7.4.3) used is agnostic w.r.t. operating system and programming language.
<|end_chunk_1579|><|start_chunk_1580|>
### 7.4.1 Starting/stopping dynamic-state estimation

The rc_visard's dynamic-state estimates are only available if the respective module, i.e., the sensor dynamics module (Section 6.3.1), is turned on. This can be done either in the Web GUI - a respective switch is offered on the Dynamics page - or via the REST-API by using the module's service calls. A sample curl request to start dynamic-state estimation would look like:

```
curl -X PUT --header 'Content-Type: application/json' -d '{}' 'http://<host>/api/v1/nodes/rc_
--dynamics/services/start'
```

Note: To save computational resources, it is recommended to stop dynamic-state estimation when not needed any longer.
<|end_chunk_1580|><|start_chunk_1581|>
### 7.4.2 Configuring data streams

Available data streams, i.e., dynamic-state estimates, can be listed and configured by the $r c \_v i s a r d ' s$ REST-API (Section 7.3.3.2), e.g., a list of all available data streams can be requested with GET /
<|end_chunk_1581|><|start_chunk_1582|>
### Page 321
datastreams. For a detailed description of the following data streams, please refer to Available state estimates (Section 6.3.1.2).

Table 7.2: Available data streams via the rc_dynamics interface

| Name | Protocol | Protobuf | Description |
| :-- | :--: | :--: | :-- |
| dynamics | UDP | Dynamics | Dynamics of sensor (pose, velocity, acceleration) from INS <br> or SLAM (best effort depending on availability) at realtime <br> frequency (IMU rate) |
| dynamics_ins | UDP | Dynamics | Dynamics of sensor (pose, velocity, acceleration) from <br> stereo INS at realtime frequency (IMU rate) |
| imu | UDP | Imu | Raw IMU (Inertial Measurement Unit) values at realtime <br> frequency (IMU rate) |
| pose | UDP | Frame | Pose of left camera from INS or SLAM (best effort <br> depending on availability) at maximum camera frequency <br> (fps) |
| pose_ins | UDP | Frame | Pose of left camera from stereo INS at maximum camera <br> frequency (fps) |
| pose_rt | UDP | Frame | Pose of left camera from INS or SLAM (best effort <br> depending on availability) at realtime frequency (IMU rate) |
| pose_rt_ins | UDP | Frame | Pose of left camera from stereo INS at realtime frequency <br> (IMU rate) |

The general procedure for working with the rc_dynamics interface is the following:

1. Request a data stream via REST-API. The following sample curl command issues a PUT / datastreams/\{stream\} request to initiate a stream of type pose_rt from the rc_visard to client host 10.0.1.14 at port 30000:
```
curl -X PUT --header 'Content-Type: application/x-www-form-urlencoded' --header
\--'Accept: application/json' -d 'destination=10.0.1.14:30000' 'http://<host>/api/v1/
\--datastreams/pose_rt'
```

2. Receive and deserialize data. With a successful request, the stream is initiated and data of the specified stream type is continuously sent to the client host. According to the Data-stream protocol (Section 7.4.3), the client needs to receive, deserialize and process the data.
3. Stop a requested data stream via REST-API. The following sample curl command issues a DELETE /datastreams/\{stream\} request to delete, i.e., stop, the previously requested stream of type pose_rt with destination 10.0.1.14:30000:
```
curl -X DELETE --header 'Accept: application/json' 'http://<host>/api/v1/datastreams/
\--pose_rt?destination=10.0.1.14:30000'
```

To remove all destinations for a stream, simply omit the destination parameter.

Warning: Data streams can not be deleted automatically, i.e., the $r c \_v i s a r d$ keeps streaming data even if the client-side is disconnected or has stopped consuming the sent datagrams. A maximum of 10 destinations per stream are allowed. It is therefore strongly recommended to stop data streams via the REST-API when they are or no longer used.
<|end_chunk_1582|><|start_chunk_1583|>
 7.4.3 Data-stream protocol 

Once a data stream is established, data is continuously sent to the specified client host and port (destination) via the following protocol:
Network protocol: The only currently supported network protocol is UDP, i.e., data is sent as UDP datagrams.
<|end_chunk_1583|><|start_chunk_1584|>
### Page 322
Data serialization: The data being sent is serialized via Google protocol buffers. The following message type definitions are used.

- The camera-pose streams and real-time camera-pose streams (Section 6.3.1.2) are serialized using the Frame message type:

```
message Frame
{
    optional PoseStamped pose = 1;
    optional string parent = 2; // Name of the parent frame
    optional string name = 3; // Name of the frame
    optional string producer = 4; // Name of the producer of this data
}
```

The producer field can take the values ins, slam, rt...ins, and rt...slam, indicating whether the data was computed by SLAM or Stereo INS, and is real-time (rt) or not.

- The real-time dynamics stream (Section 6.3.1.2) is serialized using the Dynamics message type:

| message Dynamics |  |
| :--: | :--: |
| $\square$ |  |
| optional Time timestamp | = 1; // Time when the data was_ |
| --captured |  |
| optional Pose pose | $=2 ;$ |
| optional string pose..frame | = 3; // Name of the frame that_ |
| --the pose is given in |  |
| optional Vector3d linear...velocity | = 4; // Linear velocity in m/s |
| optional string linear..velocity..frame | = 5; // Name of the frame that_ |
| --the linear..velocity is given in |  |
| optional Vector3d angular..velocity | = 6; // Angular velocity in rad/s |
| optional string angular..velocity..frame | = 7; // Name of the frame that_ |
| --the angular..velocity is given in |  |
| optional Vector3d linear...acceleration | = 8; // Gravity compensated_ |
| --linear acceleration in $\mathrm{m} / \mathrm{s}^{2}$ |  |
| optional string linear...acceleration..frame | = 9; // Name of the frame that_ |
| --the acceleration is given in |  |
| repeated double covariance | = 10 [packed=true]; // Row-major_ |
| --representation of the 15x15 covariance matrix |  |
| optional Frame cam2imu..transform | = 11; // pose of the left camera_ |
| --wrt. the IMU frame |  |
| optional bool possible...jump | = 12; // True if there possibly_ |
| --was a jump in the pose estimation |  |
| optional string producer | = 13; // Name of the producer of_ |
| --this data |  |
| \} |  |

The producer field can take the values rt...ins and rt...slam, indicating whether the data was computed by SLAM or Stereo INS.

- The IMU stream (Section 6.3.1.2) is serialized using the Imu message type:

| message Imu |  |
| :--: | :--: |
| $\square$ | $=1 ; / /$ Time when the data was_ |
| --captured |  |
| optional Vector3d linear...acceleration | = 2; // Linear acceleration in m/ |
| $s^{2}$ measured by the IMU |  |
| optional Vector3d angular..velocity | = 3; // Angular velocity in rad/ |
| --s measured by the IMU |  |
| \} |  |

- The nested types PoseStamped, Pose, Time, Quaternion, and Vector3D are defined as follows:
<|end_chunk_1584|><|start_chunk_1585|>
### Page 323
```
message PoseStamped
{
    optional Time timestamp = 1; // Time when the data was captured
    optional Pose pose = 2;
}
```

```
message Pose
{
    optional Vector3d position = 1; // Position in meters
    optional Quaternion orientation = 2; // Orientation as unit quaternion
    repeated double covariance = 3 [packed=true]; // Row-major
--representation of the 6x6 covariance matrix (x, y, z, rotation about X axis,
--rotation about Y axis, rotation about Z axis)
}
```

```
message Time
{
    /// \brief Seconds
    optional int64 sec = 1;
    /// \brief Nanoseconds
    optional int32 nsec = 2;
}
```

```
message Quaternion
{
    optional double x = 2;
    optional double y = 3;
    optional double z = 4;
    optional double w = 5;
}
```

```
message Vector3d
{
    optional double x = 1;
    optional double y = 2;
    optional double z = 3;
}
```

<|end_chunk_1585|><|start_chunk_1586|>
 7.4.4 rc_dynamics_api 

The open-source rc_dynamics_api package provides a simple, convenient C++ wrapper to request and parse rc_dynamics streams, see http://www.roboception.com/download.
<|end_chunk_1586|><|start_chunk_1587|>
### 7.5 KUKA Ethernet KRL Interface

The rc_visard provides an Ethernet KRL Interface (EKI Bridge), which allows communicating with the rc_visard from KUKA KRL via KUKA.EthernetKRL XML.

Note: The component is optional and requires a separate Roboception's EKIBridge license (Section 8.7) to be purchased.

Note: The KUKA.EthernetKRL add-on software package version 2.2 or newer must be activated on the robot controller to use this component.

The EKI Bridge can be used to programmatically
<|end_chunk_1587|><|start_chunk_1588|>
### Page 324
- do service calls, e.g. to start and stop individual computational nodes, or to use offered services such as the hand-eye calibration or the computation of grasp poses;
- set and get run-time parameters of computation nodes, e.g. of the camera, or disparity calculation.

Note: A known limitation of the EKI Bridge is that strings representing valid numbers will be converted to int/float. Hence user-defined names (like ROI IDs, etc.) should always contain at least one letter so they can be used in service call arguments.
<|end_chunk_1588|><|start_chunk_1589|>
 7.5.1 Ethernet connection configuration 

The EKI Bridge listens on port 7000 for EKI XML messages and transparently bridges the rc_visard's REST-API v2 (Section 7.3). The received EKI messages are transformed to JSON and forwarded to the rc_visard's REST-API. The response from the REST-API is transformed back to EKI XML.

The EKI Bridge gives access to run-time parameters and offered services of all computational nodes described in Software modules (Section 6).

The Ethernet connection to the rc_visard on the robot controller is configured using XML configuration files.

The EKI XML configuration files of all nodes running on the rc_visard are available for download at:
https://doc.rc-visard.com/latest/en/eki.html\#eki-xml-configuration-files
Each node offering run-time parameters has an XML configuration file for setting and getting its parameters. These are named following the scheme <node name>-parameters.xml. Each node's service has its own XML configuration file. These are named following the scheme <node_name>-<service_name>. xml.

The IP of the $r c \_v i s a r d$ in the network needs to be filled in the XML file.
These files must be stored in the directory C: \KRC $\backslash R O B O T E R \backslash C o n f i g \backslash U s e r \backslash C o m m o n \backslash E t h e r n e t K R L$ of the robot controller and they are read in when a connection is initialized.

As an example, an Ethernet connection to configure the rc_stereomatching parameters is established with the following KRL code.

```
DECL EKI_Status RET
RET = EKI_INIT("rc_stereomatching-parameters")
RET = EKI.Open("rc_stereomatching-parameters")
; Desired operation
RET = EKI.Close("rc_stereomatching-parameters")
```

Note: The EKI Bridge automatically terminates the connection to the client if the received XML telegram is invalid.
<|end_chunk_1589|><|start_chunk_1590|>
### 7.5.2 Generic XML structure

For data transmission, the EKI Bridge uses <req> as root XML element (short for request).
The root tag always includes the following elements.

- <node>. This includes a child XML element used by the EKI Bridge to identify the target node. The node name is already included in the XML configuration file.
- <end_of_request>. End of request flag that triggers the request.

The following listing shows the generic XML structure for data transmission.
<|end_chunk_1590|><|start_chunk_1591|>
### Page 325
```
<SEND>
    <XML>
        <ELEMENT Tag="req/node/<node..name>" Type="STRING"/>
        <ELEMENT Tag="req/end..of..request" Type="BOOL"/>
    </XML>
</SEND>
```

For data reception, the EKI Bridge uses <res> as root XML element (short for response). The root tag always includes a <return_code> child element.

```
<RECEIVE>
    <XML>
        <ELEMENT Tag="res/return_code/@value" Type="INT"/>
        <ELEMENT Tag="res/return_code/@message" Type="STRING"/>
        <ELEMENT Tag="res" Set Flag="998"/>
    </XML>
</RECEIVE>
```

Note: By default the XML configuration files uses 998 as flag to notify KRL that the response data record has been received. If this value is already in use, it should be changed in the corresponding XML configuration file.
<|end_chunk_1591|><|start_chunk_1592|>
 7.5.2.1 Return code 

The <return_code> element consists of a value and a message attribute.
As for all other components, a successful request returns with a res/return_code/@value of 0 . Negative values indicate that the request failed. The error message is contained in res/return_code/ @message. Positive values indicate that the request succeeded with additional information, contained in res/return_code/@message as well.

The following codes can be issued by the EKI Bridge component.
Table 7.3: Return codes of the EKI Bridge component

| Code | Description |
| :--: | :-- |
| 0 | Success |
| -1 | Parsing error in the conversion from XML to JSON |
| -2 | Internal error |
| -5 | Connection error from the REST-API |
| -9 | Missing or invalid license for EKI Bridge component |

Note: The EKI Bridge can also return return code values specific to individual nodes. They are documented in the respective software module (Section 6).

Note: Due to limitations in KRL, the maximum length of a string returned by the EKI Bridge is 512 characters. All messages larger than this value are truncated.
<|end_chunk_1592|><|start_chunk_1593|>
### 7.5.3 Services

For the nodes' services, the XML schema is generated from the service's arguments and response in JavaScript Object Notation (JSON) described in Software modules (Section 6). The conversion is done transparently, except for the conversion rules described below.

Conversions of poses:
A pose is a JSON object that includes position and orientation keys.
<|end_chunk_1593|><|start_chunk_1594|>
### Page 326
```
{
    "pose": {
        "position": {
            "x": "float64",
            "y": "float64",
            "z": "float64",
        },
        "orientation": {
            "x": "float64",
            "y": "float64",
            "z": "float64",
            "w": "float64",
        }
    }
}
```

This JSON object is converted to a KRL FRAME in the XML message.

```
<pose X="..." Y="..." Z="..." A="..." B="..." C="..."></pose>
```

Positions are converted from meters to millimeters and orientations are converted from quaternions to KUKA ABC (in degrees).

Note: No other unit conversions are included in the EKI Bridge. All dimensions and 3D coordinates that don't belong to a pose are expected and returned in meters.

Arrays:
Arrays are identified by adding the child element <le> (short for list element) to the list name. As an example, the JSON object

```
{
    "rectangles": [
        {
            "x": "float64",
            "y": "float64"
        }
    ]
}
```

is converted to the XML fragment

```
<rectangles>
    <le>
        <x>...</x>
        <y>...</y>
    </le>
</rectangles>
```

Use of XML attributes:
All JSON keys whose values are a primitive data type and don't belong to an array are stored in attributes. As an example, the JSON object

```
{
    "item": {
        "uuid": "string",
        "confidence": "float64",
        "rectangle": {
            "x": "float64",
            "y": "float64"
```

(continues on next page)
<|end_chunk_1594|><|start_chunk_1595|>
### Page 327
![img-82.jpeg](img-82.jpeg)
<|end_chunk_1595|><|start_chunk_1596|>
 7.5.3.1 Request XML structure 

The <SEND> element in the XML configuration file for a generic service follows the specification below.

```
<SEND>
    <XML>
        <ELEMENT Tag="req/node/<node_name>" Type="STRING"/>
        <ELEMENT Tag="req/service/<service_name>" Type="STRING"/>
        <ELEMENT Tag="req/args/<argX>" Type="<argX_type>"/>
        <ELEMENT Tag="req/end_of_request" Type="BOOL"/>
    </XML>
</SEND>
```

The <service> element includes a child XML element that is used by the EKI Bridge to identify the target service from the XML telegram. The service name is already included in the configuration file.
The <args> element includes the service arguments and should be configured with EKI_Set<Type> KRL instructions.

As an example, the <SEND> element of the rc_load_carrier_db's get_load_carriers service (see LoadCarrierDB, Section 6.6.1) is:

```
<SEND>
    <XML>
        <ELEMENT Tag="req/node/rc_load_carrier_db" Type="STRING"/>
        <ELEMENT Tag="req/service/get_load_carriers" Type="STRING"/>
        <ELEMENT Tag="req/args/load_carrier_ids/le" Type="STRING"/>
        <ELEMENT Tag="req/end_of_request" Type="BOOL"/>
    </XML>
</SEND>
```

The <end_of_request> element allows to have arrays in the request. For configuring an array, the request is split into as many packages as the size of the array. The last telegram contains all tags, including the <end_of_request> flag, while all other telegrams contain one array element each.

As an example, for requesting two load carrier models to the rc_load_carrier_db's get_load_carriers service, the user needs to send two XML messages. The first XML telegram is:

```
<req>
    <args>
        <load_carrier_ids>
            <le>load_carrier1</le>
        </load_carrier_ids>
    </args>
</req>
```

This telegram can be sent from KRL with the EKI_Send command, by specifying the list element as path:
<|end_chunk_1596|><|start_chunk_1597|>
### Page 328
DECL EKI_STATUS RET
RET = EKI_SetString("rc_load_carrier_db-get_load_carriers", "req/args/load_carrier_ids/ $\sim$ le", "load_carrier1")
RET = EKI_Send("rc_load_carrier_db-get_load_carriers", "req/args/load_carrier_ids/le")

The second telegram includes all tags and triggers the request to the rc_load_carrier_db node:

```
<req>
    <node>
        <rc_load_carrier_db></rc_load_carrier_db>
    </node>
    <service>
        <get_load_carriers></get_load_carriers>
    </service>
    <args>
        <load_carrier_ids>
            <le>load_carrier2</le>
        </load_carrier_ids>
    </args>
    <end_of_request></end_of_request>
</req>
```

This telegram can be sent from KRL by specifying req as path for EKI_Send:

```
DECL EKI_STATUS RET
RET = EKI_SetString("rc_load_carrier_db-get_load_carriers", "req/args/load_carrier_ids/
\l=le", "load_carrier2")
RET = EKI_Send("rc_load_carrier_db-get_load_carriers", "req")
```

<|end_chunk_1597|><|start_chunk_1598|>
 7.5.3.2 Response XML structure 

The <RECEIVE> element in the XML configuration file for a generic service follows the specification below:

```
<RECEIVE>
    <XML>
        <ELEMENT Tag="res/<resX>" Type="<resX_type>"/>
        <ELEMENT Tag="res/return_code/@value" Type="INT"/>
        <ELEMENT Tag="res/return_code/@message" Type="STRING"/>
        <ELEMENT Tag="res" Set_Flag="998"/>
    </XML>
</RECEIVE>
```

As an example, the <RECEIVE> element of the rc_april_tag_detect's detect service (see TagDetect, Section 6.4.3) is:

```
<RECEIVE>
    <XML>
        <ELEMENT Tag="res/timestamp/@sec" Type="INT"/>
        <ELEMENT Tag="res/timestamp/@nsec" Type="INT"/>
        <ELEMENT Tag="res/return_code/@message" Type="STRING"/>
        <ELEMENT Tag="res/return_code/@value" Type="INT"/>
        <ELEMENT Tag="res/tags/le/pose_frame" Type="STRING"/>
        <ELEMENT Tag="res/tags/le/timestamp/@sec" Type="INT"/>
        <ELEMENT Tag="res/tags/le/timestamp/@nsec" Type="INT"/>
        <ELEMENT Tag="res/tags/le/pose/@X" Type="REAL"/>
        <ELEMENT Tag="res/tags/le/pose/@Y" Type="REAL"/>
        <ELEMENT Tag="res/tags/le/pose/@Z" Type="REAL"/>
        <ELEMENT Tag="res/tags/le/pose/@A" Type="REAL"/>
        <ELEMENT Tag="res/tags/le/pose/@B" Type="REAL"/>
        <ELEMENT Tag="res/tags/le/pose/@C" Type="REAL"/>
```
<|end_chunk_1598|><|start_chunk_1599|>
### Page 329
```
<ELEMENT Tag="res/tags/le/instance_id" Type="STRING"/>
<ELEMENT Tag="res/tags/le/id" Type="STRING"/>
<ELEMENT Tag="res/tags/le/size" Type="REAL"/>
<ELEMENT Tag="res" Set Flag="998"/>
</XML>
</RECEIVE>
```

For arrays, the response includes multiple instances of the same XML element. Each element is written into a separate buffer within EKI and can be read from the buffer with KRL instructions. The number of instances can be requested with EKI_CheckBuffer and each instance can then be read by calling EKI_Get $<$ Type $>$.

As an example, the tag poses received after a call to the rc_april_tag_detect's detect service can be read in KRL using the following code:

```
DECL EKI_STATUS RET
DECL INT i
DECL INT num_instances
DECL FRAME poses[32]
DECL FRAME pose = {X 0.0, Y 0.0, Z 0.0, A 0.0, B 0.0, C 0.0}
RET = EKI_CheckBuffer("rc_april_tag_detect-detect", "res/tags/le/pose")
num_instances = RET. Buff
for i=1 to num_instances
    RET = EKI_GetFrame("rc_april_tag_detect-detect", "res/tags/le/pose", pose)
    poses[i] = pose
endfor
RET = EKI_ClearBuffer("rc_april_tag_detect-detect", "res")
```

Note: Before each request from EKI to the rc_visard, all buffers should be cleared in order to store only the current response in the EKI buffers.
<|end_chunk_1599|><|start_chunk_1600|>
 7.5.4 Parameters 

All nodes' parameters can be set and queried from the EKI Bridge. The XML configuration file for a generic node follows the specification below:

```
<SEND>
    <XML>
        <ELEMENT Tag="req/node/<node_name>" Type="STRING"/>
        <ELEMENT Tag="req/parameters/<parameter_x>/@value" Type="INT"/>
        <ELEMENT Tag="req/parameters/<parameter_y>/@value" Type="STRING"/>
        <ELEMENT Tag="req/end_of_request" Type="BOOL"/>
    </XML>
</SEND>
<RECEIVE>
    <XML>
        <ELEMENT Tag="res/parameters/<parameter_x>/@value" Type="INT"/>
        <ELEMENT Tag="res/parameters/<parameter_x>/@default" Type="INT"/>
        <ELEMENT Tag="res/parameters/<parameter_x>/@min" Type="INT"/>
        <ELEMENT Tag="res/parameters/<parameter_x>/@max" Type="INT"/>
        <ELEMENT Tag="res/parameters/<parameter_y>/@value" Type="REAL"/>
        <ELEMENT Tag="res/parameters/<parameter_y>/@default" Type="REAL"/>
        <ELEMENT Tag="res/parameters/<parameter_y>/@min" Type="REAL"/>
        <ELEMENT Tag="res/parameters/<parameter_y>/@max" Type="REAL"/>
        <ELEMENT Tag="res/return_code/@value" Type="INT"/>
        <ELEMENT Tag="res/return_code/@message" Type="STRING"/>
```
<|end_chunk_1600|><|start_chunk_1601|>
### Page 330
The request is interpreted as a get request if all parameter's value attributes are empty. If any value attribute is non-empty, it is interpreted as set request of the non-empty parameters.

As an example, the current value of all parameters of rc_stereomatching can be queried using the XML telegram:

```
<req>
    <node>
        <rc_stereomatching></rc_stereomatching>
    </node>
    <parameters></parameters>
    <end_of_request></end_of_request>
</req>
```

This XML telegram can be sent out with Ethernet KRL using:
DECL EKI_STATUS RET
RET $=$ EKI_Send("rc_stereomatching-parameters", "req")
The response from the EKI Bridge contains all parameters:

```
<res>
    <parameters>
        <acquisition_mode default="Continuous" max="" min="" value="Continuous"/>
        <quality default="High" max="" min="" value="High"/>
        <static_scene default="0" max="1" min="0" value="0"/>
        <seg default="200" max="4000" min="0" value="200"/>
        <smooth default="1" max="1" min="0" value="1"/>
        <fill default="3" max="4" min="0" value="3"/>
        <minconf default="0.5" max="1.0" min="0.5" value="0.5"/>
        <mindepth default="0.1" max="100.0" min="0.1" value="0.1"/>
        <maxdepth default="100.0" max="100.0" min="0.1" value="100.0"/>
        <maxdeptherr default="100.0" max="100.0" min="0.01" value="100.0"/>
    </parameters>
    <return_code message="" value="0"/>
</res>
```

The quality parameter of rc_stereomatching can be set to Low by the XML telegram:

```
<req>
    <node>
        <rc_stereomatching></rc_stereomatching>
    </node>
    <parameters>
        <quality value="Low"></quality>
    </parameters>
    <end_of_request></end_of_request>
</req>
```

This XML telegram can be sent out with Ethernet KRL using:

```
DECL EKI_STATUS RET
RET = EKI_SetString("rc_stereomatching-parameters", "req/parameters/quality/@value",
--"Low")
RET = EKI_Send("rc_stereomatching-parameters", "req")
```

In this case, only the applied value of quality is returned by the EKI Bridge:
<|end_chunk_1601|><|start_chunk_1602|>
### Page 331
```
<res>
    <parameters>
        <quality default="High" max="" min="" value="Low"/>
    </parameters>
    <return_code message="" value="0"/>
</res>
```

<|end_chunk_1602|><|start_chunk_1603|>
 7.5.5 Migration to firmware version 22.01 

From firmware version 22.01 on the EKI Bridge reflects rc_visard's REST-API v2 (Section 7.3).
This requires the following changes:

- Configuring load carriers, grippers and regions of interest is now only accessible in the global database modules:
- Use the rc_load_carrier_db XML files for getting, setting and deleting of load carriers.
- Use the rc_gripper_db XML files for getting, setting and deleting of grippers.
- Use the rc_roi_db XML files for getting, setting and deleting of regions of interest.
- Load carrier detection and filling level detection is now only accessible via the rc_load_carrier node.
- Use the rc_load_carrier XML files for detect_load_carriers and detect_filling_level services.

<|end_chunk_1603|><|start_chunk_1604|>
### 7.5.6 Example applications

More detailed robot application examples can be found at https://github.com/roboception/eki_examples.
<|end_chunk_1604|><|start_chunk_1605|>
### 7.5.7 Troubleshooting
<|end_chunk_1605|><|start_chunk_1606|>
## SmartPad error message: Limit of element memory reached

This error may occur if the number of matches exceeds the memory limit.

- Increase BUFFERING and set BUFFSIZE in EKI config files. Adapt these settings to your particular KRC.
- Decrease the 'Maximum Matches' parameter in the detection module
- Even if the total memory limit (BUFFSIZE) of a message is not reached, the KRC might not be able to parse the number of child elements in the XML tree if the BUFFERING limit is too small. For example, if your application proposes 50 different grasps, the BUFFERING limit needs to be 50 too.

<|end_chunk_1606|><|start_chunk_1607|>
### 7.6 gRPC image stream interface

The gRPC image streaming interface can be used as an alternative to the GigE Vision / GenICam interface (Section 7.2) for getting camera images and synchronized sets of images (e.g. left camera image and corresponding disparity image). gRPC is a remote procedure call system that also supports streaming. It uses Protocol Buffers (see https://developers.google.com/protocol-buffers/) as interface description language and data serialization. For a gRPC introduction and more details please see the official website (https://grpc.io/).
The advantages of the gRPC interface in comparison to GigE Vision are:

- It is simpler to use in own programs than GigE Vision.
<|end_chunk_1607|><|start_chunk_1608|>
### Page 332
- There is gRPC support for a lot of programming languages (see https://grpc.io/).
- The communication is based on TCP instead of UDP and therefore it also works over less stable networks, e.g. WLAN.

The disadvantages of the gRPC interface in comparison to GigE Vision are:

- It does not support changing parameters, but the REST-API interface (Section 7.3) can be used for changing parameters.
- It is not a standard vision interface like GigE Vision.

The rc_visard provides synchronized image sets via gRPC server side streams on port 50051.
The communication is started by sending an ImageSetRequest message to the server. The message contains the information about requested images, i.e. left, right, disparity, confidence and disparity_error images can be enabled separately.

After getting the request, the server starts continuously sending ImageSet messages that contain all requested images with all parameters necessary for interpreting the images. The images that are contained in an ImageSet message are synchronized, i.e. they are all captured at the same time. The only exception to this rule is if the out1_mode (Section 6.5.4.1) is set to AlternateExposureActive. In this case, the camera and disparity images are taken 40 ms apart, so that the GPIO Out1 is LOW when the left and right images are taken, and HIGH for the disparity, confidence and error images. This mode is useful when a random dot projector is used, because the projector would be off for capturing the left and right image, and on for the disparity image, which results in undisturbed camera images and a much denser and more accurate disparity image.

Streaming of images is done until the client closes the connection.
<|end_chunk_1608|><|start_chunk_1609|>
 7.6.1 gRPC service definition 

```
syntax = "proto3";
message Time
{
    int32 sec = 1; ///< Seconds
    int32 nsec = 2; ///< Nanoseconds
}
message Gpios
{
    uint32 inputs = 1; ///< bitmask of available inputs
    uint32 outputs = 2; ///< bitmask of available outputs
    uint32 values = 3; ///< bitmask of GPIO values
}
message Image
{
    Time timestamp = 1; ///< Acquisition timestamp of the image
    uint32 height = 2; ///< image height (number of rows)
    uint32 width = 3; ///< image width (number of columns)
    float focal_length = 4; ///< focal length in pixels
    float principal_point_u = 5; ///< horizontal position of the principal point
    float principal_point_v = 6; ///< vertical position of the principal point
    string encoding = 7; ///< Encoding of pixels ["mono8", "mono16", "rgb8"]
    bool is_bigendian = 8; ///< is data bigendian, (in our case false)
    uint32 step = 9; ///< full row length in bytes
    bytes data = 10; ///< actual matrix data, size is (step * height)
    Gpios gpios = 11; ///< GPIOs as of acquisition timestamp
    float exposure_time = 12; ///< exposure time in seconds
    float gain = 13; ///< gain factor in decibel
    float noise = 14; ///< noise
```
<|end_chunk_1609|><|start_chunk_1610|>
### Page 333
(continued from previous page)
float out1_reduction $=16 ; / / /<$ Fraction of reduction $(0.0-1.0)$ of exposure time for
...images with GPIO Out1=Low in exp_auto_mode=AdaptiveOut1
float brightness $=17 ; / / /<$ Current brightness of the image as value between 0 and 1
\}
message DisparityImage
\{
Time timestamp $=1 ; / / /<$ Acquisition timestamp of the image
float scale $=2 ; / / /<$ scale factor
float offset $=3 ; / / /<$ offset in pixels (in our case 0)
float invalid_data_value $=4 ; / / /<$ value used to mark pixels as invalid (in our case 0)
float baseline $=5 ; / / /<$ baseline in meters
float delta_d $=6 ; / / /<$ Smallest allowed disparity increment. The smallest_
...achievable depth range resolution is delta_Z = (Z^2/image.focal_length+baseline)+delta_d.
Image image $=7 ; / / /<$ disparity image
\}
message Mesh
\{
Time timestamp $=1 ; / / /<$ Acquisition timestamp of disparity image from which the mesh_
...is computed
string format $=2 ; / / /<$ currently only "ply" is supported
bytes data $=3 ; / / /<$ actual mesh data
\}
message ImageSet
\{
Time timestamp $=1 ;$
Image left $=2 ;$
Image right $=3 ;$
DisparityImage disparity $=4 ;$
Image disparity_error $=5 ;$
Image confidence $=6 ;$
Mesh mesh $=7 ;$
\}
message MeshOptions
\{
uint32 max_points $=1 ; / / /<$ limit maximum number of points, zero means default (up_
...to 3.1MP), minimum is 1000
enum BinningMethod \{
AVERAGE $=0 ; \quad / / /<$ average over all points in bin
MIN_DEPTH $=1 ; \quad / / /<$ use point with minimum depth (i.e. closest to camera) in_
...bin
\}
BinningMethod binning_method $=2 ; / / /<$ method used for binning if limited by max_points
bool watertight $=3 ; / / /<$ connect all edges and fill all holes, e.g. for collision_
...checking
bool textured $=4 ; / / /<$ add texture information to mesh
\}
message ImageSetRequest
\{
bool left_enabled $=1 ;$
bool right_enabled $=2 ;$
bool disparity_enabled $=3 ;$
bool disparity_error_enabled $=4 ;$
bool confidence_enabled $=5 ;$
bool mesh_enabled $=6 ;$
MeshOptions mesh_options $=7 ;$
bool color $=8 ; / / /<$ send left/right image as color (rgb0) images
(continues on next page)
<|end_chunk_1610|><|start_chunk_1611|>
### Page 334<|end_chunk_1611|><|start_chunk_1612|>
 (continued from previous page) 

```
}
service ImageInterface
{
    // A server-to-client streaming RPC.
    rpc StreamImageSets(ImageSetRequest) returns (stream ImageSet) {}
}
```

<|end_chunk_1612|><|start_chunk_1613|>
### 7.6.2 Image stream conversions

The conversion of disparity images into a point cloud can be done as described in the GigE Vision / GenICam interface (Section 7.2.7).
<|end_chunk_1613|><|start_chunk_1614|>
### 7.6.3 Example client

A simple example C++ client can be found at https://github.com/roboception/grpc_image_client_ example.
<|end_chunk_1614|><|start_chunk_1615|>
### 7.7 OPC UA interface

The $r c \_v i s a r d$ also offers an optional OPC UA interface running on TCP port 4840. The OPC UA server can be activated via a separate license (Section 8.7).
The OPC UA server provides access to parameters and services of all available software modules analogous to the REST-API. To browse the OPC UA Address Space use e.g. the freely available UAExpert GUI client.
The OPC UA server uses the DataTypeDefinition attribute (available in OPC UA version 1.04) for custom datatypes and also uses methods and variable length arrays. Please check if your OPC UA client supports this.
Please contact support@roboception.de if you are interested in using the OPC UA server.
<|end_chunk_1615|><|start_chunk_1616|>
### 7.8 Time synchronization

The $r c \_v i s a r d$ provides timestamps with all images and messages. To compare these with the time on the application host, the time needs to be properly synchronized.

This can be done either via the Network Time Protocol (NTP), which is the default, or the Precision Time Protocol (PTP).

Note: The $r c \_v i s a r d$ does not have a backup battery for its real time clock and hence does not retain time across power cycles. The system time starts at the last saved time (saved on reboot and every 15 minutes) at power up and is then automatically set via NTP if a server can be found.

The current system time as well as time synchronization status can be queried via REST-API (Section 7.3) and seen on the Web GUI's (Section 7.1) System page.

Note: Depending on the reachability of NTP servers or PTP masters it might take up to several minutes until the time is synchronized.
<|end_chunk_1616|><|start_chunk_1617|>
### Page 335<|end_chunk_1617|><|start_chunk_1618|>
 7.8.1 NTP 

The Network Time Protocol (NTP) is a TCP/IP protocol for synchronizing time over a network. A client periodically requests the current time from a server, and uses it to set and correct its own clock.
By default the $r c \_v i s a r d$ tries to reach NTP servers from the NTP Pool Project, which will work if the $r c \_v i s a r d$ has access to the internet.

If the $r c \_v i s a r d$ is configured for $D H C P$ (Section 4.4.2) (which is the default setting), it will also request NTP servers from the DHCP server and try to use those.

Additionally, the user can specify up to three NTP servers manually using the REST-API's /system/ntp endpoint. A more convenient way is setting the NTP servers on the Web GUI's (Section 7.1) System Time page.
<|end_chunk_1618|><|start_chunk_1619|>
### 7.8.2 PTP

The Precision Time Protocol (PTP, also known as IEEE1588) is a protocol which offers more precise and robust clock synchronization than with NTP.
The $r c \_v i s a r d$ can be configured to act as a PTP slave via the standard GigE Vision 2.0/GenICam interface (Section 7.2) using the GevIEEE1588 parameter.

At least one PTP master providing time has to be running in the network. On Linux the respective command for starting a PTP master on ethernet port eth0 is, e.g., sudo ptpd --masteronly --foreground -i eth0.

While the $r c \_v i s a r d$ is synchronized with a PTP master (rc_visard in PTP status SLAVE), the NTP synchronization is paused.
<|end_chunk_1619|><|start_chunk_1620|>
### 7.8.3 Setting time manually

The $r c \_v i s a r d$ allows to set the current date and time manually using the REST-API's/system/time endpoint, if no time synchronization is active (see System and logs, Section 7.3.3.3). A more convenient way is setting the system time on the Web GUI's (Section 7.1) System Time page.
<|end_chunk_1620|><|start_chunk_1621|>
### Page 336<|end_chunk_1621|><|start_chunk_1622|>
 8 Maintenance 

Warning: The customer does not need to open the rc_visard's housing to perform maintenance. Unauthorized opening will void the warranty.
<|end_chunk_1622|><|start_chunk_1623|>
### 8.1 Lens cleaning

Glass lenses with antireflective coating are used to reduce glare. Please take special care when cleaning the lenses. To clean them, use a soft lens-cleaning brush to remove dust or dirt particles. Then use a clean microfiber cloth that is designed to clean lenses, and gently wipe the lens using a circular motion to avoid scratches that may compromise the sensor's performance. For stubborn dirt, high purity isopropanol or a lens cleaning solution formulated for coated lenses (such as the Uvex Clear family of products) may be used.
<|end_chunk_1623|><|start_chunk_1624|>
### 8.2 Camera calibration

The cameras are calibrated during production. Under normal operating conditions, the calibration will be valid for the life time of the sensor. High impact, such as occurring when dropping the $r c \_v i s a r d$, can change the camera's parameters slightly. In this case, calibration can be verified and recalibration undertaken via the Web GUI (see Camera calibration, Section 6.5.3).
<|end_chunk_1624|><|start_chunk_1625|>
### 8.3 Creating and restoring backups of settings

The $r c \_v i s a r d$ offers the possibility to download the current settings as backup or for transferring them to a different $r c \_v i s a r d$ or $r c \_c u b e$.
The current settings of the $r c \_v i s a r d$ can be downloaded on the Web GUI's (Section 7.1) System page in the $r c \_v i s a r d$ Settings section. They can also be downloaded via the $r c \_v i s a r d$ 's REST-API interface (Section 7.3) using the GET / system/backup request.
For downloading a backup, the user can choose which settings to include:

- nodes: the settings of all modules (parameters, preferred orientations and sorting strategies)
- load_carriers: the configured load carriers
- regions_of_interest: the configured 2D and 3D regions of interest
- grippers: the configured grippers (without the CAD elements)

The returned backup should be stored as a .json file.
The templates of the SilhouetteMatch module are not included in the backup but can be downloaded manually using the REST-API or the Web GUI (see Template API, Section 6.4.6.14).
<|end_chunk_1625|><|start_chunk_1626|>
### Page 337
A backup can be restored to the rc_visard on the Web GUI's (Section 7.1) System page in the rc_visard Settings section by uploading the backup .json file. In the Web GUI the settings included in the backup are shown and can be chosen for restore. The corresponding REST-API interface (Section 7.3) call is POST / system/ backup.

Warning: When restoring load carriers, all existing load carriers on the $r c \_v i s a r d$ will get lost and will be replaced by the content of the backup. The same applies to restoring grippers and regions of interest.

When restoring a backup, only the settings which are applicable to the $r c \_v i s a r d$ are restored. Parameters for modules that do not exist on the device or do not have a valid license will be skipped. If a backup can only be restored partially, the user will be notified by warnings.
<|end_chunk_1626|><|start_chunk_1627|>
 8.4 Updating the firmware 

Information about the current firmware image version can be found on the Web GUI's (Section 7.1) System $\rightarrow$ Firmware \& License page. It can also be accessed via the $r c \_v i s a r d$ 's REST-API interface (Section 7.3) using the GET / system request. Users can use either the Web GUI or the REST-API to update the firmware.

Warning: When upgrading from a version prior to 21.07, all of the software modules' configured parameters will be reset to their defaults after a firmware update. Only when upgrading from version 21.07 or higher, the last saved parameters will be preserved. Please make sure these settings are persisted on the application-side or client PC (e.g., using the REST-API interface, Section 7.3) to request all parameters and store them prior to executing the update.
The following settings are excluded from this and will be persisted across a firmware update:

- the $r c \_v i s a r d$ 's network configuration including an optional static IP address and the userspecified device name,
- the latest result of the Hand-eye calibration (Section 6.5.1), i.e., recalibrating the $r c \_v i s a r d$ w.r.t. a robot is not required, unless camera mounting has changed, and
- the latest result of the Camera calibration (Section 6.5.3), i.e., recalibration of the rc_visard's stereo cameras is not required.

Step 1: Download the newest firmware version. Firmware updates will be supplied from of a Mender artifact file identified by its .mender suffix.
If a new firmware update is available for your $r c \_v i s a r d$ device, the respective file can be downloaded to a local computer from https://www.roboception.com/download.

Warning: Make sure the firmware version to upload is still within the software maintenance period of your $r c \_v i s a r d$. You can see the firmware version constraints on the $r c \_v i s a r d$ 's Web GUI on the System $\rightarrow$ Firmware \& License page. If the latest firmware version exceeds the software maintenance period, a new license must be purchased to use a newer firmware.

Step 2: Upload the update file. To update with the $r c \_v i s a r d$ 's REST-API, users may refer to the POST /system/update request.
To update the firmware via the Web GUI, locate the System $\rightarrow$ Firmware \& License page and press the "Upload $r c \_v i s a r d$ Update" button. Select the desired update image file (file extension .mender) from the local file system and open it to start the update.
<|end_chunk_1627|><|start_chunk_1628|>
### Page 338
Depending on the network architecture and configuration, the upload may take several minutes. During the update via the Web GUI, a progress bar indicates the progress of the upload.

Note: Depending on the web browser, the update progress status shown in the progress bar may indicate the completion of the update too early. Please wait until a notification window opens, which indicates the end of the update process. Expect an overall update time of at least five minutes.

Warning: Do not close the web browser tab which contains the Web GUI or press the renew button on this tab, because it will abort the update procedure. In that case, repeat the update procedure from the beginning.

Step 3: Reboot the rc_visard. To apply a firmware update to the $r c \_$visard device, a reboot is required after having uploaded the new image version.

Note: The new image version is uploaded to the inactive partition of the $r c \_v i s a r d$. Only after rebooting will the inactive partition be activated, and the active partition will become inactive. If the updated firmware image cannot be loaded, this partition of the $r c \_v i s a r d$ remains inactive and the previously installed firmware version from the active partition will be used automatically.

As for the REST-API, the reboot can be performed by the PUT /system/reboot request.
After having uploaded the new firmware via the Web GUI, a notification window is opened, which offers to reboot the device immediately or to postpone the reboot. To reboot the $r c \_v i s a r d$ at a later time, use the Reboot button on the Web GUI's System page.
Step 4: Confirm the firmware update. After rebooting the $r c \_v i s a r d$, please check the firmware image version number of the currently active image to make sure that the updated image was successfully loaded. You can do so either via the Web GUI's System $\rightarrow$ Firmware \& License page or via the REST-API's GET / system/update request.
Please contact Roboception in case the firmware update could not be applied successfully.
<|end_chunk_1628|><|start_chunk_1629|>
 8.5 Restoring the previous firmware version 

After a successful firmware update, the previous firmware image is stored on the inactive partition of the $r c \_v i s a r d$ and can be restored in case needed. This procedure is called a rollback.

Note: Using the latest firmware as provided by Roboception is strongly recommended. Hence, rollback functionality should only be used in case of serious issues with the updated firmware version.

Rollback functionality is only accessible via the $r c \_v i s a r d$ 's REST-API interface (Section 7.3) using the PUT / system/rollback request. It can be issued using any HTTP-compatible client or using a web browser as described in Swagger UI (Section 7.3.5). Like the update process, the rollback requires a subsequent device reboot to activate the restored firmware version.
<|end_chunk_1629|><|start_chunk_1630|>
### 8.6 Rebooting the $r c \_v i s a r d$

An $r c \_v i s a r d$ reboot is necessary after updating the firmware or performing a software rollback. It can be issued either programmatically, via the rc_visard's REST-API interface (Section 7.3) using the PUT /system/reboot request, or manually on the Web GUI's (Section 7.1) System page.
The reboot is finished when the LED turns green again.
<|end_chunk_1630|><|start_chunk_1631|>
### Page 339<|end_chunk_1631|><|start_chunk_1632|>
 8.7 Updating the software license 

Licenses that are purchased from Roboception for enabling additional features can be installed via the Web GUI's (Section 7.1) System $\rightarrow$ Firmware \& License page. The rc_visard has to be rebooted to apply the licenses.
<|end_chunk_1632|><|start_chunk_1633|>
### 8.8 Downloading log files

During operation, the $r c \_v i s a r d$ logs important information, warnings, and errors into files. If the $r c \_v i s a r d$ exhibits unexpected or erroneous behavior, the log files can be used to trace its origin. Log messages can be viewed and filtered using the Web GUI's (Section 7.1) System $\rightarrow$ Logs page. If contacting the support (Contact, Section 11), the log files are very useful for tracking possible problems. To download them as a .tar.gz file, click on Download all logs on the Web GUI's System $\rightarrow$ Logs page.
Aside from the Web GUI, the logs are also accessible via the $r c \_v i s a r d$ 's REST-API interface (Section 7.3) using the GET / logs and GET / logs/\{log\} requests.
<|end_chunk_1633|><|start_chunk_1634|>
### Page 340<|end_chunk_1634|><|start_chunk_1635|>
 9 Accessories 
<|end_chunk_1635|><|start_chunk_1636|>
### 9.1 Connectivity kit

Roboception offers an optional connectivity kit to aid customers with setting up the rc_visard. For permanent installation, the customer is responsible for providing a suitable power supply. The connectivity kit consists of a:

- network cable with straight M12 plug to straight RJ45 connector in either $2 \mathrm{~m}, 5 \mathrm{~m}$, or 10 m length,
- power adapter cable with straight M12 socket to DC barrel connector in 30 cm length,
- $24 \mathrm{~V}, 30 \mathrm{~W}$ wall power supply, or a $24 \mathrm{~V}, 60 \mathrm{~W}$ desktop power supply.

Connecting the $r c \_v i s a r d$ to residential or office grid power requires a power supply that meets EN 55011 Class B emission standards. The E2CFS 30W 24V by EGSTON System Electronics Eggenburg GmbH (http://www.egston.com) contained in the connectivity kit is certified accordingly. However, it does not meet immunity standards for industrial environments under EN 61000-6-2.
![img-83.jpeg](img-83.jpeg)

Fig. 9.1: The optional connectivity kit's components
<|end_chunk_1636|><|start_chunk_1637|>
### 9.2 Wiring

Cables are by default not provided with the $r c \_v i s a r d$. It is the customer's responsibility to obtain appropriate parts. The following sections provide an overview of suggested components.
<|end_chunk_1637|><|start_chunk_1638|>
### 9.2.1 Ethernet connections

The $r c \_v i s a r d$ provides an industrial 8-pin A-coded M12 socket connector for Ethernet connectivity. Various cabling solutions can be obtained directly from third party vendors.
CAT5 (1 Gbps) M12 plug to RJ45
<|end_chunk_1638|><|start_chunk_1639|>
### Page 341
- Straight M12 plug to straight RJ45 connector, 10 m length: Phoenix Contact NBC-MS/ 10,0-94B/R4AC SCO, Art.-Nr.: 1407417
- Straight M12 plug to straight RJ45 connector, 10 m length: MURR Electronics Art.-Nr.: 7700-48521-S4W1000
- Angled M12 plug to straight RJ45 connector, 10 m length: MURR Electronics Art.-Nr.: 7700-48551-S4W1000

<|end_chunk_1639|><|start_chunk_1640|>
 9.2.2 Power connections 

An 8-pin A-coded M12 plug connector is provided for power and GPIO connectivity. Various cabling solutions can be obtained from third party vendors. A selection of M12 to open ended cables is provided below. Customers are required to provide power and GPIO connections to the cables according to the pinouts described in Wiring (Section 3.5). The rc_visard's housing must be connected to ground.
<|end_chunk_1640|><|start_chunk_1641|>
## Sensor/Actor cable M12 socket to open end

- Straight M12 socket connector to open end, shielded, 10m length: Phoenix Contact SAC-8P-10,0PUR/M12FS SH, Art.Nr.: 1522891
- Angled M12 socket connector to open end, shielded 10m length: Phoenix Contact SAC-8P-10,0PUR/M12FR SH, Art.Nr.: 1522943

<|end_chunk_1641|><|start_chunk_1642|>
## Sensor/Actor M12 socket for field termination

- Phoenix Contact SACC-M12FS-8CON-PG9-M, Art.Nr.:1513347
- TE Connectivity T4110011081-000 (metal housing)
- TE Connectivity T4110001081-000 (plastic housing)

<|end_chunk_1642|><|start_chunk_1643|>
### 9.2.3 Power supplies

The $r c_{-}$visard is classified as an EN-55011 Class B device and immune to light industrial and industrial environments. For connecting the sensor to residential grid power, a power supply under EN 55011/55022 Class B has to be used.

It is the customer's responsibility to obtain and install a suitable power supply satisfying EN 61000-6-2 for permanent installation in industrial environments. One example that satisfies both EN 61000-6-2 and EN 55011/55022 Class B is the DIN-Rail mounted PULS MiniLine ML60.241 24V/DC 2.5 A by PULS GmbH (http://www.pulspower.com). A certified electrician must perform installation.
Only one $r c_{-}$visard shall be connected to a power supply at any time, and the total length of cables must be less than 30 m .
<|end_chunk_1643|><|start_chunk_1644|>
### 9.3 Spare parts

No user-serviceable spare parts are currently available for $r c_{-}$visard devices.
<|end_chunk_1644|><|start_chunk_1645|>
### Page 342<|end_chunk_1645|><|start_chunk_1646|>
 10 Troubleshooting 
<|end_chunk_1646|><|start_chunk_1647|>
### 10.1 LED colors

During the boot process, the LED will change color several times to indicate stages in the boot process:
Table 10.1: LED color codes

| LED color | Boot stage |
| :-- | :-- |
| white | power supply OK |
| yellow | normal boot process in progress |
| purple |  |
| blue |  |
| green | boot complete, rc_visard ready |

The LED will signal some warning or error states to support the user during troubleshooting.
Table 10.2: LED color trouble codes

| LED color | Warning or error state |
| :-- | :-- |
| off | no power to the sensor |
| brief red flash every 5 seconds | no network connectivity |
| red while sensor appears to function nor- <br> mally | high-temperature warning (case has exceeded 60 <br> $\left.{ }^{\circ} \mathrm{C}\right)$ |
| red while case is below $60^{\circ} \mathrm{C}$ | Some process has terminated and failed to restart. |
<|end_chunk_1647|><|start_chunk_1648|>
### 10.2 Hardware issues
<|end_chunk_1648|><|start_chunk_1649|>
## LED does not illuminate

The $r c \_v i s a r d$ does not start up.

- Ensure that cables are connected and secured properly.
- Ensure that adequate DC voltage ( 18 V to 30 V ) with correct polarity is applied to the power connector at the pins labeled as Power and Ground as described in the device's pin assignment specification (Section 3.6). Connecting the sensor to voltage outside of the specified range, to alternating current, with reversed polarity, or to a supply with voltage spikes will lead to permanent hardware damage.

<|end_chunk_1649|><|start_chunk_1650|>
## LED turns red while the sensor appears to function normally

This may indicate a high housing temperature. The sensor might be mounted in a position that obstructs free airflow around the cooling fins.

- Clean cooling fins and housing.
- Ensure a minimum of 10 cm free space in all directions around cooling fins to provide adequate convective cooling.
<|end_chunk_1650|><|start_chunk_1651|>
### Page 343
- Ensure that ambient temperature is within specified range.

The sensor may slow down processing when cooling is insufficient or the ambient temperature exceeds the specified range.
<|end_chunk_1651|><|start_chunk_1652|>
 Reliability issues and/or mechanical damage 

This may be an indication of ambient conditions (vibration, shock, resonance, and temperature) being outside of specified range. Please refer to the specification of environmental conditions (Section 3.4).

- Operating the rc_visard outside of specified ambient conditions might lead to damage and will void the warranty.

<|end_chunk_1652|><|start_chunk_1653|>
## Electrical shock when touching the sensor

This indicates an electrical fault in sensor, cabling, or power supply or adjacent system.

- Immediately turn off power to the system, disconnect cables, and have a qualified electrician check the setup.
- Ensure that the sensor housing is properly grounded; check for large ground loops.

<|end_chunk_1653|><|start_chunk_1654|>
### 10.3 Connectivity issues
<|end_chunk_1654|><|start_chunk_1655|>
## LED briefly flashes red every 5 seconds

If the LED briefly flashes red every 5 seconds, then the $r c \_v i s a r d$ is not able to detect a network link.

- Check that the network cable is properly connected to the $r c \_v i s a r d$ and the network.
- If no problem is visible, then replace the Ethernet cable.

<|end_chunk_1655|><|start_chunk_1656|>
## A GigE Vision client or rcdiscover-gui cannot detect the camera

- Check whether the rc_visard's LED flashes briefly every 5 seconds (check the cable if it does).
- Ensure that the $r c \_v i s a r d$ is connected to the same subnet (the discovery mechanism uses broadcasts that will not work across different subnets).

<|end_chunk_1656|><|start_chunk_1657|>
## The Web GUI is inaccessible

- Ensure that the $r c \_v i s a r d$ is turned on and connected to the same subnet as the host computer.
- Check whether the $r c \_v i s a r d$ 's LED flashes briefly every 5 seconds (check the cable if it does).
- Check whether rcdiscover-gui detects the sensor. If it reports the $r c \_v i s a r d$ as unreachable, then the $r c \_v i s a r d$ 's network configuration (Section 4.4) is wrong.
- If the $r c \_v i s a r d$ is reported as reachable, try double clicking the entry to open the Web GUI in a browser.
- If this does not work, try entering the $r c \_v i s a r d$ 's reported IP address directly in the browser as target address.

<|end_chunk_1657|><|start_chunk_1658|>
## Too many Web GUIs are open at the same time

The Web GUI consumes the $r c \_v i s a r d$ 's processing resources to compress images to be transmitted and for statistical output that is regularly polled by the browser. Leaving several instances of the Web GUI open on the same or different computers can significantly diminish the $r c \_v i s a r d$ 's performance. The Web GUI is meant for configuration and validation, not to permanently monitor the $r c \_v i s a r d$.
<|end_chunk_1658|><|start_chunk_1659|>
### 10.4 Camera-image issues
<|end_chunk_1659|><|start_chunk_1660|>
## The camera image is too bright

- If the camera is in manual exposure mode, decrease the exposure time, or
<|end_chunk_1660|><|start_chunk_1661|>
### Page 344
- switch to auto-exposure mode.

<|end_chunk_1661|><|start_chunk_1662|>
 The camera image is too dark 

- If the camera is in manual exposure mode, increase the exposure time, or
- switch to auto-exposure mode.

<|end_chunk_1662|><|start_chunk_1663|>
## The camera image is too noisy

Large gain factors cause high-amplitude image noise. To decrease the image noise,

- use an additional light source to increase the scene's light intensity, or
- choose a greater maximal auto-exposure time.

<|end_chunk_1663|><|start_chunk_1664|>
## The camera image is out of focus

- Check whether the object is too close to the lens and increase the distance between the object and the lens if it is.
- Check whether the camera lenses are dirty and clean them if they are.
- If none of the above applies, a severe hardware problem might exist. Please contact support (Section 11).

<|end_chunk_1664|><|start_chunk_1665|>
## The camera image is blurred

Fast motions in combination with long exposure times can cause blur. To reduce motion blur,

- decrease the motion speed of the camera,
- decrease the motion speed of objects in the field of view of the camera, or
- decrease the exposure time of the camera.

<|end_chunk_1665|><|start_chunk_1666|>
## The camera image is fuzzy

- Check whether the lenses are dirty and clean them if so (see Lens cleaning, Section 8.1).
- If none of the above applies, a severe hardware problem might exist. Please contact support (Section 11).

<|end_chunk_1666|><|start_chunk_1667|>
## The camera image frame rate is too low

- Increase the image frame rate.
- The maximal frame rate of the cameras is 25 Hz .

<|end_chunk_1667|><|start_chunk_1668|>
### 10.5 Depth/Disparity, error, and confidence image issues

All these guidelines also apply to error and confidence images, because they correspond directly to the disparity image.
<|end_chunk_1668|><|start_chunk_1669|>
## The disparity image is too sparse or empty

- Check whether the camera images are well exposed and sharp. Follow the instructions in Cameraimage issues (Section 10.4) if applicable.
- Check whether the scene has enough texture and install an external pattern projector if required.
- Decrease the Minimum Distance (Section 6.2.1).
- Increase the Maximum Distance (Section 6.2.1).
- Check whether the object is too close to the cameras. Consider the different depth ranges of the camera variants.
- Decrease the Minimum Confidence (Section 6.2.1).
- Increase the Maximum Depth Error (Section 6.2.1).
<|end_chunk_1669|><|start_chunk_1670|>
### Page 345
- Choose a lesser Disparity Image Quality (Section 6.2.1). Lower resolution disparity images are generally less sparse.
- Check the cameras' calibration and recalibrate if required (see Camera calibration, Section 6.5.3).

<|end_chunk_1670|><|start_chunk_1671|>
 The disparity images' frame rate is too low 

- Check and increase the frame rate of the camera images. The frame rate of the disparity image cannot be greater than the frame rate of the camera images.
- Choose a lesser Disparity Image Quality (Section 6.2.1).
- Increase the Minimum Distance (Section 6.2.1) as much as possible for the application.

<|end_chunk_1671|><|start_chunk_1672|>
## The disparity image does not show close objects

- Check whether the object is too close to the cameras. Consider the depth ranges of the camera variants.
- Decrease the Minimum Distance (Section 6.2.1).

<|end_chunk_1672|><|start_chunk_1673|>
## The disparity image does not show distant objects

- Increase the Maximum Distance (Section 6.2.1).
- Increase the Maximum Depth Error (Section 6.2.1).
- Decrease the Minimum Confidence (Section 6.2.1).

<|end_chunk_1673|><|start_chunk_1674|>
## The disparity image is too noisy

- Increase the Segmentation value (Section 6.2.1).
- Increase the Fill-In value (Section 6.2.1).

<|end_chunk_1674|><|start_chunk_1675|>
## The disparity values or the resulting depth values are too inaccurate

- Decrease the distance between the camera and the scene. Depth-measurement error grows quadratically with the distance from the cameras.
- Check whether the scene contains repetitive patterns and remove them if it does. They could cause wrong disparity measurements.

<|end_chunk_1675|><|start_chunk_1676|>
## The disparity image is too smooth

- Decrease the Fill-In value (Section 6.2.1).

<|end_chunk_1676|><|start_chunk_1677|>
## The disparity image does not show small structures

- Decrease the Segmentation value (Section 6.2.1).
- Decrease the Fill-In value (Section 6.2.1).

<|end_chunk_1677|><|start_chunk_1678|>
### 10.6 Dynamics issues
<|end_chunk_1678|><|start_chunk_1679|>
## State estimates are unavailable

- Check in the Web GUI that pose estimation has been switched on (see Parameters, Section 6.3.2.1).
- Check in the Web GUI that the update rate is about 200 Hz .
- Check the Logs in the Web GUI for errors.

<|end_chunk_1679|><|start_chunk_1680|>
## The state estimates are too noisy

- Adapt the parameters for visual odometry as described in Parameters (Section 6.3.2.1).
- Check whether the camera pose stream has enough accuracy.

<|end_chunk_1680|><|start_chunk_1681|>
## Pose estimation has jumps
<|end_chunk_1681|><|start_chunk_1682|>
### Page 346
- Has the SLAM module been turned on? SLAM can cause jumps when reducing errors due to a loop closure.
- Adapt the parameters for visual odometry as described in Parameters (Section 6.3.2.1).

<|end_chunk_1682|><|start_chunk_1683|>
 Pose frequency is too low 

- Use the real-time pose stream with a 200 Hz update rate. See Stereo INS (Section 6.3.3).

<|end_chunk_1683|><|start_chunk_1684|>
## Delay/Latency of pose is too great

- Use the real-time pose stream. See Stereo INS (Section 6.3.3).

<|end_chunk_1684|><|start_chunk_1685|>
## 10.7 GigE Vision/GenICam issues
<|end_chunk_1685|><|start_chunk_1686|>
## No images

- Check that the modules are enabled. See ComponentSelector and ComponentEnable in Important GenICam parameters (Section 7.2.2).
<|end_chunk_1686|><|start_chunk_1687|>
### Page 347<|end_chunk_1687|><|start_chunk_1688|>
 11 Contact 
<|end_chunk_1688|><|start_chunk_1689|>
### 11.1 Support

For support issues, please see http://www.roboception.com/support or contact support@roboception.de.
<|end_chunk_1689|><|start_chunk_1690|>
### 11.2 Downloads

Software SDKs, etc. can be downloaded from http://www.roboception.com/download.
<|end_chunk_1690|><|start_chunk_1691|>
### 11.3 Address

Roboception GmbH
Kaflerstrasse 2
81241 Munich
Germany

Web: http://www.roboception.com
Email: info@roboception.de
Phone: +49 8988950 79-0
<|end_chunk_1691|><|start_chunk_1692|>
### Page 348<|end_chunk_1692|><|start_chunk_1693|>
 12 Appendix 
<|end_chunk_1693|><|start_chunk_1694|>
### 12.1 Pose formats

A pose consists of a translation and rotation. The translation defines the shift along the $x, y$ and $z$ axes. The rotation can be defined in many different ways. The $r c_{-}$visard uses quaternions to define rotations and translations are given in meters. This is called the XYZ+quaternion format. This chapter explains the conversion between different common conventions and the XYZ+quaternion format.

It is quite common to define rotations in 3D by three angles that define rotations around the three coordinate axes. Unfortunately, there are many different ways to do that. The most common conventions are Euler and Cardan angles (also called Tait-Bryan angles). In both conventions, the rotations can be applied to the previously rotated axis (intrinsic rotation) or to the axis of a fixed coordinate system (extrinsic rotation).

We use $x, y$ and $z$ to denote the three coordinate axes. $x^{\prime}, y^{\prime}$ and $z^{\prime}$ refer to the axes that have been rotated one time. Similarly, $x^{\prime \prime}, y^{\prime \prime}$ and $z^{\prime \prime}$ are the axes after two rotations.

In the (original) Euler angle convention, the first and the third axis are always the same. The rotation order $z-x^{\prime}-z^{\prime \prime}$ means rotating around the $z$-axis, then around the already rotated $x$-axis and finally around the (two times) rotated $z$-axis. In the Cardan angle convention, three different rotation axes are used, e.g. $z-y^{\prime}-x^{\prime \prime}$. Cardan angles are often also just called Euler angles.

For each intrinsic rotation order, there is an equivalent extrinsic rotation order, which is inverted, e.g. the intrinsic rotation order $z-y^{\prime}-x^{\prime \prime}$ is equivalent to the extrinsic rotation order $x-y-z$.
Rotations around the $x, y$ and $z$ axes can be defined by quaternions as

$$
r_{x}(\alpha)=\left(\begin{array}{c}
\sin \frac{\alpha}{2} \\
0 \\
0 \\
\cos \frac{\alpha}{2}
\end{array}\right), \quad r_{y}(\beta)=\left(\begin{array}{c}
0 \\
\sin \frac{\beta}{2} \\
0 \\
\cos \frac{\beta}{2}
\end{array}\right), \quad r_{z}(\gamma)=\left(\begin{array}{c}
0 \\
0 \\
\sin \frac{\gamma}{2} \\
\cos \frac{\gamma}{2}
\end{array}\right)
$$

or by rotation matrices as

$$
\begin{aligned}
& r_{x}(\alpha)=\left(\begin{array}{cccc}
1 & 0 & 0 \\
0 & \cos \alpha & -\sin \alpha \\
0 & \sin \alpha & \cos \alpha
\end{array}\right) \\
& r_{y}(\beta)=\left(\begin{array}{ccc}
\cos \beta & 0 & \sin \beta \\
0 & 1 & 0 \\
-\sin \beta & 0 & \cos \beta
\end{array}\right) \\
& r_{z}(\gamma)=\left(\begin{array}{ccc}
\cos \gamma & -\sin \gamma & 0 \\
\sin \gamma & \cos \gamma & 0 \\
0 & 0 & 1
\end{array}\right)
\end{aligned}
$$

The extrinsic rotation order $x-y-z$ can be computed by multiplying the individual rotations in inverse order, i.e. $r_{z}(\gamma) r_{y}(\beta) r_{x}(\alpha)$.
Based on these definitions, the following sections explain the conversion between common conventions and the XYZ+quaternion format.
<|end_chunk_1694|><|start_chunk_1695|>
### Page 349
Note: Please be aware of units for positions and orientations. rc_visard devices always specify positions in meters, while most robot manufacturers use millimeters or inches. Angles are typically specified in degrees, but may sometimes also be given in radians.
<|end_chunk_1695|><|start_chunk_1696|>
 12.1.1 Rotation matrix and translation vector 

A pose can also be defined by a rotation matrix $R$ and a translation vector $T$.

$$
R=\left(\begin{array}{lll}
r_{00} & r_{01} & r_{02} \\
r_{10} & r_{11} & r_{12} \\
r_{20} & r_{21} & r_{22}
\end{array}\right), \quad T=\left(\begin{array}{c}
X \\
Y \\
Z
\end{array}\right)
$$

The pose transformation can be applied to a point $P$ by

$$
P^{\prime}=R P+T
$$
<|end_chunk_1696|><|start_chunk_1697|>
### 12.1.1.1 Conversion from rotation matrix to quaternion

The conversion from a rotation matrix (with $\operatorname{det}(R)=1$ ) to a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ can be done as follows.

$$
\begin{aligned}
& x=\operatorname{sign}\left(r_{21}-r_{12}\right) \frac{1}{2} \sqrt{\max \left(0,1+r_{00}-r_{11}-r_{22}\right)} \\
& y=\operatorname{sign}\left(r_{02}-r_{20}\right) \frac{1}{2} \sqrt{\max \left(0,1-r_{00}+r_{11}-r_{22}\right)} \\
& z=\operatorname{sign}\left(r_{10}-r_{01}\right) \frac{1}{2} \sqrt{\max \left(0,1-r_{00}-r_{11}+r_{22}\right)} \\
& w=\frac{1}{2} \sqrt{\max \left(0,1+r_{00}+r_{11}+r_{22}\right)}
\end{aligned}
$$

The sign operator returns -1 if the argument is negative. Otherwise, 1 is returned. It is used to recover the sign for the square root. The max function ensures that the argument of the square root function is not negative, which can happen in practice due to round-off errors.
<|end_chunk_1697|><|start_chunk_1698|>
### 12.1.1.2 Conversion from quaternion to rotation matrix

The conversion from a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ with $\|q\|=1$ to a rotation matrix can be done as follows.

$$
R=2\left(\begin{array}{ccc}
\frac{1}{2}-y^{2}-z^{2} & x y-z w & x z+y w \\
x y+z w & \frac{1}{2}-x^{2}-z^{2} & y z-x w \\
x z-y w & y z+x w & \frac{1}{2}-x^{2}-y^{2}
\end{array}\right)
$$
<|end_chunk_1698|><|start_chunk_1699|>
### 12.1.2 ABB pose format

ABB robots use a position and a quaternion for describing a pose, like $r c \_v i s a r d$ devices. There is no conversion of the orientation needed.
<|end_chunk_1699|><|start_chunk_1700|>
### 12.1.3 FANUC XYZ-WPR format

The pose format that is used by FANUC robots consists of a position $X Y Z$ in millimeters and an orientation $W P R$ that is given by three angles in degrees, with $W$ rotating around $x$-axis, $P$ rotating around $y$-axis and $R$ rotating around $z$-axis. The rotation order is $x-y-z$ and computed by $r_{z}(R) r_{y}(P) r_{x}(W)$.
<|end_chunk_1700|><|start_chunk_1701|>
### Page 350<|end_chunk_1701|><|start_chunk_1702|>
 12.1.3.1 Conversion from FANUC-WPR to quaternion 

The conversion from the $W P R$ angles in degrees to a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ can be done by first converting all angles to radians

$$
\begin{aligned}
W_{r} & =W \frac{\pi}{180} \\
P_{r} & =P \frac{\pi}{180} \\
R_{r} & =R \frac{\pi}{180}
\end{aligned}
$$

and then calculating the quaternion with

$$
\begin{aligned}
& x=\cos \left(R_{r} / 2\right) \cos \left(P_{r} / 2\right) \sin \left(W_{r} / 2\right)-\sin \left(R_{r} / 2\right) \sin \left(P_{r} / 2\right) \cos \left(W_{r} / 2\right) \\
& y=\cos \left(R_{r} / 2\right) \sin \left(P_{r} / 2\right) \cos \left(W_{r} / 2\right)+\sin \left(R_{r} / 2\right) \cos \left(P_{r} / 2\right) \sin \left(W_{r} / 2\right) \\
& z=\sin \left(R_{r} / 2\right) \cos \left(P_{r} / 2\right) \cos \left(W_{r} / 2\right)-\cos \left(R_{r} / 2\right) \sin \left(P_{r} / 2\right) \sin \left(W_{r} / 2\right) \\
& w=\cos \left(R_{r} / 2\right) \cos \left(P_{r} / 2\right) \cos \left(W_{r} / 2\right)+\sin \left(R_{r} / 2\right) \sin \left(P_{r} / 2\right) \sin \left(W_{r} / 2\right)
\end{aligned}
$$
<|end_chunk_1702|><|start_chunk_1703|>
### 12.1.3.2 Conversion from quaternion to FANUC-WPR

The conversion from a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ with $\|q\|=1$ to the $W P R$ angles in degrees can be done as follows.

$$
\begin{aligned}
R & =\operatorname{atan}_{2}\left(2\left(w z+x y\right), 1-2\left(y^{2}+z^{2}\right)\right) \frac{180}{\pi} \\
P & =\operatorname{asin}(2(w y-z x)) \frac{180}{\pi} \\
W & =\operatorname{atan}_{2}\left(2\left(w x+y z\right), 1-2\left(x^{2}+y^{2}\right)\right) \frac{180}{\pi}
\end{aligned}
$$
<|end_chunk_1703|><|start_chunk_1704|>
### 12.1.4 Franka Emika Pose Format

Franka Emika robots use a transformation matrix $T$ to define a pose. A transformation matrix combines a rotation matrix $R$ and a translation vector $t=\left(\begin{array}{llll}x & y & z\end{array}\right)^{T}$.

$$
T=\left(\begin{array}{cccc}
r_{00} & r_{01} & r_{02} & x \\
r_{10} & r_{11} & r_{12} & y \\
r_{20} & r_{21} & r_{22} & z \\
0 & 0 & 0 & 1
\end{array}\right)
$$

The pose given by Franka Emika's "Measure Pose" App consists of a translation $x, y, z$ in millimeters and a rotation $x, y, z$ in degrees. The rotation convention is $z-y^{\prime}-x^{\prime \prime}$ (i.e. $x-y-z$ ) and is computed by $r_{z}(z) r_{y}(y) r_{x}(x)$
<|end_chunk_1704|><|start_chunk_1705|>
### 12.1.4.1 Conversion from transformation matrix to quaternion

The conversion from a rotation matrix (with $\operatorname{det}(R)=1$ ) to a quaternion $q=\left(\begin{array}{llll}q_{x} & q_{y} & q_{z} & q_{w}\end{array}\right)$ can be done as follows:

$$
\begin{aligned}
& q_{x}=\operatorname{sign}\left(r_{21}-r_{12}\right) \frac{1}{2} \sqrt{\max \left(0,1+r_{00}-r_{11}-r_{22}\right)} \\
& q_{y}=\operatorname{sign}\left(r_{02}-r_{20}\right) \frac{1}{2} \sqrt{\max \left(0,1-r_{00}+r_{11}-r_{22}\right)} \\
& q_{z}=\operatorname{sign}\left(r_{10}-r_{01}\right) \frac{1}{2} \sqrt{\max \left(0,1-r_{00}-r_{11}+r_{22}\right)} \\
& q_{w}=\frac{1}{2} \sqrt{\max \left(0,1+r_{00}+r_{11}+r_{22}\right)}
\end{aligned}
$$
<|end_chunk_1705|><|start_chunk_1706|>
### Page 351
The sign operator returns -1 if the argument is negative. Otherwise, 1 is returned. It is used to recover the sign for the square root. The max function ensures that the argument of the square root function is not negative, which can happen in practice due to round-off errors.
<|end_chunk_1706|><|start_chunk_1707|>
 12.1.4.2 Conversion from Rotation-XYZ to quaternion 

The conversion from the $x, y, z$ angles in degrees to a quaternion $q=\left(\begin{array}{llll}q_{x} & q_{y} & q_{z} & q_{w}\end{array}\right)$ can be done by first converting all angles to radians

$$
\begin{aligned}
X_{r} & =x \frac{\pi}{180} \\
Y_{r} & =y \frac{\pi}{180} \\
Z_{r} & =z \frac{\pi}{180}
\end{aligned}
$$

and then calculating the quaternion with

$$
\begin{aligned}
& q_{x}=\cos \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right)-\sin \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right) \\
& q_{y}=\cos \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right)+\sin \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right) \\
& q_{z}=\sin \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right)-\cos \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right) \\
& q_{w}=\cos \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right)+\sin \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right)
\end{aligned}
$$
<|end_chunk_1707|><|start_chunk_1708|>
### 12.1.4.3 Conversion from quaternion and translation to transformation

The conversion from a quaternion $q=\left(\begin{array}{llll}q_{x} & q_{y} & q_{z} & q_{w}\end{array}\right)$ and a translation vector $t=\left(\begin{array}{llll}x & y & z\end{array}\right)^{T}$ to a transformation matrix $T$ can be done as follows:

$$
T=\left(\begin{array}{cccc}
1-2 s\left(q_{y}^{2}+q_{z}^{2}\right) & 2 s\left(q_{x} q_{y}-q_{z} q_{w}\right) & 2 s\left(q_{x} q_{z}+q_{y} q_{w}\right) & x \\
2 s\left(q_{x} q_{y}+q_{z} q_{w}\right) & 1-2 s\left(q_{x}^{2}+q_{z}^{2}\right) & 2 s\left(q_{y} q_{z}-q_{x} q_{w}\right) & y \\
2 s\left(q_{x} q_{z}-q_{y} q_{w}\right) & 2 s\left(q_{y} q_{z}+q_{x} q_{w}\right) & 1-2 s\left(q_{x}^{2}+q_{y}^{2}\right) & z \\
0 & 0 & 0 & 1
\end{array}\right)
$$

where $s=\|q\|^{-2}=\frac{1}{q_{x}^{2}+q_{y}^{2}+q_{z}^{2}+q_{w}^{2}}$ and $s=1$ if $q$ is a unit quaternion.
<|end_chunk_1708|><|start_chunk_1709|>
### 12.1.4.4 Conversion from quaternion to Rotation-XYZ

The conversion from a quaternion $q=\left(\begin{array}{llll}q_{x} & q_{y} & q_{z} & q_{w}\end{array}\right)$ with $\|q\|=1$ to the $x, y, z$ angles in degrees can be done as follows.

$$
\begin{aligned}
& x=\operatorname{atan}_{2}\left(2\left(q_{w} q_{z}+q_{x} q_{y}\right), 1-2\left(q_{y}^{2}+q_{z}^{2}\right)\right) \frac{180}{\pi} \\
& y=\operatorname{asin}\left(2\left(q_{w} q_{y}-q_{z} q_{x}\right)\right) \frac{180}{\pi} \\
& z=\operatorname{atan}_{2}\left(2\left(q_{w} q_{x}+q_{y} q_{z}\right), 1-2\left(q_{x}^{2}+q_{y}^{2}\right)\right) \frac{180}{\pi}
\end{aligned}
$$
<|end_chunk_1709|><|start_chunk_1710|>
### 12.1.4.5 Pose representation in RaceCom messages and state machines

In RaceCom messages and in state machines a pose is usually defined as one-dimensional array of 16 float values, representing the transformation matrix in column-major order. The indices of the matrix entries below correspond to the array indices

$$
T=\left(\begin{array}{cccc}
a_{0} & a_{4} & a_{8} & a_{12} \\
a_{1} & a_{5} & a_{9} & a_{13} \\
a_{2} & a_{6} & a_{10} & a_{14} \\
a_{3} & a_{7} & a_{11} & a_{15}
\end{array}\right)
$$
<|end_chunk_1710|><|start_chunk_1711|>
### Page 352<|end_chunk_1711|><|start_chunk_1712|>
 12.1.5 Fruitcore HORST pose format 

Fruitcore HORST robots use a position in meters and a quaternion with $q_{0}=w, q_{1}=x, q_{2}=y$ and $q_{3}=z$ for describing a pose, like rc_visard devices. There is no conversion needed.
<|end_chunk_1712|><|start_chunk_1713|>
### 12.1.6 Kawasaki XYZ-OAT format

The pose format that is used by Kawasaki robots consists of a position $X Y Z$ in millimeters and an orientation $O A T$ that is given by three angles in degrees, with $O$ rotating around $z$ axis, $A$ rotating around the rotated $y$ axis and $T$ rotating around the rotated $z$ axis. The rotation convention is $z-y^{\prime}-z^{\prime \prime}$ (i.e. $z-y-z$ ) and computed by $r_{z}(O) r_{y}(A) r_{z}(T)$.
<|end_chunk_1713|><|start_chunk_1714|>
### 12.1.6.1 Conversion from Kawasaki-OAT to quaternion

The conversion from the $O A T$ angles in degrees to a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ can be done by first converting all angles to radians

$$
\begin{aligned}
O_{r} & =O \frac{\pi}{180} \\
A_{r} & =A \frac{\pi}{180} \\
T_{r} & =T \frac{\pi}{180}
\end{aligned}
$$

and then calculating the quaternion with

$$
\begin{aligned}
& x=\cos \left(O_{r} / 2\right) \sin \left(A_{r} / 2\right) \sin \left(T_{r} / 2\right)-\sin \left(O_{r} / 2\right) \sin \left(A_{r} / 2\right) \cos \left(T_{r} / 2\right) \\
& y=\cos \left(O_{r} / 2\right) \sin \left(A_{r} / 2\right) \cos \left(T_{r} / 2\right)+\sin \left(O_{r} / 2\right) \sin \left(A_{r} / 2\right) \sin \left(T_{r} / 2\right) \\
& z=\sin \left(O_{r} / 2\right) \cos \left(A_{r} / 2\right) \cos \left(T_{r} / 2\right)+\cos \left(O_{r} / 2\right) \cos \left(A_{r} / 2\right) \sin \left(T_{r} / 2\right) \\
& w=\cos \left(O_{r} / 2\right) \cos \left(A_{r} / 2\right) \cos \left(T_{r} / 2\right)-\sin \left(O_{r} / 2\right) \cos \left(A_{r} / 2\right) \sin \left(T_{r} / 2\right)
\end{aligned}
$$
<|end_chunk_1714|><|start_chunk_1715|>
### 12.1.6.2 Conversion from quaternion to Kawasaki-OAT

The conversion from a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ with $\|q\|=1$ to the $O A T$ angles in degrees can be done as follows.

If $x=0$ and $y=0$ the conversion is

$$
\begin{aligned}
& O=\operatorname{atan}_{2}(2(z-w), 2(z+w)) \frac{180}{\pi} \\
& A=\operatorname{acos}\left(w^{2}+z^{2}\right) \frac{180}{\pi} \\
& T=\operatorname{atan}_{2}(2(z+w), 2(w-z)) \frac{180}{\pi}
\end{aligned}
$$

If $z=0$ and $w=0$ the conversion is

$$
\begin{aligned}
& O=\operatorname{atan}_{2}(2(y-x), 2(x+y)) \frac{180}{\pi} \\
& A=\operatorname{acos}(-1.0) \frac{180}{\pi} \\
& T=\operatorname{atan}_{2}(2(y+x), 2(y-x)) \frac{180}{\pi}
\end{aligned}
$$
<|end_chunk_1715|><|start_chunk_1716|>
### Page 353
In all other cases the conversion is

$$
\begin{aligned}
& O=\operatorname{atan}_{2}(2(y z-w x), 2(x z+w y)) \frac{180}{\pi} \\
& A=\operatorname{acos}\left(w^{2}-x^{2}-y^{2}+z^{2}\right) \frac{180}{\pi} \\
& T=\operatorname{atan}_{2}(2(y z+w x), 2(w y-x z)) \frac{180}{\pi}
\end{aligned}
$$
<|end_chunk_1716|><|start_chunk_1717|>
 12.1.7 KUKA XYZ-ABC format 

KUKA robots use the so called XYZ-ABC format. $X Y Z$ is the position in millimeters. $A B C$ are angles in degrees, with $A$ rotating around $z$ axis, $B$ rotating around $y$ axis and $C$ rotating around $x$ axis. The rotation convention is $z-y^{\prime}-x^{\prime \prime}$ (i.e. $x-y-z$ ) and computed by $r_{z}(A) r_{y}(B) r_{x}(C)$.
<|end_chunk_1717|><|start_chunk_1718|>
### 12.1.7.1 Conversion from KUKA-ABC to quaternion

The conversion from the $A B C$ angles in degrees to a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ can be done by first converting all angles to radians

$$
\begin{aligned}
& A_{r}=A \frac{\pi}{180} \\
& B_{r}=B \frac{\pi}{180} \\
& C_{r}=C \frac{\pi}{180}
\end{aligned}
$$

and then calculating the quaternion with

$$
\begin{aligned}
& x=\cos \left(A_{r} / 2\right) \cos \left(B_{r} / 2\right) \sin \left(C_{r} / 2\right)-\sin \left(A_{r} / 2\right) \sin \left(B_{r} / 2\right) \cos \left(C_{r} / 2\right) \\
& y=\cos \left(A_{r} / 2\right) \sin \left(B_{r} / 2\right) \cos \left(C_{r} / 2\right)+\sin \left(A_{r} / 2\right) \cos \left(B_{r} / 2\right) \sin \left(C_{r} / 2\right) \\
& z=\sin \left(A_{r} / 2\right) \cos \left(B_{r} / 2\right) \cos \left(C_{r} / 2\right)-\cos \left(A_{r} / 2\right) \sin \left(B_{r} / 2\right) \sin \left(C_{r} / 2\right) \\
& w=\cos \left(A_{r} / 2\right) \cos \left(B_{r} / 2\right) \cos \left(C_{r} / 2\right)+\sin \left(A_{r} / 2\right) \sin \left(B_{r} / 2\right) \sin \left(C_{r} / 2\right)
\end{aligned}
$$
<|end_chunk_1718|><|start_chunk_1719|>
### 12.1.7.2 Conversion from quaternion to KUKA-ABC

The conversion from a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ with $\|q\|=1$ to the $A B C$ angles in degrees can be done as follows.

$$
\begin{aligned}
& A=\operatorname{atan}_{2}\left(2(w z+x y), 1-2\left(y^{2}+z^{2}\right)\right) \frac{180}{\pi} \\
& B=\operatorname{asin}(2(w y-z x)) \frac{180}{\pi} \\
& C=\operatorname{atan}_{2}\left(2(w x+y z), 1-2\left(x^{2}+y^{2}\right)\right) \frac{180}{\pi}
\end{aligned}
$$
<|end_chunk_1719|><|start_chunk_1720|>
### 12.1.8 Mitsubishi XYZ-ABC format

The pose format that is used by Mitsubishi robots is the same as that for KUKA robots (see KUKA XYZ-ABC format, Section 12.1.7), except that $A$ is a rotation around $x$ axis and $C$ is a rotation around $z$ axis. Thus, the rotation is computed by $r_{z}(C) r_{y}(B) r_{x}(A)$.
<|end_chunk_1720|><|start_chunk_1721|>
### Page 354<|end_chunk_1721|><|start_chunk_1722|>
 12.1.8.1 Conversion from Mitsubishi-ABC to quaternion 

The conversion from the $A B C$ angles in degrees to a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ can be done by first converting all angles to radians

$$
\begin{aligned}
& A_{r}=A \frac{\pi}{180} \\
& B_{r}=B \frac{\pi}{180} \\
& C_{r}=C \frac{\pi}{180}
\end{aligned}
$$

and then calculating the quaternion with

$$
\begin{aligned}
& x=\cos \left(C_{r} / 2\right) \cos \left(B_{r} / 2\right) \sin \left(A_{r} / 2\right)-\sin \left(C_{r} / 2\right) \sin \left(B_{r} / 2\right) \cos \left(A_{r} / 2\right) \\
& y=\cos \left(C_{r} / 2\right) \sin \left(B_{r} / 2\right) \cos \left(A_{r} / 2\right)+\sin \left(C_{r} / 2\right) \cos \left(B_{r} / 2\right) \sin \left(A_{r} / 2\right) \\
& z=\sin \left(C_{r} / 2\right) \cos \left(B_{r} / 2\right) \cos \left(A_{r} / 2\right)-\cos \left(C_{r} / 2\right) \sin \left(B_{r} / 2\right) \sin \left(A_{r} / 2\right) \\
& w=\cos \left(C_{r} / 2\right) \cos \left(B_{r} / 2\right) \cos \left(A_{r} / 2\right)+\sin \left(C_{r} / 2\right) \sin \left(B_{r} / 2\right) \sin \left(A_{r} / 2\right)
\end{aligned}
$$
<|end_chunk_1722|><|start_chunk_1723|>
### 12.1.8.2 Conversion from quaternion to Mitsubishi-ABC

The conversion from a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ with $\|q\|=1$ to the $A B C$ angles in degrees can be done as follows.

$$
\begin{aligned}
& A=\operatorname{atan}_{2}\left(2(w x+y z), 1-2\left(x^{2}+y^{2}\right)\right) \frac{180}{\pi} \\
& B=\operatorname{asin}(2(w y-z x)) \frac{180}{\pi} \\
& C=\operatorname{atan}_{2}\left(2(w z+x y), 1-2\left(y^{2}+z^{2}\right)\right) \frac{180}{\pi}
\end{aligned}
$$
<|end_chunk_1723|><|start_chunk_1724|>
### 12.1.9 Universal Robots pose format

The pose format that is used by Universal Robots consists of a position $X Y Z$ in millimeters and an orientation in angle-axis format $V=\left(\begin{array}{llll}R X & R Y & R Z\end{array}\right)^{T}$. The rotation angle $\theta$ in radians is the length of the rotation axis $U$.

$$
V=\left(\begin{array}{c}
R X \\
R Y \\
R Z
\end{array}\right)=\left(\begin{array}{c}
\theta u_{x} \\
\theta u_{y} \\
\theta u_{z}
\end{array}\right)
$$

$V$ is called a rotation vector.
<|end_chunk_1724|><|start_chunk_1725|>
### 12.1.9.1 Conversion from angle-axis format to quaternion

The conversion from a rotation vector $V$ to a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ can be done as follows.
We first recover the angle $\theta$ in radians from the rotation vector $V$ by

$$
\theta=\sqrt{R X^{2}+R Y^{2}+R Z^{2}}
$$
<|end_chunk_1725|><|start_chunk_1726|>
### Page 355
If $\theta=0$, then the quaternion is $q=\left(\begin{array}{llll}0 & 0 & 0 & 1\end{array}\right)$, otherwise it is

$$
\begin{gathered}
x=R X \frac{\sin (\theta / 2)}{\theta} \\
y=R Y \frac{\sin (\theta / 2)}{\theta} \\
z=R Z \frac{\sin (\theta / 2)}{\theta} \\
w=\cos (\theta / 2)
\end{gathered}
$$
<|end_chunk_1726|><|start_chunk_1727|>
 12.1.9.2 Conversion from quaternion to angle-axis format 

The conversion from a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ with $\|q\|=1$ to a rotation vector in angle-axis form can be done as follows.

We first recover the angle $\theta$ in radians from the quaternion by

$$
\theta=2 \cdot \operatorname{acos}(w)
$$

If $\theta=0$, then the rotation vector is $V=\left(\begin{array}{llll}0 & 0 & 0\end{array}\right)^{T}$, otherwise it is

$$
\begin{aligned}
& R X=\theta \frac{x}{\sqrt{1-w^{2}}} \\
& R Y=\theta \frac{y}{\sqrt{1-w^{2}}} \\
& R Z=\theta \frac{z}{\sqrt{1-w^{2}}}
\end{aligned}
$$
<|end_chunk_1727|><|start_chunk_1728|>
### 12.1.10 Yaskawa Pose Format

The pose format that is used by Yaskawa robots consists of a position $X Y Z$ in millimeters and an orientation that is given by three angles in degrees, with $R x$ rotating around $x$-axis, $R y$ rotating around $y$-axis and $R z$ rotating around $z$-axis. The rotation order is $x-y-z$ and computed by $r_{z}(R z) r_{y}(R y) r_{x}(R x)$.
<|end_chunk_1728|><|start_chunk_1729|>
### 12.1.10.1 Conversion from Yaskawa Rx, Ry, Rz to quaternion

The conversion from the $R x, R y, R z$ angles in degrees to a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ can be done by first converting all angles to radians

$$
\begin{aligned}
X_{r} & =R x \frac{\pi}{180} \\
Y_{r} & =R y \frac{\pi}{180} \\
Z_{r} & =R z \frac{\pi}{180}
\end{aligned}
$$

and then calculating the quaternion with

$$
\begin{aligned}
& x=\cos \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right)-\sin \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right) \\
& y=\cos \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right)+\sin \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right) \\
& z=\sin \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right)-\cos \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right) \\
& w=\cos \left(Z_{r} / 2\right) \cos \left(Y_{r} / 2\right) \cos \left(X_{r} / 2\right)+\sin \left(Z_{r} / 2\right) \sin \left(Y_{r} / 2\right) \sin \left(X_{r} / 2\right)
\end{aligned}
$$
<|end_chunk_1729|><|start_chunk_1730|>
### Page 356<|end_chunk_1730|><|start_chunk_1731|>
 12.1.10.2 Conversion from quaternion to Yaskawa Rx, Ry, Rz 

The conversion from a quaternion $q=\left(\begin{array}{llll}x & y & z & w\end{array}\right)$ with $\|q\|=1$ to the $R x, R y, R z$ angles in degrees can be done as follows.

$$
\begin{aligned}
& R x=\operatorname{atan}_{2}\left(2(w x+y z), 1-2\left(x^{2}+y^{2}\right)\right) \frac{180}{\pi} \\
& R y=\operatorname{asin}(2(w y-z x)) \frac{180}{\pi} \\
& R z=\operatorname{atan}_{2}\left(2(w z+x y), 1-2\left(y^{2}+z^{2}\right)\right) \frac{180}{\pi}
\end{aligned}
$$
<|end_chunk_1731|><|start_chunk_1732|>
### Page 357<|end_chunk_1732|><|start_chunk_1733|>
 HTTP Routing Table 

/cad
GET /cad/gripper_elements, 251
GET /cad/gripper_elements/\{id\}, 252
PUT /cad/gripper_elements/\{id\}, 252
DELETE /cad/gripper_elements/\{id\}, 253
<|end_chunk_1733|><|start_chunk_1734|>
## /datastreams

GET /datastreams, 285
GET /datastreams/\{stream\}, 286
PUT /datastreams/\{stream\}, 287
DELETE /datastreams/\{stream\}, 287
<|end_chunk_1734|><|start_chunk_1735|>
## /logs

GET /logs, 288
GET /logs/\{log\}, 289
<|end_chunk_1735|><|start_chunk_1736|>
## /nodes

GET /nodes, 271
GET /nodes/\{node\}, 272
GET /nodes/\{node\}/services, 272
GET /nodes/\{node\}/services/\{service\}, 273
GET /nodes/\{node\}/status, 274
PUT /nodes/\{node\}/services/\{service\}, 274
<|end_chunk_1736|><|start_chunk_1737|>
## /pipelines

GET /pipelines/\{pipeline\}/nodes, 275
GET /pipelines/\{pipeline\}/nodes/\{node\}, 276
GET /pipelines/\{pipeline\}/nodes/\{node\}/parameter 277
GET /pipelines/\{pipeline\}/nodes/\{node\}/parameter 279
GET /pipelines/\{pipeline\}/nodes/\{node\}/services, 281
GET /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\}, 282
GET /pipelines/\{pipeline\}/nodes/\{node\}/status, 284
PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters, 278
PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters/\{param\}, 280
PUT /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\}, 283
<|end_chunk_1737|><|start_chunk_1738|>
## /system

GET /system, 290
GET /system/backup, 292

```
GET /system/dns, 293
GET /system/license, 294
GET /system/max_power_test, 295
GET /system/network, 295
GET /system/network/settings, 296
GET /system/ntp, 297
GET /system/rollback, 299
GET /system/time, 299
GET /system/ui_lock, 300
GET /system/update, 302
POST /system/backup, 292
POST /system/license, 294
POST /system/max_power_test, 295
POST /system/ui_lock, 301
POST /system/update, 302
PUT /system/dns, 293
PUT /system/network/settings, 296
PUT /system/ntp, 298
PUT /system/reboot, 298
PUT /system/rollback, 299
PUT /system/time, 300
DELETE /system/ui_lock, 301
```

<|end_chunk_1738|><|start_chunk_1739|>
## /templates

GET /templates/rc_boxpick, 148
GET /templates/rc_boxpick/\{id\}, 149
GET /templates/rc_silhouettematch, 184
GET /templates/rc_silhouettematch/\{id\}, 185
PUT /templates/rc_boxpick/\{id\}, 149
PUT /templates/rc_silhouettematch/\{id\}, 185
DELETED-Ptemblates/rc_boxpick/\{id\}, 150
DELETE /templates/rc_silhouettematch/\{id\}, 186
GET /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\},
284
PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters,
278
PUT /pipelines/\{pipeline\}/nodes/\{node\}/parameters/\{param\},
280
PUT /pipelines/\{pipeline\}/nodes/\{node\}/services/\{service\},
283
<|end_chunk_1739|><|start_chunk_1740|>
## /system

GET /system, 290
GET /system/backup, 292
<|end_chunk_1740|><|start_chunk_1741|>
### Page 358<|end_chunk_1741|><|start_chunk_1742|>
 Index 
<|end_chunk_1742|><|start_chunk_1743|>
## Symbols

3D coordinates, 33
disparity image, 33
3D modeling, 33, 56
<|end_chunk_1743|><|start_chunk_1744|>
## A

acceleration, 56, 57
dynamics, 34
acquisition mode
disparity image, 47
AcquisitionAlternateFilter GenICam, 262
AcquisitionFrameRate GenICam, 259
AcquisitionMultiPartMode GenICam, 262
active partition, 337
AdaptiveOut1
auto exposure mode, 41
angular
velocity, 56, 57
AprilTag, 94
pose estimation, 96
re-identification, 97
return codes, 105
services, 99
auto
exposure, 41
auto exposure, 40, 41
auto exposure mode, 41
AdaptiveOut1, 41
Normal, 41
Out1High, 41
<|end_chunk_1744|><|start_chunk_1745|>
## B

backup
settings, 335
BalanceRatio
GenICam, 259
BalanceRatioSelector GenICam, 259
BalanceWhiteAuto GenICam, 259
base-plane
SilhouetteMatch, 152
base-plane calibration SilhouetteMatch, 152
Baseline

GenICam, 263
baseline, 36
Baumer
IpConfigTool, 30
bin picking, 105, 123
BoxPick, 123
filling level, 80
grasp, 125
grasp sorting, 125
item models, 123
load carrier, 79, 229
parameters, 128
preferred orientation, 126
RECTANGLE, 124
region of interest, 237
return codes, 147
services, 134
status, 134
template api, 148
template deletion, 148
template download, 148
template upload, 148
texture, 124
TEXTURED_BOX, 124
views, 124
<|end_chunk_1745|><|start_chunk_1746|>
## C

cables, 21, 339
CAD model, 19
calibration
camera, 217
camera to IMU, 56
hand-eye calibration, 191
rectification, 36
calibration grid, 218
camera
calibration, 217
frame rate, 39
gamma, 40
parameters, 37
pose stream, 56
Web GUI, 37
camera calibration
monocalibration, 223
parameters, 224
services, 224
stereo calibration, 221
camera model, 36
<|end_chunk_1746|><|start_chunk_1747|>
### Page 359
camera to IMU
calibration, 56
transformation, 56
Chunk data
GenICam, 261
collision check, 209, 243
CollisionCheck, 209
return codes, 217
compartment
load carrier, 232
ComponentEnable
GenICam, 258
ComponentIDValue
GenICam, 258
components
rc_visard, 16
ComponentSelector
GenICam, 258
Confidence
GenICam image stream, 265
confidence, 33
minimum, 51
connectivity kit, 339
conversions
GenICam image stream, 266
cooling, 20
coordinate frames
dynamics, 56
mounting, 24
state estimation, 54
corners
visual odometry, 62, 64
correspondences
visual odometry, 62
<|end_chunk_1747|><|start_chunk_1748|>
## D

data
IMU, 57
inertial measurement unit, 57
data model
REST-API, 302
data stream
dynamics, 56
imu, 57
pose, 56
pose_rt, 56
REST-API, 285
data-type
REST-API, 302
definition
load carrier, 229
depth error
maximum, 51
depth image, 32, 33, 33, 45
Web GUI, 45
depth measurement, 74
DepthAcquisitionMode
GenICam, 263

DepthAcquisitionTrigger
GenICam, 263
DepthDoubleShot
GenICam, 264
DepthFill
GenICam, 264
DepthMaxDepth
GenICam, 264
DepthMaxDepthErr
GenICam, 265
DepthMinConf
GenICam, 264
DepthMinDepth
GenICam, 264
DepthQuality
GenICam, 264
DepthSeg
GenICam, 264
DepthSmooth
GenICam, 264
DepthStaticScene
GenICam, 264
detection
load carrier, 79
tag, 92
DHCP, 12
DHCP, 29
dimensions
load carrier, 229
rc_visard, 18
disable parameter lock
GenICam, 262
discovery GUI, 26
Disparity
GenICam image stream, 265
disparity, 31, 32, 36, 45
disparity error, 33
disparity image, 31, 32, 45
3D coordinates, 33
acquisition mode, 47
double_shot, 49
exposure adaptation timeout, 48
parameters, 45
quality, 48
smooth, 50
static_scene, 49
Web GUI, 45
disparity range
visual odometry, 64
DNS, 12
DOF, 12
double_shot
disparity image, 49
GenICam, 264
download
images, 37
log files, 338
settings, 335
<|end_chunk_1748|><|start_chunk_1749|>
### Page 360
dynamic state, 34
dynamics
acceleration, 34
coordinate frames, 56
data stream, 56
jump flag, 56
pose, 34
REST-API, 285
services, 57
velocity, 34
Web GUI, 62
dynamics stream, 56
<|end_chunk_1749|><|start_chunk_1750|>
## E

egomotion, 34, 62
eki, 322
Error
GenICam image stream, 265
error, 33
hand-eye calibration, 197
pose, 67
Ethernet
pin assignments, 21
exposure
auto, 40,41
HDR, 40
manual, 40
exposure adaptation timeout
disparity image, 48
exposure region, 42
exposure time, 42
maximum, 41
ExposureAuto
GenICam, 259
ExposureRegionHeight
GenICam, 263
ExposureRegionOffsetX
GenICam, 262
ExposureRegionOffsetY
GenICam, 262
ExposureRegionWidth
GenICam, 263
ExposureTime
GenICam, 259
ExposureTimeAutoMax
GenICam, 262
external reference frame
hand-eye calibration, 187
<|end_chunk_1750|><|start_chunk_1751|>
## F

features
visual odometry, 65
fill-in, 51
GenICam, 264
filling level
BoxPick, 80
ItemPick, 80
LoadCarrier, 80

SilhouetteMatch, 80
firmware
mender, 336
rollback, 337
update, 336
version, 336
focal length, 36
focal length factor
GenICam, 263
FocalLengthFactor
GenICam, 263
fps, see frame rate
frame rate, 17
camera, 39
GenICam, 259
pose, 56
visual odometry, 62
<|end_chunk_1751|><|start_chunk_1752|>
## G

Gain
GenICam, 259
gain factor, 41, 43
gamma
camera, 40
GenICam, 12
GenICam
AcquisitionAlternateFilter, 262
AcquisitionFrameRate, 259
AcquisitionMultiPartMode, 262
BalanceRatio, 259
BalanceRatioSelector, 259
BalanceWhiteAuto, 259
Baseline, 263
Chunk data, 261
ComponentEnable, 258
ComponentIDValue, 258
ComponentSelector, 258
DepthAcquisitionMode, 263
DepthAcquisitionTrigger, 263
DepthDoubleShot, 264
DepthFill, 264
DepthMaxDepth, 264
DepthMaxDepthErr, 265
DepthMinConf, 264
DepthMinDepth, 264
DepthQuality, 264
DepthSeg, 264
DepthSmooth, 264
DepthStaticScene, 264
disable parameter lock, 262
double_shot, 264
ExposureAuto, 259
ExposureRegionHeight, 263
ExposureRegionOffsetX, 262
ExposureRegionOffsetY, 262
ExposureRegionWidth, 263
ExposureTime, 259
ExposureTimeAutoMax, 262
<|end_chunk_1752|><|start_chunk_1753|>
### Page 361
fill-in, 264
focal length factor, 263
FocalLengthFactor, 263
frame rate, 259
Gain, 259
Height, 258
HeightMax, 258
LineSelector, 260
LineSource, 260
LineStatus, 260
LineStatusAll, 260
maximum depth error, 265
maximum distance, 264
minimum confidence, 264
minimum distance, 264
PixelFormat, 258, 265
PtpEnable, 260
quality, 264
RcExposureAutoAverageMax, 263
RcExposureAutoAverageMin, 263
Scan3dBaseline, 261
Scan3dCoordinateOffset, 261
Scan3dCoordinateScale, 261
Scan3dDistanceUnit, 260
Scan3dFocalLength, 260
Scan3dInvalidDataFlag, 261
Scan3dInvalidDataValue, 261
Scan3dOutputMode, 260
Scan3dPrinciplePointU, 261
Scan3dPrinciplePointV, 261
segmentation, 264
smooth, 264
static_scene, 264
system ready, 262
timestamp, 266
Width, 258
WidthMax, 258
GenICam image stream
Confidence, 265
conversions, 266
Disparity, 265
Error, 265
Intensity, 265
IntensityCombined, 265
GigE, 12
GigE Vision, 12
GigE Vision, see GenICam
IP address, 30
GPIO
pin assignments, 22
grasp computation, 105, 123
gripper CAD element api, 251
gripper CAD element deletion, 251
gripper CAD element download, 251
gripper CAD element upload, 251
GripperDB, 243
return codes, 251
gRPC, 330
<|end_chunk_1753|><|start_chunk_1754|>
## H

hand-eye calibration
calibration, 191
error, 197
external reference frame, 187
mounting, 188
parameters, 197
robot frame, 187
slot, 194
Height
GenICam, 258
HeightMax
GenICam, 258
host name, 29
housing temperature
LED, 20
humidity, 20
<|end_chunk_1754|><|start_chunk_1755|>
## I

image
timestamp, 266
image features
visual odometry, 62
image noise, 41
images
download, 37
IMU, 12
IMU, 34
data, 57
inertial measurement unit, 62
imu
data stream, 57
inactive partition, 337
inertial measurement unit
data, 57
IMU, 62
inner volume
load carrier, 229
INS, 12
INS, 34
installation, 26
Intensity
GenICam image stream, 265
IntensityCombined
GenICam image stream, 265
IP, 12
IP address, 12
IP address, 28
GigE Vision, 30
IP54, 20
IpConfigTool
Baumer, 30
ItemPick, 105
filling level, 80
grasp, 106
grasp sorting, 106
load carrier, 79, 229
parameters, 109
<|end_chunk_1755|><|start_chunk_1756|>
### Page 362
preferred orientation, 107
region of interest, 237
return codes, 122
services, 112
status, 112
<|end_chunk_1756|><|start_chunk_1757|>
## J

jump flag
dynamics, 56
SLAM, 56
<|end_chunk_1757|><|start_chunk_1758|>
## K

keyframes, 62
visual odometry, 62, 64
<|end_chunk_1758|><|start_chunk_1759|>
## L

LED, 26
colors, 341
housing temperature, 20
linear
velocity, 56
LineSelector
GenICam, 260
LineSource
GenICam, 260
LineStatus
GenICam, 260
LineStatusAll
GenICam, 260
Link-Local, 12
Link-Local, 30
load carrier
BoxPick, 79, 229
compartment, 232
definition, 229
detection, 79
dimensions, 229
inner volume, 229
ItemPick, 79, 229
orientation prior, 229
pose, 229
rim, 229
SilhouetteMatch, 79, 229
load carrier detection, 79
load carrier model, 229
LoadCarrier, 79
filling level, 80
parameters, 82
return codes, 92
services, 83
LoadCarrierDB, 229
return codes, 236
services, 233
log files
download, 338
logs
REST-API, 288
loop closure, 67
<|end_chunk_1759|><|start_chunk_1760|>
## M

MAC address, 12
MAC address, 29
manual exposure, 40,42
maximum
depth error, 51
exposure time, 41
maximum depth error, 51
GenICam, 265
maximum distance, 50
GenICam, 264
mDNS, 12
Measure, 74
parameters, 75
return codes, 78
services, 76
mender
firmware, 336
minimum
confidence, 51
minimum confidence, 51
GenICam, 264
minimum distance, 49
GenICam, 264
monocalibration
camera calibration, 223
motion blur, 41
mounting, 23
hand-eye calibration, 188
<|end_chunk_1760|><|start_chunk_1761|>
## N

network cable, 339
network configuration, 28
node
REST-API, 269
Normal
auto exposure mode, 41
NTP, 12
NTP
synchronization, 334
<|end_chunk_1761|><|start_chunk_1762|>
## 0

object detection, 150
OPC UA, 333
operating conditions, 20
orientation prior
load carrier, 229
Out1High
auto exposure mode, 41
<|end_chunk_1762|><|start_chunk_1763|>
## $P$

parameter
REST-API, 270
parameters
camera, 37
camera calibration, 224
disparity image, 45
hand-eye calibration, 197
<|end_chunk_1763|><|start_chunk_1764|>
### Page 363
services, 44
visual odometry, 62
pin assignments
Ethernet, 21
GPIO, 22
power, 22
PixelFormat
GenICam, 258, 265
point cloud, 33
pose
data stream, 56
dynamics, 34
error, 67
frame rate, 56
load carrier, 229
timestamp, 55
pose estimation, see state estimation
AprilTag, 96
QR code, 96
pose stream, 56
camera, 56
pose_rt
data stream, 56
power
pin assignments, 22
power cable, 339, 340
power supply, 20, 340
protection class, 20
PTP, 12
PTP
synchronization, 260, 334
PtpEnable
GenICam, 260
<|end_chunk_1764|><|start_chunk_1765|>
## 0

QR Code
return codes, 105
QR code, 93
pose estimation, 96
re-identification, 97
services, 99
quality
disparity image, 48
GenICam, 264
quaternion
rotation, 56
<|end_chunk_1765|><|start_chunk_1766|>
## $R$

rc_dynamics, 319
rc_visard
components, 16
RcExposureAutoAverageMax GenICam, 263
RcExposureAutoAverageMin GenICam, 263
re-identification
AprilTag, 97
QR code, 97
real-time pose, 56
reboot, 337
rectification, 36
reset, 26
resolution, 17
REST-API, 267
data model, 302
data stream, 285
data-type, 302
dynamics, 285
entry point, 267
logs, 288
node, 269
parameter, 270
services, 270
status value, 270
system, 288
version, 267
restore
settings, 335
return codes
AprilTag, 105
BoxPick, 147
CollisionCheck, 217
GripperDB, 251
ItemPick, 122
LoadCarrier, 92
LoadCarrierDB, 236
Measure, 78
QR Code, 105
RoiDB, 243
SilhouetteMatch, 183
rim
load carrier, 229
robot frame
hand-eye calibration, 187
ROI, 237
RoiDB, 237
return codes, 243
services, 238
rollback
firmware, 337
rotation
quaternion, 56
<|end_chunk_1766|><|start_chunk_1767|>
## S

Scan3dBaseline GenICam, 261
Scan3dCoordinateOffset GenICam, 261
Scan3dCoordinateScale GenICam, 261
Scan3dDistanceUnit GenICam, 260
Scan3dFocalLength GenICam, 260
Scan3dInvalidDataFlag GenICam, 261
<|end_chunk_1767|><|start_chunk_1768|>
### Page 364
Scan3dInvalidDataValue
GenICam, 261
Scan3dOutputMode
GenICam, 260
Scan3dPrinciplePointU
GenICam, 261
Scan3dPrinciplePointV
GenICam, 261
SDK, 12
segmentation, 51
GenICam, 264
self-calibration, 218
Semi-Global Matching, see SGM
sensor fusion, 62
serial number, 27, 29
services
AprilTag, 99
camera calibration, 224
dynamics, 57
parameters, 44
QR code, 99
REST-API, 270
tag detection, 99
visual odometry, 65
set
time, 334
settings
backup, 335
download, 335
restore, 335
upload, 335
SGM, 12
SGM, 31, 32
silhouette, 150
SilhouetteMatch, 150
base-plane, 152
base-plane calibration, 152
collision check, 159
detection of objects, 155
filling level, 80
grasp points, 153
load carrier, 79, 229
object template, 153
parameters, 160
preferred orientation, 155
region of interest, 153, 237
return codes, 183
services, 165
sorting, 155
status, 165
template api, 184
template deletion, 184
template download, 184
template upload, 184
Simultaneous Localization and Mapping, SE SEALAM
SLAM, 13
SLAM, 67
jump flag, 56
Web GUI, 67
slot
hand-eye calibration, 194
smooth
disparity image, 50
GenICam, 264
spare parts, 340
specifications
rc_visard, 17
state estimate, 55
state estimation
coordinate frames, 54
static_scene
disparity image, 49
GenICam, 264
status value
REST-API, 270
stereo calibration
camera calibration, 221
stereo camera, 36
stereo matching, 31
Swagger UI, 315
synchronization
NTP, 334
PTP, 260, 334
time, 260, 333
system
REST-API, 288
system ready
GenICam, 262
<|end_chunk_1768|><|start_chunk_1769|>
## T

tag detection, 92
families, 94
pose estimation, 96
re-identification, 97
services, 99
TCP, 13
temperature range, 20
texture, 32
time
set, 334
synchronization, 260, 333
timestamp
GenICam, 266
image, 266
pose, 55
transformation
camera to IMU, 56
translation, 56
tripod, 23
<|end_chunk_1769|><|start_chunk_1770|>
## U

UDP, 13
update
firmware, 336
upload
<|end_chunk_1770|><|start_chunk_1771|>
### Page 365
settings, 335
URI, 13
URL, 13
<|end_chunk_1771|><|start_chunk_1772|>
 V 

velocity
angular, 56, 57
dynamics, 34
linear, 56
version
firmware, 336
REST-API, 267
visual odometry, 34, 62
corners, 62, 64
correspondences, 62
disparity range, 64
features, 65
frame rate, 62
image features, 62
keyframes, 62, 64
parameters, 62
services, 65
Web GUI, 62
v0, see visual odometry
<|end_chunk_1772|><|start_chunk_1773|>
## W

Web GUI, 254
backup, 335
camera, 37
depth image, 45
disparity image, 45
dynamics, 62
logs, 338
SLAM, 67
update, 336
visual odometry, 62
white balance, 43
Width
GenICam, 258
WidthMax
GenICam, 258
<|end_chunk_1773|><|start_chunk_1774|>
## $X$

XYZ+quaternion, 13
XYZABC, 13
<|end_chunk_1774|><|start_chunk_1775|>
### Page 366<|end_chunk_1775|><|start_chunk_1776|>
 roboception 
<|end_chunk_1776|><|start_chunk_1777|>
## rc_visard 3D Stereo Sensor

ASSEMBLY AND OPERATING MANUAL
<|end_chunk_1777|><|start_chunk_1778|>
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
+498988950790
(09:00-17:00 CET) support@roboception.de<|end_chunk_1778|>
</document>

Respond only with the IDs of the chunks where you believe a split should occur. 
YOU MUST RESPOND WITH AT LEAST ONE SPLIT.
