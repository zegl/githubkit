"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import exclude_unset

from .models import BasicError, CodeOfConduct

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class CodesOfConductClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_all_codes_of_conduct(
        self,
    ) -> "Response[List[CodeOfConduct]]":
        url = "/codes_of_conduct"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeOfConduct],
        )

    async def async_get_all_codes_of_conduct(
        self,
    ) -> "Response[List[CodeOfConduct]]":
        url = "/codes_of_conduct"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeOfConduct],
        )

    def get_conduct_code(
        self,
        key: str,
    ) -> "Response[CodeOfConduct]":
        url = f"/codes_of_conduct/{key}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeOfConduct,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_conduct_code(
        self,
        key: str,
    ) -> "Response[CodeOfConduct]":
        url = f"/codes_of_conduct/{key}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeOfConduct,
            error_models={
                "404": BasicError,
            },
        )
