from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: List[Dict[str, str]], hall_number: int, cleaner: str, movie: str):
    # Cria instâncias de Customer a partir da lista de dicionários
    customer_objects = [Customer(name=c["name"], food=c["food"]) for c in customers]

    # Vende comida aos clientes usando CinemaBar (método estático)
    for cust in customer_objects:
        CinemaBar.sell_product(customer=cust, product=cust.food)

    # Cria instância do CinemaHall com o número do corredor
    hall = CinemaHall(number=hall_number)

    # Cria instância do Cleaner com o nome do faxineiro
    cleaning_staff = Cleaner(name=cleaner)

    # Executa a sessão do filme na sala
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)
