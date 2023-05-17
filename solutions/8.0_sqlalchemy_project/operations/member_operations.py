from models.member import Member


def add_member(session, name, email, phone):
    member = Member(name=name, email=email, phone=phone)
    session.add(member)
    session.commit()


def get_all_members(session):
    return session.query(Member).all()


def get_member_by_id(session, member_id):
    return session.query(Member).get(member_id)


def update_member_info(session, member_id, name=None, email=None, phone=None):
    member = session.query(Member).get(member_id)
    if name:
        member.name = name
    if email:
        member.email = email
    if phone:
        member.phone = phone
    session.commit()


def delete_member(session, member_id):
    member = session.query(Member).get(member_id)
    session.delete(member)
    session.commit()
