import copy


class KnowledgeBase:
    def __init__(self, query_function, facts_generator_function, klass):
        self.facts = []
        self.rules = []
        self.query_function = query_function
        self.facts_generator_function = facts_generator_function
        self.klass = klass
        self.possibilities = []
        self.all_possible_problem_facts = []

    def add_fact(self, new_fact):
        for fact in self.facts:
            if fact.check_if_are_exactly_the_same(new_fact):
                return
        self.facts.append(new_fact)

    def add_rule(self, new_rule):
        for rule in self.rules:
            if rule.check_if_are_exactly_the_same(new_rule):
                return
        self.rules.append(new_rule)

    def check_query(self, condition):
        return self.query_function(self, condition)

    def add_possibilities(self, possibilities: list):
        self.possibilities = copy.deepcopy(possibilities)

    def evaluate(self):
        if (len(self.facts) == 0 or len(self.possibilities) == 0
                or len(self.possibilities) != len(self.facts[0].get_data())):
            return False

        possible_facts_count = len(self.possibilities) ** len(self.possibilities[0])
        while True:
            self.all_possible_problem_facts.clear()
            for i in range(len(self.possibilities) ** len(self.possibilities[0])):
                new_possible_problem_facts = self.klass(data=self._prepare_problem_facts(i))
                if self._check_new_possible_problem_facts(new_possible_problem_facts):
                    self.all_possible_problem_facts.append(new_possible_problem_facts)
            if len(self.all_possible_problem_facts) == possible_facts_count:
                break
            possible_facts_count = len(self.all_possible_problem_facts)
            self._add_new_facts()
        return True

    def display_all_possible_problem_facts(self):
        for problem_fact in self.all_possible_problem_facts:
            print(problem_fact)

    def _check_new_possible_problem_facts(self, new_possible_problem_facts):
        for fact in self.facts:
            if fact.exclude(new_possible_problem_facts):
                return False
        return True

    def _prepare_problem_facts(self, value: int):
        data = []
        for i in range(len(self.possibilities)):
            data.append(self.possibilities[i][value % len(self.possibilities[0])])
            value = value // len(self.possibilities[0])
        return data

    def _add_new_facts(self):
        for possibility in self.possibilities[0]:
            possibility_data = [possibility]
            for _ in range(len(self.possibilities)-1):
                possibility_data.append(None)
            dummy = self.klass(data=possibility_data)
            result = self.facts_generator_function(self, dummy)
            if result:
                self.add_fact(result)
