# This file is a preliminary file, it works as it should but there are some limitations
# Limitiations:
# 1. Only run this file ONCE upon start up to populate the database, once the database is populated, running this code will cause a crash to occur
# 2. If you find any other errors such as value errors please contact me ASAP to fix (open an issue on Github)

# The .json file that we are parsing is called drugs.json, this filename is not the original from the fda website, please rename the file before running
# to prevent errors
# The original .json file can be found here https://open.fda.gov/apis/drug/drugsfda/download/
#TODO: Text search is working but is not efficient, will be updated in the next push. 
#TODO: Collate everything into a migration file instead of querying manually, will be updated in the next push
#Update: deleted tsvector

import psycopg2, psycopg2.extensions, psycopg2.extras
import pandas as pd
import json

connection = psycopg2.connect("dbname=postgres user=postgres_user password=postgres_password host=127.0.0.1 port=5000") 


def create_staging_table(cursor):
    cursor.execute("""
        DROP 
            TABLE 
        IF EXISTS 
        product;
        CREATE TYPE mkt_status AS ENUM ('Discontinued', 'Over-the-counter', 'Prescription', 'None (Tentative Approval)' );
        CREATE TABLE product (
            id BIGSERIAL NOT NULL PRIMARY KEY,
            reference_drug F,
            brand_name VARCHAR(64),
            reference_standard VARCHAR(64),
            dosage_form VARCHAR(64),
            route VARCHAR(64),
            marketing_status mkt_status,
        );
        CREATE TABLE ingredient (
            id BIGSERIAL PRIMARY KEY,
            name VARCHAR(128),
            strength VARCHAR(64)
        );
        CREATE TABLE ingredient_product (
            ingredient_id BIGINT,
            product_id BIGINT,
            PRIMARY KEY (product_id, ingredient_id)
        );
        """)

with connection.cursor() as cur:
    # create_staging_table(cursor)
    f = open('drugs.json')
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    print(data.keys())

    for sub in data['results']:
        if 'products' in sub.keys():
            for p in sub['products']:
                "INSERT INTO ({}, {}) products {}"
                cur.execute("""
                    INSERT INTO product (reference_drug, brand_name, reference_standard, dosage_form, route, marketing_status)
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """,
                    (p['reference_drug'], p['brand_name'], p['reference_standard'] if 'reference_standard' in p.keys() else 'No', p['dosage_form'], p['route'], p['marketing_status'] if p['marketing_status'] != ' ' else 'None (Tentative Approval)'))

    
    # psycopg2.extras.execute_batch(cur, insert_stmt, df.values)
    connection.commit()