"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import exclude_unset

from .models import ActionsBillingUsage, CombinedBillingUsage, PackagesBillingUsage

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class BillingClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_github_actions_billing_org(
        self,
        org: str,
    ) -> "Response[ActionsBillingUsage]":
        url = f"/orgs/{org}/settings/billing/actions"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    async def async_get_github_actions_billing_org(
        self,
        org: str,
    ) -> "Response[ActionsBillingUsage]":
        url = f"/orgs/{org}/settings/billing/actions"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    def get_github_packages_billing_org(
        self,
        org: str,
    ) -> "Response[PackagesBillingUsage]":
        url = f"/orgs/{org}/settings/billing/packages"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    async def async_get_github_packages_billing_org(
        self,
        org: str,
    ) -> "Response[PackagesBillingUsage]":
        url = f"/orgs/{org}/settings/billing/packages"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    def get_shared_storage_billing_org(
        self,
        org: str,
    ) -> "Response[CombinedBillingUsage]":
        url = f"/orgs/{org}/settings/billing/shared-storage"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )

    async def async_get_shared_storage_billing_org(
        self,
        org: str,
    ) -> "Response[CombinedBillingUsage]":
        url = f"/orgs/{org}/settings/billing/shared-storage"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )

    def get_github_actions_billing_user(
        self,
        username: str,
    ) -> "Response[ActionsBillingUsage]":
        url = f"/users/{username}/settings/billing/actions"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    async def async_get_github_actions_billing_user(
        self,
        username: str,
    ) -> "Response[ActionsBillingUsage]":
        url = f"/users/{username}/settings/billing/actions"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ActionsBillingUsage,
        )

    def get_github_packages_billing_user(
        self,
        username: str,
    ) -> "Response[PackagesBillingUsage]":
        url = f"/users/{username}/settings/billing/packages"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    async def async_get_github_packages_billing_user(
        self,
        username: str,
    ) -> "Response[PackagesBillingUsage]":
        url = f"/users/{username}/settings/billing/packages"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=PackagesBillingUsage,
        )

    def get_shared_storage_billing_user(
        self,
        username: str,
    ) -> "Response[CombinedBillingUsage]":
        url = f"/users/{username}/settings/billing/shared-storage"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )

    async def async_get_shared_storage_billing_user(
        self,
        username: str,
    ) -> "Response[CombinedBillingUsage]":
        url = f"/users/{username}/settings/billing/shared-storage"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CombinedBillingUsage,
        )
