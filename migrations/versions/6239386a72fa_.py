"""empty message

Revision ID: 6239386a72fa
Revises: b5d2284c7039
Create Date: 2021-02-19 11:51:11.486703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6239386a72fa'
down_revision = 'b5d2284c7039'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###