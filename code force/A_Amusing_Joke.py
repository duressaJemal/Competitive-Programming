guest_name = list(input())
host_name = list(input())
pile_letters = list(input())

combined = guest_name + host_name
combined.sort()
pile_letters.sort()

print("YES" if combined == pile_letters else "NO")