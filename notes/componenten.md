Aantekeningen basiscomponenten
==============================

Transistors
-----------

* Bipolar junction transistor: een "gewoon" transistortje. Heeft een base, emittor en collector. Heeft een versterkingsfactor (gain) voor de ampére. 
    * NPN BJT
    * PNP BJT
* Unipolar (junction) transistor, of FET: Een field effect transistor. Werk volgens een ander principe dan de BJP, principe gelijkaardig.
    * MOSFET: het meest voorkomende type van FET. 
* Tyristor: soort van dubbele transistor. Als eenmaal de gate geactiveerd is zal ze blijven geleiden, ook als het voltage op de gate wegvalt.
* Triac: dient voor AC te controleren. Werk als een (in twee richtingen) gecombineerde tyristor: als de gate geactiveerd is, blijft er stroom vloeien in beide richtingen.
* Darlington array: serie-schakeling van transistors. Door de gecombineerde gain sterke toename stroom. 

Diodes
------

* Diode: Laat stroom in één richting vloeien.
* Light Emmiting Diode (LED): Laat stroom in één richting vloeien, en produceerd daarbij licht.
* Zener diode: laat stroom door in de standaard richting, maar ook in de omgekeerde richting als de voltage groter is dan de "breakdown voltage".
* Diode bridge of bridge rectifier. Vier diodes die samen AC gelijkrichten.

Voltage regulators
------------------

* Linear voltage regulator: een gedurig actief component houdt het voltage op een bepaald niveau.
    * Shunt voltage regulator: via een Zener diode. (classificatie?)
    * Fixed linear voltage regulator. Bv. LM78xx 
    * Adjustable linear voltage regulator. Bv. LM317
* Switching voltage regulator: door een component aan/uit te zetten, wordt het voltage op een bepaald niveau gehouden.

Amplifiers
----------

* Differential amplifier: twee voltages als inputs (V+, V-), het verschil tussen beide voltage wordt vermenigvuldigd met een constante factor (gain), wat één outputvoltage (Vout) geeft. (kijkt dus naar interne actieve weerstand?)
    * Opprational amplifier (op-amp): heeft een feedback mechanisme. Bv. x741.
    * Instrumentation amplifier: met input buffers. (?)
* Switching amplifier: via PWM wordt een transistor aan/uitgezet (class D amp)

Varia
-----

* Comparator 
    * Via differential amplifier 
    * Geïntegreerd circuit. Bv. LM339
    * Schmitt trigger. Bij een gewone comparator kan een onzuiver signaal rond de threshold een snel state wisselen veroorzaken. Door positieve feedback vermijdt een Smitt trigger dit.
* D/A-convertoren
    * Digital to analog convertor (DAC)
    * Analog to digital convertor (ADC): gebruikt comparator


TODO
----

* Darlington array
* Long-tailed pair differential amplifier

