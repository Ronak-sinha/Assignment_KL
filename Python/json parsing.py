import json


def json_parsing():
    """from file we are parsing the data min, max and avg value of every 
    parameter and store in output_data_res.json
    """
    try: 
        with open("sample_data.json", "r") as data_file:
            data = json.load(data_file)

        output_data = []

        para_list = data["parametersList"]

        for para_name in para_list:
            value1 = {'parameterName': para_name["parameterName"],
                    'min_value': para_name["min"], 'man_value': para_name["max"],
                    'avg_value': para_name["avg"]}
            output_data.append(value1)
        with open("output_data_res.json", "w") as output_data_file:
            json.dump(output_data, output_data_file, indent=2)

        data_file.close()
        output_data_file.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    json_parsing()
