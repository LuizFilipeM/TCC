import pyvrp
import pyvrp.plotting
import pyvrp.stop



def main(depot, clients, demand_ww, period):

    DEPOT_COORDINATES = (depot.x, depot.y)
    
    for p in range(period):

        print("\n\nINICIO PYVRP PARA PERIODO: ", p, "\n\n")

        COORDINATES = []

        for i in clients:
            COORDINATES.append((i.x, i.y))
        
        DEMANDS = []

        for i in clients:
            DEMANDS.append(int(round(i.d[p]))) # Pega a demanda do período atual, pois o pyVRP não trabalha com múltiplos períodos


        m = pyvrp.Model()

        depot = m.add_depot(
            location=m.add_location(DEPOT_COORDINATES[0], DEPOT_COORDINATES[1]),
            name="Depot",
        )

        vehicles = m.add_vehicle_type(num_available=7, capacity=322)

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

        
        print("\n")
        for idx, route in enumerate(res.best.routes()):
            print(f"\nRoute #{idx}:")

            for activity in route:
                if activity.is_depot():
                    where = m.depots[activity.idx]
                else:
                    where = m.clients[activity.idx]

                print(f" - At {where}.")

        
        print("\n\n\nFIM PYVRP PARA PERIODO: ", p)
        print("\n***********************************************************\n\n")

    