import pymysql
 
result_set=set()

conn=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="test",port=3306)
cursor = conn.cursor()
cursor.execute("select index_info from journal_info;")
results = cursor.fetchall()
cursor.close()
conn.close()

for row in results:
    index_information = row[0]
    temp_list=index_information.split('|')
    for each_element in temp_list:
        result_set.add(each_element)

for each_element in result_set:
    print(each_element, end=' ')