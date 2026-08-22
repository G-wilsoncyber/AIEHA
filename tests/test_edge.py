
from aieha.graph.models import Edge, EdgeType, Node, NodeType


def test_edge_creation():
    workload = Node(type=NodeType.WORKLOAD)
    model = Node(type=NodeType.MODEL)

    edge = Edge(
        source=workload.id,
        target=model.id,
        type=EdgeType.USES,
    )

    assert edge.source == workload.id
    assert edge.target == model.id
    assert edge.type == EdgeType.USES
    assert edge.attributes == {}
    assert edge.created_at is not None