calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def string_lower():
    count_calls()

def is_contains(string, search_list):
    count_calls()
    for search in search_list:
        if string_lower() == search.lower():
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban', 'BaNan', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cycle']))
print(calls)










