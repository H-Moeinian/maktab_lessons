# name_list=['hanieh','maryam']
# new_name=input('enter your name: ')
# if new_name in name_list:
#     print('this name exists!')
#     raise Exception('this name exists')
# import sys
#
# print(sys.platform)
# assert ('linux' in sys.platform), 'this code only runs on linux'

# try:
#     name_list=['hanieh','maryam']
#     new_name=input('enter your name: ')
#     if new_name in name_list:
#         raise Exception('this name exists')
#     name_list.append(new_name)
# except:
#     print('this name exists2!')
# print(f"hello {new_name}")
# print(name_list)


# try:
#     with open('file2.log') as new_file:
#         read_file=new_file.read()
# except FileNotFoundError or ValueError as fnf_error:
#     print(fnf_error)
# except Exception as e:
#     print(e)
# else:
#     print(read_file)


# try:
#     read_file=open('file2.log')
#     read_file.write('hello')
# except Exception as e:
#     print(e)
# finally:
#     read_file.close()


