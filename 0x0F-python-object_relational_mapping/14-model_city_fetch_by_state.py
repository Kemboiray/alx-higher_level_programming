#!/usr/bin/python3
"""
Prints all ``City`` objects from a database

Usage:
    $ ./14-model_city_fetch_by_state.py <user_name> <password> <database_name>

"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:'
                           + f'{sys.argv[2]}@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City)\
            .filter(City.state_id == State.id)\
            .order_by(City.id):
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
