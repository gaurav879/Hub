from datetime import datetime
from hub.client.utils import get_user_name
from typing import List, Optional


class CommitNode:
    """Contains all the Version Control information about a particular commit."""

    def __init__(self, branch: str, commit_id: str):
        self.commit_id = commit_id
        self.branch = branch
        self.children: List["CommitNode"] = []
        self.parent: Optional["CommitNode"] = None
        self.pseudo_parents = []
        self.commit_message: Optional[str] = None
        self.commit_time: Optional[datetime] = None
        self.commit_user_name: Optional[str] = None

    def add_child(self, node: "CommitNode"):
        """Adds a child to the node, used for branching."""
        node.parent = self
        self.children.append(node)

    def add_successor(self, node: "CommitNode", message: Optional[str] = None):
        """Adds a successor (a type of child) to the node, used for commits."""
        node.parent = self
        self.children.append(node)
        self.commit_message = message
        self.commit_user_name = get_user_name()
        self.commit_time = datetime.now()

    def __repr__(self) -> str:
        return f"Commit : {self.commit_id} ({self.branch}) \nAuthor : {self.commit_user_name}\nTime   : {str(self.commit_time)[:-7]}\nMessage: {self.commit_message}"

    def __getstate__(self) -> dict:
        return self.__dict__

    def __setstate__(self, state: dict):
        self.__dict__.update(state)
        if "pseudo_parents" not in state:
            self.pseudo_parents = []

    __str__ = __repr__
