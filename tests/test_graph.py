import pytest

from aieha.graph.graph import AIEHAGraph
from aieha.graph.models import Edge, EdgeType, Node, NodeType


def test_graph_adds_and_retrieves_node():
    graph = AIEHAGraph()
    node = Node(type=NodeType.WORKLOAD)

    graph.add_node(node)

    retrieved = graph.get_node(node.id)

    assert retrieved == node


def test_graph_adds_and_retrieves_edge():
    graph = AIEHAGraph()

    workload = Node(type=NodeType.WORKLOAD)
    model = Node(type=NodeType.MODEL)

    graph.add_node(workload)
    graph.add_node(model)

    edge = Edge(
        source=workload.id,
        target=model.id,
        type=EdgeType.USES,
    )

    graph.add_edge(edge)

    retrieved = graph.get_edge(workload.id, model.id)

    assert retrieved == edge


def test_graph_rejects_edge_with_missing_source():
    graph = AIEHAGraph()

    workload = Node(type=NodeType.WORKLOAD)
    model = Node(type=NodeType.MODEL)

    graph.add_node(model)

    edge = Edge(
        source=workload.id,
        target=model.id,
        type=EdgeType.USES,
    )

    with pytest.raises(ValueError):
        graph.add_edge(edge)


def test_graph_returns_successors():
    graph = AIEHAGraph()

    workload = Node(type=NodeType.WORKLOAD)
    model = Node(type=NodeType.MODEL)

    graph.add_node(workload)
    graph.add_node(model)

    edge= Edge(
        source=workload.id,
        target=model.id,
        type=EdgeType.USES,
    )

    graph.add_edge(edge)

    successors = graph.successors(workload.id)

    assert successors == [model]
    
