from collections import namedtuple

# Define named tuples for each table
Supplier = namedtuple('Supplier', ['sno', 'sname', 'status', 'city'])
Part = namedtuple('Part', ['pno', 'pname', 'color', 'weight', 'city'])
Project = namedtuple('Project', ['jno', 'jname', 'city'])
SPJ = namedtuple('SPJ', ['sno', 'pno', 'jno', 'qty'])

# Read data from text files and create sets of named tuples
def read_data(filename, named_tuple):
    data = []
    with open(filename, 'r') as file:
        next(file)  # Skip the first line (table name)
        column_names = next(file).strip().split(',')
        for line in file:
            values = line.strip().split(',')
            data.append(named_tuple(*values))
    return data

suppliers = read_data('suppliers.txt', Supplier)
parts = read_data('parts.txt', Part)
projects = read_data('projects.txt', Project)
spj = read_data('spj.txt', SPJ)

# Query 1: Get names of all suppliers that supply bolts
query1_result = {s.sname for s in suppliers for r in spj for p in parts
                 if r.sno == s.sno if r.pno == p.pno if p.pname == 'Bolt'}

# Query 2: Get names of all suppliers that supply blue parts
query2_result = {s.sname for s in suppliers for r in spj for p in parts
                 if r.sno == s.sno if r.pno == p.pno if p.color == 'Blue'}

# Query 3: Get names of all suppliers not used in Athens projects
athens_projects = {j.jno for j in projects if j.city == 'Athens'}
query3_result = {s.sname for s in suppliers if all(r.jno not in athens_projects for r in spj if r.sno == s.sno)}

# Query 4: Get names and colors of all parts not used in Oslo
oslo_projects = {j.jno for j in projects if j.city == 'Oslo'}
query4_result = {(p.pname, p.color) for p in parts if all(r.jno not in oslo_projects for r in spj if r.pno == p.pno)}

# Query 5: Get pairs of names of all suppliers that are located in the same city
query5_result = {(s1.sname, s2.sname) for s1 in suppliers for s2 in suppliers if s1.sno != s2.sno and s1.city == s2.city}

# Query 6: Print all suppliers out by city
supplier_by_city = {}
for s in suppliers:
    if s.city not in supplier_by_city:
        supplier_by_city[s.city] = set()
    supplier_by_city[s.city].add(s.sname)

# Print query results
print(query1_result)
print(query2_result)
print(query3_result)
print(query4_result)
print(query5_result)
print(supplier_by_city)
