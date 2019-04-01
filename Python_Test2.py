import pymysql
import json
 
result_set=set()
conn=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="test",port=3306)
cursor = conn.cursor()

cursor.execute("select id,basic_info,publish_info, evaluate_info from journal_info;")
results = cursor.fetchall()

for row in results:
    temp_dict_basic_information={}
    temp_dict_publish_information={}
    temp_dict_evaluate_information={}
    id_index = str(row[0])
    basic_information = row[1].replace(' ','').replace('\n','')
    publish_information = row[2].replace(' ','').replace('\n','')
    evaluate_information = row[3].replace(' ','').replace('\n','')

    index_1 = basic_information.find('曾用刊名：')
    index_2 = basic_information.find('主办单位：')
    index_3 = basic_information.find('出版周期：')
    index_4 = basic_information.find('ISSN：')
    index_5 = basic_information.find('CN：')
    index_6 = basic_information.find('出版地：')
    index_7 = basic_information.find('语种：')
    index_8 = basic_information.find('开本：')
    index_9 = basic_information.find('邮发代号：')
    index_10 = basic_information.find('创刊时间：')
    index_11 = publish_information.find('专辑名称：')
    index_12 = publish_information.find('专题名称：')
    index_13 = publish_information.find('出版文献量：')
    index_14 = publish_information.find('总下载次数：')
    index_15 = publish_information.find('总被引次数：')
    index_16 = evaluate_information.find('（2018版）复合影响因子：')
    index_17 = evaluate_information.find('（2018版）综合影响因子：')
    index_18 = evaluate_information.find('该刊被以下数据库收录：')
    index_19 = evaluate_information.find('来源期刊：')
    index_20 = evaluate_information.find('期刊荣誉：')

    if(index_1 != -1):
        temp_dict_basic_information['曾用刊名'] =  basic_information[index_1+5:index_2] 
    if(index_2 != -1):
        temp_dict_basic_information['主办单位'] =  basic_information[index_2+5:index_3]
    if(index_3 != -1):
        temp_dict_basic_information['出版周期'] =  basic_information[index_3+5:index_4]
    if(index_4 != -1):
        temp_dict_basic_information['ISSN'] =  basic_information[index_4+5:index_5]
    if(index_5 != -1):
        temp_dict_basic_information['CN'] =  basic_information[index_5+3:index_6]
    if(index_6 != -1):
        temp_dict_basic_information['出版地'] =  basic_information[index_6+4:index_7]
    if(index_7 != -1):
        temp_dict_basic_information['语种'] =  basic_information[index_7+3:index_8]
    if(index_8 != -1):
        temp_dict_basic_information['开本'] =  basic_information[index_8+3:index_9]
    if(index_9 != -1):
        temp_dict_basic_information['邮发代号'] =  basic_information[index_9+5:index_10]
    if(index_10 != -1):
        temp_dict_basic_information['创刊时间'] =  basic_information[index_10+5:]
    if(index_11 != -1):
        temp_dict_publish_information['专辑名称'] =  publish_information[index_11+5:index_12]
    if(index_12 != -1):
        temp_dict_publish_information['专题名称'] =  publish_information[index_12+5:index_13]
    if(index_13 != -1):
        temp_dict_publish_information['出版文献量'] =  publish_information[index_13+6:index_14]
    if(index_14 != -1):
        temp_dict_publish_information['总下载次数'] =  publish_information[index_14+6:index_15]
    if(index_15 != -1):
        temp_dict_publish_information['总被引次数'] =  publish_information[index_15+6:]
    if(index_16 != -1):
        temp_dict_evaluate_information['（2018版）复合影响因子'] =  evaluate_information[index_16+14:index_17]
    if(index_17 != -1):
        temp_dict_evaluate_information['（2018版）综合影响因子'] =  evaluate_information[index_17+14:index_18]
    if(index_18 != -1):
        temp_dict_evaluate_information['该刊被以下数据库收录'] =  evaluate_information[index_18+11:index_19]
    if(index_19 != -1):
        temp_dict_evaluate_information['来源期刊'] =  evaluate_information[index_19+5:index_20]
    if(index_20 != -1):
        temp_dict_evaluate_information['期刊荣誉'] =  evaluate_information[index_20+5:]
    
    temp_json_string_basic = json.dumps(temp_dict_basic_information, ensure_ascii=False)
    temp_json_string_publish = json.dumps(temp_dict_publish_information, ensure_ascii=False)
    temp_json_string_evaluate = json.dumps(temp_dict_evaluate_information, ensure_ascii=False)
    cursor.execute("update journal_info set basic_info = '"+temp_json_string_basic+"' where id = "+id_index)
    cursor.execute("update journal_info set publish_info = '"+temp_json_string_publish+"' where id = "+id_index)
    cursor.execute("update journal_info set evaluate_info = '"+temp_json_string_evaluate+"' where id = "+id_index)
    conn.commit()

cursor.close()
conn.close()
print('Test finished')


