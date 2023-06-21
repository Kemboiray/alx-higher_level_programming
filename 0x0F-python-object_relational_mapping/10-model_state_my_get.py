#!/usr/bin/python3
"""
Lists the ``State`` object matching the name provided as a command-line
argument

Usage:
    $ ./10-model_state_my_get.py <user_name> <password> <database_name>

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

    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state:
        print(f'{state.id}')
    else:
        print('Not found')
    session.close()
