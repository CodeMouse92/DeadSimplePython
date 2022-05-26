from pathlib import Path

path = Path('78SomewhereRd.txt')

with path.open('r') as real_estate_listing:
    contents = real_estate_listing.read()
    contents = contents.replace('Tiny', 'Cozy')
    contents = contents.replace('Needs repairs', 'Full of potential')
    contents = contents.replace('Small', 'Compact')
    contents = contents.replace('old storage shed', 'detached workshop')
    contents = contents.replace('Built on ancient burial ground.',
                                'Unique atmosphere.')


tmp_path = path.with_name(path.name + '.tmp')

with tmp_path.open('w') as file:
    file.write(contents)

tmp_path.replace(path)  # move the new file into place of the old one
