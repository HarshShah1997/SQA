
"""
Populated place related regex
"""

from refo import Plus, Question
from parsy.dsl import HasKeyword
from parsy.parsing import Lemma, Pos, QuestionTemplate, Token, Particle
from .dsl import IsPopulatedPlace, IncumbentOf, CapitalOf, \
    LabelOf, PopulationOf


class PopulatedPlace(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return IsPopulatedPlace() + HasKeyword(name)


class CapitalOfQuestion(QuestionTemplate):
    """
    Regex for questions about the capital of a country.
    Ex: "What is the capital of Massachussets?"
    """

    opening = Lemma("what") + Lemma("be")
    regex = Question(opening) + Question(Pos("DT")) + Lemma("capital") + Pos("IN") + \
        Question(Pos("DT")) + PopulatedPlace() + Question(Pos("."))

    def interpret(self, match):
        capital = CapitalOf(match.populatedplace)
        label = LabelOf(capital)
        return label, "enum"


class PopulationOfQuestion(QuestionTemplate):
    """
    Regex for questions about the population of a country.
    Ex: "What is the population of Cordoba?"
        "How many people live in Cordoba?"
    """

    openings = (Question(Pos("WP") + Lemma("be") + Pos("DT")) +
                Lemma("population") + Pos("IN")) | \
               (Pos("WRB") + Lemma("many") + Lemma("people") +
                Token("live") + Pos("IN"))
    regex = openings + Question(Pos("DT")) + PopulatedPlace() + Question(Pos("."))

    def interpret(self, match):
        population = PopulationOf(match.populatedplace)
        return population, "literal"
