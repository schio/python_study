
def unpacking_a_sequence_into_separate_variables():
  """
  1.1 Unpacking a Sequence into Separate Variables
  Problem
  You have an N-element tuple or sequence that you would like to unpack into a collection
  of N variables.
  """
  p = (4,5)
  x, y = p
  print(x,y)

  data = ['chioh', 50, 91.1, (2020, 1, 13)]
  name, shares, price, date = data
  print(name, shares, price, date)

  word = "World"
  a, b, c, d, e = word
  print(a)

  data = ['chioh', 50, 91.1, (2020, 1, 13)]
  _, shares, price, _ = data
  print(shares, price)

def unpacking_elements_from_iterables_of_arbitrary_length():
  """
  1.2 Unpacking Elements from Iterables of Arbitrary Length
  Problem
  You need to unpack N elements from an iterable, but the iterable may be longer than N
  elements, causing a “too many values to unpack” exception.
  """
  record = ('chioh', 'ghsehr1@gmail.com', '010-1111-2222', '02-111-2222')
  name, email, *call_number = record
  print(name, email, call_number)

  *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
  print(trailing, current)

  records = [
    ('foo', 1, 2),
    ('body', 'hello'),
    ('foo', 3, 4),
  ]
  def do_foo(x, y):
    print('foo', x, y)

  def do_body(s):
    print('body', s)

  for tag, *args in records:
    if tag == 'foo':
      print(*args)
      do_foo(*args)
    elif tag == 'body':
      do_body(*args)

  line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
  uname, *fields, homedir, sh = line.split(':')
  print(uname, *fields, homedir, sh)

  record = ['chioh', 50, 91.1, (2020, 1, 13)]
  name, *_, (*_, year) = record
  print(name, year)

  def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

  items = [1, 10, 7, 4, 5, 9]
  print(sum(items))
  # memo - *var로 받으면 var은 list 형태지만 
  # *var은 len(var)개의 변수로 변환되어 각 변수마다 1개의 값만 저장함.

def keeping_the_last_n_items():
  """
  1.3 Keeping the Last N Items
  Problem
  You want to keep a limited history of the last few items seen during iteration or during
  some other kind of processing.
  """
  from collections import deque
  def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
      if pattern in line:
        yield line, previous_line
      previous_line.append(line)

  with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
      for pline in prevlines:
        print(pline, end='')
      print(line, end='')
      print('-'*40)
      
def finding_the_largest_or_msallest_n_items():
  """
  1.4 Finding the Largest or Smallest N Items
  Problem
  You want to make a list of the largest or smallest N items in a collection.
  """
  import heapq
  nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
  print(heapq.nlargest(3, nums))
  print(heapq.nsmallest(3, nums))

  portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
  ]
  cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
  expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
  print(cheap, expensive)

  heap = list(nums)
  heapq.heapify(heap)
  print(heap)

  print(heapq.heappop(heap))
  print(heapq.heappop(heap))
  print(heapq.heappop(heap))
  print(lambda s: s['price'])

  """
  숙제 : 이진트리 이해, 매직메소드 이해
  https://www.daleseo.com/python-heapq/
  https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__
  """

# unpacking_a_sequence_into_separate_variables()
# unpacking_elements_from_iterables_of_arbitrary_length()
# keeping_the_last_n_items()
finding_the_largest_or_msallest_n_items()
