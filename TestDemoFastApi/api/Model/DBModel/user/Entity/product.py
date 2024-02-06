from sqlalchemy import Column, Integer, String, MetaData, Table

metadata = MetaData()


class ProductEntity:
    product = Table('cxx_product', metadata,
                    Column('product_id', Integer, primary_key=True, nullable=False),
                    Column('product_name', String(20), nullable=False),
                    Column('product_size', String(20), nullable=False),
                    Column('product_color', String(20), nullable=False),
                    Column('product_system', String(20), nullable=False),
                    Column('product_price', String(20), nullable=False),
                    Column('phone_number', String(20), nullable=False),
                    Column('phone_putaway_time', String(20), nullable=False),
                    Column('product_is_delete', String(20), nullable=False),
                    Column('product_is_putaway', String(20), nullable=False),
                    Column('create_time', String(20), nullable=False)
                    )


productEntity = ProductEntity()
