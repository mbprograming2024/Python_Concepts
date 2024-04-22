# def process_data(data, ts_key, bill_cycle_id, date):
#     if ts_key in data:
#         if bill_cycle_id in data[ts_key]:
#             if date in data[ts_key][bill_cycle_id]:
#                 data[ts_key][bill_cycle_id].remove(date)
#                 if not data[ts_key][bill_cycle_id]:
#                     del data[ts_key][bill_cycle_id]
#                     if not data[ts_key]:
#                         del data[ts_key]
#     return data
#
# # Given data
# data = {
#     94181: {79: ['30-09-2006']},
#     94188: {79: ['30-09-2006'], 63623: ['31-10-2006']}
# }
#
# # Example usage:
# ts_key = 94188
# bill_cycle_id = 79
# date = '30-09-2006'
#
# result = process_data(data, ts_key, bill_cycle_id, date)
#
# # Print the updated data
# print("Updated Data:")
# print(result)


# def process_data(data, ts_key, bill_cycle_id, date):
#     updated_data = data.copy()  # Create a copy of the original data
#     updated_ts_list = []  # List to store updated ts_keys
#
#     if ts_key in updated_data:
#         if bill_cycle_id in updated_data[ts_key]:
#             if date in updated_data[ts_key][bill_cycle_id]:
#                 updated_data[ts_key][bill_cycle_id].remove(date)
#                 if not updated_data[ts_key][bill_cycle_id]:
#                     del updated_data[ts_key][bill_cycle_id]
#                     if not updated_data[ts_key]:
#                         del updated_data[ts_key]
#
#     # Iterate over the original data to update the ts_list
#     for key in data.keys():
#         if key not in updated_data:
#             updated_ts_list.append(key)
#
#     return updated_data, updated_ts_list
#
# # Given data
# data = {
#     94181: {79: ['30-09-2006']},
#     94188: {79: ['30-09-2006'], 63623: ['31-10-2006']}
# }
#
# # Example usage:
# ts_key = 94188
# bill_cycle_id = 79
# date = '30-09-2006'
#
# updated_data, updated_ts_list = process_data(data, ts_key, bill_cycle_id, date)
#
# # Print the updated data and ts_list
# print("Updated Data:")
# print(updated_data)
# print("\nUpdated ts_list:")
# print(updated_ts_list)
#


def process_data(data, bill_cycle_id, date):
    updated_data = data.copy()  # Create a copy of the original data
    updated_ts_list = []  # List to store updated ts_keys

    # Iterate over each ts_key in the data
    for ts_key in list(updated_data.keys()):
        print(type(updated_data[ts_key]))
        if bill_cycle_id in updated_data[ts_key]:
            print(bill_cycle_id)
            if date in updated_data[ts_key][bill_cycle_id]:
                print(date)
                updated_data[ts_key][bill_cycle_id].remove(date)
                if not updated_data[ts_key][bill_cycle_id]:
                    del updated_data[ts_key][bill_cycle_id]
                    if not updated_data[ts_key]:
                        del updated_data[ts_key]
                        updated_ts_list.append(ts_key)

    return updated_data, updated_ts_list

# Given data
data = {
    94181: {79: ['30-09-2006']},
    94188: {79: ['30-09-2006'], 63623: ['31-10-2006']}
}
print(type(data))
# Example usage:
bill_cycle_id = 63623
date = '31-10-2006'


updated_data, updated_ts_list = process_data(data, bill_cycle_id, date)

# Print the updated data and ts_list
print("Updated Data:")
print(updated_data)
print("\nUpdated ts_list:")
print(updated_ts_list)
