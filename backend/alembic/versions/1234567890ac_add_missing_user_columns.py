"""Add missing columns to users table

Revision ID: 1234567890ac
Revises: 1234567890ab
Create Date: 2026-02-11 23:50:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = '1234567890ac'
down_revision = '1234567890ab'
branch_labels = None
depends_on = None


def upgrade():
    # Add full_name column to users table
    op.add_column('users', sa.Column('full_name', sa.String(100), nullable=True))
    
    # Add profile_picture column to users table
    op.add_column('users', sa.Column('profile_picture', sa.String(500), nullable=True))


def downgrade():
    # Remove full_name column from users table
    op.drop_column('users', 'full_name')
    
    # Remove profile_picture column from users table
    op.drop_column('users', 'profile_picture')