from pydantic import BaseModel
from typing import List,Optional

class Node(BaseModel):
    id: str
    label: str
    concepts:list[str]
    usesfull_where:list[str]
    resources_website:str
    projects:list[str]

class Edge(BaseModel):
    from_node: str
    to_node: str

class reply(BaseModel):
    answer:Optional[str]=None
class RoadmapGraph(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
    reply:reply