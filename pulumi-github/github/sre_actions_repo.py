import pulumi
import pulumi_github as github

sre_actions_repo = github.Repository(
    resource_name = "sre_actions_repo",
    description = "for auto trigger some action managed by sre",
    has_downloads = True,
    has_issues = True,
    has_projects = True,
    has_wiki = True,
    name = "sre_actions",
    visibility = "private",
    opts = pulumi.ResourceOptions(
        protect = True
    ),
)

sre_actions_default_branch = github.BranchDefault(
    resource_name = "sre_actions_default_branch",
    branch = "main",
    repository = sre_actions_repo.name,
    rename = False,
    opts = pulumi.ResourceOptions(
        protect = True
    )
)

sre_actions_secret_ssh = github.ActionsSecret(
    resource_name = "sre_actions_secret_ssh",
    repository = sre_actions_repo.name,
    secret_name = "REPO_SSH_KEY",
    opts = pulumi.ResourceOptions(
        protect = True
    )
)

environ_dev_iam_role = github.ActionsVariable(
    resource_name = "environ_dev_iam_role",
    repository = sre_actions_repo.name,
    variable_name = "DEV_ACTION_ROLE",
    value = "arn:aws:iam::073903779593:role/SRE_ActionsRole"
)

environ_dev_artifacts_bucket = github.ActionsVariable(
    resource_name = "environ_dev_artifacts_bucket",
    repository = sre_actions_repo.name,
    variable_name = "DEV_S3_BUCKET",
    value = "vortex-build-artifacts-dev-apne1"
)

environ_dev_aws_region = github.ActionsVariable(
    resource_name = "environ_dev_aws_region",
    repository = sre_actions_repo.name,
    variable_name = "DEV_AWS_REGION",
    value = "ap-northeast-1"
)