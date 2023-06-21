#!/usr/bin/python3
"""
Lists all ``State`` objects containing the letter ``a``

Usage:
    $ ./9-model_state_filter_a.py <user_name> <password> <database_name>

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

    for state in session.query(State).filter_by(State.name='%a%').all():
        print(f'{state.id}: {state.name}')

    session.close()
