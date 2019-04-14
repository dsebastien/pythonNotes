def foo():
    print("cool")

message = "Hello world"
print(message)
print(len(message))
#print(message[0])

for x in message:
    print(x)

print("Last letter " + message[-1])

print("Chars 1 to 2: " + message[1:3])

print("Chars 1 to the end: " + message[1:])

print("Everything but the last: " + message[:-1])

print("Full message: " + message[:])

new_message = message + ". Foo!"

print(new_message)

print(message*3)

new_message = "F" + message[1:]

print(new_message)

message_as_list = list(message)
message_as_list.reverse()

print(message_as_list)

message_as_list[0] = 'a'

changed_message = ''.join(message_as_list)

print(changed_message)

message_as_bytes = bytearray(b'something')
message_as_bytes.extend(b' is different')

print(message_as_bytes.decode())

print(message.find('Hello'))

print(message.replace('Hello', 'foo'))

comma_delimited_string = 'aaa,bbb,ccc,ddd'

split_string = comma_delimited_string.split(',')

print(split_string)

print(message.upper())
