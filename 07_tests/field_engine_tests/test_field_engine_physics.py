import pytest
from field_engine_physics import Node, Edge, FieldEnginePhysics


def test_two_charges_repulsion():
    n1 = Node("a", (0.0, 0.0), charge=1.0)
    n2 = Node("b", (1.0, 0.0), charge=1.0)
    eng = FieldEnginePhysics([n1, n2], [])

    eng.step(20)
    pos1 = eng.get_positions()["a"]
    pos2 = eng.get_positions()["b"]

    assert pos1[0] < 0.0
    assert pos2[0] > 1.0


def test_spring_pull_together():
    n1 = Node("a", (0.0, 0.0))
    n2 = Node("b", (3.0, 0.0))
    e = Edge("a", "b", k=1.0, rest=1.0)
    eng = FieldEnginePhysics([n1, n2], [e])

    eng.step(30)
    pos1 = eng.get_positions()["a"]
    pos2 = eng.get_positions()["b"]

    assert pos2[0] < 3.0
    assert pos1[0] > 0.0


def test_fixed_node_behavior():
    n1 = Node("a", (0.0, 0.0), fixed=True)
    n2 = Node("b", (2.0, 0.0))
    e = Edge("a", "b", k=1.0, rest=1.0)
    eng = FieldEnginePhysics([n1, n2], [e])

    eng.step(30)
    pos1 = eng.get_positions()["a"]
    pos2 = eng.get_positions()["b"]

    assert pos1 == (0.0, 0.0)
    assert pos2[0] < 2.0
