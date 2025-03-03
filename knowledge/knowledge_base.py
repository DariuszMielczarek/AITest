import copy

from knowledge.problem_facts import ProblemFacts


class KnowledgeBase:
    def __init__(self, query_function):
        self.facts = []
        self.rules = []
        self.query_function = query_function
        self.possibilities = []
        self.all_possible_problem_facts = []

    def add_fact(self, fact: ProblemFacts):
        if fact not in self.facts:
            self.facts.append(fact)

    def add_rule(self, rule):
        if rule not in self.rules:
            self.rules.append(rule)

    def check_query(self, condition):
        return self.query_function(self, condition)

    def add_possibilities(self, possibilities: list):
        self.possibilities = copy.deepcopy(possibilities)

    def evaluate(self):
        if (len(self.facts) == 0 or len(self.possibilities) == 0
                or len(self.possibilities) != len(self.facts[0].get_data())):
            return False

        for i in range(len(self.possibilities) ** len(self.possibilities[0])):
            new_possible_problem_facts = Person(data=self._prepare_problem_facts(i))
            if self._check_new_possible_problem_facts(new_possible_problem_facts):
                self.all_possible_problem_facts.append(new_possible_problem_facts)
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


class Person(ProblemFacts):
    def __init__(self, nationality: str | None = None, age: int | None = None, house: str | None = None,
                 data: list = None):
        self.nationality = data[0] if data else nationality
        self.age = data[1] if data else age
        self.house = data[2] if data else house

    def get_data(self):
        return self.nationality, self.age, self.house

    def __str__(self):
        return f'Person({self.nationality}, {self.age}, {self.house})'

    def __eq__(self, other):
        return ((self.nationality == other.nationality if (self.nationality and other.nationality) else True)
                and (self.age == other.age if (self.age and other.age) else True)
                and (self.house == other.house if (self.house and other.house) else True))
