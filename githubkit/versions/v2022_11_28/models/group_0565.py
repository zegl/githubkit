"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0351 import EnterpriseWebhooks
from .group_0352 import SimpleInstallation
from .group_0354 import RepositoryWebhooks
from .group_0355 import SimpleUserWebhooks
from .group_0353 import OrganizationSimpleWebhooks


class WebhookMarketplacePurchasePurchased(GitHubModel):
    """marketplace_purchase purchased event"""

    action: Literal["purchased"] = Field()
    effective_date: str = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    marketplace_purchase: WebhookMarketplacePurchasePurchasedPropMarketplacePurchase = (
        Field()
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    previous_marketplace_purchase: Missing[
        WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchase
    ] = Field(default=UNSET, title="Marketplace Purchase")
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchase(GitHubModel):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchase"""

    account: WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedAccount = (
        Field()
    )
    billing_cycle: str = Field()
    free_trial_ends_on: Union[Union[str, None], None] = Field()
    next_billing_date: Union[Union[str, None], None] = Field()
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedPlan = Field()
    unit_count: int = Field()


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedAccount"""

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[Union[str, None], None] = Field()
    type: str = Field()


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedPlan(GitHubModel):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedPlan"""

    bullets: List[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[Union[str, None], None] = Field()
    yearly_price_in_cents: int = Field()


class WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchase(GitHubModel):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccount = (
        Field()
    )
    billing_cycle: str = Field()
    free_trial_ends_on: None = Field()
    next_billing_date: Missing[Union[str, None]] = Field(default=UNSET)
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlan = (
        Field()
    )
    unit_count: int = Field()


class WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccount"""

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[str, None] = Field()
    type: str = Field()


class WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlan"""

    bullets: List[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[str, None] = Field()
    yearly_price_in_cents: int = Field()


model_rebuild(WebhookMarketplacePurchasePurchased)
model_rebuild(WebhookMarketplacePurchasePurchasedPropMarketplacePurchase)
model_rebuild(WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedAccount)
model_rebuild(WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedPlan)
model_rebuild(WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchase)
model_rebuild(
    WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccount
)
model_rebuild(
    WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlan
)

__all__ = (
    "WebhookMarketplacePurchasePurchased",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchase",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedAccount",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseMergedPlan",
    "WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchase",
    "WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccount",
    "WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlan",
)