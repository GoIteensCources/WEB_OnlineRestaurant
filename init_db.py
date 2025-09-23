from models import Base, OrderMenu, User, Menu, Orders, Reservations
from settings import  Session
from werkzeug.security import generate_password_hash, check_password_hash


# Ініціалізація бази даних і додавання товарів
def init_db():
    base = Base()
    base.drop_db()
    base.create_db()  # Створюємо таблиці

    session = Session()

    user = User(username="admin", 
                email="admin@example.com", 
                hash_password=generate_password_hash("admin"),
                is_admin=True)
    
    user2 = User(username="user", 
                email="user@example.com", 
                hash_password=generate_password_hash("user"),
                )
    
    menu1 = Menu(
        name = "Burger",
        description = "булка, котлета теляча, сир, помідор, соус, лук, зелень",
        price = 250, 
        image_path = "static/images_menu/burger.jpg",
        category = "fast food"
    )
    
    menu2 = Menu(
        name = "shashlik",
        description = "телятина у маринаді з апельсинів",
        price = 500, 
        image_path = "static/images_menu/unnamed.jpg",
        category = "bbq"
    )


    session.add_all([user, user2, menu1, menu2])    
    session.flush()

    order = Orders(user_id=user.id)
    session.add(order)
    session.flush()
    
    om1_1 = OrderMenu(order_id=order.id, menu_id=menu1.id, quantity=2)
    om1_2 = OrderMenu(order_id=order.id, menu_id=menu2.id, quantity=4)

    session.add_all([om1_1, om1_2])
    session.commit()

    session.close()


if __name__ == "__main__":
    init_db()
