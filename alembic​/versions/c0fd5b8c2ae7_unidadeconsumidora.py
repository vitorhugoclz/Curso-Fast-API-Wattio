"""unidadeConsumidora‚Äč

Revision ID: c0fd5b8c2ae7
Revises: 4786e3d9c42b
Create Date: 2021-10-17 21:30:34.447215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0fd5b8c2ae7'
down_revision = '4786e3d9c42b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unidade_consumidora',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero_identificacao', sa.String(), nullable=True),
    sa.Column('estado', sa.String(), nullable=True),
    sa.Column('cidade', sa.String(), nullable=True),
    sa.Column('bairro', sa.String(), nullable=True),
    sa.Column('rua', sa.String(), nullable=True),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_unidade_consumidora_id'), 'unidade_consumidora', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_unidade_consumidora_id'), table_name='unidade_consumidora')
    op.drop_table('unidade_consumidora')
    # ### end Alembic commands ###
