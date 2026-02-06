# WindPower_DigitalTwin 
### Ολοκληρωμένη Προσέγγιση Ψηφιακού Διδύμου με Factory Pattern & Pydantic

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-AGPL--v3-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

---

##  Περιγραφή Έργου
Το **WindPower_DigitalTwin** αποτελεί τη μετάβαση ενός ακαδημαϊκού έργου σε ένα ισχυρό, επεκτάσιμο οικοσύστημα ανοιχτού κώδικα. Στόχος είναι η δημιουργία ενός Ψηφιακού Διδύμου για αιολικά πάρκα που εκτελεί ωριαία πρόβλεψη ισχύος και ανίχνευση ανωμαλιών με βιομηχανική ακρίβεια.

##  Αρχιτεκτονική Συστήματος
Το έργο υιοθετεί τη δομή **src-layout** για τον διαχωρισμό της βασικής λογικής από τα σενάρια χρήστη. Η εισαγωγή δεδομένων βασίζεται στο **Factory Design Pattern**, επιτρέποντας την προσθήκη νέων πηγών χωρίς αλλαγές στον κεντρικό κώδικα.

```mermaid
architecture-beta
    group source(cloud)
    service ninja(logos:aws-lambda) in source
    service kassel(logos:aws-ec2) in source

    group ingestion(server) [Επίπεδο Εισαγωγής]
    service factory(server) in ingestion
    service pydantic(logos:pydantic) in ingestion

    group twin(cloud)
    service storage(database) in twin
    service model(logos:tensorflow) in twin

    ninja:R -- L:factory
    kassel:R -- L:factory
    factory:R -- L:pydantic
    pydantic:R -- L:storage
    storage:B -- T:model