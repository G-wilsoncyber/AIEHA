from aieha.graph.models import Node, NodeType


def test_node_creation():
    node = Node(
        type=NodeType.MODEL,
        attributes={
            "provider": "example-provider",
            "model": "example-model",
        },
    )

    assert node.type == NodeType.MODEL
    assert node.attributes["provider"] == "example-provider"
    assert node.attributes["model"] == "example-model"
    assert node.id is not None
    assert node.created_at is not None