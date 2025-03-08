# app/routes/groups.py
# 그룹 생성, 그룹 멤버 관리, 그룹 게시판 API 엔드포인트
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.groups import Group
from app.models.group_members import GroupMember
from app.schemas import group_schema

router = APIRouter()

def get_db():
    """
    DB 세션 반환 함수.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=group_schema.GroupResponse)
def create_group(group: group_schema.GroupCreate, db: Session = Depends(get_db)):
    """
    새 그룹을 생성합니다.
    """
    new_group = Group(
        name=group.name,
        owner_id=group.owner_id
    )
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group

@router.post("/invite", response_model=group_schema.GroupInviteResponse)
def invite_to_group(invite: group_schema.GroupInvite, db: Session = Depends(get_db)):
    """
    그룹에 사용자를 초대합니다.
    """
    new_member = GroupMember(
        group_id=invite.group_id,
        user_id=invite.user_id
    )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return {"group_id": invite.group_id, "user_id": invite.user_id}
