"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0005 import IntegrationType


class DeploymentType(TypedDict):
    """Deployment

    A request for a specific ref(branch,sha,tag) to be deployed
    """

    url: str
    id: int
    node_id: str
    sha: str
    ref: str
    task: str
    payload: Union[DeploymentPropPayloadOneof0Type, str]
    original_environment: NotRequired[str]
    environment: str
    description: Union[str, None]
    creator: Union[None, SimpleUserType]
    created_at: datetime
    updated_at: datetime
    statuses_url: str
    repository_url: str
    transient_environment: NotRequired[bool]
    production_environment: NotRequired[bool]
    performed_via_github_app: NotRequired[Union[None, IntegrationType]]


class DeploymentPropPayloadOneof0Type(TypedDict):
    """DeploymentPropPayloadOneof0"""


__all__ = (
    "DeploymentType",
    "DeploymentPropPayloadOneof0Type",
)