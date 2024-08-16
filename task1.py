from pulp import LpMaximize, LpProblem, LpVariable, lpSum

model = LpProblem(name="drink-production", sense=LpMaximize)

limonade = LpVariable(name="limonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

model += lpSum([limonade, fruit_juice]), "Total Production"

model += (2 * limonade + 1 * fruit_juice <= 100), "Water Constraint"
model += (1 * limonade <= 50), "Sugar Constraint"
model += (1 * limonade <= 30), "Lemon Juice Constraint"
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"

model.solve()

limonade_qty = limonade.value()
fruit_juice_qty = fruit_juice.value()

print(f"Optimal production:")
print(f"Limonade: {limonade_qty} units")
print(f"Fruit Juice: {fruit_juice_qty} units")
