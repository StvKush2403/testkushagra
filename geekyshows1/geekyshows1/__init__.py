from .depend import *
import pymysql
pymysql.install_as_MySQLdb()
print("CALLING MAIN FUNCTION")
main()