import threading
import time
import http.client

# Define a function to be executed in the thread

# clive = True
# curr_time = time.time()
# print(curr_time)
#
#
# def thread_function():
#     while clive:
#         print("Thread is running")
#         time.sleep(2)
#         print(time.time() - curr_time)
#         print(clive)
#     print("Thread is finished")
#
#
# def time_monitor():
#     global clive
#     while True:
#         if time.time() - curr_time > 6:
#             print("Time Limit Exceeded!")
#             clive = False
#             break
#
#
# # Create a new thread
# my_thread = threading.Thread(target=thread_function)
# time_monitor_thread = threading.Thread(target=time_monitor)
#
# # Start the thread
# my_thread.start()
# time_monitor_thread.start()
#
# print("Still not finished")
#
# # Optionally, you can join the thread to wait for its completion
# my_thread.join()
# time_monitor_thread.join()
#
# print("Main thread is done")


def five():
    global start_time, answered, fetched
    while True:
        if time.time() - start_time > 2:
            if (not fetched) and (not fetch_low):
                print("SLOW!")
                start_time = time.time()
            else:
                break


def fetch_random_number():
    conn = http.client.HTTPSConnection("www.random.org")
    conn.request("GET", "/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new")
    response = conn.getresponse()
    if response.status == 200:
        random_number = int(response.read().decode())
        print(f"Random: {random_number}")
        return random_number
    else:
        print("Failed to fetch random number. Status code:", response.status)
        return None


def fetch_number():
    global fetched
    fetch = fetch_random_number()
    while fetch < 90:
        fetch = fetch_random_number()
    print("Higher value is " + str(fetch))
    fetched = True


def fetch_lower():
    global fetch_low
    fetch = fetch_random_number()
    while fetch > 10:
        fetch = fetch_random_number()
    print("Lower value is " + str(fetch))
    fetch_low = True


five_second = threading.Thread(target=five)
fetch_num = threading.Thread(target=fetch_number)
fetch_second = threading.Thread(target=fetch_lower)

start_time = time.time()
answered = False
fetched = False
fetch_low = False
answer = ""
five_second.start()
fetch_num.start()
fetch_second.start()

fetch_num.join()
five_second.join()
fetch_second.join()
