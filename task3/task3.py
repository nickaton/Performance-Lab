import json
import sys

def item_generator(json_input, results):
    if isinstance(json_input, dict):
        if 'id' in json_input.keys() and 'value' in json_input.keys():
            json_input['value'] = results[int(json_input['id'])]
        item_generator(list(json_input.values()), results)

    elif isinstance(json_input, list):
        for item in json_input:
            item_generator(item, results)



values_txt = sys.argv[1]
tests_txt = sys.argv[2]
report_txt = sys.argv[3]

with open(f"{values_txt}", mode="r") as file:
    values = json.load(file)['values']
    results = {}
    for item in values:
        results[item['id']] = item["value"]


with open(f"{tests_txt}") as example, open(f"{report_txt}", 'w') as res:
    data = json.load(example)
    item_generator(data['tests'], results)
    print(data)
    json.dump(data, res, indent=2)