Commandos voor probleemdiagnose
===============================

Netwerk-configuratie

    iwlist # geef informatie over de draadloze interface(s)
    iwconfig # configureerd draadloze interface(s)

    ethtool # configuratie tool
    ifconfig # configureerd vaste draad-verbindingen

Informatie bij het opstarten

    dmesg # geef de informatie/foutmeldingen bij het opstarten 

Informatie over onderdelen

    cat /proc/cpuinfo # informatie over de processor(s)
    cat /proc/meminfo # informatie over beschikbaar geheugen

Geïnstalleerde kernel-modules

    cat /proc/modules
    lsmod

Lijstjes    

    lspci # Geeft lijstje alle pci-apparaten
    lshal # 
    lspcmcia # PCMCIA-apparaten
    lsusb # USB-apparaten
    sudo lshw # Lijstje van hardware
    sudo lspci -vvnn # Uitgebreide informatie

Versie-informatie

    uname -a # Geeft kernel versie, i368 ed.
    lsb_release -a # Geeft verie-informatie op Ubuntu
    cat /proc/version_signature # kernel nummer


Voor input/toetsen te testen

    showkey -s
    xev

