#coding:utf-8

import MySQLdb

#############################################################################
#																			#
#								query example								#
#																			#
#############################################################################
#	db_config = {															#
#		'host': '127.0.0.1',												#
#		'port': 3306,														#
#		'user': 'root',														#
#		'passwd': '123456',													#
#		'db': 'test',														#
#		'charset': 'utf8'													#
#	}																		#
#	params = ["test_name", "test_agent"]									#
#																			#
#	query_sql = "select * from test_table where name = %s and agent=%s"		#
#	query(db_config, query_sql, params)											#
#############################################################################

def query(db_config, sql, params = []):
    try:
        connection = MySQLdb.connect(**db_config)
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql, params)
        return cursor.fetchall()
    except:
        import traceback
        traceback.print_exc()
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def insert_update(db_config, sql, params = []):
    try:
        connection = MySQLdb.connect(**db_config)
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql, params)
        connection.commit()
    except Exception, e:
        print e
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
