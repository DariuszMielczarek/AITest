from knowledge.knowledge_base import KnowledgeBase
from knowledge.problem_facts import ProblemFacts


def model_checking(kb: KnowledgeBase, query: ProblemFacts):
    possibilities = []
    for possibility in kb.all_possible_problem_facts:
        if possibility == query:
            possibilities.append(possibility)
    if len(possibilities) != 0 and all(possibility == possibilities[0] for possibility in possibilities):
        return True
    else:
        return False
