from connection import connection_handler


@connection_handler
def get_applicants(cursor):
    cursor.execute("""
                    SELECT first_name FROM applicants
                   """)
    applicants = cursor.fetchall()
    return applicants
