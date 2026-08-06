import pyvrp
import pyvrp.plotting
import pyvrp.stop

DEPOT_COORDINATES = (51.0, 51.0)
COORDINATES = [(39, 76.5), (64.2, 47), (73, 61), (32, 38.8)]
DEMANDS = [98, 0, 97, 0, 121, 0, 0, 112, 0, 67, 135, 0]



m = pyvrp.Model()

depot = m.add_depot(
    location=m.add_location(DEPOT_COORDINATES[0], DEPOT_COORDINATES[1]),
    name="Depot",
)

vehicles = m.add_vehicle_type(num_available=2, capacity=20)

for idx in range(len(COORDINATES)):
    m.add_client(
        location=m.add_location(COORDINATES[idx][0], COORDINATES[idx][1]),
        delivery=DEMANDS[idx],
        name=f"Client {idx + 1}",
    )

for frm in m.locations:
    for to in m.locations:
        dist = int(abs(frm.x - to.x) + abs(frm.y - to.y))
        m.add_edge(frm, to, distance=dist)

res = m.solve(stop=pyvrp.stop.MaxRuntime(1))  # one second of runtime