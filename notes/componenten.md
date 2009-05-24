Aantekeningen basiscomponenten
==============================

Transistors
-----------

* [Bipolar junction transistor](http://en.wikipedia.org/wiki/Bipolar_junction_transistor): een "gewoon" transistortje. Heeft een base, emittor en collector. Heeft een versterkingsfactor (gain) voor de ampére. 
    * NPN BJT
    * PNP BJT
* [Unipolar (junction) transistor](http://en.wikipedia.org/wiki/Field_effect_transistor), of FET: Een field-effect transistor. Werk volgens een ander principe dan de BJP, principe gelijkaardig.
    * [MOSFET](http://en.wikipedia.org/wiki/MOSFET): het meest voorkomende type van FET. 
* [Tyristor](http://en.wikipedia.org/wiki/Thyristor): soort van dubbele transistor. Als eenmaal de gate geactiveerd is zal ze blijven geleiden, ook als het voltage op de gate wegvalt.
* [TRIAC](http://en.wikipedia.org/wiki/TRIAC): dient voor AC te controleren. Werk als een (in twee richtingen) gecombineerde tyristor: als de gate geactiveerd is, blijft er stroom vloeien in beide richtingen.
* [Darlington pair](http://en.wikipedia.org/wiki/Darlington_transistor): koppeling van twee bipolaire transistors. Door de gecombineerde gain sterke toename stroom. 

Diodes
------

* [Diode](http://en.wikipedia.org/wiki/Diode): Laat stroom in één richting vloeien.
* [Schottky diode](http://en.wikipedia.org/wiki/Schottky_diode): een gewone diode, maar met een kleine switch-tijd en een lage forward voltage drop (er gaat niet veel voltage "verloren" als de diode stroom doorgeeft).
* [Flyback diode](http://en.wikipedia.org/wiki/Flyback_diode): Geen apart soort diode, maar verwijst naar het gebruik van een diode bij een inductor (spoel, relais, motor, etc.). Ze wordt parallel met de inductor geplaats, in de omgekeerde richting, zodat er geen stroom "terugvloeit" in het circuit. Meestal een Schottky diode. Andere termen: "free wheeling (clamp) diode for transient suppresion".
* [Light Emmiting Diode](http://en.wikipedia.org/wiki/Light-emitting_diode) (LED): Laat stroom in één richting vloeien, en produceerd daarbij licht.
* [Zener diode](http://en.wikipedia.org/wiki/Zener_diode): laat stroom door in de standaard richting, maar ook in de omgekeerde richting als de voltage groter is dan de "breakdown voltage".
* [Diode bridge/rectifier](http://en.wikipedia.org/wiki/Bridge_rectifier): Vier diodes die samen AC gelijkrichten.

Voltage regulators
------------------

* [Linear voltage regulator](http://en.wikipedia.org/wiki/Linear_regulator): een gedurig actief component houdt het voltage op een bepaald niveau.
    * [Shunt voltage regulator](http://en.wikipedia.org/wiki/Shunt_regulator): via een Zener diode. (classificatie?)
    * [Fixed linear voltage regulator](http://en.wikipedia.org/wiki/Linear_regulator#Fixed_regulators). Bv. LM78xx 
    * [Adjustable linear voltage regulator](http://en.wikipedia.org/wiki/Linear_regulator#Adjustable_regulators). Bv. LM317
* [Switching voltage regulator](http://en.wikipedia.org/wiki/Switched-mode_power_supply): door een component aan/uit te zetten, wordt het voltage op een bepaald niveau gehouden.

Amplifiers
----------

* [Differential amplifier](http://en.wikipedia.org/wiki/Differential_amplifier): twee voltages als inputs (V+, V-), het verschil tussen beide voltage wordt vermenigvuldigd met een constante factor (gain), wat één outputvoltage (Vout) geeft. (kijkt dus naar interne actieve weerstand?)
    * [Operational amplifier](http://en.wikipedia.org/wiki/Operational_amplifier) (op-amp): heeft een feedback mechanisme. Bv. x741.
    * [Instrumentation amplifier](http://en.wikipedia.org/wiki/Instrumentation_amplifier): met input buffers. (?)
* [Switching amplifier](http://en.wikipedia.org/wiki/Switching_amplifier): via PWM wordt een transistor aan/uitgezet (class D amp)

Varia
-----

* [Comparator](http://en.wikipedia.org/wiki/Comparator): twee voltages als input, het output-voltage geeft aan welke het grootste is.
    * Via differential amplifier 
    * Geïntegreerd circuit. Bv. LM339
    * [Schmitt trigger](http://en.wikipedia.org/wiki/Schmitt_trigger): Bij een gewone comparator kan een onzuiver signaal rond de threshold een snel state wisselen veroorzaken. Door positieve feedback vermijdt een Schmitt trigger dit.
* D/A-convertoren
    * [Digital to analog convertor](http://en.wikipedia.org/wiki/Digital-to-analog_converter) (DAC)
    * [Analog to digital convertor](http://en.wikipedia.org/wiki/Analog_to_digital_converter) (ADC): gebruikt comparator
* [Optocoupler](http://en.wikipedia.org/wiki/Optocoupler): combinatie van een ledje en een foto-gevoelige transitor. Dit geeft een bescherming tussen het schakelcircuit en het te schakelen-circuit. Werk dus eveneens als een flyback diode.

Componenten met specifieke functionaliteit:

* [ULN2803](http://www.datasheetcatalog.com/datasheets_pdf/U/L/N/2/ULN2803.shtml): array van 8 darlington pairs, met telken een flyback diode. Bedoeld om digitale signalen aan relais, ed. te koppelen. 
* [H-bridge](http://en.wikipedia.org/wiki/H-bridge): combinatie van 4 switch-elementen (bv. transistors) zodat voor een stroom/een motor in beide richtingen kan draaien. Zeker handig voor stepper-motors, waar er meerdere spoelen in beide richtingen afwisselend geactiveerd moeten worden. 

TODO
----

* Darlington pair
* Long-tailed pair differential amplifier

