from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    id:int
    username:str
    email:str

    class Config:
        orm_mode =True


class MovieSchema(BaseModel):
    movie_id:int
    movie_name:str
    movie_description:str
    movie_duration:str
    rating:int
    type:str


    class Config:
        orm_mode =True

class TheatreSchema(BaseModel):
    theatre_id:int
    theatre_name:str

    
    class Config:
        orm_mode =True

class SeatsSchema(BaseModel):
    seat_id:int
    seat_type:str
    seat_price:int
    
    class Config:
        orm_mode =True
class ShowsSchema(BaseModel):
    show_id:int
    theatre_id:int
    movie_id:int
    timeslot_id:int
    seats_booked:int
    seat_available:int
    
    class Config:
        orm_mode =True

class TicketBookedSchema(BaseModel):
    ticket_id:int
    movie_id:int
    id:int
    theatre_id:int
    timeslot_id:int
    seat_id:int
    show_id:int
    class Config:
        orm_mode =True
class TimeslotSchema(BaseModel):
    timeslot_id:int
    timeslot_name:str
    timeslot_starttime:str
    timeslot_endtime:int
    
    class Config:
        orm_mode =True



class UserUpdateSchema(BaseModel):
    email:str

    class Config:
        orm_mode =True

class MovieUpdateSchema(BaseModel):
    movie_name:str

    class Config:
        orm_mode =True


