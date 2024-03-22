from sqlalchemy.orm import Session
import models

def create_user(db: Session, user: models.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()

def search_users(db: Session, first_name_mask: str = None, last_name_mask: str = None):
    query = db.query(models.User)
    if first_name_mask:
        query = query.filter(models.User.first_name.like(f"%{first_name_mask}%"))
    if last_name_mask:
        query = query.filter(models.User.last_name.like(f"%{last_name_mask}%"))
    return query.all()