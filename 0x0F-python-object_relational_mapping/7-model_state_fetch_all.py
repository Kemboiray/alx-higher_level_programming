#!/usr/bin/python3
"""Start link class to table in database
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
    for state in session.query(State).order_by(State.id).all():
        print(f'{state.id}: {state.name}')
    session.close()
