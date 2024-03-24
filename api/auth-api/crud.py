from sqlalchemy.orm import Session
import models
import redis

redis_conn = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

def cache_user(db: Session, user: models.User):
    redis_conn.set(f"user:{user.login}", user.user_id, ex=60)

def get_cached_user(login: str):
    user_id = redis_conn.get(f"user:{login}")
    return user_id

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

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def cache_search_results(first_name_mask: str, last_name_mask: str, users: list):
    key = f"search:{first_name_mask}:{last_name_mask}"
    users_str = ",".join([str(user.user_id) for user in users])
    redis_conn.set(key, users_str, ex=60)

def get_cached_search_results(first_name_mask: str, last_name_mask: str):
    key = f"search:{first_name_mask}:{last_name_mask}"
    users_str = redis_conn.get(key)
    if users_str:
        user_ids = [int(user_id) for user_id in users_str.split(",")]
        return user_ids
    return None