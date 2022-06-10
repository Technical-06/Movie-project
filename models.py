from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey


class User(Base):
    __tablename__= "users"
    id=Column(Integer,primary_key=True,index=True)
    username = Column(String(255))
    email=Column(String(255))


class Movie(Base):
    __tablename__="movies"
    movie_id=Column(Integer,primary_key=True,index=True)
    movie_name=Column(String(255))
    movie_description=Column(String(255))
    movie_duration=Column(String(255))
    rating=Column(Integer())
    type=Column(String(255))
    
class Shows(Base):
    __tablename__="shows"
    show_id=Column(Integer,primary_key=True,index=True)
    theatre_id=Column(Integer, ForeignKey('theatre.theatre_id'))
    movie_id=Column(Integer, ForeignKey('movies.movie_id'))
    timeslot_id=Column(Integer, ForeignKey('timeslot.timeslot_id'))
    seats_booked=Column(Integer())
    seat_available=Column(Integer())
    

class Theatre(Base):
    __tablename__="theatre"
    theatre_id=Column(Integer,primary_key=True,index=True)
    theatre_name = Column(String(255))
    
    
    
class Seats(Base):
    __tablename__="seats"
    seat_id=Column(Integer,primary_key=True,index=True)
    seat_type=Column(Integer())
    seat_price=Column(Integer())
    
class timeslot(Base):
    __tablename__="timeslot"
    timeslot_id=Column(Integer,primary_key=True,index=True)
    timeslot_name=Column(String(255))
    timeslot_starttime=Column(String(255))
    timeslot_endtime=Column(Integer())
class TicketBooked(Base):
    __tablename__="Ticket_Booked"
    ticket_id=Column(Integer,primary_key=True,index=True)
    movie_id = Column(Integer, ForeignKey('movies.movie_id'))
    id = Column(Integer, ForeignKey('users.id'))
    theatre_id =Column(Integer, ForeignKey('theatre.theatre_id'))
    timeslot_id=Column(Integer, ForeignKey('timeslot.timeslot_id'))
    seat_id=Column(Integer, ForeignKey('seats.seat_id'))
    show_id=Column(Integer, ForeignKey('shows.show_id'))
