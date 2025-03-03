from knowledge.knowledge_base import KnowledgeBase, Person
from knowledge.models import model_checking

if __name__ == '__main__':
    kb = KnowledgeBase(model_checking)

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
        kb.display_all_possible_problem_facts()
        person_50_yo = Person(None, 50, None)
        result = kb.check_query(person_50_yo)
        print(result)
