import datetime
import random

import factory

from .models import (
    Interest,
    Lobbyist,
    LobbyistYear,
    Compensation,
    ExpenseCoversheet,
)
from .factory_names_list import surnames_list, first_names_list


class InterestFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Interest

    name = factory.Sequence(lambda n: 'Interest {0}'.format(n))
    state = 'TX'


class LobbyistFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Lobbyist
    filer_id = factory.Sequence(lambda n: n)
    first_name = factory.LazyAttribute(lambda a: random.choice(first_names_list))
    last_name = factory.LazyAttribute(lambda a: random.choice(surnames_list))
    sort_name = factory.LazyAttribute(lambda a: "%s %s" % (
        a.last_name, a.first_name))
    updated_at = factory.LazyAttribute(lambda a: datetime.date.today())


class LobbyistYearFactory(factory.DjangoModelFactory):
    FACTORY_FOR = LobbyistYear
    lobbyist = factory.SubFactory(LobbyistFactory)
    year = 2013


class CompensationFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Compensation
    amount_high = factory.LazyAttribute(lambda a: random.randint(10000, 100000))
    amount_low = factory.LazyAttribute(lambda a: random.randint(0, a.amount_high))
    amount_guess = factory.LazyAttribute(lambda a: (a.amount_high + a.amount_low) / 2)
    year = factory.SubFactory(LobbyistYearFactory)
    interest = factory.SubFactory(InterestFactory)
    updated_at = factory.LazyAttribute(lambda a: datetime.date.today())


class ExpenseCoversheetFactory(factory.DjangoModelFactory):
    FACTORY_FOR = ExpenseCoversheet
    lobbyist = factory.SubFactory(LobbyistFactory)
    report_date = '2001-04-01'
    report_id = factory.Sequence(lambda n: n)
    year = '2001'
    spent_guess = factory.LazyAttribute(lambda a: random.randint(10000, 100000))
