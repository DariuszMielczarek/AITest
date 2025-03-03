class KnowledgeLogic:
    @staticmethod
    def not_func(condition):
        return lambda fact: not condition(fact)
