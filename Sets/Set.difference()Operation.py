i, english_subscribers = input(), set(map(int, input().split()))
z, french_subscribers = input(), set(map(int, input().split()))
print(len(english_subscribers.difference(french_subscribers)))
