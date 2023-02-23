import sys
import psycopg2

param_dic = {
    "host"      : "localhost",
    "database"  : "exampledb",
    "user"      : "docker",
    "password"  : "docker"
}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn

def write_data_to_db(connection, table, filename):
    #HAS TO BE TRY CATCH
    cursor = connection.cursor()
    with open(filename, 'r') as f:
        next(f)
        cursor.copy_from(f, table, sep=',')

    connection.commit()
    cursor.close()

if __name__ == "__main__":
    conn = connect(param_dic)
    write_data_to_db(conn, "food_data", "food_data.csv")
