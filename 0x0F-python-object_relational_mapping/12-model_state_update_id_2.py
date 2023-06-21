#!/usr/bin/python3
"""
Changes the name of a ``State`` object with id = 2

Usage:
    $ ./12-model_state_update_id_2.py <user_name> <password> <database_name>

"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:'
                           + f'{sys.argv[2]}@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
