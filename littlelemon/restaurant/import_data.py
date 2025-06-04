import logging
import pandas as pd
from django.contrib.auth.models import User
from restaurant.models import Category, MenuItem, Booking
from datetime import datetime, timezone

def run():
    # set up logging
    lgr = logging.getLogger()
    lgr.setLevel(logging.INFO)
    
    logging.info("Loading Menu Items ...")
    # read csv file and iterate through the data and create model instances
    menu_item_fpath = "restaurant/static/data/menu_items.csv"
    menu_item_data = pd.read_csv(menu_item_fpath, encoding="utf-8")
    for index, row in menu_item_data.iterrows():
        # create or get the category instance
        category, created = Category.objects.get_or_create(
            title=row["category"],
            defaults={"slug": row["category"].lower().replace(" ", "-")}
        )
        # create the instance
        menuitem, created = MenuItem.objects.update_or_create(
            name=row["name"],
            price=row["price"],
            quantity=row["quantity"],
            description=row["description"],
            featured=row["featured"],
            category=category
        )
    
    logging.info("Loading Bookings ...")
    # read csv file and iterate through the data and create model instances
    booking_fpath = "restaurant/static/data/bookings.csv"
    booking_data = pd.read_csv(booking_fpath, encoding="utf-8")
    for index, row in booking_data.iterrows():
        # create the instance
        booking = Booking.objects.update_or_create(
            first_name=row["first_name"],
            last_name=row["last_name"],
            guest_number=row["guest_number"],
            date_time=datetime.strptime(row["date_time"], '%d/%m/%Y %H:%M').replace(tzinfo=timezone.utc).astimezone(tz=None),
            comment=row["comment"]
        )