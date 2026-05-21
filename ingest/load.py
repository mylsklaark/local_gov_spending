import logging
import duckdb
import pathlib

def connect_to_database():
    logging.info("Connecting to the database...")
    path = pathlib.Path(__file__).parent.parent / "transform" / "dev.duckdb"
    conn = duckdb.connect(str(path))
    return conn

def read_xlsx_files():
    logging.info("Fetching data to load...")
    file_names = []
    path = pathlib.Path(__file__).parent.parent / "data"
    for file in path.glob("*.xlsx"):
        logging.info(f"Reading file: {file}")
        file_names.append(file)
    return file_names

def load_data(connection, data):
    logging.info("Loading data into the database...")
    for i, file in enumerate(data):
        if i == 0:
            connection.execute(f"CREATE OR REPLACE TABLE raw_spending AS SELECT * FROM read_xlsx('{file}')")
        else:
            connection.execute(f"INSERT INTO raw_spending SELECT * FROM read_xlsx('{file}')")
        logging.info(f"Data from {file} loaded successfully. {i+1} of {len(data)}")
    connection.close()
    
def main():
    logging.basicConfig(level=logging.INFO)
    connection = connect_to_database()
    data = read_xlsx_files()
    load_data(connection, data)
    
if __name__ == "__main__":
    main()