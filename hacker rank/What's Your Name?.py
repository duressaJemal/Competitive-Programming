# Link: https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=false
#Q: What's Your Name?

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)