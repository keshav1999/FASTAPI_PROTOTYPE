# import os
#
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
# load_dotenv(env_file, override=True)
# # from common.secret_manager import SecreteData
#
# key = ""
# sql_client_driver = key.DB_DRIVER
# connection_string = sql_client_driver \
#                     + key.DB_USER \
#                     + ":" + key.DB_PASS \
#                     + "@" + key.DB_HOST \
#                     + "/" + key.IVR_DB_NAME
#
# engine = create_engine(connection_string, pool_size=int(key.POOL_SIZE),
#                        connect_args={'options': '-csearch_path={}'.format(str(key.IVR_SCHEMA))}, echo=False)
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
