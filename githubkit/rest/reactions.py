"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, Literal

from githubkit.utils import UNSET, Unset, exclude_unset

from .types import (
    ReposOwnerRepoCommentsCommentIdReactionsPostBodyType,
    ReposOwnerRepoIssuesIssueNumberReactionsPostBodyType,
    ReposOwnerRepoReleasesReleaseIdReactionsPostBodyType,
    ReposOwnerRepoPullsCommentsCommentIdReactionsPostBodyType,
    ReposOwnerRepoIssuesCommentsCommentIdReactionsPostBodyType,
    TeamsTeamIdDiscussionsDiscussionNumberReactionsPostBodyType,
    OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberReactionsPostBodyType,
    TeamsTeamIdDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBodyType,
    OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBodyType,
)
from .models import (
    Reaction,
    BasicError,
    ValidationError,
    ReposOwnerRepoCommentsCommentIdReactionsPostBody,
    ReposOwnerRepoIssuesIssueNumberReactionsPostBody,
    ReposOwnerRepoReleasesReleaseIdReactionsPostBody,
    ReposOwnerRepoPullsCommentsCommentIdReactionsPostBody,
    ReposOwnerRepoIssuesCommentsCommentIdReactionsPostBody,
    TeamsTeamIdDiscussionsDiscussionNumberReactionsPostBody,
    OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberReactionsPostBody,
    TeamsTeamIdDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBody,
    OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBody,
)

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


class ReactionsClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_for_team_discussion_comment_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    async def async_list_for_team_discussion_comment_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    def create_for_team_discussion_comment_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        json = OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(
            by_alias=True
        )

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )

    async def async_create_for_team_discussion_comment_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        json = OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(
            by_alias=True
        )

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )

    def delete_for_team_discussion_comment(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_for_team_discussion_comment(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_for_team_discussion_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    async def async_list_for_team_discussion_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    def create_for_team_discussion_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions"

        json = OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )

    async def async_create_for_team_discussion_in_org(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions"

        json = OrgsOrgTeamsTeamSlugDiscussionsDiscussionNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )

    def delete_for_team_discussion(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_for_team_discussion(
        self,
        org: str,
        team_slug: str,
        discussion_number: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_for_commit_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    async def async_list_for_commit_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    def create_for_commit_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"

        json = ReposOwnerRepoCommentsCommentIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    async def async_create_for_commit_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"

        json = ReposOwnerRepoCommentsCommentIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    def delete_for_commit_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_for_commit_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_for_issue_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    async def async_list_for_issue_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    def create_for_issue_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"

        json = ReposOwnerRepoIssuesCommentsCommentIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    async def async_create_for_issue_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"

        json = ReposOwnerRepoIssuesCommentsCommentIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    def delete_for_issue_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_for_issue_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_for_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
                "410": BasicError,
            },
        )

    async def async_list_for_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
                "410": BasicError,
            },
        )

    def create_for_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"

        json = ReposOwnerRepoIssuesIssueNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    async def async_create_for_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"

        json = ReposOwnerRepoIssuesIssueNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    def delete_for_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_for_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_for_pull_request_review_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    async def async_list_for_pull_request_review_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    def create_for_pull_request_review_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"

        json = ReposOwnerRepoPullsCommentsCommentIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    async def async_create_for_pull_request_review_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"

        json = ReposOwnerRepoPullsCommentsCommentIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    def delete_for_pull_request_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        reaction_id: int,
    ) -> "Response":
        url = (
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}"
        )

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_for_pull_request_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        reaction_id: int,
    ) -> "Response":
        url = (
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}"
        )

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_for_release(
        self,
        owner: str,
        repo: str,
        release_id: int,
        content: Union[
            Unset, Literal["+1", "laugh", "heart", "hooray", "rocket", "eyes"]
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/releases/{release_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    async def async_list_for_release(
        self,
        owner: str,
        repo: str,
        release_id: int,
        content: Union[
            Unset, Literal["+1", "laugh", "heart", "hooray", "rocket", "eyes"]
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/repos/{owner}/{repo}/releases/{release_id}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
            error_models={
                "404": BasicError,
            },
        )

    def create_for_release(
        self,
        owner: str,
        repo: str,
        release_id: int,
        *,
        content: Literal["+1", "laugh", "heart", "hooray", "rocket", "eyes"],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/releases/{release_id}/reactions"

        json = ReposOwnerRepoReleasesReleaseIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    async def async_create_for_release(
        self,
        owner: str,
        repo: str,
        release_id: int,
        *,
        content: Literal["+1", "laugh", "heart", "hooray", "rocket", "eyes"],
    ) -> "Response[Reaction]":
        url = f"/repos/{owner}/{repo}/releases/{release_id}/reactions"

        json = ReposOwnerRepoReleasesReleaseIdReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
            error_models={
                "422": ValidationError,
            },
        )

    def delete_for_release(
        self,
        owner: str,
        repo: str,
        release_id: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/releases/{release_id}/reactions/{reaction_id}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_for_release(
        self,
        owner: str,
        repo: str,
        release_id: int,
        reaction_id: int,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/releases/{release_id}/reactions/{reaction_id}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_for_team_discussion_comment_legacy(
        self,
        team_id: int,
        discussion_number: int,
        comment_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    async def async_list_for_team_discussion_comment_legacy(
        self,
        team_id: int,
        discussion_number: int,
        comment_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    def create_for_team_discussion_comment_legacy(
        self,
        team_id: int,
        discussion_number: int,
        comment_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        json = TeamsTeamIdDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(
            by_alias=True
        )

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )

    async def async_create_for_team_discussion_comment_legacy(
        self,
        team_id: int,
        discussion_number: int,
        comment_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"

        json = TeamsTeamIdDiscussionsDiscussionNumberCommentsCommentNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(
            by_alias=True
        )

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )

    def list_for_team_discussion_legacy(
        self,
        team_id: int,
        discussion_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    async def async_list_for_team_discussion_legacy(
        self,
        team_id: int,
        discussion_number: int,
        content: Union[
            Unset,
            Literal[
                "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
            ],
        ] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[Reaction]]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/reactions"

        params = {
            "content": content,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[Reaction],
        )

    def create_for_team_discussion_legacy(
        self,
        team_id: int,
        discussion_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/reactions"

        json = TeamsTeamIdDiscussionsDiscussionNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )

    async def async_create_for_team_discussion_legacy(
        self,
        team_id: int,
        discussion_number: int,
        *,
        content: Literal[
            "+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"
        ],
    ) -> "Response[Reaction]":
        url = f"/teams/{team_id}/discussions/{discussion_number}/reactions"

        json = TeamsTeamIdDiscussionsDiscussionNumberReactionsPostBody(
            **{
                "content": content,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=Reaction,
        )