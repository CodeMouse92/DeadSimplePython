from calendar import c


# with open('78SomewhereRd.txt', 'r+') as real_estate_listing:
#     contents = real_estate_listing.read()

#     contents = contents.replace('Tiny', 'Cozy')
#     contents = contents.replace('Needs repairs', 'Full of potential')
#     contents = contents.replace('Small', 'Compact')
#     contents = contents.replace('old storage shed', 'detached workshop')
#     contents = contents.replace('Built on ancient burial ground.',
#                                 'Unique atmosphere.')
#     real_estate_listing.seek(0)
#     real_estate_listing.write(contents)
#     real_estate_listing.truncate()

with open('78SomewhereRd.txt', 'r+') as real_estate_listing:
    contents = real_estate_listing.readlines()
    new_contents = []
    for line in contents:
        line = line.replace('Tiny', 'Cozy')
        line = line.replace('Needs repairs', 'Full of potential')
        line = line.replace('Small', 'Compact')
        line = line.replace('old storage shed', 'detached workshop')
        line = line.replace('Built on ancient burial ground.',
                                    'Unique atmosphere.')
        new_contents.append(line)
    real_estate_listing.seek(0)
    real_estate_listing.writelines(new_contents)
    real_estate_listing.truncate()
