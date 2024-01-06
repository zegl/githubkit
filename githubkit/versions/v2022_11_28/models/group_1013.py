"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoGitRefsRefPatchBody(GitHubModel):
    """ReposOwnerRepoGitRefsRefPatchBody"""

    sha: str = Field(description="The SHA1 value to set this reference to")
    force: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether to force the update or to make sure the update is a fast-forward update. Leaving this out or setting it to `false` will make sure you're not overwriting work.",
    )


model_rebuild(ReposOwnerRepoGitRefsRefPatchBody)

__all__ = ("ReposOwnerRepoGitRefsRefPatchBody",)