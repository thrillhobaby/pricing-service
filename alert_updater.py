from models.alert import Alert


alerts = Alert.all()[0].

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_is_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")