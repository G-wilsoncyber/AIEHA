from uuid import UUID

import networkx as nx

from aieha.graph.models import Edge, Node


class AIEHAGraph:
    """Graph container for canonical AIEHA nodes and edges."""

    def __init__(self) -> None:
        self._graph = nx.DiGraph()

    def add_node(self, node: Node) -> None:
        """Add a canonical AIEHA node to the graph."""

        self._graph.add_node(
            node.id,
            data=node,
        )


    def get_node(self, node_id: UUID) -> Node:
        """Return a node by UUID."""

        return self._graph.nodes[node_id]["data"]

    def add_edge(self, edge: Edge) -> None:
        """Add a canonical AIEHA edge between existing nodes."""

        if edge.source not in self._graph:
            raise ValueError(f"Target node does not exist: {edge.target}")

        self._graph.add_edge(
            edge.source,
            edge.target,
            data=edge,
        )

    def get_edge(self, source: UUID, target: UUID) -> Edge:
        """Return an edge between two nodes."""

        return self._graph.edges[source, target]["data"]

    def successors(self, node_id: UUID) -> list[Node]:
        """Return nodes directly reachable from a node."""

        return [
            self.get_node(successor)
            for successor in self._graph.successors(node_id)
        ]
    