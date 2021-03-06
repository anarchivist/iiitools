#! /usr/bin/env python

# To change this template, choose Tools | Templates
# and open the template in the editor.

import iiitools

def print_record(record, full_output=False, output_marc=False, output_raw=False, items=None):
    print '*'*60
    print "Bib #: {0}".format(record.bibnumber)
    print "Check digit: {0}".format(record.check_digit)
    print "Call #: {0}".format(record.call_number)
    print "Source URL: {0}".format(record.src_host)
    print "Record URL: {0}".format(record.record_url)
    print "Record MARC URL: {0}".format(record.record_marc_url)
    print "Type: {0}".format(record.type)
    print '-'*60
    print "Title: {0}".format(record.title)
    print "Statement of Responsibility: {0}".format(record.statement_of_responsibility)
    print "ISSN(s): {0}".format(', '.join(record.issn))
    print "ISBN(s): {0}".format(', '.join(record.isbn))
    print "Publisher(s): {0}".format(', '.join(record.publishers))
    print "Publisher name(s): {0}".format(', '.join(record.publisher_names))
    print "Date publised: {0}".format(record.date_published)
    print "Author: {0}".format(record.author)
    print "URLs:"
    for url in record.links: print " - {0}: {1}".format(url['label'], url['url'])
    if full_output:
        print "Author name: {0}".format(record.author_name)
        print "Author dates: {0}".format('; '.join(record.author_dates))
        print "Other authors: "
        for a in record.other_authors: print " - {0}".format(a)

        print "Uniform title: {0}".format(record.title_uniform)
        print "Abbreviated title(s): {0}".format(', '.join(record.title_abbrv))
        print "Key title(s): {0}".format(', '.join(record.title_key))
        print "Varying form(s) of title: {0}".format(', '.join(record.title_varying_forms))
        print "Edition: {0}".format(record.edition)
        print "Computer file characteristics: {0}".format(record.comp_file_characteristics)
        print "Physical description: {0}".format(record.physical_description)
        print "Publication frequency: {0}".format(record.pub_frequency)
        print "Former publication frequencies: {0}".format('; '.join(record.former_pub_frequencies))
        print "Publication dates: {0}".format('; '.join(record.pub_dates))
        print "Series: {0}".format('; '.join(record.series))
        print "Notes: "
        for n in record.notes: print " - {0}".format(n)

        print "Summary: {0}".format(record.summary)
        print "Contents: {0}".format(record.contents)
        print "Subjects: "
        for s in record.subjects: print " - {0}".format(s)

        print "Preceding titles: "
        for ep in record.entry_preceding: print " - {0}".format(ep['title'])

        print "Succeeding titles: "
        for es in record.entry_succeeding: print " - {0}".format(es['title'])

        print "Entry notes:"
        for en in record.entry_notes: print " - {0}".format(en)
    
    if items:
        print '-'*60
        print "Current Holdings:"
        print '-'*60
        print "Location\t\t\tCall Number\t\t\tStatus"
        for i in items:
            print "{0}\t\t\t{1}\t\t\t{2}".format(i['location'], i['call_num'],i['status'])
    if output_marc:
        print '-'*60
        print record
    if output_raw:
        print '-'*60
        print record.raw
    print '*'*60


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    reader = iiitools.Reader('http://opac.uthsc.edu', scope=2)

    if len(args) == 1:
        record = reader.get_record(args[0])
        items = reader.get_items_for_record(args[0])
        if record:
            print_record(record, True, True, True, items)
    elif len(args) == 2:
        if not args[0].startswith('b') or not args[1].startswith('b'):
            raise ValueError("Invalid bib record number(s).")

        bib_start = int(args[0][1:])
        bib_end = int(args[1][1:])+1
        if bib_end < bib_start: raise ValueError("2nd bib record occurs before the 1st.")
        
        for num in range(bib_start, bib_end):
            bibnum = "b{0}".format(num)
            record = reader.get_record(bibnum)
            if record: print_record(record, True)