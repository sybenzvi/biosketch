#!/usr/bin/env python
"""Reduce ADS RIS bibliographies to a manageable size. When downloading the
bibliography from NASA ADS (https://ui.adsabs.harvard.edu/), make sure you
check the box to include refereed papers only.
"""

from argparse import ArgumentParser

# Not a complete list of RIS tags, but these are useful for ADS citations.
ris_tags = {
    'TY': 'type_of_reference',
    'TI': 'title',
    'AU': 'authors',
    'C1': 'custom1',
    'JO': 'journal_name',
    'VL': 'volume',
    'Y1': 'publication_year',
    'SP': 'start_page',
    'UR': 'url',
    'DO': 'doi',
    'ER': 'end_of_reference' }

def get_record(filename):
    """Extract RIS records from a RIS file.

    Parameters
    ----------
    filename : str
        Path to an ASCII file with a RIS bibliography.

    Returns
    -------
    record : list
        A RIS record as a list of strings.
    """
    with open(filename, 'r') as f:
        record = []
        nauth = 0

        for row in f:
            if row[:2] not in ris_tags.keys():
                continue

            if row.startswith('TY'):
                record = [row.strip()]
            elif row.startswith('AU'):
                nauth += 1
                if nauth == 4:
                    record.append('AU  - et al')
                elif nauth > 4:
                    continue
                else:
                    record.append(row.strip())
            elif row.startswith('ER'):
                record.append(row.strip())
                nauth = 0
                yield record
            else:
                record.append(row.strip())

        if len(record) > 0:
            yield record

if __name__ == '__main__':
    p = ArgumentParser(description='Shorten RIS files from NASA ADS')
    p.add_argument('risfile', nargs=1, help='ASCII bibliography in RIS format')
    p.add_argument('-o,--output', dest='output', default=None,
                   help='Output file name')

    args = p.parse_args()
    output = args.output if args.output is not None else 'reduced_bib.ris'

    with open(output, 'w') as f:
        for i, record in enumerate(get_record(args.risfile[0])):
            f.write('{}\n'.format('\n'.join(record)))

        print('Wrote {} records to {}.'.format(i, output))
