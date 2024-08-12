"""primerasd

Revision ID: 96a5652c4b9d
Revises: 
Create Date: 2024-08-12 01:15:04.514480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96a5652c4b9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accesorio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.Column('compatible_con_modelos', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('costo', sa.Float(), nullable=False),
    sa.Column('modelo', sa.String(length=100), nullable=False),
    sa.Column('marca', sa.String(length=100), nullable=False),
    sa.Column('categoria', sa.String(length=100), nullable=False),
    sa.Column('caracteristica', sa.String(length=200), nullable=False),
    sa.Column('stock', sa.String(length=100), nullable=False),
    sa.Column('proveedor', sa.String(length=100), nullable=False),
    sa.Column('accesorio', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fabricante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('pais_origen', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('contacto', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidad_disponible', sa.Integer(), nullable=False),
    sa.Column('sucursal', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modelo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('fabricante_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fabricante_id'], ['fabricante.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('modelo')
    op.drop_table('stock')
    op.drop_table('proveedor')
    op.drop_table('marca')
    op.drop_table('fabricante')
    op.drop_table('equipo')
    op.drop_table('caracteristica')
    op.drop_table('accesorio')
    # ### end Alembic commands ###
