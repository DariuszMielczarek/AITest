from knowledge.knowledge_base import KnowledgeBase
from knowledge.problem_facts import ProblemFacts


def model_checking(kb: KnowledgeBase, query: ProblemFacts):
    possibilities = []
    for possibility in kb.all_possible_problem_facts:
        if possibility == query:
            possibilities.append(possibility)
    if len(possibilities) != 0 and all(possibility == possibilities[0] for possibility in possibilities):
        return possibilities[0]
    else:
        return None


def full_model_checking(kb: KnowledgeBase, _: ProblemFacts):
    if len(kb.all_possible_problem_facts) == kb.klass.get_attr_count():
        return kb.all_possible_problem_facts
    else:
        return None
