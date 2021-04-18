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

# import logging
# logging.basicConfig(level=logging.DEBUG,filename='test.log',filemode='w',
#                     format='%(levelname)s-%(asctime)s-%(name)s-%(message)s',datefmt='%d-%b-%y %H:%M:%S')
# logging.debug('a')
# logging.info('b')
# logging.warning('c')
# logging.error('d')
# logging.critical('e')
#
# a = 10
# b = 0
# try:
#     div = a/b
# except ZeroDivisionError as e:
#     logging.error("Exception occured",exc_info=True)


# import logging
# logger=logging.getLogger('logger1')
# file_handler = logging.FileHandler('file.log')
# std_handler = logging.StreamHandler()
# std_handler.setLevel(logging.DEBUG)
# file_handler.setLevel(logging.INFO)
# s_format= logging.Formatter('%(levelname)s-%(asctime)s-%(name)s-%(message)s')
# n_format = logging.Formatter('%(levelname)s-%(asctime)s-%(message)s')
# std_handler.setFormatter(s_format)
# file_handler.setFormatter(n_format)
# logger.addHandler(std_handler)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
# logger.debug('This is just an information')
# logger.error('This is an error')




#code ostad
# import logging
# my_logger = logging.getLogger('logger1')
# #create handlers
# file_handler = logging.FileHandler('file.log')
# std_handler = logging.StreamHandler()
# #set level for handlers
# file_handler.setLevel(logging.WARNING)
# std_handler.setLevel(logging.ERROR)
# #create format for handlers
# s_format = logging.Formatter('%(levelname)s-%(asctime)s-%(name)s-%(message)s')
# n_format = logging.Formatter('%(levelname)s*%(asctime)s -%(message)s')
# file_handler.setFormatter(s_format)
# std_handler.setFormatter(n_format)
# #add handlers to logger
# my_logger.addHandler(file_handler)
# my_logger.addHandler(std_handler)
# my_logger.setLevel(logging.DEBUG)
# my_logger.warning('This is just an information')
# my_logger.error('This is an error')