import pandas as pd


old = pd.read_excel('employees_old.xlsx')
new = pd.read_excel('employees_new.xlsx')

filename = "compare.xlsx"

old.set_index('ID', inplace=True)
new.set_index('ID', inplace=True)

common_ids = old.index.intersection(new.index)
added_ids = new.index.difference(old.index)
removed_ids = old.index.difference(new.index)

added = new.loc[added_ids]
removed = old.loc[removed_ids]

changed_ids = []
for _id in common_ids:
    if not old.loc[_id].equals(new.loc[_id]):
        changed_ids.append(_id)
changed = pd.concat([
    old.loc[changed_ids].add_prefix("Old_"),
    new.loc[changed_ids].add_prefix("New_")
], axis=1)

with pd.ExcelWriter(filename) as writer:
    added.to_excel(writer, sheet_name="Added")
    removed.to_excel(writer, sheet_name="Removed")
    changed.to_excel(writer, sheet_name="Changed")
print("Comparison complete!")