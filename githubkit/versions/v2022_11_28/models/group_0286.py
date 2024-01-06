"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0016 import LicenseSimple


class PullRequestPropBasePropRepo(GitHubModel):
    """PullRequestPropBasePropRepo"""

    archive_url: str = Field()
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    deployments_url: str = Field()
    description: Union[str, None] = Field()
    downloads_url: str = Field()
    events_url: str = Field()
    fork: bool = Field()
    forks_url: str = Field()
    full_name: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    hooks_url: str = Field()
    html_url: str = Field()
    id: int = Field()
    is_template: Missing[bool] = Field(default=UNSET)
    node_id: str = Field()
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    languages_url: str = Field()
    merges_url: str = Field()
    milestones_url: str = Field()
    name: str = Field()
    notifications_url: str = Field()
    owner: PullRequestPropBasePropRepoPropOwner = Field()
    private: bool = Field()
    pulls_url: str = Field()
    releases_url: str = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    url: str = Field()
    clone_url: str = Field()
    default_branch: str = Field()
    forks: int = Field()
    forks_count: int = Field()
    git_url: str = Field()
    has_downloads: bool = Field()
    has_issues: bool = Field()
    has_projects: bool = Field()
    has_wiki: bool = Field()
    has_pages: bool = Field()
    has_discussions: bool = Field()
    homepage: Union[str, None] = Field()
    language: Union[str, None] = Field()
    master_branch: Missing[str] = Field(default=UNSET)
    archived: bool = Field()
    disabled: bool = Field()
    visibility: Missing[str] = Field(
        default=UNSET,
        description="The repository visibility: public, private, or internal.",
    )
    mirror_url: Union[str, None] = Field()
    open_issues: int = Field()
    open_issues_count: int = Field()
    permissions: Missing[PullRequestPropBasePropRepoPropPermissions] = Field(
        default=UNSET
    )
    temp_clone_token: Missing[Union[str, None]] = Field(default=UNSET)
    allow_merge_commit: Missing[bool] = Field(default=UNSET)
    allow_squash_merge: Missing[bool] = Field(default=UNSET)
    allow_rebase_merge: Missing[bool] = Field(default=UNSET)
    license_: Union[None, LicenseSimple] = Field(alias="license")
    pushed_at: datetime = Field()
    size: int = Field()
    ssh_url: str = Field()
    stargazers_count: int = Field()
    svn_url: str = Field()
    topics: Missing[List[str]] = Field(default=UNSET)
    watchers: int = Field()
    watchers_count: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    allow_forking: Missing[bool] = Field(default=UNSET)
    web_commit_signoff_required: Missing[bool] = Field(default=UNSET)


class PullRequestPropBasePropRepoPropOwner(GitHubModel):
    """PullRequestPropBasePropRepoPropOwner"""

    avatar_url: str = Field()
    events_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    gravatar_id: Union[str, None] = Field()
    html_url: str = Field()
    id: int = Field()
    node_id: str = Field()
    login: str = Field()
    organizations_url: str = Field()
    received_events_url: str = Field()
    repos_url: str = Field()
    site_admin: bool = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    type: str = Field()
    url: str = Field()


class PullRequestPropBasePropRepoPropPermissions(GitHubModel):
    """PullRequestPropBasePropRepoPropPermissions"""

    admin: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    push: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)
    pull: bool = Field()


model_rebuild(PullRequestPropBasePropRepo)
model_rebuild(PullRequestPropBasePropRepoPropOwner)
model_rebuild(PullRequestPropBasePropRepoPropPermissions)

__all__ = (
    "PullRequestPropBasePropRepo",
    "PullRequestPropBasePropRepoPropOwner",
    "PullRequestPropBasePropRepoPropPermissions",
)