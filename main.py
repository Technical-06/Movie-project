from fastapi import FastAPI
from typing import List
from fastapi.params import Depends
import models,schemas
from database import SessionLocal,engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import pymysql, pandas as pd
from database import con
import json


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
@app.get('/getusers/',response_model=List[schemas.UserSchema])
def show_users(db:Session=Depends(get_db)):
    obj = db.query(models.User).all()
    return obj
@app.post('/createuser/',response_model=schemas.UserSchema)
def create_users(item:schemas.UserSchema,db:Session=Depends(get_db)):
    obj = models.User(id=item.id,
                      username = item.username,
                      email=item.email)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
@app.put('/updateuser/{user_id}',response_model=schemas.UserSchema)
def update_users(user_id:int,item:schemas.UserUpdateSchema,db:Session=Depends(get_db)):
    obj = db.query(models.User).filter_by(id=user_id).first()
    obj.email=item.email
    db.commit()
    db.refresh(obj)
    return obj
@app.delete('/deleteuser/{user_id}',response_model=schemas.UserSchema)
def delete_users(user_id:int,db:Session=Depends(get_db)):
    obj = db.query(models.User).filter_by(id=user_id).first()
    db.delete(obj)
    db.commit()
    return obj
@app.get('/getmovies/',response_model=List[schemas.MovieSchema])
def show_users(db:Session=Depends(get_db)):
    obj = db.query(models.Movie).all()
    return obj

@app.get('/getshows/',response_model=List[schemas.MovieSchema])
def show_users(db:Session=Depends(get_db)):
    obj = db.query(models.Shows).all()
    return obj

@app.post('/createshows/',response_model=schemas.ShowsSchema)
def create_users(item:schemas.ShowsSchema,db:Session=Depends(get_db)):
    obj = models.Shows(show_id=item.show_id,
                      theatre_id=item.theatre_id,
                      movie_id = item.movie_id,
                      timeslot_id=item.timeslot_id,
                      seat_available=item.seat_available,
                      seats_booked=item.seats_booked,
                      )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj



@app.post('/createmovies/',response_model=schemas.MovieSchema)
def create_users(item:schemas.MovieSchema,db:Session=Depends(get_db)):
    obj = models.Movie(movie_id=item.movie_id,
                      movie_name = item.movie_name,
                      movie_description=item.movie_description,
                      movie_duration=item.movie_duration,
                      rating=item.rating,
                      type=item.type,
                      )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
@app.put('/updatemovie/{movie_id}',response_model=schemas.MovieUpdateSchema)
def update_users(movie_id:int,item:schemas.MovieUpdateSchema,db:Session=Depends(get_db)):
    obj = db.query(models.Movie).filter_by(movie_id=movie_id).first()
    obj.movie_name=item.movie_name
    db.commit()
    db.refresh(obj)
    return obj
@app.delete('/deletemovie/{movie_id}',response_model=schemas.MovieSchema)
def delete_users(movie_id:int,db:Session=Depends(get_db)):
    obj = db.query(models.Movie).filter_by(movie_id=movie_id).first()
    db.delete(obj)
    db.commit()
    return obj
@app.get('/gettheatre/',response_model=List[schemas.TheatreSchema])
def show_threater(db:Session=Depends(get_db)):
    obj = db.query(models.Theatre).all()
    return obj

@app.post('/createthreatre/',response_model=schemas.TheatreSchema)
def create_users(item:schemas.TheatreSchema,db:Session=Depends(get_db)):
    obj = models.Theatre(theatre_id=item.theatre_id,
                      theatre_name = item.theatre_name,
                            )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@app.get('/getseats/',response_model=List[schemas.SeatsSchema])
def show_seats(db:Session=Depends(get_db)):
    obj = db.query(models.Seats).all()
    return obj
@app.post('/createseats/',response_model=schemas.SeatsSchema)
def create_seats(item:schemas.SeatsSchema,db:Session=Depends(get_db)):
    obj = models.Seats(seat_id=item.seat_id,
                      seat_type = item.seat_type,
                      seat_price=item.seat_price,
                      )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
@app.get('/getslots/',response_model=List[schemas.TimeslotSchema])
def show_timeslot(db:Session=Depends(get_db)):
    obj = db.query(models.timeslot).all()
    return obj
@app.post('/createslots/',response_model=schemas.TimeslotSchema)
def create_users(item:schemas.TimeslotSchema,db:Session=Depends(get_db)):
    obj = models.timeslot(timeslot_id=item.timeslot_id,
                      timeslot_name = item.timeslot_name,
                      timeslot_starttime=item.timeslot_starttime,
                      timeslot_endtime=item.timeslot_endtime
                      )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


# @app.get('/gettickets/',response_model=List[schemas.TicketBookedSchema])
@app.get('/gettickets/{ticket.id}')
def show_tickets(db:Session=Depends(get_db)):
    obj = db.query(models.TicketBooked).all()
    return obj
    

@app.post('/createticket/')
def book_ticket(item:schemas.TicketBookedSchema,db:Session=Depends(get_db)):
    
    checkShows=db.query(models.Shows).filter(models.Shows.show_id==item.show_id).first()
    if checkShows==None:
        return {"error":"invalid show id"}
    if checkShows.seat_available>0:

       obj1 = db.query(models.TicketBooked).filter(models.TicketBooked.ticket_id==item.ticket_id).first()
       if obj1!=None:
         return {"data":" your seat is already booked"}
       else:
            obj = models.TicketBooked(ticket_id=item.ticket_id,
                        movie_id = item.movie_id,
                        id=item.id,
                        theatre_id=item.theatre_id,
                        timeslot_id=item.timeslot_id,
                        seat_id=item.seat_id,
                        show_id=item.show_id)
            currseatavailable=db.query(models.Shows).filter(models.Shows.movie_id==item.movie_id).order_by(models.Shows.seat_available).first()
            if currseatavailable==None:
              currseatavailable.seat_available=39
            else:    
              checkShows.seat_available=currseatavailable.seat_available-1
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
    else:
        return {"data":" Housefull"}
    