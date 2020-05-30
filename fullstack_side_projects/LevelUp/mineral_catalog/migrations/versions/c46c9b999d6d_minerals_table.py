"""minerals table

Revision ID: c46c9b999d6d
Revises: 
Create Date: 2020-05-30 16:35:28.190792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c46c9b999d6d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('minerals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('img_filename', sa.String(length=255), nullable=True),
    sa.Column('img_caption', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('formula', sa.String(length=255), nullable=True),
    sa.Column('strunz_classification', sa.String(length=255), nullable=True),
    sa.Column('crystal_system', sa.String(length=255), nullable=True),
    sa.Column('unit_cell', sa.String(length=255), nullable=True),
    sa.Column('color', sa.String(length=255), nullable=True),
    sa.Column('crystal_symmetry', sa.String(length=255), nullable=True),
    sa.Column('cleavage', sa.String(length=255), nullable=True),
    sa.Column('mohs_hardness', sa.String(length=255), nullable=True),
    sa.Column('luster', sa.String(length=255), nullable=True),
    sa.Column('streak', sa.String(length=255), nullable=True),
    sa.Column('diaphaneity', sa.String(length=255), nullable=True),
    sa.Column('optical_properties', sa.String(length=255), nullable=True),
    sa.Column('refractive_index', sa.String(length=255), nullable=True),
    sa.Column('crystal_habit', sa.String(length=255), nullable=True),
    sa.Column('specific_gravity', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('minerals')
    # ### end Alembic commands ###
