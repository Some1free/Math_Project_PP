Do poprawnego działania programu należy przygotować plik tekstowy z konfiguracją (.txt lub .cfg). W plku tym należy zawrzeć takie informacje jak całkowita długość belki, oraz w zależności od potrzeby: siła, moment, ociążenie ciągłe. Domyślny plik kongiguracyjny nazywa się config.cfg. Zaleca się nieużywania polskich znaków. Funkcjonalności programu dostępne są po uruchomieniu go z dopiskiem --help. Program NIE uwzględnia jednostek - nalezy zadbać o ich zgodnosc we wlasnym zakresie oraz nie podawac ich w pliku konfiguracyjnym - w miejsca /.../ nalezy podac tylko liczby. 

Wzór konfiguracji:

Dlugosc_belki = /wartość długości/
Sila = /wartość siły/ , /odległość od podpory/
Sila2 = /wartość siły/ , /odległość od podpory/
Moment = /wartość momentu/ , /ewentualna odległość od podpory - nie uwzględniona w obliczeniach/
Moment2 = /wartość momentu/ , /ewentualna odległość od podpory - nie uwzględniona w obliczeniach/
Obciazenie_ciagle = /wartość jednostkowa/ , /długosc (odleglosc) trwania obciązenia/ , /odleglosc od podpory/