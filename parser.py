import csv
from collections import defaultdict


def load_lookup_table(lookup_file):
    lookup_dict = {}
    with open(lookup_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dstport = row['dstport'].strip().lower()
            protocol = row['protocol'].strip().lower()
            tag = row['tag'].strip()
            lookup_dict[(dstport, protocol)] = tag
    return lookup_dict


def parse_flow_logs(flow_log_file, lookup_dict):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(flow_log_file, 'r') as log:
        for line in log:
            line_elements = line.split()
            if len(line_elements) < 11:
                print("Invalid line element count, skipping...")
                continue

            dstport = line_elements[6]
            protocol = line_elements[7]

            protocol_dict = {"6": "tcp", "17": "udp", "1": "icmp"}
            protocol_name = protocol_dict.get(protocol, protocol)

            port_protocol_counts[(dstport, protocol_name)] += 1

            tag_key = (dstport, protocol_name)
            if tag_key in lookup_dict:
                tag_counts[lookup_dict[tag_key]] += 1
            else:
                tag_counts["Untagged"] += 1

    return tag_counts, port_protocol_counts


def write_output(output_file, tag_counts, port_protocol_counts):
    with open(output_file, 'w') as outfile:
        outfile.write("Tag Counts:\n")
        outfile.write("Tag,Count\n")
        for tag, count in sorted(tag_counts.items()):
            outfile.write(f"{tag},{count}\n")

        outfile.write("\nPort/Protocol Combination Counts:\n")
        outfile.write("Port,Protocol,Count\n")
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            outfile.write(f"{port},{protocol},{count}\n")


def main():
    flow_log_file = 'flow_logs.txt'
    lookup_file = 'lookup_table.csv'
    output_file = 'output.txt'
    lookup_dict = load_lookup_table(lookup_file)
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_dict)
    write_output(output_file, tag_counts, port_protocol_counts)


if __name__ == "__main__":
    main()
