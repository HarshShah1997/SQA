"""
Basic questions for DBpedia.
"""

from refo import Group, Plus, Question
from quepy.parsing import Lemma, Pos, QuestionTemplate, Token, Particle, \
                          Lemmas
from quepy.dsl import HasKeyword, IsRelatedTo, HasType
from .dsl import DefinitionOf, LabelOf, IsPlace, \
    UTCof, LocationOf
import re


# Openings
LISTOPEN = Lemma("list") | Lemma("name")


class Thing(Particle):
    regex = Question(Pos("JJ")) + ((Pos("NN") | Pos("NNP") | Pos("NNS")) |\
            Pos("VBN")) + Question(Pos("NN") | Pos("NNP") | Pos("NNS")) 

    def interpret(self, match):
        #print(match.words.tokens)
        tokens = match.words.tokens
        #tokens = tokens.split(" ")[1]
        iiit = re.compile("IIIT")
        tokens = iiit.sub("Indian Institute of Information Technology,", tokens)
        iit = re.compile("IIT")
        tokens = iit.sub("Indian Institute of Technology", tokens)
        return HasKeyword(tokens)


class WhatIs(QuestionTemplate):
    """
    Regex for questions like "What is a blowtorch
    Ex: "What is a Car"
        "What is Seinfield?"
    """

    regex = Lemma("what") + Lemma("be") + Question(Pos("DT")) + \
        Thing() + Question(Pos("."))

    def interpret(self, match):
        label = DefinitionOf(match.thing)

        return label, "define"


class ListEntity(QuestionTemplate):
    """
    Regex for questions like "List Microsoft software"
    """

    entity = Group(Pos("NNP"), "entity")
    target = Group(Pos("NN") | Pos("NNS"), "target")
    regex = LISTOPEN + entity + target

    def interpret(self, match):
        entity = HasKeyword(match.entity.tokens)
        target_type = HasKeyword(match.target.lemmas)
        target = HasType(target_type) + IsRelatedTo(entity)
        label = LabelOf(target)

        return label, "enum"


class WhatTimeIs(QuestionTemplate):
    """
    Regex for questions about the time
    Ex: "What time is it in Cordoba"
    """

    nouns = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))
    place = Group(nouns, "place")
    openings = (Lemma("what") +
        ((Token("is") + Token("the") + Question(Lemma("current")) +
        Question(Lemma("local")) + Lemma("time")) |
        (Lemma("time") + Token("is") + Token("it")))) | \
               Lemma("time")
    regex = openings + Pos("IN") + place + Question(Pos("."))

    def interpret(self, match):
        place = HasKeyword(match.place.lemmas.title()) + IsPlace()
        utc_offset = UTCof(place)

        return utc_offset, "time"


class WhereIsQuestion(QuestionTemplate):
    """
    Ex: "where in the world is the Eiffel Tower"
    """

    thing = Group(Plus(Pos("IN") | Pos("NP") | Pos("NNP") | Pos("NNPS")),
                  "thing")
    regex = Lemma("where") + Question(Lemmas("in the world")) + Lemma("be") + \
        Question(Pos("DT")) + thing + Question(Pos("."))

    def interpret(self, match):
        thing = HasKeyword(match.thing.tokens)
        location = LocationOf(thing)
        location_name = LabelOf(location)

        return location_name, "enum"
