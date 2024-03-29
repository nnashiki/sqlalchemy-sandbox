"""base

Revision ID: 0002
Revises: 0001
Create Date: 2022-08-23 08:22:24.046363+09:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 前処理
    pre_upgrade()

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tenant",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tenant")),
        sa.UniqueConstraint("name", name=op.f("uq_tenant_name")),
    )
    op.create_table(
        "teams",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenant.id"],
            name=op.f("fk_teams_tenant_id_tenant"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_teams")),
        sa.UniqueConstraint("name", name=op.f("uq_teams_name")),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenant.id"],
            name=op.f("fk_users_tenant_id_tenant"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("name", name=op.f("uq_users_name")),
    )
    # ### end Alembic commands ###

    # 後処理
    post_upgrade()


def downgrade() -> None:
    # 前処理
    pre_downgrade()

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_table("teams")
    op.drop_table("tenant")
    # ### end Alembic commands ###

    # 後処理
    post_downgrade()


def pre_upgrade():
    # スキーマ更新前に実行する必要がある処理
    pass


def post_upgrade():
    # スキーマ更新後に実行する必要がある処理
    pass


def pre_downgrade():
    # スキーマ更新前に実行する必要がある処理
    pass


def post_downgrade():
    # スキーマ更新後に実行する必要がある処理
    pass
