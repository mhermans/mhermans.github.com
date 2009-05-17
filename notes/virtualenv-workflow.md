Virtualenv workflow
===================

Kwestie van het volgende keer niet opnieuw te moeten uitzoeken.

Installeer virtualenv globaal
    
    sudo easy_install virtualenv

Installeer virtualenv wrapper globaal
    
    download tarbal van http://www.doughellmann.com/projects/virtualenvwrapper/
    mkdir .virtualenvs # directory waar je envs gaan staan
    cp virtualenvwrapper_bashrc /usr/local/bin/ # script zelf kopiëren
    
Volgende lijnen toevoegen aan .bashrc

    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper_bashrc

Aangepaste .bashrc exporteren

    source ~/.bashrc

Nieuwe virtualenv omgeving aanmaken

    mkvirtualenv envnaam

Switched automatisch na aanmaak, anders activeren

    workon envnaam

Packages installeren

    easy_install ipython
    easy_install rdflib
    cd tmp/rdfalchemy
    python setup.py install
    ...

Virtualenv omgeving stoppen
    
    deactivate

Virtualenv omgeving verwijderen

    rmvirtualenv envnaam
