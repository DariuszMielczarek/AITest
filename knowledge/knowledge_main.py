from knowledge.knowledge_base import KnowledgeBase
from knowledge.models import model_checking, full_model_checking
from knowledge.problem_facts import Person

if __name__ == '__main__':
    # kb = KnowledgeBase(model_checking, model_checking, Person)
    #
    # fact1 = Person('England', None, 'red')
    # fact2 = Person(None, 40, 'green')
    # fact3 = Person('Sweden', 30, None)
    # kb.add_fact(fact1)
    # kb.add_fact(fact2)
    # kb.add_fact(fact3)
    #
    # possibilities = [
    #     ['England', 'Poland', 'Sweden'],
    #     [30, 40, 50],
    #     ['red', 'green', 'blue']
    # ]
    # kb.add_possibilities(possibilities)
    #
    # if kb.evaluate():
    #     person_50_yo = Person(None, 50, None)
    #     result = kb.check_query(person_50_yo)
    #     print(result)

    kb = KnowledgeBase(full_model_checking, model_checking, Person)

    fact1 = Person('England', None, 'red')
    fact2 = Person(None, 40, 'green')
    fact3 = Person('Sweden', 30, None)
    kb.add_fact(fact1)
    kb.add_fact(fact2)
    kb.add_fact(fact3)

    possibilities = [
        ['England', 'Poland', 'Sweden'],
        [30, 40, 50],
        ['red', 'green', 'blue']
    ]
    kb.add_possibilities(possibilities)

    if kb.evaluate():
        result = kb.check_query(None)
        if result:
            text = [str(person) for person in result]
            print('Riddle results: ' + str(text))
        else:
            print('Not enough knowledge to get full model check')
