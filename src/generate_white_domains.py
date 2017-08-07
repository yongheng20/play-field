
import json

with open('../data/whitelist.json', 'r') as f:
    data = json.load(f)

output_file = open("../output/pac_whitelist_9568items.txt", 'w')
for root_name, secondary_domain_names in data.iteritems():
    for secondary_domain_name, label in secondary_domain_names.iteritems():
        print >> output_file, "*.{0}.{1};".format(secondary_domain_name, root_name),

output_file.close()
