#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import create_engine, MetaData, Table, exc
import openfoodfacts

# connect to server
engine = create_engine(
    'postgresql+psycopg2://pur_beurre_web_app:Hummm@localhost/db_pur_beurre')
conn = engine.connect()
metadata = MetaData()
# Construct Product table
Product = Table("product_product", metadata, autoload=True, autoload_with=engine)

# make request page per page to get all products
new_request = True
prod_saved = 0
i = 13990
while new_request is True:
    page_prods = openfoodfacts.products.get_by_facets(
        {'country': 'france'}, page=i, locale="fr"
    )
    if page_prods == []:
        new_request = False
    else:
        for product in page_prods:
            # insert each product in db
            try:
                product["brands"]
            except KeyError:
                product["brands"] = ""
            try:
                nutrient_level = product["nutrient_levels"]
                fat = nutrient_level["fat"]
                salt = nutrient_level["salt"]
                sugars = nutrient_level["sugars"]
                saturated_fat = nutrient_level["saturated-fat"]
            except KeyError:
                fat = ""
                salt = ""
                sugars = ""
                saturated_fat = ""
            try:
                nutriments = product["nutriments"]
                fat_100g = nutriments["fat"]
                salt_100g = nutriments["salt"]
                saturated_fat_100g = nutriments["saturated-fat_100g"]
                sugars_100g = nutriments["sugars_100g"]
            except KeyError:
                fat_100g = ""
                salt_100g = ""
                saturated_fat_100g = ""
                sugars_100g = ""
            try:
                new_product = Product.insert().values(
                    code = product["code"],
                    product_name = product["product_name"],
                    brands = product["brands"],
                    categories = product["categories"],
                    nutrition_grades = product["nutrition_grades"],
                    url = product["url"],
                    image_url = product["image_url"], # big
                    image_small_url = product["image_small_url"], # small
                    fat = fat,
                    salt = salt,
                    saturated_fat = saturated_fat,
                    sugars = sugars,
                    fat_100g = fat_100g,
                    saturated_fat_100g = saturated_fat_100g,
                    sugars_100g = sugars_100g,
                    salt_100g = salt_100g,
                )
            except KeyError:
                pass
            else:
                try:
                    conn.execute(new_product)
                except exc.DataError:
                    pass
                else:
                    prod_saved += 1 
        print("".join(["page ", str(i), " OK!!!  product saved = ", str(prod_saved)]))
        i += 1

conn.close()
