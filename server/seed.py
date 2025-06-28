from app import app
from models import db, Plant

with app.app_context():
    db.drop_all()
    db.create_all()

    aloe = Plant(
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
        is_in_stock=True
    )

    ficus = Plant(
        name="Ficus",
        image="./images/ficus.jpg",
        price=24.99,
        is_in_stock=False
    )

    db.session.add_all([aloe, ficus])
    db.session.commit()

    print("🌱 Seeded plants!")