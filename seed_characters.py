from application import db
from application.characters.models import Character, Moveset

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
entry1 = Character(alignment="Good", name="Blanka", species="Human", birthplace="Brazil", height=192, weight=98)
entry2 = Character(alignment="Lawful Good", name="Chun-Li", species="Human", birthplace="China", height=170)
entry3 = Character(alignment="Good", name="Dhalsim", species="Human", birthplace="India", height=176,)
entry4 = Character(alignment="Evil", name="M. Bison", species="Human", birthplace="Unknown", height=182)
entry5 = Character(alignment="Good", name="Ryu", species="Human", birthplace="Japan", height=175, weight=68)

entry1_moveset1 = Moveset(move_type="Special" , move_name="Electric Thunder", character_id=entry1.id)
entry1_moveset2 = Moveset(move_type="Special" , move_name="Roll Attack", character_id=entry1.id)
entry1_moveset3 = Moveset(move_type="Special" , move_name="Vertical Roll", character_id=entry1.id)
entry1_moveset4 = Moveset(move_type="Unique" , move_name="Rock Crush", character_id=entry1.id)

entry1.movesets.extend([entry1_moveset1, entry1_moveset2, entry1_moveset3, entry1_moveset4])
db.session.add_all([entry1, entry2, entry3, entry4, entry5])

db.session.commit()
