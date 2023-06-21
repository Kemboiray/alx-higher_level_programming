#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'

Usage:
    $ ./13-model_state_delete_a.py <user_name> <password> <database_name>

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

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)

    session.commit()
    session.close()
