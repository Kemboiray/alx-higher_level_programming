#!/usr/bin/python3
"""
Adds ``State`` object 'Louisiana' to a database

Usage:
    $ ./11-model_state_insert.py <user_name> <password> <database_name>

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
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
