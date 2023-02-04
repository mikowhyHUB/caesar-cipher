from time import sleep
from manager import Manager
from buffer import Buffer


def main():
    manager = Manager()
    while True:
        start = manager.main_menu()
        if start in [1, 2, 3, 4]:
            sleep(1)
            manager.additional_menu()
            sleep(1)


if __name__ == "__main__":
    main()

"""Pytania:
2. Po co dziedziczyć skoro można w __init__ zrobić atrybut jako dana klasa i mamy te same metody dostępne
3. Czy tam gdzie pycharm mi podkresla by powinno byc staticmethod to robic staticmethod?
4. odnośnie branchy. Jak zmerdżuje z mainem to usuwać branch?
5. czy kolenosc metod w klasie jest wazna dla czytelnosci kodu?
7. Jaki jest proces twórczy osoby doświadczonej. Co po kolei robi
8. Ten pre-commit mi coś szwankuje"""
