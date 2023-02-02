from time import sleep
from manager import Manager


def main():
    manager = Manager()
    while True:

        start = manager.main_menu()
        if start in [1, 2, 3, 4]:
            sleep(1)
            manager.additional_menu()
            sleep(1)


if __name__ == '__main__':
    main()

'''Pytania:
1. dlaczego w menu_options jak zrobię do metody () to się z automatu wywołuje nawet jak jej nie calluje
2. Po co dziedziczyć skoro można w __init__ zrobić atrybut jako dana klasa i mamy te same metody dostępne
3. Czy tam gdzie pycharm mi podkresla by powinno byc staticmethod to robic staticmethod?
4. odnośnie branchy. Jak zmerdżuje z mainem to usuwać branch?
5. czy kolenosc metod w klasie jest wazna dla czytelnosci kodu?
3. Jaki jest proces twórczy osoby doświadczonej. Co po kolei robi'''
